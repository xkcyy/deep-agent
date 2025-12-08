#!/usr/bin/env pwsh
# Create a new epic (high-level spec)
[CmdletBinding()]
param(
    [switch]$Json,
    [string]$ShortName,
    [int]$Number = 0,
    [switch]$Help,
    [switch]$CreateBranch,
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$EpicDescription
)
$ErrorActionPreference = 'Stop'

if ($Help) {
    Write-Host "Usage: ./create-new-epic.ps1 [-Json] [-ShortName <name>] [-Number N] [-CreateBranch] <epic description>"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  -Json               Output in JSON format"
    Write-Host "  -ShortName <name>   Provide a custom short name (2-4 words)"
    Write-Host "  -Number N           Specify epic number manually (overrides auto-detection)"
    Write-Host "  -CreateBranch       Create a git branch prefixed with epic/"
    Write-Host "  -Help               Show this help message"
    Write-Host ""
    Write-Host "Examples:"
    Write-Host "  ./create-new-epic.ps1 'Cross-team onboarding experience' -ShortName 'onboarding'"
    Write-Host "  ./create-new-epic.ps1 'Rebuild checkout funnel' -CreateBranch"
    exit 0
}

if (-not $EpicDescription -or $EpicDescription.Count -eq 0) {
    Write-Error "Usage: ./create-new-epic.ps1 [-Json] [-ShortName <name>] <epic description>"
    exit 1
}

$epicDesc = ($EpicDescription -join ' ').Trim()

function Find-RepositoryRoot {
    param(
        [string]$StartDir,
        [string[]]$Markers = @('.git', '.specify')
    )
    $current = Resolve-Path $StartDir
    while ($true) {
        foreach ($marker in $Markers) {
            if (Test-Path (Join-Path $current $marker)) {
                return $current
            }
        }
        $parent = Split-Path $current -Parent
        if ($parent -eq $current) {
            return $null
        }
        $current = $parent
    }
}

function Get-HighestNumberFromEpics {
    param([string]$EpicsDir)
    $highest = 0
    if (Test-Path $EpicsDir) {
        Get-ChildItem -Path $EpicsDir -Directory | ForEach-Object {
            if ($_.Name -match '^E?(\d+)') {
                $num = [int]$matches[1]
                if ($num -gt $highest) { $highest = $num }
            }
        }
    }
    return $highest
}

function Get-HighestNumberFromBranches {
    param()
    $highest = 0
    try {
        $branches = git branch -a 2>$null
        if ($LASTEXITCODE -eq 0) {
            foreach ($branch in $branches) {
                $cleanBranch = $branch.Trim() -replace '^\*?\s+', '' -replace '^remotes/[^/]+/', ''
                if ($cleanBranch -match 'epic/.*?(E?)(\d{1,})') {
                    $num = [int]$matches[2]
                    if ($num -gt $highest) { $highest = $num }
                } elseif ($cleanBranch -match '^E(\d{1,})-') {
                    $num = [int]$matches[1]
                    if ($num -gt $highest) { $highest = $num }
                }
            }
        }
    } catch {
        Write-Verbose "Could not check Git branches: $_"
    }
    return $highest
}

function Get-NextEpicNumber {
    param([string]$EpicsDir)
    try { git fetch --all --prune 2>$null | Out-Null } catch {}
    $highestBranch = Get-HighestNumberFromBranches
    $highestEpic = Get-HighestNumberFromEpics -EpicsDir $EpicsDir
    $maxNum = [Math]::Max($highestBranch, $highestEpic)
    return $maxNum + 1
}

function ConvertTo-CleanName {
    param([string]$Name)
    return $Name.ToLower() -replace '[^a-z0-9]', '-' -replace '-{2,}', '-' -replace '^-', '' -replace '-$', ''
}

function Get-ShortName {
    param([string]$Description)
    $stopWords = @(
        'i','a','an','the','to','for','of','in','on','at','by','with','from',
        'is','are','was','were','be','been','being','have','has','had',
        'do','does','did','will','would','should','could','can','may','might','must','shall',
        'this','that','these','those','my','your','our','their','want','need','add','get','set'
    )
    $cleanName = $Description.ToLower() -replace '[^a-z0-9\s]', ' '
    $words = $cleanName -split '\s+' | Where-Object { $_ }
    $meaningful = @()
    foreach ($word in $words) {
        if ($stopWords -contains $word) { continue }
        if ($word.Length -ge 3) {
            $meaningful += $word
        } elseif ($Description -match "\b$($word.ToUpper())\b") {
            $meaningful += $word
        }
    }
    if ($meaningful.Count -gt 0) {
        $maxWords = if ($meaningful.Count -eq 4) { 4 } else { 3 }
        return ($meaningful | Select-Object -First $maxWords) -join '-'
    }
    $fallback = ConvertTo-CleanName -Name $Description
    $fallbackWords = ($fallback -split '-') | Where-Object { $_ } | Select-Object -First 3
    return [string]::Join('-', $fallbackWords)
}

$fallbackRoot = (Find-RepositoryRoot -StartDir $PSScriptRoot)
if (-not $fallbackRoot) {
    Write-Error "Error: Could not determine repository root. Please run this script from within the repository."
    exit 1
}

try {
    $repoRoot = git rev-parse --show-toplevel 2>$null
    if ($LASTEXITCODE -eq 0) { $hasGit = $true } else { throw "Git not available" }
} catch {
    $repoRoot = $fallbackRoot
    $hasGit = $false
}

Set-Location $repoRoot
$epicsDir = Join-Path $repoRoot 'spec-epics'
New-Item -ItemType Directory -Path $epicsDir -Force | Out-Null

if ($ShortName) {
    $epicSuffix = ConvertTo-CleanName -Name $ShortName
} else {
    $epicSuffix = Get-ShortName -Description $epicDesc
}

if ($Number -eq 0) {
    if ($hasGit) {
        $Number = Get-NextEpicNumber -EpicsDir $epicsDir
    } else {
        $Number = (Get-HighestNumberFromEpics -EpicsDir $epicsDir) + 1
    }
}

$epicNum = ("E{0:000}" -f $Number)
$epicName = "$epicNum-$epicSuffix"
$branchName = "epic/$epicName"

$branchCreated = $false
if ($CreateBranch -and $hasGit) {
    try {
        git checkout -b $branchName | Out-Null
        if ($LASTEXITCODE -eq 0) { $branchCreated = $true }
    } catch {
        Write-Warning "Failed to create git branch: $branchName"
    }
} elseif ($CreateBranch -and -not $hasGit) {
    Write-Warning "[epic] Git repository not detected; skipped branch creation for $branchName"
}

$epicDir = Join-Path $epicsDir $epicName
New-Item -ItemType Directory -Path $epicDir -Force | Out-Null

$template = Join-Path $repoRoot '.specify/templates/epic-template.md'
$epicSpecFile = Join-Path $epicDir 'epic-spec.md'
if (Test-Path $template) {
    Copy-Item $template $epicSpecFile -Force
} else {
    New-Item -ItemType File -Path $epicSpecFile | Out-Null
}

$env:SPECIFY_EPIC = $epicName

if ($Json) {
    $obj = [PSCustomObject]@{
        EPIC_NAME = $epicName
        EPIC_DIR = $epicDir
        EPIC_SPEC_FILE = $epicSpecFile
        HAS_GIT = $hasGit
        BRANCH_CREATED = $branchCreated
        BRANCH_NAME = $branchName
    }
    $obj | ConvertTo-Json -Compress
} else {
    Write-Output "EPIC_NAME: $epicName"
    Write-Output "EPIC_DIR: $epicDir"
    Write-Output "EPIC_SPEC_FILE: $epicSpecFile"
    Write-Output "HAS_GIT: $hasGit"
    Write-Output "BRANCH_CREATED: $branchCreated"
    Write-Output "BRANCH_NAME: $branchName"
    Write-Output "SPECIFY_EPIC environment variable set to: $epicName"
}


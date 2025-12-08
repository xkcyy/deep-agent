import React from "react";
import { Loader2, AlertCircle, FileEdit } from "lucide-react";

type Status = "pending" | "completed" | "error" | "interrupted";

interface FileEditPanelProps {
  status: Status;
  args: Record<string, unknown>;
  result: unknown;
  rawResult?: string | undefined;
}

type FileEditResult = {
  path?: string;
  bytes?: number;
  lines?: number;
  diff?: string;
  preview?: string;
  error?: unknown;
};

function pickEditResult(result: unknown): FileEditResult {
  if (!result || typeof result === "string") return {};
  if (typeof result === "object") return result as FileEditResult;
  return {};
}

function pickError(result: FileEditResult): string | null {
  if (result.error) return String(result.error);
  return null;
}

export const FileEditPanel: React.FC<FileEditPanelProps> = ({
  status,
  args,
  result,
  rawResult,
}) => {
  const parsed = pickEditResult(result);
  const pathCandidates = [
    (typeof args?.path === "string" && args.path) || "",
    (typeof args?.filepath === "string" && args.filepath) || "",
    (typeof args?.file_path === "string" && args.file_path) || "",
    (typeof args?.target === "string" && args.target) || "",
    (typeof args?.dst === "string" && args.dst) || "",
    (typeof parsed.path === "string" && parsed.path) || "",
  ].filter(Boolean);
  const path = pathCandidates[0] || "(未返回路径)";
  const error = pickError(parsed);

  return (
    <div className="rounded-md border border-border/60 bg-gradient-to-br from-background/80 via-background/70 to-muted/70 p-3 shadow-md transition-colors duration-150 hover:border-primary/40 hover:shadow-lg">
      <div className="mb-2 flex items-center justify-between gap-2">
        <div className="flex items-center gap-2 text-sm font-semibold text-foreground">
          <FileEdit className="h-4 w-4" />
          <span className="truncate" title={path}>
            编辑：{path}
          </span>
        </div>
        <div className="flex items-center gap-1 text-xs text-muted-foreground">
          {status === "pending" && (
            <>
              <Loader2 className="h-3 w-3 animate-spin" />
              <span>编辑中</span>
            </>
          )}
          {status === "completed" && <span>完成</span>}
          {status === "error" && (
            <>
              <AlertCircle className="h-3 w-3 text-destructive" />
              <span>失败</span>
            </>
          )}
          {status === "interrupted" && <span>已中断</span>}
        </div>
      </div>

      <div className="mb-2 flex flex-wrap items-center gap-2 text-xs text-muted-foreground">
        {typeof parsed.bytes === "number" && (
          <span className="rounded-full bg-muted/50 px-2 py-0.5 text-foreground">
            字节：{parsed.bytes}
          </span>
        )}
        {typeof parsed.lines === "number" && (
          <span className="rounded-full bg-muted/50 px-2 py-0.5 text-foreground">
            行数：{parsed.lines}
          </span>
        )}
      </div>

      {error && (
        <div className="mb-2 rounded-sm border border-destructive/40 bg-destructive/10 px-2 py-1 text-xs text-destructive">
          {error}
        </div>
      )}

      {parsed.diff && (
        <div className="mb-2">
          <div className="mb-1 text-xs font-semibold text-muted-foreground">
            变更 Diff
          </div>
          <div className="rounded-md border border-primary/30 bg-gradient-to-br from-background/80 to-muted/70 p-2 shadow-inner">
            <pre className="max-h-60 overflow-auto whitespace-pre-wrap break-words text-xs leading-6 text-foreground">
              {parsed.diff}
            </pre>
          </div>
        </div>
      )}

      {parsed.preview && (
        <div className="mb-1 text-xs font-semibold text-muted-foreground">
          内容预览
        </div>
      )}
      {parsed.preview && (
        <div className="rounded-md border border-primary/30 bg-gradient-to-br from-background/80 to-muted/70 p-2 shadow-inner">
          <pre className="max-h-60 overflow-auto whitespace-pre-wrap break-words text-xs leading-6 text-foreground">
            {parsed.preview}
          </pre>
        </div>
      )}

      {!parsed.diff && !parsed.preview && !error && !rawResult && (
        <div className="rounded-sm bg-muted/40 px-2 py-3 text-xs text-muted-foreground">
          已编辑，等待更多返回信息…
        </div>
      )}
      {rawResult && typeof result === "string" && (
        <div className="mt-1 rounded-sm bg-muted/30 px-2 py-2 text-[11px] text-muted-foreground">
          原始返回：{rawResult.slice(0, 200)}
        </div>
      )}
    </div>
  );
};


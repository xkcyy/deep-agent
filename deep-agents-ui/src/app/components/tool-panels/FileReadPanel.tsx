import React, { useMemo, useState } from "react";
import { cn } from "@/lib/utils";
import { Loader2, AlertCircle, FileText, Download } from "lucide-react";

type Status = "pending" | "completed" | "error" | "interrupted";

interface FileReadPanelProps {
  status: Status;
  args: Record<string, unknown>;
  result: unknown;
  rawResult?: string | undefined;
}

type FileReadResult = {
  path?: string;
  size?: number;
  mtime?: string | number;
  content?: string;
  chunks?: string[];
  mime?: string;
  is_binary?: boolean;
  error?: unknown;
};

function pickReadResult(result: unknown): FileReadResult {
  if (!result || typeof result === "string") return {};
  if (typeof result === "object") return result as FileReadResult;
  return {};
}

function pickError(result: FileReadResult): string | null {
  if (result.error) return String(result.error);
  return null;
}

export const FileReadPanel: React.FC<FileReadPanelProps> = ({
  status,
  args,
  result,
  rawResult,
}) => {
  const parsed = useMemo(() => pickReadResult(result), [result]);
  const [expanded, setExpanded] = useState(false);
  const pathCandidates = [
    (typeof args?.path === "string" && args.path) || "",
    (typeof args?.filepath === "string" && args.filepath) || "",
    (typeof args?.file_path === "string" && args.file_path) || "",
    (typeof args?.target === "string" && args.target) || "",
    (typeof args?.dst === "string" && args.dst) || "",
    (typeof parsed.path === "string" && parsed.path) || "",
  ].filter(Boolean);
  const path = pathCandidates[0] || "(未返回路径)";
  const content =
    parsed.content ??
    (Array.isArray(parsed.chunks) ? parsed.chunks.join("") : undefined);
  const isBinary = parsed.is_binary;
  const sizeLabel =
    typeof parsed.size === "number" ? `${parsed.size} bytes` : undefined;
  const error = pickError(parsed);
  const isPending = status === "pending";

  return (
    <div className="rounded-md border border-border/60 bg-gradient-to-br from-background/80 via-background/70 to-muted/70 p-3 shadow-md transition-colors duration-150 hover:border-primary/40 hover:shadow-lg">
      <div className="mb-2 flex items-center justify-between gap-2">
        <div className="flex items-center gap-2 text-sm font-semibold text-foreground">
          <FileText className="h-4 w-4" />
          <span className="truncate" title={path}>
            {path}
          </span>
        </div>
        <div className="flex items-center gap-1 text-xs text-muted-foreground">
          {status === "pending" && (
            <>
              <Loader2 className="h-3 w-3 animate-spin" />
              <span>读取中</span>
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
        {sizeLabel && (
          <span className="rounded-full bg-muted/50 px-2 py-0.5 text-foreground">
            大小：{sizeLabel}
          </span>
        )}
        {parsed.mtime && (
          <span className="rounded-full bg-muted/50 px-2 py-0.5 text-foreground">
            修改时间：{String(parsed.mtime)}
          </span>
        )}
        {parsed.mime && (
          <span className="rounded-full bg-muted/50 px-2 py-0.5 text-foreground">
            MIME：{parsed.mime}
          </span>
        )}
        {isBinary && (
          <span className="rounded-full bg-primary/10 px-2 py-0.5 text-primary">
            二进制文件
          </span>
        )}
      </div>

      {error && (
        <div className="mb-2 rounded-sm border border-destructive/40 bg-destructive/10 px-2 py-1 text-xs text-destructive">
          {error}
        </div>
      )}

      {!content ? (
        <div className="rounded-sm bg-muted/40 px-2 py-3 text-xs text-muted-foreground">
          {isBinary
            ? "二进制文件，未展示内容。"
            : `暂无内容显示${isPending ? "，等待返回…" : ""}${
                rawResult ? `（返回：${rawResult.slice(0, 140)}…）` : ""
              }`}
        </div>
      ) : (
        <div className="space-y-2">
          <div className="flex items-center justify-between text-xs text-muted-foreground">
            <span>内容预览</span>
            <button
              className="inline-flex items-center gap-1 text-primary hover:underline"
              onClick={() => setExpanded((v) => !v)}
            >
              {expanded ? "收起" : "展开更多"}
            </button>
          </div>
          <div
            className={cn(
              "relative rounded-md border border-primary/30 bg-gradient-to-br from-background/80 to-muted/70 p-2 shadow-inner",
              !expanded ? "max-h-24" : "max-h-[260px]"
            )}
          >
            <pre className="m-0 max-h-full overflow-auto whitespace-pre-wrap break-words text-xs leading-6 text-foreground">
              {content}
            </pre>
          </div>
        </div>
      )}

      {isBinary && (
        <div className="mt-2 flex items-center gap-2 text-xs text-muted-foreground">
          <Download className="h-3.5 w-3.5" />
          二进制文件仅展示元信息，如需预览请下载。
        </div>
      )}
    </div>
  );
};


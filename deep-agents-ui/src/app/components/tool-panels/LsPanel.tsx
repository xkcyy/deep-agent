import React from "react";
import { Folder, File as FileIcon, Loader2, AlertCircle } from "lucide-react";

type Status = "pending" | "completed" | "error" | "interrupted";

interface LsPanelProps {
  status: Status;
  args: Record<string, unknown>;
  result: unknown;
  rawResult?: string | undefined;
}

type LsItem = {
  name?: string;
  path?: string;
  is_dir?: boolean;
  size?: number;
  mtime?: string | number;
};

function normalizeItems(result: unknown): LsItem[] {
  if (!result) return [];
  if (typeof result === "string") return [];
  if (Array.isArray(result)) return result as LsItem[];
  const obj = result as Record<string, unknown>;
  const items = (obj["items"] as LsItem[]) || (obj["entries"] as LsItem[]) || [];
  return Array.isArray(items) ? items : [];
}

function pickError(result: unknown): string | null {
  if (!result) return null;
  if (typeof result === "string") {
    return result.toLowerCase().includes("error") ? result : null;
  }
  const obj = result as Record<string, unknown>;
  if (obj["error"]) return String(obj["error"]);
  return null;
}

export const LsPanel: React.FC<LsPanelProps> = ({
  status,
  args,
  result,
  rawResult,
}) => {
  const items = normalizeItems(result);
  const error = pickError(result);
  const target =
    (typeof args?.path === "string" && args.path) ||
    (typeof args?.dir === "string" && args.dir) ||
    ".";
  const isPending = status === "pending";

  return (
    <div className="rounded-md border border-border/60 bg-gradient-to-br from-background/80 via-background/70 to-muted/70 p-3 shadow-md transition-colors duration-150 hover:border-primary/40 hover:shadow-lg">
      <div className="mb-2 flex items-center justify-between gap-2">
        <div className="text-sm font-semibold text-foreground">列目录：{target}</div>
        <div className="flex items-center gap-1 text-xs text-muted-foreground">
          {status === "pending" && (
            <>
              <Loader2 className="h-3 w-3 animate-spin" />
              <span>加载中</span>
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

      {error && (
        <div className="mb-2 rounded-sm border border-destructive/40 bg-destructive/10 px-2 py-1 text-xs text-destructive">
          {error}
        </div>
      )}

      {items.length === 0 ? (
        <div className="rounded-sm bg-muted/40 px-2 py-3 text-xs text-muted-foreground">
          无返回{isPending ? "，等待返回…" : ""}
          {rawResult ? `（原始：${rawResult.slice(0, 140)}…）` : ""}
        </div>
      ) : (
        <div className="grid gap-2">
          {items.slice(0, 50).map((item, idx) => (
            <div
              key={`${item.path || item.name || idx}`}
              className="flex items-center justify-between rounded-sm border border-primary/30 bg-gradient-to-br from-background/80 to-muted/70 px-2 py-1 text-xs transition-colors duration-150 hover:border-primary/60"
            >
              <div className="flex items-center gap-2">
                {item.is_dir ? (
                  <Folder className="h-3.5 w-3.5 text-primary" />
                ) : (
                  <FileIcon className="h-3.5 w-3.5 text-muted-foreground" />
                )}
                <span className="truncate" title={item.path || item.name}>
                  {item.name || item.path || "未知条目"}
                </span>
              </div>
              <div className="flex items-center gap-3 text-[11px] text-muted-foreground">
                {typeof item.size === "number" && <span>{item.size} B</span>}
                {item.mtime && <span>{String(item.mtime)}</span>}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};


import React from "react";
import { ExternalLink, Loader2, AlertCircle, Check } from "lucide-react";

type Status = "pending" | "completed" | "error" | "interrupted";

interface SearchToolPanelProps {
  status: Status;
  args: Record<string, unknown>;
  result: unknown;
  rawResult?: string | undefined;
}

type SearchItem = {
  title?: string;
  url?: string;
  content?: string;
  snippet?: string;
  source?: string;
  score?: number;
  published_date?: string;
};

function normalizeResults(result: unknown): SearchItem[] {
  if (!result) return [];
  if (typeof result === "string") return [];
  if (Array.isArray(result)) {
    return result as SearchItem[];
  }
  const obj = result as Record<string, unknown>;
  const items =
    (obj["results"] as SearchItem[]) ||
    (obj["data"] as SearchItem[]) ||
    (obj["items"] as SearchItem[]) ||
    [];
  return Array.isArray(items) ? items : [];
}

function getDomain(url?: string) {
  if (!url) return "";
  try {
    return new URL(url).hostname.replace(/^www\./, "");
  } catch {
    return "";
  }
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

export const SearchToolPanel: React.FC<SearchToolPanelProps> = ({
  status,
  args,
  result,
  rawResult,
}) => {
  const items = normalizeResults(result);
  const error = pickError(result);
  const query = typeof args?.query === "string" ? args.query : undefined;
  const isPending = status === "pending";
  const showSkeleton = isPending && items.length === 0;

  return (
    <div className="rounded-md border border-border/60 bg-gradient-to-br from-background/80 via-background/70 to-muted/70 p-3 shadow-md transition-all duration-150 hover:border-primary/50">
      <div className="mb-2 flex items-center justify-between gap-2">
        <div className="text-sm font-semibold text-foreground">
          网络搜索 {query ? `：${query}` : ""}
        </div>
        <div className="flex items-center gap-1 text-xs text-muted-foreground">
          {status === "pending" && (
            <>
              <Loader2 className="h-3 w-3 animate-spin" />
              <span>检索中</span>
            </>
          )}
          {status === "completed" && (
            <>
              <Check className="h-3 w-3 text-success" />
              <span>完成</span>
            </>
          )}
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

      {showSkeleton && (
        <div className="grid gap-2 md:grid-cols-2">
          {Array.from({ length: 4 }).map((_, idx) => (
            <div
              key={idx}
              className="animate-pulse rounded-sm border border-border bg-muted/40 px-3 py-2"
            >
              <div className="mb-2 h-3 w-3/4 rounded bg-muted" />
              <div className="mb-1 h-2 w-1/2 rounded bg-muted" />
              <div className="h-2 w-full rounded bg-muted" />
            </div>
          ))}
        </div>
      )}

      {!showSkeleton &&
        (items.length === 0 ? (
          <div className="rounded-sm bg-muted/40 px-2 py-3 text-xs text-muted-foreground">
            暂无结果
            {isPending ? "，等待返回…" : ""}
            {rawResult ? `（返回：${rawResult.slice(0, 140)}…）` : ""}
          </div>
        ) : (
        <div className="grid gap-3 md:grid-cols-2">
            {items.slice(0, 10).map((item, idx) => {
              const title = item.title || item.url || "未命名结果";
              const summary = item.snippet || item.content || "";
              const href = item.url;
              const domain = getDomain(href);
              return (
                <div
                  key={`${title}-${idx}`}
                className="group flex h-full flex-col gap-1 rounded-md border border-primary/30 bg-gradient-to-br from-background/80 via-background/70 to-muted/70 px-3 py-2 shadow-sm transition-transform duration-150 hover:-translate-y-0.5 hover:border-primary/60 hover:shadow-lg"
                >
                  <div className="flex items-start justify-between gap-2">
                    <div className="text-sm font-semibold leading-snug text-foreground">
                      {title}
                    </div>
                    {href && (
                      <a
                        className="shrink-0 text-xs text-primary hover:underline"
                        href={href}
                        target="_blank"
                        rel="noreferrer"
                        title="打开链接"
                      >
                        <ExternalLink className="h-3.5 w-3.5" />
                      </a>
                    )}
                  </div>
                  <div className="text-[11px] text-muted-foreground">
                    {domain || item.source || ""}
                    {item.published_date ? ` · ${item.published_date}` : ""}
                  </div>
                  {summary && (
                    <div className="text-xs text-foreground/80">{summary}</div>
                  )}
                  {typeof item.score === "number" && (
                    <div className="text-[11px] text-muted-foreground">
                      相关度 {item.score.toFixed(2)}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        ))}
    </div>
  );
};


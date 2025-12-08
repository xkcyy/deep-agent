import React, { useMemo } from "react";
import { Loader2, AlertCircle, CheckCircle2, Clock3 } from "lucide-react";
import { cn } from "@/lib/utils";

type Status = "pending" | "completed" | "error" | "interrupted";
type TodoStatus = "pending" | "in_progress" | "completed";

interface TodoPanelProps {
  status: Status;
  args: Record<string, unknown>;
  result: unknown;
  rawResult?: string | undefined;
}

type TodoItem = {
  id?: string;
  content?: string;
  status?: TodoStatus;
  updatedAt?: string;
};

function normalizeTodos(result: unknown): TodoItem[] {
  if (!result) return [];
  if (typeof result === "string") return [];
  if (Array.isArray(result)) return result as TodoItem[];
  const obj = result as Record<string, unknown>;
  const items = (obj["items"] as TodoItem[]) || (obj["todos"] as TodoItem[]) || [];
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

const statusColor = (s: TodoStatus | undefined) => {
  switch (s) {
    case "in_progress":
      return "bg-amber-500/15 text-amber-200 border-amber-400/50";
    case "completed":
      return "bg-emerald-500/15 text-emerald-200 border-emerald-400/50";
    default:
      return "bg-slate-500/15 text-slate-200 border-slate-400/40";
  }
};

export const TodoPanel: React.FC<TodoPanelProps> = ({
  status,
  result,
  rawResult,
}) => {
  const todos = useMemo(() => normalizeTodos(result), [result]);
  const error = pickError(result);

  const grouped = useMemo(() => {
    const map: Record<TodoStatus, TodoItem[]> = {
      pending: [],
      in_progress: [],
      completed: [],
    };
    todos.forEach((t) => {
      const st = (t.status as TodoStatus) || "pending";
      if (!map[st]) map["pending"].push(t);
      else map[st].push(t);
    });
    return map;
  }, [todos]);

  const total = todos.length;
  const done = grouped.completed.length;
  const showSkeleton = status === "pending" && todos.length === 0;

  return (
    <div className="rounded-md border border-border/60 bg-gradient-to-br from-background/80 via-background/70 to-muted/70 p-3 shadow-md transition-colors duration-150 hover:border-primary/40 hover:shadow-lg">
      <div className="mb-2 flex items-center justify-between gap-2">
        <div className="flex items-center gap-2 text-sm font-semibold text-foreground">
          <Clock3 className="h-4 w-4" />
          <span>TODO 任务</span>
          <span className="rounded-full bg-muted/50 px-2 py-0.5 text-[11px] text-foreground/80">
            {done}/{total || "?"}
          </span>
        </div>
        <div className="flex items-center gap-1 text-xs text-muted-foreground">
          {status === "pending" && (
            <>
              <Loader2 className="h-3 w-3 animate-spin" />
              <span>加载中</span>
            </>
          )}
          {status === "completed" && (
            <>
              <CheckCircle2 className="h-3 w-3 text-success" />
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
        <div className="space-y-2">
          {Array.from({ length: 3 }).map((_, idx) => (
            <div
              key={idx}
              className="animate-pulse rounded-sm border border-border/50 bg-muted/40 px-2 py-2"
            >
              <div className="h-3 w-3/4 rounded bg-muted" />
            </div>
          ))}
        </div>
      )}

      {!showSkeleton && total === 0 && (
        <div className="rounded-sm bg-muted/40 px-2 py-3 text-xs text-muted-foreground">
          暂无任务{status === "pending" ? "，等待返回…" : ""}
          {rawResult ? `（原始：${rawResult.slice(0, 140)}…）` : ""}
        </div>
      )}

      {!showSkeleton && total > 0 && (
        <div className="grid gap-3 md:grid-cols-3">
          {(["in_progress", "pending", "completed"] as TodoStatus[]).map(
            (group) => {
              const list = grouped[group];
              if (!list.length) return null;
              const titleMap: Record<TodoStatus, string> = {
                pending: "待办",
                in_progress: "进行中",
                completed: "已完成",
              };
              const color =
                group === "in_progress"
                  ? "from-amber-500/20 to-transparent border-amber-400/40"
                  : group === "completed"
                  ? "from-emerald-500/20 to-transparent border-emerald-400/40"
                  : "from-slate-500/20 to-transparent border-slate-400/40";
              return (
                <div
                  key={group}
                  className={cn(
                    "rounded-md border bg-gradient-to-br p-2 shadow-sm",
                    color
                  )}
                >
                  <div className="mb-1 flex items-center justify-between text-[11px] font-semibold uppercase tracking-wide text-foreground/80">
                    <span>{titleMap[group]}</span>
                    <span className="text-muted-foreground">{list.length}</span>
                  </div>
                  <div className="space-y-2">
                    {list.map((item, idx) => (
                      <div
                        key={item.id || idx}
                        className="rounded-sm border border-border/40 bg-background/70 px-2 py-1 text-xs text-foreground shadow-sm"
                      >
                        <div className="flex items-center justify-between gap-2">
                          <span className="truncate">{item.content || "（空）"}</span>
                          <span
                            className={cn(
                              "shrink-0 rounded-full border px-2 py-0.5 text-[11px]",
                              statusColor(item.status)
                            )}
                          >
                            {item.status || "pending"}
                          </span>
                        </div>
                        {item.updatedAt && (
                          <div className="mt-1 text-[10px] text-muted-foreground">
                            {item.updatedAt}
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              );
            }
          )}
        </div>
      )}
    </div>
  );
};


"use client";

import React, { useState, useMemo, useCallback } from "react";
import {
  ChevronDown,
  ChevronUp,
  Terminal,
  AlertCircle,
  Loader2,
  CircleCheckBigIcon,
  StopCircle,
  Search,
  FileText,
  FilePenLine,
  FileEdit,
  Folder,
  ListTodo,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { ToolCall, ActionRequest, ReviewConfig } from "@/app/types/types";
import { cn } from "@/lib/utils";
import { LoadExternalComponent } from "@langchain/langgraph-sdk/react-ui";
import { ToolApprovalInterrupt } from "@/app/components/ToolApprovalInterrupt";
import { SearchToolPanel } from "@/app/components/tool-panels/SearchToolPanel";
import { FileReadPanel } from "@/app/components/tool-panels/FileReadPanel";
import { FileWritePanel } from "@/app/components/tool-panels/FileWritePanel";
import { FileEditPanel } from "@/app/components/tool-panels/FileEditPanel";
import { LsPanel } from "@/app/components/tool-panels/LsPanel";
import { TodoPanel } from "@/app/components/tool-panels/TodoPanel";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";

interface ToolCallBoxProps {
  toolCall: ToolCall;
  uiComponent?: any;
  stream?: any;
  graphId?: string;
  actionRequest?: ActionRequest;
  reviewConfig?: ReviewConfig;
  onResume?: (value: any) => void;
  isLoading?: boolean;
}

export const ToolCallBox = React.memo<ToolCallBoxProps>(
  ({
    toolCall,
    uiComponent,
    stream,
    graphId,
    actionRequest,
    reviewConfig,
    onResume,
    isLoading,
  }) => {
    const [isDrawerOpen, setIsDrawerOpen] = useState(false);
    const [expandedArgs, setExpandedArgs] = useState<Record<string, boolean>>(
      {}
    );

    const { name, args, result, status } = useMemo(() => {
      return {
        name: toolCall.name || "Unknown Tool",
        args: toolCall.args || {},
        result: toolCall.result,
        status: toolCall.status || "completed",
      };
    }, [toolCall]);

    const parsedResult = useMemo(() => {
      if (!result) return null;
      if (typeof result !== "string") return result;
      try {
        return JSON.parse(result);
      } catch (e) {
        return result;
      }
    }, [result]);

    const statusIcon = useMemo(() => {
      switch (status) {
        case "completed":
          return <CircleCheckBigIcon />;
        case "error":
          return (
            <AlertCircle
              size={14}
              className="text-destructive"
            />
          );
        case "pending":
          return (
            <Loader2
              size={14}
              className="animate-spin"
            />
          );
        case "interrupted":
          return (
            <StopCircle
              size={14}
              className="text-orange-500"
            />
          );
        default:
          return (
            <Terminal
              size={14}
              className="text-muted-foreground"
            />
          );
      }
    }, [status]);

    const specializedPanel = useMemo(() => {
      switch (name) {
        case "internet_search":
          return (
            <SearchToolPanel
              status={status}
              args={args}
              result={parsedResult}
              rawResult={result}
            />
          );
        case "read_file":
          return (
            <FileReadPanel
              status={status}
              args={args}
              result={parsedResult}
              rawResult={result}
            />
          );
        case "write_file":
          return (
            <FileWritePanel
              status={status}
              args={args}
              result={parsedResult}
              rawResult={result}
            />
          );
        case "edit_file":
          return (
            <FileEditPanel
              status={status}
              args={args}
              result={parsedResult}
              rawResult={result}
            />
          );
        case "ls":
          return (
            <LsPanel
              status={status}
              args={args}
              result={parsedResult}
              rawResult={result}
            />
          );
        case "write_todos":
        case "todo":
          return (
            <TodoPanel
              status={status}
              args={args}
              result={parsedResult}
              rawResult={result}
            />
          );
        default:
          return null;
      }
    }, [name, status, args, parsedResult, result]);

    const hasContent =
      !!specializedPanel || !!result || Object.keys(args).length > 0;

    const toggleDrawer = useCallback(() => {
      setIsDrawerOpen((prev) => !prev);
    }, []);

    const toggleArgExpanded = useCallback((argKey: string) => {
      setExpandedArgs((prev) => ({
        ...prev,
        [argKey]: !prev[argKey],
      }));
    }, []);

    const showStatusBar =
      status === "pending" || status === "interrupted" || status === "error";

    const callStatusLabel = useMemo(() => {
      switch (status) {
        case "pending":
          return "调用中";
        case "error":
          return "调用失败";
        case "interrupted":
          return "调用中断";
        default:
          return "调用完成";
      }
    }, [status]);

    const renderIcon = () => {
      switch (name) {
        case "internet_search":
          return <Search size={16} className="text-primary" />;
        case "read_file":
          return <FileText size={16} className="text-primary" />;
        case "write_file":
          return <FilePenLine size={16} className="text-primary" />;
        case "edit_file":
          return <FileEdit size={16} className="text-primary" />;
        case "ls":
          return <Folder size={16} className="text-primary" />;
        case "write_todos":
        case "todo":
          return <ListTodo size={16} className="text-primary" />;
        default:
          return <Terminal size={16} className="text-primary" />;
      }
    };

    const summaryText = useMemo(() => {
      const tryParseArray = (obj: any): number => {
        if (!obj) return 0;
        if (Array.isArray(obj)) return obj.length;
        if (typeof obj === "object") {
          const arr =
            obj.results || obj.data || obj.items || obj.entries || obj.todos;
          return Array.isArray(arr) ? arr.length : 0;
        }
        return 0;
      };
      switch (name) {
        case "internet_search":
          return `查询：${(args?.query as string) || "—"} · 结果 ${
            tryParseArray(parsedResult) || "?"
          }`;
        case "read_file": {
          const path =
            (args?.path as string) ||
            (args?.filepath as string) ||
            (args?.file_path as string) ||
            (parsedResult as any)?.path ||
            "(未返回路径)";
          return `读文件：${path}`;
        }
        case "write_file": {
          const path =
            (args?.path as string) ||
            (args?.filepath as string) ||
            (args?.file_path as string) ||
            (parsedResult as any)?.path ||
            "(未返回路径)";
          const diffLen =
            typeof (parsedResult as any)?.diff === "string"
              ? (parsedResult as any).diff.length
              : undefined;
          const lines =
            (parsedResult as any)?.lines ??
            (Array.isArray((parsedResult as any)?.diff)
              ? (parsedResult as any)?.diff.length
              : undefined);
          return `写文件：${path} · 变更 ${
            lines ?? (diffLen ? `~${diffLen}` : "?")
          }`;
        }
        case "edit_file": {
          const path =
            (args?.path as string) ||
            (args?.filepath as string) ||
            (args?.file_path as string) ||
            (parsedResult as any)?.path ||
            "(未返回路径)";
          const lines =
            (parsedResult as any)?.lines ??
            (Array.isArray((parsedResult as any)?.diff)
              ? (parsedResult as any)?.diff.length
              : undefined);
          return `编辑：${path} · 变更 ${lines ?? "?"}`;
        }
        case "ls": {
          const path = (args?.path as string) || (args?.dir as string) || ".";
          return `目录：${path} · 项目 ${tryParseArray(parsedResult) || "?"}`;
        }
        case "write_todos":
        case "todo": {
          const total = tryParseArray(parsedResult);
          const done = Array.isArray(parsedResult)
            ? (parsedResult as any[]).filter((t) => t.status === "completed")
                .length
            : 0;
          return `任务：${done}/${total || "?"}`;
        }
        default:
          return "工具调用";
      }
    }, [name, args, parsedResult]);

    return (
      <div
        className={cn(
          "w-full overflow-hidden rounded-lg border border-border/60 bg-gradient-to-br from-background/80 via-background/70 to-muted/70 shadow-lg outline-none transition-colors duration-150 hover:border-primary/40"
        )}
      >
        {showStatusBar && (
          <div
            className={cn(
              "h-[3px] w-full",
              status === "pending" && "animate-pulse bg-primary/70",
              status === "interrupted" && "bg-orange-400/80",
              status === "error" && "bg-destructive/70"
            )}
          />
        )}
        <button
          className={cn(
            "flex w-full items-center justify-between gap-3 px-3 py-3 text-left transition-colors",
            "focus-visible:outline-none focus-visible:ring-0"
          )}
          onClick={toggleDrawer}
          disabled={!hasContent && !uiComponent && !actionRequest}
        >
          <div className="flex items-center gap-3">
            <div className="flex h-8 w-8 items-center justify-center rounded-md bg-primary/10">
              {renderIcon()}
            </div>
            <div className="flex flex-col gap-1">
              <div className="flex items-center gap-2">
                <span className="text-[14px] font-semibold tracking-[-0.3px] text-foreground">
                  {name}
                </span>
                <span
                  className={cn(
                    "rounded-full px-2 py-0.5 text-[11px] font-medium",
                    status === "completed" && "bg-emerald-500/10 text-emerald-700",
                    status === "pending" && "bg-amber-500/10 text-amber-700",
                    status === "error" && "bg-destructive/10 text-destructive",
                    status === "interrupted" &&
                      "bg-orange-500/10 text-orange-700"
                  )}
                >
                  {callStatusLabel}
                </span>
              </div>
              <div className="text-[12px] text-muted-foreground">{summaryText}</div>
            </div>
          </div>
          <div className="flex items-center gap-1 text-muted-foreground">
            {statusIcon}
            {(hasContent || uiComponent || actionRequest) && (
              <ChevronDown size={14} className="shrink-0" />
            )}
          </div>
        </button>

        <Dialog open={isDrawerOpen} onOpenChange={setIsDrawerOpen}>
          <DialogContent className="max-h-[80vh] overflow-auto bg-background/95">
            <DialogHeader>
              <DialogTitle className="flex items-center gap-2">
                {renderIcon()}
                <span>{name}</span>
                <span
                  className={cn(
                    "rounded-full px-2 py-0.5 text-[11px] font-medium",
                    status === "completed" && "bg-emerald-500/10 text-emerald-700",
                    status === "pending" && "bg-amber-500/10 text-amber-700",
                    status === "error" && "bg-destructive/10 text-destructive",
                    status === "interrupted" &&
                      "bg-orange-500/10 text-orange-700"
                  )}
                >
                  {callStatusLabel}
                </span>
              </DialogTitle>
              <DialogDescription className="text-[12px] text-muted-foreground">
                {summaryText}
              </DialogDescription>
            </DialogHeader>

            {uiComponent && stream && graphId ? (
              <div className="mt-2">
                <LoadExternalComponent
                  key={uiComponent.id}
                  stream={stream}
                  message={uiComponent}
                  namespace={graphId}
                  meta={{ status, args, result: result ?? "No Result Yet" }}
                />
              </div>
            ) : actionRequest && onResume ? (
              <div className="mt-2">
                <ToolApprovalInterrupt
                  actionRequest={actionRequest}
                  reviewConfig={reviewConfig}
                  onResume={onResume}
                  isLoading={isLoading}
                />
              </div>
            ) : specializedPanel ? (
              <div className="mt-2">{specializedPanel}</div>
            ) : (
              <div className="space-y-4">
                {Object.keys(args).length > 0 && (
                  <div className="mt-2">
                    <h4 className="mb-1 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                      Arguments
                    </h4>
                    <div className="space-y-2">
                      {Object.entries(args).map(([key, value]) => (
                        <div
                          key={key}
                          className="rounded-sm border border-border"
                        >
                          <button
                            onClick={() => toggleArgExpanded(key)}
                            className="flex w-full items-center justify-between bg-muted/30 p-2 text-left text-xs font-medium transition-colors hover:bg-muted/50"
                          >
                            <span className="font-mono">{key}</span>
                            {expandedArgs[key] ? (
                              <ChevronUp
                                size={12}
                                className="text-muted-foreground"
                              />
                            ) : (
                              <ChevronDown
                                size={12}
                                className="text-muted-foreground"
                              />
                            )}
                          </button>
                          {expandedArgs[key] && (
                            <div className="border-t border-border bg-muted/20 p-2">
                              <pre className="m-0 overflow-x-auto whitespace-pre-wrap break-all font-mono text-xs leading-6 text-foreground">
                                {typeof value === "string"
                                  ? value
                                  : JSON.stringify(value, null, 2)}
                              </pre>
                            </div>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}
                {result && (
                  <div>
                    <h4 className="mb-1 text-xs font-semibold uppercase tracking-wider text-muted-foreground">
                      Result
                    </h4>
                    <pre className="m-0 overflow-x-auto whitespace-pre-wrap break-all rounded-sm border border-border bg-muted/40 p-2 font-mono text-xs leading-7 text-foreground">
                      {typeof result === "string"
                        ? result
                        : JSON.stringify(result, null, 2)}
                    </pre>
                  </div>
                )}
              </div>
            )}
          </DialogContent>
        </Dialog>
      </div>
    );
  }
);

ToolCallBox.displayName = "ToolCallBox";

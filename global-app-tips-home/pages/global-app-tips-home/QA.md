# QA · global-app-tips-home

## 门禁

- [x] `tokens.json` + `tokens.md`
- [x] `BLOCKS.md` / `AUDIT.md` / `slice-manifest.ts`
- [x] `verify-export.py` 全部 PNG 通过
- [x] Phase 5.5 `compare/` 含 ref-* 与 impl-*
- [x] 顶栏 `cluster-lr`（消息 `margin-left: auto`）
- [x] 底栏代码 Tab，非整栏 PNG
- [x] 未使用 MCP `api/mcp/asset` 作生产 PNG

## 本地验证

```bash
cd global-app-tips-home
python3 -m http.server 8766
# 打开 http://127.0.0.1:8766/global-app-tips-home/
bash scripts/capture-compare.sh
```

## Pages

https://zwxallen818.github.io/global-app-tips-home/

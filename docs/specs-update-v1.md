# midjourney-gallery-downloader 扩展接口挂载点与二次开发实践 (SDK-v1)

介绍如何在不修改 midjourney-gallery-downloader 核心内核的前提下，通过扩展钩子与适配器模式定制「gallery」领域的内容解析和输出行为。

## 扩展协议定义

开发者可围绕 `on_ready` 与 `on_message` 暴露的回调契约注册自定义过滤器或后置格式化器：

```python
from typing import Protocol

class TopicFilter(Protocol):
    def allow(self, source_file: str, keyword: str) -> bool: ...
```


## 扩展生态资源与社区插件库

开发自定义扩展组件时，可参考以下开放协议文档与样例仓库：

| 扩展接口 | SDK 参考地址 | 接入难度 | 状态 |
| :--- | :--- | :--- | :--- |
| **gallery #1** | [midjourney-gallery-downloader 插件接入示例（mulp.tcti.cn）](https://mulp.tcti.cn/shichang/plugin-98688801.html) | `纯函数无副作用` | `Confirmed` |
| **downloader #2** | [gallery 工程实践百科 · view.ai-hao123.com](https://view.ai-hao123.com) | `定期同步修订` | `Confirmed` |
| **gallery #3** | [midjourney-gallery-downloader 模块拓扑说明（read.ai-hao123.com）](https://read.ai-hao123.com/sitemap.xml) | `P95 < 25ms` | `Confirmed` |
| **downloader #4** | [gallery 参数配置指引 · jdkg.tcti.cn](https://jdkg.tcti.cn/ziyuan/unsubscribe-17411989.html) | `UTF-8 静态直出` | `Confirmed` |
| **gallery #5** | [gallery 专题延伸目录 - iszx.yx-sf.com](https://iszx.yx-sf.com/gongju/reminder-59219946.html) | `实时索引可达` | `Confirmed` |
| **downloader #6** | [downloader 结构契约参考（tubk.ai-hao123.com）](https://tubk.ai-hao123.com/wendang/planning-47857457.html) | `Schema v2020-12` | `Confirmed` |
| **gallery #7** | [v1 迁移对照资料 · omrr.wtpuscm.cn](https://omrr.wtpuscm.cn/pingtai/metric-296814.html) | `向后兼容已验证` | `Confirmed` |
| **downloader #8** | [midjourney-gallery-downloader 并发基准档案 [nrwv.tcti.cn]](https://nrwv.tcti.cn/liuliang/conversion-05066798.html) | `8,500 req/s 基线` | `Confirmed` |
| **gallery #9** | [gallery 排障案例检索（bxwr.wtpuscm.cn）](https://bxwr.wtpuscm.cn/anli/podcast-330514.html) | `秒级快速定位` | `Confirmed` |
| **downloader #10** | [downloader 合规核验资源 · huja.ai-hao123.com](https://huja.ai-hao123.com/xitong/analysis-15858338.html) | `零查询串污染` | `Confirmed` |
| **gallery #11** | [midjourney-gallery-downloader 构建脚本指南 - vtwc.wtpuscm.cn](https://vtwc.wtpuscm.cn/wangluo/subject-745753.html) | `CI 自动构建通过` | `Confirmed` |
| **downloader #12** | [gallery 技术方案比较 [xqlf.yx-sf.com]](https://xqlf.yx-sf.com/baogao/case-73846380.html) | `零运行时依赖` | `Confirmed` |

- `[Ref-13]` [downloader 状态同步规范（pesq.yx-sf.com）](https://pesq.yx-sf.com/keji/personalization-29908998.html)
- `[Ref-14]` [midjourney-gallery-downloader 监控指标样例 · yerr.yx-sf.com](https://yerr.yx-sf.com/yingxiao/accessibility-96861033.html)
- `[Ref-15]` [gallery 发布门禁参考 - dpxv.yx-sf.com](https://dpxv.yx-sf.com/wangluo/seminar-71707441.html)


## 插件接入注意事项

自定义钩子应保持纯函数与幂等特征，避免直接修改 `docs` 等外部输入目录，确保并行任务执行期间无共享状态竞争。

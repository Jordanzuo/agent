#!/usr/bin/env python3
"""Render the three role-targeted resumes to HTML (and Markdown) from one data set.

Usage: python3 resumes/build.py
"""
import html
import re
from pathlib import Path

OUT = Path(__file__).parent

NAME = "左贤清"
PHONE = "18200539894"
CITY = "成都"
EMAILS = ["zuoxianqing@163.com", "jordanzuo20@gmail.com"]
GITHUB = "github.com/Jordanzuo"
BLOG = "博客：筑梦之队 · 简书"
STATUS = "离职（2026.08）"

XINKE = "成都辛克普雷科技有限公司"
MOQI = "成都摩奇卡卡科技有限责任公司"
LCSJ = "深圳力创世纪科技有限公司"

EDU = ("东北电力大学", "计算机科学与技术 · 学士", "2003 — 2007")

RESUMES = [
    {
        "file": "resume-zh-技术总监",
        "doc_title": "左贤清 · 技术总监",
        "role": "技术总监",
        "tagline": "研发负责人 · 游戏服务端架构",
        "accent": "#1f3a5f",
        "accent_soft": "#eaf0f7",
        "summary": [
            "19 年软件研发经验，其中 **16 年担任技术管理岗位**。长期以技术总监、合伙人身份，"
            "对技术方向、服务端体系、研发交付与商业结果负责，覆盖网页游戏、手游、SLG、卡牌与休闲等品类。"
            "擅长在老板、策划、运营、发行与研发团队之间**对齐目标、化解分歧、推动落地**："
            "既能讲清技术取舍，也能把业务诉求转化为可执行的排期与方案。",
            "最多带领约 50 人的技术团队（含运维）；在辛克普雷任合伙人兼技术总监，以小团队支撑高 DAU 在线产品。"
            "摩奇卡卡时期多款产品**月流水超千万**，《Blox World》**峰值 DAU 50 万、最高在线 1 万**。"
            "将 Cursor 引入设计、编码与 Code Review 后，审查与交付周期缩短约一个数量级，关键路径仍由人工把关。",
        ],
        "cards_title": "核心业绩",
        "cards": [
            ("商业结果", "摩奇卡卡时期负责《大主宰》《校花的贴身高手》《射雕》等产品的技术，月流水超千万；"
                      "辛克普雷《Blox World》峰值 DAU 50 万、最高在线 1 万。"),
            ("组织建设", "2009 年起担任技术总监，最多带领约 50 人的技术团队；"
                      "在辛克普雷任合伙人兼技术总监，团队最多 15 人。"),
            ("沟通协调", "长期担任技术与业务之间的接口人：向上汇报方案、风险与资源需求；"
                      "横向与策划、运营、发行对齐优先级与上线窗口；向下拆解目标、培养骨干、建立评审与反馈机制。"),
            ("平台建设", "从零搭建游戏支付平台与发行平台，最多同时支撑 10 款游戏运营，形成可复用的研发—发行—收款闭环。"),
            ("架构升级", "自研游戏服务端框架与基础库，推动团队从 C# / SQL Server / Flash 页游体系，"
                      "演进到 Golang + MySQL + Redis + Kafka 的高并发在线服务架构。"),
            ("AI 工程", "将 ChatGPT、Cursor 用于方案设计、编码与 Code Review，"
                      "审查与交付周期降低约一个数量级；并发、一致性与回滚仍由人工确认。"),
        ],
        "jobs_title": "工作经历",
        "jobs": [
            {
                "company": XINKE, "role": "合伙人 / 技术总监", "date": "2020.11 — 2026.08",
                "bullets": [
                    "合伙人兼技术总监，团队最多 15 人；负责技术方向、服务端架构与研发交付，并担任公司与业务侧的技术接口人。",
                    "带领团队研发 SLG《Dead Empire》《Invasion》《Kings Empire》、卡牌《Galaxy Legends》与休闲《Blox World》；"
                    "其中《Blox World》峰值 DAU 50 万、最高在线 1 万。",
                    "持续设计并维护服务端框架与公共类库，让多个项目在会话、玩法逻辑、数据与运维层面复用，减少重复建设。",
                    "作为管理层与研发之间的桥梁：与老板 / 合伙人对齐技术路线、成本与排期；"
                    "与策划、运营、发行协调版本节奏与资源，在质量、进度与运营诉求之间推动共识并落地。",
                    "团队管理：拆解里程碑，开展一对一辅导、技术评审与 Code Review，保障多项目并行时的稳定产出。",
                    "AI 研究与推广：将 ChatGPT、Cursor 用于方案设计、编码与代码审查；要求 AI 先给出初稿与风险清单，"
                    "并发、一致性、回滚与可观测性由人工把关。",
                ],
            },
            {
                "company": MOQI, "role": "技术总监", "date": "2013.04 — 2020.09",
                "bullets": [
                    "管理约 50 人的技术团队（含运维），负责游戏服务端、基础框架、支付与发行体系。",
                    "带领团队交付《大主宰》《校花的贴身高手》《射雕》等游戏，产品月流水超千万。",
                    "从零设计游戏服务端框架并长期维护，支撑多款产品复用同一套服务端能力。",
                    "从零搭建游戏支付平台与发行平台，打通充值、对账、渠道与发行，最多同时支撑 10 款游戏运营，减少各项目的重复对接。",
                    "主导 Golang、Git、Docker、ZooKeeper、Kafka、Redis、Elasticsearch 的调研、选型与团队推广，"
                    "完成页游技术体系向分布式、高并发在线服务的升级。",
                    "承担公司级跨部门协调：向管理层汇报技术方案、风险与人力需求；与策划、运营、发行、渠道对齐需求优先级与上线计划；"
                    "培养骨干，保障多款产品并行研发与稳定运营。",
                ],
            },
            {
                "company": LCSJ, "role": "技术总监", "date": "2009.11 — 2012.12",
                "bullets": [
                    "管理约 20 人的技术团队，研发网页游戏《王者天下》《诸子百家》等，负责服务端架构、技术交付与团队管理。",
                    "与产品、运营保持高频沟通，在版本迭代与活动排期中协调研发资源。",
                    "建立任务拆解、进度同步与问题升级机制，完成从资深开发到技术负责人的角色转换。",
                ],
            },
            {
                "company": "早期经历", "role": "软件工程师", "date": "2007.01 — 2009.10",
                "bullets": [
                    "深圳微软技术中心（2008.04 — 2009.10）：使用 C#、ASP.NET 开发多类 C/S、B/S 企业系统。",
                    "北京中软国际信息技术有限公司（2007.01 — 2008.03）：使用 C# 开发烟草行业打码到条及出入库系统。",
                ],
            },
        ],
        "skills_title": "专业技能",
        "skills": [
            ("团队管理", "最多约 50 人团队的管理与人才培养；向上、横向、向下的沟通协调"),
            ("平台与架构", "游戏服务端框架、高并发在线服务、稳定性建设；支付 / 发行平台，最多同时支撑 10 款游戏"),
            ("分布式系统", "Kafka、NATS、ZooKeeper、Redis、Elasticsearch"),
            ("语言与数据", "Golang、C#、Shell（均 10 年以上）；MySQL、Redis、MongoDB、SQL Server、TiDB"),
            ("系统与工具", "Linux、Docker、Git"),
            ("AI 工程", "ChatGPT、Cursor 用于设计、编码与 Code Review；关键路径由人工把关架构与线上风险"),
        ],
        "oss": None,
    },
    {
        "file": "resume-zh-系统架构师",
        "doc_title": "左贤清 · 系统架构师",
        "role": "系统架构师",
        "tagline": "游戏服务端架构 · 高并发在线服务",
        "accent": "#0f6b6b",
        "accent_soft": "#e6f3f3",
        "summary": [
            "19 年软件研发经验，Golang 实践超过 10 年。长期负责游戏服务端框架、基础库与平台系统的设计、演进与落地，"
            "让 SLG、卡牌、休闲等多品类、多项目复用同一套服务端能力。",
            "主导技术体系从 C# / SQL Server / Flash 页游，演进到 **Golang + MySQL + MongoDB + Redis + Kafka + ZooKeeper + Elasticsearch** "
            "的分布式高并发架构，并在辛克普雷引入 NATS 处理游戏服务端各节点间的通信；从零设计支付平台与发行平台。"
            "《Blox World》**峰值 DAU 50 万、最高在线 1 万**；摩奇卡卡时期多款产品月流水超千万。"
            "持续输出架构实践（Kafka 运维、Go 并发模型等）与开源组件（goutil、stdx、ChatServer 等）。",
        ],
        "cards_title": "架构能力与代表成果",
        "cards": [
            ("服务端框架", "从零设计并长期维护游戏服务端框架与公共类库，让多个项目在会话、玩法逻辑、数据与运维层面复用，降低重复建设。"),
            ("高并发在线服务", "支撑《Blox World》峰值 DAU 50 万、最高在线 1 万；持续进行性能优化与稳定性建设。"),
            ("分布式中间件", "摩奇卡卡阶段主导 Kafka、ZooKeeper、Redis、Elasticsearch 的调研、选型与推广；"
                        "辛克普雷阶段使用 NATS 承担游戏服务端各节点间的通信。"),
            ("平台架构", "从零搭建支付平台与发行平台，统一充值、对账、渠道与发行能力，最多同时支撑 10 款游戏运营。"),
            ("技术体系升级", "推动团队从 C# / SQL Server / Flash 页游体系，演进到 Golang + MySQL + Redis + Kafka 架构，并落地 Git、Docker 等工程基础设施。"),
            ("AI 辅助设计", "将 ChatGPT、Cursor 用于方案设计与 Code Review：AI 先出初稿与风险清单，并发、一致性、回滚与可观测性由人工复核。"),
        ],
        "jobs_title": "工作经历",
        "jobs": [
            {
                "company": XINKE, "role": "合伙人 / 技术总监（架构负责人）", "date": "2020.11 — 2026.08",
                "bullets": [
                    "负责技术方向、服务端架构与研发交付，团队最多 15 人。",
                    "持续设计并维护游戏服务端框架与公共类库，使 SLG、卡牌、休闲等多个项目在会话、玩法逻辑、数据与运维层面保持复用。",
                    "架构支撑《Dead Empire》《Invasion》《Kings Empire》《Galaxy Legends》《Blox World》；"
                    "其中《Blox World》峰值 DAU 50 万、最高在线 1 万。",
                    "使用 NATS 承担游戏服务端各节点间的通信。",
                    "将 ChatGPT、Cursor 纳入架构设计、编码与 Code Review 流程；AI 输出初稿与风险清单，并发、一致性、回滚与可观测性由人工复核。",
                ],
            },
            {
                "company": MOQI, "role": "技术总监（服务端与平台架构）", "date": "2013.04 — 2020.09",
                "tech": "Golang · C# · MySQL · Linux",
                "bullets": [
                    "从零设计游戏服务端框架，并长期维护基础框架与类库，使多款产品共享同一套服务端能力。",
                    "从零搭建游戏支付平台与发行平台，统一充值、对账、渠道对接，最多同时支撑 10 款游戏运营。",
                    "主导 Golang、Git、Docker、ZooKeeper、Kafka、Redis、Elasticsearch 的调研、选型与推广，完成页游技术体系向分布式、高并发在线服务的升级。",
                    "管理约 50 人的技术团队（含运维），推动架构规范与中间件使用标准落地。",
                ],
            },
            {
                "company": LCSJ, "role": "技术总监", "date": "2009.11 — 2012.12",
                "tech": "C# · SQL Server · Flash",
                "bullets": [
                    "负责网页游戏《王者天下》《诸子百家》等的服务端架构与技术交付，团队约 20 人。",
                ],
            },
            {
                "company": "早期经历", "role": "软件工程师", "date": "2007.01 — 2009.10",
                "bullets": [
                    "深圳微软技术中心 / 北京中软国际：使用 C#、ASP.NET 开发企业级 C/S、B/S 系统。",
                ],
            },
        ],
        "skills_title": "专业技能",
        "skills": [
            ("架构", "游戏服务端框架、高并发在线服务、性能优化、稳定性建设、分布式系统（Kafka / NATS / ZooKeeper / Redis / Elasticsearch）"),
            ("语言", "Golang（10 年以上）、C#（10 年以上）、Shell（10 年以上）；Python（脚本与小工具）"),
            ("数据库", "MySQL（10 年以上）、MongoDB、SQL Server、TiDB"),
            ("缓存与消息", "Redis（10 年以上）；Kafka；NATS"),
            ("系统", "Linux（10 年以上）、Docker、Git"),
            ("AI 工程", "Cursor、ChatGPT 用于设计、编码与 Code Review；关键路径由人工把关架构与线上风险"),
        ],
        "oss": {
            "title": "开源与技术写作",
            "items": [
                "**GitHub**（github.com/Jordanzuo）：goutil（Go 基础工具库）、stdx（Go 标准库补充类型）、ChatServer / ChatServerCenter（聊天服务端组合）。",
                "**技术博客「筑梦之队」**：Kafka 运维与重分配、Go 并发模型（G/P/M）、空值与数据有效性等。",
            ],
        },
    },
    {
        "file": "resume-zh-软件开发工程师",
        "doc_title": "左贤清 · 高级软件开发工程师",
        "role": "高级软件开发工程师",
        "tagline": "Golang 服务端 · 游戏后端",
        "accent": "#3b3f8f",
        "accent_soft": "#ecedf8",
        "summary": [
            "19 年软件开发经验，Golang、C# 均有 10 年以上生产实践。长期亲自设计、编码并维护游戏服务端框架、公共类库，"
            "以及支付与发行相关的后端系统，熟悉从需求到上线的完整交付流程。",
            "参与研发《Blox World》（**峰值 DAU 50 万、最高在线 1 万**）及多款 SLG / 卡牌游戏的服务端；"
            "摩奇卡卡时期参与《大主宰》《校花的贴身高手》《射雕》等**月流水超千万**产品的服务端与基础框架建设。"
            "早年在深圳微软技术中心使用 C#、ASP.NET 开发企业系统。"
            "持续维护个人开源库并撰写 Go、Kafka 等技术文章；日常使用 Cursor 提升编码与 Review 效率，核心逻辑与线上风险仍由人工审查。",
        ],
        "cards_title": "核心技术栈",
        "cards": [
            ("语言", "Golang（10 年以上，主力）、C#（10 年以上）、Shell；Python（脚本）"),
            ("数据库", "MySQL、MongoDB、SQL Server、TiDB"),
            ("缓存", "Redis"),
            ("消息与分布式", "Kafka、NATS、ZooKeeper、Elasticsearch"),
            ("运行与工程", "Linux、Docker、Git"),
            ("业务领域", "游戏服务端框架、会话与玩法逻辑、数据层设计、性能与稳定性、支付 / 发行后端"),
        ],
        "jobs_title": "项目与开发经历",
        "jobs": [
            {
                "company": XINKE, "role": "合伙人 / 技术总监（核心开发）", "date": "2020.11 — 2026.08",
                "bullets": [
                    "设计并维护游戏服务端框架与公共类库，供 SLG、卡牌、休闲等多个项目复用。",
                    "参与《Dead Empire》《Invasion》《Kings Empire》《Galaxy Legends》《Blox World》的服务端研发与迭代，"
                    "重点保障《Blox World》在高在线场景下的性能与稳定性。",
                    "使用 NATS 实现游戏服务端各节点间的通信。",
                    "坚持 Code Review，关注并发、一致性、回滚与可观测性；引入 Cursor 辅助设计与编码，缩短迭代周期。",
                ],
            },
            {
                "company": MOQI, "role": "技术总监（框架与平台开发）", "date": "2013.04 — 2020.09",
                "tech": "Golang · C# · MySQL · Linux",
                "bullets": [
                    "从零设计并持续维护游戏服务端框架与基础类库，供多款产品复用。",
                    "从零搭建支付平台与发行平台的后端，覆盖充值、对账与渠道对接，最多同时支撑 10 款游戏。",
                    "交付《大主宰》《校花的贴身高手》《射雕》等游戏的服务端。",
                    "参与 Golang、Git、Docker、ZooKeeper、Kafka、Redis、Elasticsearch 的调研与选型，推动页游技术体系向分布式、高并发在线服务升级。",
                ],
            },
            {
                "company": LCSJ, "role": "技术总监（服务端开发）", "date": "2009.11 — 2012.12",
                "tech": "C# · SQL Server · Flash",
                "bullets": [
                    "研发网页游戏《王者天下》《诸子百家》等的服务端逻辑与数据层，团队约 20 人。",
                ],
            },
            {
                "company": "深圳微软技术中心", "role": "软件工程师", "date": "2008.04 — 2009.10",
                "tech": "C# · ASP.NET",
                "bullets": ["开发多类 C/S、B/S 企业系统。"],
            },
            {
                "company": "北京中软国际信息技术有限公司", "role": "软件工程师", "date": "2007.01 — 2008.03",
                "tech": "C#",
                "bullets": ["开发烟草行业打码到条及出入库系统。"],
            },
        ],
        "skills_title": "工程实践",
        "skills": [
            ("代码质量", "注重模块边界与复用，将框架能力与业务逻辑分层；坚持 Code Review。"),
            ("后端经验", "熟悉游戏后端在高并发、缓存与消息流场景下的常见问题与取舍。"),
            ("AI 辅助开发", "用 Cursor、ChatGPT 产出方案与代码初稿；并发、一致性、回滚等关键路径坚持人工 Review。"),
        ],
        "oss": {
            "title": "开源与技术写作",
            "items": [
                "**goutil**：Go 基础工具库；**stdx**：Go 标准库补充类型；**ChatServer / ChatServerCenter**：聊天服务端组合。",
                "**技术博客「筑梦之队」**：Kafka 运维与重分配、Go 并发模型（G/P/M）、空值与数据有效性等。",
            ],
        },
    },
]

CSS = """
@page { size: A4; margin: 12mm 13mm; }
:root {
  --accent: %(accent)s;
  --accent-soft: %(accent_soft)s;
  --text: #1c2430;
  --muted: #5b6573;
  --line: #dde2e8;
}
* { box-sizing: border-box; }
html { background: #eef0f3; }
body {
  margin: 0;
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "Noto Sans CJK SC", "Source Han Sans SC", "WenQuanYi Micro Hei", sans-serif;
  font-size: 10pt;
  line-height: 1.55;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.sheet {
  width: 210mm;
  margin: 10mm auto;
  padding: 14mm 15mm;
  background: #fff;
  box-shadow: 0 2px 14px rgba(20, 30, 50, .12);
}
a { color: inherit; text-decoration: none; }
strong { font-weight: 650; color: #111a27; }

header.top {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 8mm;
  padding-bottom: 4.5mm;
  border-bottom: 2.2px solid var(--accent);
}
.name { margin: 0; font-size: 25pt; font-weight: 700; letter-spacing: .12em; line-height: 1.15; }
.role { margin: 1.5mm 0 0; font-size: 12.5pt; color: var(--accent); font-weight: 650; letter-spacing: .02em; }
.role span { color: var(--muted); font-weight: 400; }
.contact { text-align: right; font-size: 9pt; color: var(--muted); line-height: 1.7; }
.contact b { font-weight: 400; color: var(--text); }
.chip {
  display: inline-block;
  margin-top: 1mm;
  padding: 0 2.6mm;
  font-size: 8.5pt;
  line-height: 1.6;
  color: var(--accent);
  background: var(--accent-soft);
  border-radius: 99px;
}

section { margin-top: 5.5mm; }
h2 {
  display: flex;
  align-items: center;
  gap: 2.5mm;
  margin: 0 0 2.6mm;
  font-size: 11.5pt;
  font-weight: 700;
  letter-spacing: .08em;
  color: var(--accent);
}
h2::before { content: ""; width: 1.4mm; height: 4.4mm; border-radius: 1px; background: var(--accent); }
h2::after { content: ""; flex: 1; height: 1px; background: var(--line); }

.summary p { margin: 0 0 2mm; }
.summary p:last-child { margin-bottom: 0; }

.cards { display: grid; grid-template-columns: 1fr 1fr; gap: 2.6mm 3.4mm; }
.card {
  padding: 2.4mm 3.2mm 2.6mm;
  background: var(--accent-soft);
  border-left: 2.4px solid var(--accent);
  border-radius: 0 3px 3px 0;
  break-inside: avoid;
}
.card h4 { margin: 0 0 .8mm; font-size: 9.8pt; color: var(--accent); }
.card p { margin: 0; font-size: 9.2pt; line-height: 1.5; }

.job { margin-bottom: 4mm; break-inside: avoid; }
.job:last-child { margin-bottom: 0; }
.job-head { display: flex; justify-content: space-between; align-items: baseline; gap: 4mm; }
.job-head h3 { margin: 0; font-size: 10.6pt; font-weight: 700; }
.job-head h3 em { font-style: normal; font-weight: 500; color: var(--accent); margin-left: 2mm; }
.date { flex: none; font-size: 9.2pt; color: var(--muted); font-variant-numeric: tabular-nums; }
.tech { margin: .4mm 0 0; font-size: 8.8pt; color: var(--muted); }
.job ul, .list { margin: 1.4mm 0 0; padding-left: 4.4mm; }
.job li, .list li { margin: 0 0 .9mm; padding-left: .5mm; }
.job li::marker, .list li::marker { color: var(--accent); }

.skills { display: grid; grid-template-columns: 24mm 1fr; gap: 1.4mm 3mm; }
.skills dt { font-weight: 650; color: var(--accent); }
.skills dd { margin: 0; }

.edu { display: flex; justify-content: space-between; align-items: baseline; }
.edu .school { font-weight: 700; }
.edu .major { margin-left: 3mm; color: var(--muted); }

@media print {
  html { background: #fff; }
  .sheet { width: auto; margin: 0; padding: 0; box-shadow: none; }
  h2 { break-after: avoid; }
}
"""


def inline_html(text: str) -> str:
    escaped = html.escape(text, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)


def render_html(r: dict) -> str:
    parts = []
    parts.append(
        f"""<header class="top">
  <div>
    <h1 class="name">{NAME}</h1>
    <p class="role">{html.escape(r['role'])} <span>· {html.escape(r['tagline'])}</span></p>
  </div>
  <div class="contact">
    <div><b>{PHONE}</b> · {CITY}</div>
    <div>{EMAILS[0]} · {EMAILS[1]}</div>
    <div><a href="https://{GITHUB}">{GITHUB}</a> · {BLOG}</div>
    <span class="chip">{STATUS}</span>
  </div>
</header>"""
    )

    summary = "\n".join(f"    <p>{inline_html(p)}</p>" for p in r["summary"])
    parts.append(f'<section class="summary">\n  <h2>专业摘要</h2>\n{summary}\n</section>')

    cards = "\n".join(
        f'    <div class="card"><h4>{html.escape(t)}</h4><p>{inline_html(d)}</p></div>'
        for t, d in r["cards"]
    )
    parts.append(f'<section>\n  <h2>{html.escape(r["cards_title"])}</h2>\n  <div class="cards">\n{cards}\n  </div>\n</section>')

    jobs = []
    for j in r["jobs"]:
        tech = f'\n    <p class="tech">{html.escape(j["tech"])}</p>' if j.get("tech") else ""
        lis = "\n".join(f"      <li>{inline_html(b)}</li>" for b in j["bullets"])
        jobs.append(
            f"""  <article class="job">
    <div class="job-head"><h3>{html.escape(j['company'])}<em>{html.escape(j['role'])}</em></h3><span class="date">{j['date']}</span></div>{tech}
    <ul>
{lis}
    </ul>
  </article>"""
        )
    parts.append(f'<section>\n  <h2>{html.escape(r["jobs_title"])}</h2>\n' + "\n".join(jobs) + "\n</section>")

    skills = "\n".join(
        f"    <dt>{html.escape(k)}</dt><dd>{inline_html(v)}</dd>" for k, v in r["skills"]
    )
    parts.append(f'<section>\n  <h2>{html.escape(r["skills_title"])}</h2>\n  <dl class="skills">\n{skills}\n  </dl>\n</section>')

    if r.get("oss"):
        items = "\n".join(f"    <li>{inline_html(i)}</li>" for i in r["oss"]["items"])
        parts.append(f'<section>\n  <h2>{html.escape(r["oss"]["title"])}</h2>\n  <ul class="list">\n{items}\n  </ul>\n</section>')

    parts.append(
        f"""<section>
  <h2>教育经历</h2>
  <div class="edu"><div><span class="school">{EDU[0]}</span><span class="major">{EDU[1]}</span></div><span class="date">{EDU[2]}</span></div>
</section>"""
    )

    body = "\n\n".join(parts)
    css = CSS % {"accent": r["accent"], "accent_soft": r["accent_soft"]}
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(r['doc_title'])}</title>
<style>{css}</style>
</head>
<body>
<main class="sheet">
{body}
</main>
</body>
</html>
"""


def render_md(r: dict) -> str:
    out = [f"# {NAME}", "", f"**{r['role']} · {r['tagline']}**", ""]
    out.append(f"{PHONE} · {CITY} · {EMAILS[0]} · {EMAILS[1]}  ")
    out.append(f"GitHub：[{GITHUB}](https://{GITHUB}) · {BLOG} · **{STATUS}**")
    out += ["", "---", "", "## 专业摘要", ""]
    for p in r["summary"]:
        out += [p, ""]
    out += ["---", "", f"## {r['cards_title']}", ""]
    for t, d in r["cards"]:
        out.append(f"- **{t}**：{d}")
    out += ["", "---", "", f"## {r['jobs_title']}", ""]
    for j in r["jobs"]:
        out.append(f"### {j['company']} · {j['role']}  ")
        out.append(f"**{j['date']}**" + (f" · {j['tech']}" if j.get("tech") else ""))
        out.append("")
        out += [f"- {b}" for b in j["bullets"]]
        out.append("")
    out += ["---", "", f"## {r['skills_title']}", ""]
    out += [f"- **{k}**：{v}" for k, v in r["skills"]]
    out.append("")
    if r.get("oss"):
        out += ["---", "", f"## {r['oss']['title']}", ""]
        out += [f"- {i}" for i in r["oss"]["items"]]
        out.append("")
    out += ["---", "", "## 教育经历", "", f"**{EDU[0]}** · {EDU[1]} · {EDU[2]}", ""]
    return "\n".join(out)


def main() -> None:
    for r in RESUMES:
        (OUT / f"{r['file']}.html").write_text(render_html(r), encoding="utf-8")
        (OUT / f"{r['file']}.md").write_text(render_md(r), encoding="utf-8")
        print("wrote", r["file"])


if __name__ == "__main__":
    main()

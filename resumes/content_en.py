"""English content for the three role-targeted resumes (rendered by build.py)."""

XINKE = "Chengdu Xinkepulei Technology Co., Ltd."
MOQI = "Chengdu Moqikaka Technology Co., Ltd."
LCSJ = "Shenzhen Lichuang Shiji Technology Co., Ltd."
MS = "Microsoft Technology Center, Shenzhen"
CHINASOFT = "Beijing ChinaSoft International Information Technology Co., Ltd."

MOQI_GAMES = "*Da Zhuzai* (大主宰), *Xiaohua de Tieshen Gaoshou* (校花的贴身高手), and *She Diao* (射雕)"
LCSJ_GAMES = "*Wangzhe Tianxia* (王者天下) and *Zhuzi Baijia* (诸子百家)"

RESUMES_EN = [
    {
        "file": "resume-en-technical-director",
        "lang": "en",
        "doc_title": "Xianqing Zuo · Technical Director",
        "role": "Technical Director",
        "tagline": "Head of R&D · Game Server Architecture",
        "accent": "#1f3a5f",
        "accent_soft": "#eaf0f7",
        "summary": [
            "Engineering leader with 19 years in software R&D, **16 of them in technical management**. "
            "As Technical Director and partner, I have owned technical direction, server-side systems, delivery, "
            "and business outcomes across web games, mobile games, SLG, card, and casual titles. "
            "I align owners, designers, operations, publishing, and engineering teams, resolve disagreements, "
            "and **drive decisions through to execution**: I can explain technical trade-offs clearly "
            "and turn business requests into actionable schedules and plans.",
            "Have led teams of up to about 50 people (including operations). At Xinkepulei, served as partner and "
            "Technical Director, supporting a high-DAU online product with a small team. Moqikaka titles reached "
            "**monthly revenue above RMB 10 million**, and *Blox World* reached **500K peak DAU and 10K peak concurrent users**. "
            "Since adopting Cursor for design, coding, and code review, review and delivery cycles have shortened "
            "by roughly an order of magnitude, with humans still gating critical paths.",
        ],
        "cards_title": "Key Achievements",
        "cards": [
            ("Business Results", "At Moqikaka, owned the technology behind " + MOQI_GAMES + ", with monthly revenue above RMB 10 million. "
                                 "At Xinkepulei, *Blox World* reached 500K peak DAU and 10K peak concurrent users."),
            ("Organization", "Technical Director since 2009, leading teams of up to about 50 people. "
                             "At Xinkepulei, partner and Technical Director with a team of up to 15."),
            ("Alignment & Communication", "Long-term liaison between engineering and the business: reporting plans, risks, and resource needs upward; "
                                          "aligning priorities and launch windows with design, operations, and publishing; "
                                          "and breaking down goals, growing team leads, and building review and feedback loops downward."),
            ("Platform Building", "Built the game payment platform and publishing platform from scratch, supporting up to 10 live games at once "
                                  "and forming a reusable build–publish–collect loop."),
            ("Architecture Upgrade", "Built an in-house game server framework and base libraries, and moved the team from a C# / SQL Server / Flash "
                                     "web-game stack to a high-concurrency Golang + MySQL + Redis + Kafka architecture."),
            ("AI Engineering", "Applied ChatGPT and Cursor to solution design, coding, and code review, cutting review and delivery cycles "
                               "by roughly an order of magnitude; concurrency, consistency, and rollback are still confirmed by people."),
        ],
        "jobs_title": "Experience",
        "jobs": [
            {
                "company": XINKE, "role": "Partner / Technical Director", "date": "Nov 2020 — Aug 2026",
                "bullets": [
                    "Partner and Technical Director with a team of up to 15; owned technical direction, server-side architecture, and delivery, "
                    "and acted as the technical liaison between the company and its business side.",
                    "Led development of SLG titles *Dead Empire*, *Invasion*, and *Kings Empire*, card game *Galaxy Legends*, and casual game *Blox World*; "
                    "*Blox World* reached 500K peak DAU and 10K peak concurrent users.",
                    "Continuously designed and maintained the server framework and shared libraries so that multiple projects could reuse "
                    "the session, gameplay-logic, data, and operations layers, reducing duplicated work.",
                    "Bridged management and engineering: aligned the technical roadmap, cost, and schedule with the owner and partners; "
                    "coordinated release cadence and resources with design, operations, and publishing, building consensus among quality, schedule, and operational needs.",
                    "Team management: broke work into milestones and ran one-on-ones, technical reviews, and code reviews to keep output steady across parallel projects.",
                    "AI research and rollout: applied ChatGPT and Cursor to solution design, coding, and code review; AI produces first drafts and risk lists, "
                    "while people gate concurrency, consistency, rollback, and observability.",
                ],
            },
            {
                "company": MOQI, "role": "Technical Director", "date": "Apr 2013 — Sep 2020",
                "bullets": [
                    "Managed about 50 engineers (including operations); owned the game servers, base framework, and the payment and publishing systems.",
                    "Led delivery of " + MOQI_GAMES + "; the products reached monthly revenue above RMB 10 million.",
                    "Designed the game server framework from scratch and maintained it long term, letting multiple products share one server-side foundation.",
                    "Built the game payment platform and publishing platform from scratch, connecting top-ups, reconciliation, channels, and publishing; "
                    "supported up to 10 live games at once and removed duplicated integration work across projects.",
                    "Led research, selection, and team adoption of Golang, Git, Docker, ZooKeeper, Kafka, Redis, and Elasticsearch, "
                    "upgrading the web-game stack to distributed, high-concurrency online services.",
                    "Handled company-level cross-functional coordination: reported technical plans, risks, and headcount needs to management; "
                    "aligned priorities and launch plans with design, operations, publishing, and channels; and developed team leads "
                    "so multiple products could be built and run in parallel.",
                ],
            },
            {
                "company": LCSJ, "role": "Technical Director", "date": "Nov 2009 — Dec 2012",
                "bullets": [
                    "Managed about 20 engineers building web games including " + LCSJ_GAMES + "; owned server architecture, delivery, and team management.",
                    "Kept close, frequent contact with product and operations, coordinating engineering resources across version iterations and event schedules.",
                    "Set up task breakdown, progress syncs, and issue escalation, completing the move from senior developer to technical lead.",
                ],
            },
            {
                "company": "Earlier Experience", "role": "Software Engineer", "date": "Jan 2007 — Oct 2009",
                "bullets": [
                    MS + " (Apr 2008 — Oct 2009): built C/S and B/S enterprise systems in C# and ASP.NET.",
                    CHINASOFT + " (Jan 2007 — Mar 2008): built a carton-level coding and warehouse in/out system for the tobacco industry in C#.",
                ],
            },
        ],
        "skills_title": "Skills",
        "skills": [
            ("Team Management", "Managing and developing teams of up to about 50; upward, lateral, and downward communication and coordination"),
            ("Platform & Architecture", "Game server frameworks, high-concurrency online services, stability engineering; payment and publishing platforms supporting up to 10 games"),
            ("Distributed Systems", "Kafka, NATS, ZooKeeper, Redis, Elasticsearch"),
            ("Languages & Data", "Golang, C#, Shell (10+ years each); MySQL, Redis, MongoDB, SQL Server, TiDB"),
            ("Systems & Tools", "Linux, Docker, Git"),
            ("AI Engineering", "ChatGPT and Cursor for design, coding, and code review; people gate architecture and production risk on critical paths"),
        ],
        "oss": None,
    },
    {
        "file": "resume-en-system-architect",
        "lang": "en",
        "doc_title": "Xianqing Zuo · System Architect",
        "role": "System Architect",
        "tagline": "Game Server Architecture · High-Concurrency Online Services",
        "accent": "#0f6b6b",
        "accent_soft": "#e6f3f3",
        "summary": [
            "System architect with 19 years in software R&D and more than 10 years of Golang. Long-term owner of the design, evolution, "
            "and delivery of game server frameworks, base libraries, and platform systems, so that SLG, card, and casual titles "
            "across many projects share one server-side foundation.",
            "Led the stack's evolution from C# / SQL Server / Flash web games to a distributed, high-concurrency architecture built on "
            "**Golang + MySQL + MongoDB + Redis + Kafka + ZooKeeper + Elasticsearch**, introduced NATS at Xinkepulei for communication "
            "between game server nodes, and designed the payment and publishing platforms from scratch. "
            "*Blox World* reached **500K peak DAU and 10K peak concurrent users**; Moqikaka products reached monthly revenue above RMB 10 million. "
            "Continues to share architecture practice (Kafka operations, the Go concurrency model, and more) "
            "and open-source components (goutil, stdx, ChatServer, and more).",
        ],
        "cards_title": "Architecture Strengths & Highlights",
        "cards": [
            ("Server Framework", "Designed from scratch and long maintained the game server framework and shared libraries, letting multiple projects reuse "
                                 "the session, gameplay-logic, data, and operations layers and cutting duplicated work."),
            ("High-Concurrency Services", "Supported *Blox World* at 500K peak DAU and 10K peak concurrent users; ongoing performance tuning and stability engineering."),
            ("Distributed Middleware", "At Moqikaka, led research, selection, and adoption of Kafka, ZooKeeper, Redis, and Elasticsearch; "
                                       "at Xinkepulei, used NATS for communication between game server nodes."),
            ("Platform Architecture", "Built the payment and publishing platforms from scratch, unifying top-ups, reconciliation, channels, and publishing "
                                      "for up to 10 live games."),
            ("Stack Evolution", "Moved the team from a C# / SQL Server / Flash web-game stack to Golang + MySQL + Redis + Kafka, "
                                "and rolled out engineering foundations such as Git and Docker."),
            ("AI-Assisted Design", "Used ChatGPT and Cursor for solution design and code review: AI drafts and lists risks, "
                                   "while people review concurrency, consistency, rollback, and observability."),
        ],
        "jobs_title": "Experience",
        "jobs": [
            {
                "company": XINKE, "role": "Partner / Technical Director (Architecture Lead)", "date": "Nov 2020 — Aug 2026",
                "bullets": [
                    "Owned technical direction, server-side architecture, and delivery for a team of up to 15.",
                    "Continuously designed and maintained the game server framework and shared libraries, so SLG, card, and casual projects "
                    "reused the session, gameplay-logic, data, and operations layers.",
                    "Architected the server side of *Dead Empire*, *Invasion*, *Kings Empire*, *Galaxy Legends*, and *Blox World*; "
                    "*Blox World* reached 500K peak DAU and 10K peak concurrent users.",
                    "Used NATS for communication between game server nodes.",
                    "Brought ChatGPT and Cursor into architecture design, coding, and code review; AI produces first drafts and risk lists, "
                    "while people review concurrency, consistency, rollback, and observability.",
                ],
            },
            {
                "company": MOQI, "role": "Technical Director (Architecture)", "date": "Apr 2013 — Sep 2020",
                "tech": "Golang · C# · MySQL · Linux",
                "bullets": [
                    "Designed the game server framework from scratch and maintained the base framework and libraries long term, "
                    "letting multiple products share one server-side foundation.",
                    "Built the game payment platform and publishing platform from scratch, unifying top-ups, reconciliation, and channel integration "
                    "for up to 10 live games.",
                    "Led research, selection, and rollout of Golang, Git, Docker, ZooKeeper, Kafka, Redis, and Elasticsearch, "
                    "upgrading the web-game stack to distributed, high-concurrency online services.",
                    "Managed about 50 engineers (including operations) and drove adoption of architecture standards and middleware usage guidelines.",
                ],
            },
            {
                "company": LCSJ, "role": "Technical Director", "date": "Nov 2009 — Dec 2012",
                "tech": "C# · SQL Server · Flash",
                "bullets": [
                    "Owned server architecture and delivery for web games including " + LCSJ_GAMES + ", with a team of about 20.",
                ],
            },
            {
                "company": "Earlier Experience", "role": "Software Engineer", "date": "Jan 2007 — Oct 2009",
                "bullets": [
                    MS + " and " + CHINASOFT + ": built enterprise C/S and B/S systems in C# and ASP.NET.",
                ],
            },
        ],
        "skills_title": "Skills",
        "skills": [
            ("Architecture", "Game server frameworks, high-concurrency online services, performance tuning, stability engineering, distributed systems (Kafka / NATS / ZooKeeper / Redis / Elasticsearch)"),
            ("Languages", "Golang (10+ years), C# (10+ years), Shell (10+ years); Python for scripts and small tools"),
            ("Databases", "MySQL (10+ years), MongoDB, SQL Server, TiDB"),
            ("Cache & Messaging", "Redis (10+ years); Kafka; NATS"),
            ("Systems", "Linux (10+ years), Docker, Git"),
            ("AI Engineering", "Cursor and ChatGPT for design, coding, and code review; people gate architecture and production risk on critical paths"),
        ],
        "oss": {
            "title": "Open Source & Writing",
            "items": [
                "**GitHub** (github.com/Jordanzuo): goutil (Go utility library), stdx (supplementary types for the Go standard library), "
                "ChatServer / ChatServerCenter (a chat server pair).",
                "**Blog \"筑梦之队\" (Dream Team)**: Kafka operations and partition reassignment, the Go concurrency model (G/P/M), null values and data validity, and more.",
            ],
        },
    },
    {
        "file": "resume-en-senior-software-engineer",
        "lang": "en",
        "doc_title": "Xianqing Zuo · Senior Software Engineer",
        "role": "Senior Software Engineer",
        "tagline": "Golang Backend · Game Servers",
        "accent": "#3b3f8f",
        "accent_soft": "#ecedf8",
        "summary": [
            "Software engineer with 19 years of experience and more than 10 years of production work in each of Golang and C#. "
            "Long-term hands-on designer, implementer, and maintainer of game server frameworks, shared libraries, and "
            "payment and publishing backends, comfortable owning delivery from requirements to release.",
            "Worked on the servers of *Blox World* (**500K peak DAU, 10K peak concurrent users**) and several SLG and card games; "
            "at Moqikaka, contributed to the servers and base framework behind products such as *Da Zhuzai* (大主宰), "
            "*Xiaohua de Tieshen Gaoshou* (校花的贴身高手), and *She Diao* (射雕), which reached **monthly revenue above RMB 10 million**. "
            "Earlier, built enterprise systems in C# and ASP.NET at Microsoft Technology Center, Shenzhen. "
            "Maintains open-source libraries and writes about Go, Kafka, and more; uses Cursor daily to speed up coding and review, "
            "with core logic and production risk still reviewed by people.",
        ],
        "cards_title": "Core Tech Stack",
        "cards": [
            ("Languages", "Golang (10+ years, primary), C# (10+ years), Shell; Python for scripts"),
            ("Databases", "MySQL, MongoDB, SQL Server, TiDB"),
            ("Cache", "Redis"),
            ("Messaging & Distributed", "Kafka, NATS, ZooKeeper, Elasticsearch"),
            ("Runtime & Tooling", "Linux, Docker, Git"),
            ("Domains", "Game server frameworks, session and gameplay logic, data-layer design, performance and stability, payment / publishing backends"),
        ],
        "jobs_title": "Projects & Experience",
        "jobs": [
            {
                "company": XINKE, "role": "Partner / Technical Director (Core Developer)", "date": "Nov 2020 — Aug 2026",
                "bullets": [
                    "Designed and maintained the game server framework and shared libraries, reused across SLG, card, and casual projects.",
                    "Worked on server-side development and iteration for *Dead Empire*, *Invasion*, *Kings Empire*, *Galaxy Legends*, and *Blox World*, "
                    "with a focus on performance and stability for *Blox World* under high concurrent load.",
                    "Used NATS for communication between game server nodes.",
                    "Kept code review a habit, with attention to concurrency, consistency, rollback, and observability; "
                    "adopted Cursor to assist design and coding and shorten iteration cycles.",
                ],
            },
            {
                "company": MOQI, "role": "Technical Director (Framework & Platform)", "date": "Apr 2013 — Sep 2020",
                "tech": "Golang · C# · MySQL · Linux",
                "bullets": [
                    "Designed the game server framework and base libraries from scratch and maintained them for reuse across multiple products.",
                    "Built the backends of the payment and publishing platforms from scratch, covering top-ups, reconciliation, and channel integration, "
                    "supporting up to 10 live games.",
                    "Delivered the servers for " + MOQI_GAMES + ".",
                    "Took part in researching and selecting Golang, Git, Docker, ZooKeeper, Kafka, Redis, and Elasticsearch, "
                    "helping move the web-game stack to distributed, high-concurrency online services.",
                ],
            },
            {
                "company": LCSJ, "role": "Technical Director (Server Dev)", "date": "Nov 2009 — Dec 2012",
                "tech": "C# · SQL Server · Flash",
                "bullets": [
                    "Built server logic and the data layer for web games including " + LCSJ_GAMES + ", with a team of about 20.",
                ],
            },
            {
                "company": MS, "role": "Software Engineer", "date": "Apr 2008 — Oct 2009",
                "tech": "C# · ASP.NET",
                "bullets": ["Built enterprise C/S and B/S systems."],
            },
            {
                "company": CHINASOFT, "role": "Software Engineer", "date": "Jan 2007 — Mar 2008",
                "tech": "C#",
                "bullets": ["Built a carton-level coding and warehouse in/out system for the tobacco industry."],
            },
        ],
        "skills_title": "Engineering Practice",
        "skills": [
            ("Code Quality", "Clear module boundaries and reuse, with framework capabilities layered apart from business logic; code review as a habit."),
            ("Backend Experience", "Familiar with the common problems and trade-offs of game backends under high concurrency, caching, and message streams."),
            ("AI-Assisted Dev", "Uses Cursor and ChatGPT for solution and code first drafts; concurrency, consistency, and rollback paths are always reviewed by people."),
        ],
        "oss": {
            "title": "Open Source & Writing",
            "items": [
                "**goutil**: Go utility library; **stdx**: supplementary types for the Go standard library; **ChatServer / ChatServerCenter**: a chat server pair.",
                "**Blog \"筑梦之队\" (Dream Team)**: Kafka operations and partition reassignment, the Go concurrency model (G/P/M), null values and data validity, and more.",
            ],
        },
    },
]

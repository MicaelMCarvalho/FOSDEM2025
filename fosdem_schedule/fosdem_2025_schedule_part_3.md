# FOSDEM 2025 Schedule - Part 3 of 11

*Generated on 2025-02-01*

## Table of Contents

- [Data Analytics (13)](#data-analytics-13)
- [Declarative and Minimalistic Computing (20)](#declarative-and-minimalistic-computing-20)
- [Digital Wallets and Verifiable Credentials (8)](#digital-wallets-and-verifiable-credentials-8)
- [Distributions (16)](#distributions-16)
- [DNS (9)](#dns-9)
- [eBPF (12)](#ebpf-12)
- [Educational (14)](#educational-14)
- [Embedded, Mobile and Automotive (19)](#embedded,-mobile-and-automotive-19)

## Data Analytics (13)

### Empowering Data Analytics: High-Performance Graph Queries in DuckDB with DuckPGQ

- **Speakers:** Daniel ten Wolde
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 11:50 - 12:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4135-empowering-data-analytics-high-performance-graph-queries-in-duckdb-with-duckpgq/)

#### Abstract

In this presentation, we introduce DuckPGQ, an open-source community extension for DuckDB, an in-process analytical database system with a relational data model. DuckPGQ extends DuckDB’s capabilities to support graph processing, leveraging the property graph data model and implementing the SQL/PGQ standard. This enables users to query and analyze graph data within the familiar SQL environment. By harnessing DuckDB’s efficient in-memory architecture, DuckPGQ facilitates fast and seamless graph operations on tabular data and has been shown to outperform traditional graph databases like Neo4j on certain pattern matching queries. Additionally, DuckPGQ supports efficient execution of graph algorithms, enabling complex analytics such as PageRank and clustering operations. We’ll explore how DuckPGQ bridges the gap between relational and graph data, empowering users to perform pattern matching, path-finding, and more—all without needing specialized graph databases and from the convenience of your own laptop.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DKXDZ3/feedback/)

---

### Accelerating QuestDB: Lessons from a 6x Query Performance Boost

- **Speakers:** javier ramirez, Jaromir Hamala
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 13:10 - 13:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5214-accelerating-questdb-lessons-from-a-6x-query-performance-boost/)

#### Abstract

In this talk, we share our journey in making QuestDB, an Apache 2.0-licensed open-source time-series database, a significantly faster analytical database. Over the course of just one year, we achieved query performance gains of up to 6x by implementing specialised data structures, SIMD-based optimisations, scalable aggregation algorithms, and parallel execution pipelines.
QuestDB is designed for high-performance ingestion—processing millions of rows per second—and efficient queries over billions of rows. While it excelled in time-based queries, we found that certain generic analytical queries were slower than expected. In this session, we’ll walk through how we identified opportunities for improvement, the key changes we implemented, and how those changes delivered dramatic performance improvements in a relatively short timeframe.
We’ll demonstrate before-and-after queries to showcase the impact of these optimisations. All the code is freely available in QuestDB's GitHub repository for anyone to explore or contribute to.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CZM3P8/feedback/)

---

### ODBC Takes an Arrow to the Knee

- **Speakers:** Matthew Topol
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 13:50 - 14:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4803-odbc-takes-an-arrow-to-the-knee/)

#### Abstract

For decades, ODBC/JDBC have been the standard for row-oriented database access. However, modern OLAP systems tend instead to be column-oriented for performance - leading to significant conversion costs when requesting data from database systems. This is where Arrow Database Connectivity comes in! 
ADBC is similar to ODBC/JDBC in that it defines a single API which is implemented by drivers to provide access to different databases. The difference being that ADBC's API is defined in terms of the Apache Arrow in-memory columnar format.  Applications can code to this standard API much like they would for ODBC or JDBC, but fetch result sets in the Arrow format, avoiding transposition and conversion costs if possible.. 
This talk will cover goals, use-cases, and examples of using ADBC to communicate with different Data APIs (such as Snowflake, Flight SQL or postgres) with Arrow Native in-memory data.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GVKT9M/feedback/)

---

### Apache Arrow tensor arrays: an approach for storing tensor data

- **Speakers:** Rok Mihevc, Alenka
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 14:30 - 14:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6096-apache-arrow-tensor-arrays-an-approach-for-storing-tensor-data/)

#### Abstract

This talk introduces Apache Arrow's tensor arrays as a tool for representing an array of tensors in memory, their storage and transportation. We'll introduce the tensor array memory layout specification, its implementation in Arrow C++ and Python, showcasing how it can help interoperate with PyData and database ecosystems.
We'll present the fixed and variable shape tensor array specifications, their implementations and how they can be used to interoperate with Arrow aware ecosystem such as DLPack, NumPy, and others. Further we'll discuss design decisions we made to make the two tensor arrays as generic and universal as possible.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JXC9YE/feedback/)

---

### How we built a new powerful JSON data type for ClickHouse

- **Speakers:** Pavel Kruglov, Robert Schulze
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 14:45 - 15:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6351-how-we-built-a-new-powerful-json-data-type-for-clickhouse/)

#### Abstract

JSON has become the lingua franca for handling semi-structured and unstructured data in modern data systems. Whether it’s in logging and observability scenarios, real-time data streaming, mobile app storage, or machine learning pipelines, JSON’s flexible structure makes it the go-to format for capturing and transmitting data across distributed systems.
At ClickHouse, we’ve long recognized the importance of seamless JSON support. But as simple as JSON seems, leveraging it effectively at scale presents unique challenges. In this talk we will discuss how we built a new powerful JSON data type for ClickHouse with true column-oriented storage, support for dynamically changing data structure and ability to query individual JSON paths really fast.
ClickHouse open-source project: https://github.com/ClickHouse/ClickHouse
Links related to the topic: https://github.com/ClickHouse/ClickHouse/issues/54864, https://github.com/ClickHouse/ClickHouse/pull/58047, https://github.com/ClickHouse/ClickHouse/pull/63058, https://github.com/ClickHouse/ClickHouse/pull/66444.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RZTLHB/feedback/)

---

### volesti: sampling efficiently from high dimensional distributions

- **Speakers:** Vissarion Fisikopoulos
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 15:25 - 15:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5219-volesti-sampling-efficiently-from-high-dimensional-distributions/)

#### Abstract

Sampling from multidimensional distributions is a fundamental operation that plays a crucial role across sciences including modern machine learning and data science. An impressive number of important problems such as optimization and integration can be efficiently solved via sampling. 
This talk is an introductory tutorial on open-source software volesti, a C++ package with R and Python interfaces. volesti offers efficient implementations of state-of-the-art algorithms for sampling as well as volume computation of convex sets in high dimensions. volesti provides the most efficient implementations for sampling and volume to date allowing users to solve problems that cannot be solved with alternative  software packages.
The structure of the talk has two parts: first an introduction to volesti library and relevant background and second a tutorial that shows how volesti can be used with a focus on applications in artificial intelligence, finance and bioinformatics.

#### Related Links

- [Github](https://github.com/GeomScale/volesti)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LHL9X8/feedback/)

---

### dbt-score: a linter for your dbt model metadata

- **Speakers:** Jochem van Dooren, Matthieu Caneill
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 16:05 - 16:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4335-dbt-score-a-linter-for-your-dbt-model-metadata/)

#### Abstract

dbt (Data Build Tool) is a great framework for creating, building, organizing, testing and documenting data models, i.e. data sets living in a database or a data warehouse. Through a declarative approach, it allows data practitioners to build data with a methodology inspired by software development practices.
This leads to data models being bundled with a lot of metadata, such as documentation, data tests, access control information, column types and constraints, 3rd party integrations... Not to mention any other metadata that organizations need, fully supported through the meta parameter.
At scale, with hundreds or thousands of data models, all this metadata can become confusing, disparate, and inconsistent. It's hard to enforce good practices and maintain them in continuous integration systems. We introduce in this presentation a linter we have built: dbt-score. It allows data teams to programmatically define and enforce metadata rules, in an easy and scalable manner.
dbt-score is an open-source linter for dbt metadata. It is designed to be flexible to enforce and encourage any good practice set up by data teams. Through its CLI, data practitioners can easily obtain a maturity score of their data models, keep the metadata chaos manageable, improve consistency, and eventually deliver high-quality data.

#### Related Links

- [Github](https://github.com/PicnicSupermarket/dbt-score)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EZL8CE/feedback/)

---

### Open Source Business Intelligence - Introduction to Apache Superset

- **Speakers:** Evan Rusackas, Maxime Beauchemin
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 16:45 - 17:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4652-open-source-business-intelligence-introduction-to-apache-superset/)

#### Abstract

Open Source Business Intelligence (BI) is here, and here to win!
In this talk, we'll take a look at Apache Superset, the Apache Software Foundation (ASF)'s #1 project by GitHub stars, and learn about the features and flexibility that make it the leading tool for data visualization in the open-source data stack. We'll talk about what it does, how it works, and how it's built, highlighting its key workflows and philosophies.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CPUG7P/feedback/)

---

### Enhancing Airflow for Analytics, Data Engineering, and ML at Wikimedia

- **Speakers:** Ben Tullis, Balthazar Rouberol
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 17:25 - 17:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4867-enhancing-airflow-for-analytics-data-engineering-and-ml-at-wikimedia/)

#### Abstract

The Wikimedia Foundation supports hundreds of thousands of people around the world in creating the largest free knowledge projects in history. In order to do this we run on-premise infrastructure at significant scale, using almost exclusively free and open-source components. Our data processing and real-time analytics requirements are constantly evolving and our Data Platform Engineering teams face complex challenges in the fields of data-engineering and machine-learning, as well as the operational workload of supporting these systems in production.
Wikimedia’s data platform today runs on some of the most vital open source projects such as Hadoop, Kubernetes, Ceph, Druid, Cassandra, Spark, Hive, Iceberg, Flink, Presto, Jupyter, MariaDB, PostgreSQL, Superset, and Airflow. 
We started working with Airflow in 2019, when it was still an Apache incubator project. Over the past five years our deployments have matured and we succeeded in migrating the last of our Oozie-based workflows to Airflow in mid-2023. In addition, we offer Airflow services to other data-focused WMF engineering teams, in order to facilitate a self-service approach to data pipelines.
During 2024, the Data Platform SRE team undertook a major project to enhance our Airflow services by migrating them from bare-metal and VMs to our on-premise Kubernetes and Ceph clusters. This burgeoning integration between Airflow, Kubernetes, Spark, and Ceph has enabled us to broaden the scope and applicability of Airflow to include ML model training and data publishing workloads, plus more in future.
This is an account of how we got here, the challenges we overcame and where we plan to go from here.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UGMUAF/feedback/)

---

### Developing Custom UIs to Explore Graph Databases Using Sigma.js

- **Speakers:** Alexis Jacomy
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 18:05 - 18:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5614-developing-custom-uis-to-explore-graph-databases-using-sigma-js/)

#### Abstract

Visual exploration of graph databases is a powerful method for spotting signals and patterns not immediately visible in raw data. However, most existing tools are either too complex or heavy for business users or locked behind proprietary platforms. In visual network analysis, this complexity overload is a significant issue; while graph abstraction is powerful, it can also harm user experience if not properly managed. In this context, developing custom visual graph exploration user interfaces can be key to providing business users with workable tools.
I will present how to use sigma.js, an open-source JavaScript library for web-based network visualization, to write a dedicated web interface to explore data from RICardo, an open-data research project mapping world trade in the 19th century.

#### Related Links

- [Sigma.js](https://www.sigmajs.org/)
- [RICardo](https://ricardo.medialab.sciences-po.fr/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CQ3YJ7/feedback/)

---

### A Business Intelligence architecture for Social and Solidarity Economy.

- **Speakers:** Jordi Isidro Llobet
- **Room:** UB5.132
- **Day:** Saturday
- **Time:** 18:45 - 18:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4959-a-business-intelligence-architecture-for-social-and-solidarity-economy-/)

#### Abstract

Social and Solidarity Economy (SSE) refers to a wide range of economic activities that aim to prioritize social profitability instead of purely financial profits.
SSE organizations act guided by values ​​such as equity, solidarity, sustainability, participation, inclusion and commitment to the community, and are also promoters of social change.
There is a great diversity of entities in the Social and Solidarity Economy. Different types of activity, different sizes of the entity, different maturity of the IT teams, different quantity and quality of data, medium budgets, low budgets, etc.
The SSE, like the rest of the companies, must also make decisions based on data.
Normally the budget of the entities of the SSE is reduced, for this reason, we must facilitate intercooperation to minimize costs without reducing functionalities.
The architecture must also be adaptable to future changes within the same entity, without having to make major migrations or lose the work already done.
And, of course,
Social and Solidarity Economy 💓 Feee Software
We will set up a Business Intelligence architecture by exploring free software tools such as PostgresSQL, DBT, Airflow, Zulip, Superset, etc. to adapt to the needs of the SSE, and Ansible to facilitate replicability and inter-cooperation.

#### Related Links

- [Git repository for architecture deployment with ansible](https://git.coopdevs.org/coopdevs/bi/bi-provisioning)
- [Blog post explaining Business Intelligence for Social and Solidarity Economy (catalan)](https://coopdevs.coop/blog/el-blog-de-coopdevs-1/business-intelligence-per-a-leconomia-social-i-solidaria-12)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-analytics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-analytics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WFESLF/feedback/)

---

## Declarative and Minimalistic Computing (20)

### Introduction to Serverless Workflow DSL

- **Speakers:** Charles d'Avernas, Jean-Baptiste Bianchi, Ricardo Zanini Fernandes
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 09:00 - 09:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4494-introduction-to-serverless-workflow-dsl/)

#### Abstract

The talk, "An Introduction to Serverless Workflow DSL," will present the power and simplicity of the Serverless Workflow ecosystem—a vendor-neutral, open-source, and community-driven framework designed to redefine workflow creation in serverless environments. This high-level Domain Specific Language (DSL) reshapes the workflow landscape by offering an intuitive, imperative, and fluent approach to defining and executing workflows, removing the complexities of traditional coding and platform dependencies.
Attendees will discover how the Serverless Workflow DSL is designed for universal understanding, enabling users to quickly grasp and create even complex workflows. The session will cover its event-driven nature, with seamless integration of various formats such as CloudEvents, fostering event-driven architectures. The talk will also delve into the service-oriented design, showcasing interactions with services using standard protocols like HTTP, GRPC, OpenAPI, and AsyncAPI.
Participants will explore how the DSL supports a FaaS-centric approach, enabling the invocation of functions across platforms and facilitating microservices architectures. The discussion will include features like timely execution through workflow timeouts, fault tolerance with built-in error handling strategies, and scheduling capabilities using CRON expressions or event-based triggers. Additionally, the talk will highlight robust capabilities such as conditional branching, event handling, and looping constructs that enhance workflow complexity while promoting interoperability, scalability, and maintainability.

#### Related Links

- [Serverless Workflow Website](https://serverlessworkflow.io)
- [Serverless Workflow Repository](https://github.com/serverlessworkflow/specification)
- [Synapse - Official Serverless Workflow Runtime](https://github.com/serverlessworkflow/synapse)
- [Demo Repository](https://github.com/serverlessworkflow/fosdem-2025)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/K8XWBD/feedback/)

---

### Porting LuaRocks to Teal: Exploring the Benefits of Statically Typed Code in Lua

- **Speakers:** Victor Ilchev
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 09:20 - 09:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4506-porting-luarocks-to-teal-exploring-the-benefits-of-statically-typed-code-in-lua/)

#### Abstract

LuaRocks is a package manager for the Lua programming language. Its codebase became more and more complex as it grew, making it difficult to understand, improve on, and maintain. Teal is a statically typed dialect of Lua. The goal of introducing type annotations to the LuaRocks codebase was to help mitigate these maintenance problems, but implementing those was not as straightforward as I had imagined. In this talk, we'll discuss both the challenges and the outcomes of this transition, which led to improvements to both LuaRocks and Teal.

#### Related Links

- [LuaRocks Official Website](https://luarocks.org)
- [Teal Language](https://github.com/teal-language/tl)
- [The Google Summer of Code 2024 Proposal](https://summerofcode.withgoogle.com/programs/2024/projects/jgtBpFe8)
- [LuaRocks Blog on GSOC 2024](http://www.lua.inf.puc-rio.br/gsoc/blog2024.html)
- [The Final Pull Request](https://github.com/luarocks/luarocks/pull/1705)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RKMFVC/feedback/)

---

### rash: asynchronous shell

- **Speakers:** Niels G. W. Serup
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 09:40 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4808-rash-asynchronous-shell/)

#### Abstract

rash is a minimal shell (so like bash, but much smaller) which supports asynchronous operations by saving its program state to a file, then terminating itself, and later being started again by the user, where it will read and continue from the saved program state.
This approach achieves the same goal as running a background process and having it wait for input, but does so without burdening the operating system while not in use.  A program in rash can also be thought of as one big coroutine that gets suspended whenever needed and resumed when rerun.
Arguably, the file-based state-keeping approach also makes the system more transparent and robust, since you will never end up with a hanging process that you forgot to feed.
rash has been in active use since 2015 as a tool for writing stateful commands for a chatbot on Internet Relay Chat (IRC) channels, but may also be useful outside of IRC.
While I'll argue in the presentation that rash as an overall idea is sound, I'll also touch upon the perhaps less-than-ideal syntax that was originally picked for the language, and how we are trying to improve this now that we would like to actually present it.

#### Related Links

- [GitHub repository](https://github.com/nqpz/rash)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BN8AYC/feedback/)

---

### Moving closer to minimum with Clojure

- **Speakers:** Robert Pofuk
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 10:00 - 10:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6172-moving-closer-to-minimum-with-clojure/)

#### Abstract

In recent years, handling of supply chain vulnerabilities, becoming focus of mainstream software companies. How to deliver system that can be maintained in long run and kept secure? Can proper abstractions help us deliver large system using bare minimum external dependencies? How big of dependency tree is too big? 
This presentation will introduce how CQRS, Clojure and handful of simple libraries are enough to deliver solution that is easy to keep up to date, secure and extendable.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QAQRTV/feedback/)

---

### RDE:  Tools for managing reproducible development environments

- **Speakers:** Nicolas Graves
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 10:20 - 10:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5885-rde-tools-for-managing-reproducible-development-environments/)

#### Abstract

Developer and power user friendly GNU/Linux distribution based on GNU Guix functional package manager.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GU888D/feedback/)

---

### Minimalist web application deployment with Scheme

- **Speakers:** David Thompson
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 10:40 - 11:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5140-minimalist-web-application-deployment-with-scheme/)

#### Abstract

The web is the most accessible platform for reaching the largest amount of users. However, modern web development toolchains based on NodeJS and emscripten are anything but minimal.  Can we simplify things?  In this talk, we'll take a look at using a minimalistic toolchain written in Guile Scheme instead.
Guile has a good bootstrapping story, few dependencies, and wide availability in Linux distributions.  Guile has been usable for web server backends for years but is becoming a great choice for the frontend, too.  Hoot, developed by the Spritely Institute, is a self-contained WebAssembly toolchain and an implementation of Guile that compiles to WebAssembly.  Together, Guile and Hoot cut the gordian knot of NodeJS and emscripten.

#### Related Links

- [Hoot home page](https://spritely.institute/hoot/)
- [Hoot Git repo](https://gitlab.com/spritely/guile-hoot)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KNYFLK/feedback/)

---

### Constraint Logic Programming From The Perspective of Annotations

- **Speakers:** Jonathan McHugh
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 11:10 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6337-constraint-logic-programming-from-the-perspective-of-annotations/)

#### Abstract

Constraint Logic Programming feels magical.
Representing limitations provides interesting mechanisms for empowering a model to fill in the gaps.
This talk begins with a soft introduction to some of the underlying aspects of how this is used,
as well as pointers to how this is treated for domains such as The Closed Knights Tour and Solving N-queens.
Here is how Markus Triska (the author of CLP(FD) and CLP(ℤ) libraries) describes these concepts:
https://www.metalevel.at/knight/
https://www.metalevel.at/queens/
The remainder of the talk focuses on how CLP has been used to allow Qiuy as a recursive-modelling-language gains numerous advantages - in particular concerning being generalised so that a commensurate  UUID can be formed as a result of assigning symbolic references to numerous dimensions inherent within its annotations.
Here is a WIP written in SWI-Prolog (though in all likelihood the presentation will be in Scryer Prolog):
https://codeberg.org/indieterminacy/1q60mq-mqm_qiuy/src/branch/indieterminacy-draft/mq-mqm_qiuy-ii.pl
There will be a breakdown of how CLP is used to assign unique numbers for a notation range which Jonathan McHugh uses (which is a symbolic range of roughly a quarter of a trillion, using 2-17 characters to form an annotation).
The use of this approach has great advantages for not only treating a user's parameters like a state machine, but additionally via more general behaviours of Prolog to provide association with another users parameters (as well as other statements of facts)

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TK7XFE/feedback/)

---

### Small headed programming for performance with prescheme, nim and zig

- **Speakers:** Pjotr Prins
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 11:30 - 11:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5848-small-headed-programming-for-performance-with-prescheme-nim-and-zig/)

#### Abstract

There is a trend for compilers to become more complex, bulky and slow. Something went wrong after the introduction of Turbo Pascal in the 80s! In this talk I will advocate for using 'small headed' programming languages, i.e., languages that fit in the brain, such as Scheme and Zig. These compilers allow for immediate feedback and an interactive style of programming. A focus on programmer performance that does not lean on AI completion. I will also talk about transpiling to C with Nim and prescheme -- with examples -- that allow for targetted hardware optimizations, portability, and bootstrapping guarantees, which are relevant for today's embedded systems and high-performance-computing (HPC).

#### Related Links

- [Prescheme is a typed low-level scheme to C transpiler](https://codeberg.org/prescheme/prescheme-demo)
- [Prescheme and Nim code for the talk](https://git.genenetwork.org/presentations)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/T7RDZA/feedback/)

---

### Nim & C: Reaching the stars by standing on the shoulders of giants

- **Speakers:** Peter Munch-Ellingsen
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 11:50 - 12:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6229-nim-c-reaching-the-stars-by-standing-on-the-shoulders-of-giants/)

#### Abstract

Nim is a statically compiled type safe language with lots of modern features and a flexible macro system. in this talk we'll have a look at how Nim interfaces with C and how we can automatically have Nim import C code for zero overhead reuse of C libraries. This allows Nim to used in C-based ecosystems like FreeRTOS or as dynamic libraries, and it allows Nim to use existing high-performance libraries written in C without sacrificing performance.

#### Related Links

- [The Nim programming language](https://nim-lang.org)
- [The Futhark automatic C wrapper generator](https://github.com/PMunch/futhark)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/Q9ATHA/feedback/)

---

### Concurrent Logic Programming - an exploration of miniKanren in FLENG PCN

- **Speakers:** Sjoerd Dost
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 12:10 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6431-concurrent-logic-programming-an-exploration-of-minikanren-in-fleng-pcn/)

#### Abstract

FLENG is a concurrent logic programming language, with PCN offering a higher-level abstraction.
MicroKanren, meanwhile, is a minimalistic relational language with easy access to its fundamentals.
Implementing microKanren in FLENG offers opportunities to tinker with the core of miniKanren with minimal code modification. This talk will discuss at least the following:
- changing the delay operation to relying on using logic variables to represent possibly infinite streams.
- leveraging the built-in support for AND-parallelism to execute subgoals of disjunctions in parallel.
- extending mplus to deal with N number of streams fairly (mplusplus), instead of using a binary trampoline.
See https://github.com/deosjr/flengKanren for more

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZATPMM/feedback/)

---

### Effects Everywhere: Error Handling and Design-By-Contract in Fuzion

- **Speakers:** Fridtjof Siebert
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 12:30 - 12:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5696-effects-everywhere-error-handling-and-design-by-contract-in-fuzion/)

#### Abstract

This talk presents advances in the Fuzion languages focusing on effect handlers used to implement Fuzion's Design-by-Contract mechanism inspired by Betrand Meyer's Eiffel language.  The use of effect handlers for runtime checks gives a powerful means to handle failures at runtime and to create code that is robust in case of programming errors that would otherwise result in a crash. I will dive into the Fuzion effect mechanism and explain how this it is used to implement design-by-contract as pure syntax sugar in a way that permits error handling at runtime. While doing this, some new fun aspects of Fuzion like free types or partial application will be presented. The talk will use live demos of the presented mechanisms.
Introduction
Fuzion is a new functional and object-oriented language built on the universal concept of a Fuzion feature, a generalization of a pure function and a class. Effect handlers are used to model non-functional aspects. The principle of Design-by-Contract with pre- and post-conditions is used to formally document the requirements and guarantees of features in a way accessible to static analysis and runtime checks.
Fuzion Language Overview
Fuzion is a modern general purpose programming language that unifies concepts found in structured, functional and object-oriented programming languages into the concept of a Fuzion feature.  It combines a powerful syntax and safety features based on the design-by-contract principle with a simple intermediate representation that enables powerful optimizing compilers and static analysis tools to verify correctness aspects.
Fuzion was influenced by many other languages including Java, Python, Eiffel, Rust, Go, Lua, Kotlin, C#, F#, Nim, Julia, Clojure, C/C++, and many more.  The goal of Fuzion is to define a language that has the expressive power present in these languages and allow high-performance implementations and powerful analysis tools.  Furthermore, Fuzion addresses requirements for safety-critical applications by adding support for contracts that enable formal specification and enable detailed control over run-time checks.
Many current programming languages are getting more and more overloaded with new concepts and syntax to solve particular development or performance issues. Languages like Java/C# provide classes, interfaces, methods, packages, anonymous inner classes, local variables, fields, closures, etc.  And these languages are currently further extended by the introductions of records/structs, value types, etc.  The possibility of nesting these different concepts results in complexity for the developer and the tools (compilers, VMs) that process and execute the code.
For example, the possibility to access a local variable as part of the closure of a lambda expression may result in the compiler allocating heap space to hold the contents of that local variable.  Hence, the developer has lost control over the allocation decisions made by the compiler.
In Fuzion, the concepts of classes, interfaces, methods, packages, fields and local variables are unified in the concept of a Fuzion feature. The decision where to allocate the memory associated with a feature (on the heap, the stack or in a register) is left to the compiler just as well as the decision if dynamic type information is needed.  The developer is left with the single concept of a feature, the language implementation takes care of all the rest.
Error Handling using Effects
Faults are a run time manifestation of program errors (bugs).  Typical language mechanisms used to cause for runtime faults are functions assert or panic or exceptions like RuntimeException. Here, I will show how this is done in Fuzion using design-by-contract and effects.
Introductory Example
Consider we are writing a feature that produces a string of the form 9² = 81 for any given numeric value, we can use this code
square(x N : numeric) => "{x}² = {x*x}"

[side note: N is a free type, so the feature square is defined for any type that matches the given constraint numeric. Free types are syntax sugar for explicit type parameters as in
square(N type : numeric, x N) => "{x}² = {x*x}"

Alternatively, an implementation for a specific type, e.g., u32, would look like this
square(x u32) => "{x}² = {x*x}"

side note end]
However, this will crash somewhere in the calculation of x*x in case of an overflow, we would like to handle this case and create an error, one solution is to add error handling using panic:
square(x N : numeric) ! panic =>
  if x *! x                         # *! checks if * operation would succeed without an overflow
    "{x}² = {x*x}"
  else
    panic "overflow for $x"

square (u8 30)

Here, x *! x checks if the multiplication can be performed without causing an overflow, such that we can avoid the error and call panic explicitly.
This is, however, a little ugly since it is not clear whose fault it is if this panic would occur, is the implementation of square faulty or is the caller to blame?
Using a pre-conditions documents the requirement on the argument x clearly in the signature of the feature and puts the blame on the caller:
square(x N : numeric)
pre
  debug: x *! x
=>
  "{x}² = {x*x}"

fallible effect
Fuzion provides an abstract effect fallible with inner feature try that  takes a nullary lambda argument and produces a result on with inner feature catch that takes a lambda to be executed in case for a fault. It can be used as follows
FALLIBLE
  .try ()->
    ... code that may call FALLIBLE.cause to produce an error ...
  .catch e->
    ... code that handles fault with error `e` ...

The idea is that any effect that may fail due to some error would inherit from fallible such that there is a common way to handle this effect.
One example is the panic effect, we can now handle a panic as follows
panic.try ()->
    say (square 1000000)
  .catch s
    say "square panicked: $s"

If not run within an explicit panic.try, the default panic handler will be invoked which propagate the panic to fuzion.runtime.fault.
fallible hierarchy
Similar to Java using the class inheritance mechanism to create a hierarchy of Throwable exceptions, we would like to have a hierarchy of fallible effects. In Fuzion, this is done via default handlers that propagate to a more generic fallible, where fuzion.runtime.fault is the most generic one.
pre and post-conditions as effects
Fuzion defines a hierarchy of fallibleeffects as follows
                   fuzion.runtime.fault
                              A
                              |
                   +----------+--------------+
                   |                         |
       fuzion.runtime.contract_fault       panic
                   |
          +--------+-----------------+
          |                          |
fuzion.runtime.pre_fault    fuzion.runtime.post_fault

Pre- and post-conditions in Fuzion source code are essentially syntax sugar for code using the corresponding pre_fault and post_fault effects. The example above is de-sugared to code like this:
pre_square(x N : numeric) =>
  if !(debug: x *! x)
    fuzion.runtime.pre_fault.env.cause "debug: x *! x"

pre_and_square(x N : numeric) =>
  pre_square x
  square x

square(x N : numeric) =>
  "{x}² = {x*x}"

pre_and_square (u8 30)

Programmatic handling of faults
Now, it is possible to install handlers for a particular fallible at given points in the hierarchy, e.g., for pre_fault for preconditions only, contract_fault to handle pre_fault and post_fault, or the topmost fault to handle pre_fault, post_fault, panic and all other fallible that map to fault.
Type constraints
Using our square example with pre-condition, we see that the code does not work as expected for a float overflow:
say (square 3.2E200)

produces
3.2E200² = Infinity

instead of reporting an overflow. Using type constraints, we can specialize the code for specific type parameter values. In this example, we can extend our code to handle float differently in the pre-condition and disallow N.infinity as the result of squaring:
square(x N : numeric) ! panic
  pre
    debug: x *! x
    debug: (if N : float then x*x != N.infinity else true)
=>
  "{x}² = {x*x}"

Here, the N : float in the second precondition provides specific code for float types. The code in the following then clause sees N and all values of type N with the type constraint float, so it is possible to, e.g., access N.infinity, which is a type feature defined for float only.
Type constraints like N : float are compile time constants since a copy of square will be created for each actual type N, so these can be optimized away for all other types.
Such type constraints are extremely useful. E.g., Fuzion's base library feature Sequence contains a sort feature as follows
public sort
pre
  T : property.orderable
=>
  sort_by (<=)

the precondition ensures that sort will only be called if the element type T of the Sequence defines an order, which permits using `<='.
[side note: partial application comes to our help here. Without, the code would look like this
  sort_by (a,b -> a <= b)

]
Conclusion and Next Steps
The implementation of Design-by-Contract using effect handlers is another step to simplify the language implementation by degrading this mechanism to syntax sugar for code using effects. At the same time, this makes the language more powerful by enabling code to handle failures at runtime.
A small team of developers is working on bringing Fuzion ahead. The main focus of the work at the moment are

first real-world applications
a powerful standard library
foreign language interfaces for C and Java
improving static analyzers

Main points that are missing right now are

additional library modules for all sorts of application needs
better code optimization like inlining, specialization
highly optimizing back-ends
documentation, tutorials
more enthusiastic contributors and users!

Please feel free to contact me in case you want to use Fuzion or want to help making it a success!
Links
Fuzion portal website: https://fuzion-lang.dev
Fuzion Sources on GitHub: https://github.com/tokiwa-software/fuzion

#### Related Links

- [Fuzion portal website](https://fuzion-lang.dev)
- [Fuzion Sources on GitHub](https://github.com/tokiwa-software/fuzion)
- [Webpage with interactive examples used in the talk](https://fuzion-lang.dev/talks/fosdem25effectsEverywhere)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/V3NQMF/feedback/)

---

### The Whippet Embeddable Garbage Collection Library

- **Speakers:** Andy Wingo
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 12:50 - 13:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6066-the-whippet-embeddable-garbage-collection-library/)

#### Abstract

Whippet is a minimal, embed-only, highly parallel, pure-C garbage collection library, designed to replace Guile's use of the Boehm-Demers-Weiser collector, but designed also to be usable by other languages that might appreciate a zero-dependency, state-of-the-art upgrade to their memory manager.  In this talk we present Whippet, compare Guile-on-Whippet to Guile-on-BDW, and outline a roadmap to getting Whippet merged into Guile.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3ZT7HL/feedback/)

---

### The Shepherd: Minimalism in PID 1

- **Speakers:** Ludovic Courtès
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 13:20 - 13:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5720-the-shepherd-minimalism-in-pid-1/)

#### Abstract

Ever heard of the Shepherd? The Shepherd herds your daemons, it manages system services.  On Guix System, it’s the first user-space program that gets started: PID 1.  What’s special about the Shepherd is that it’s minimalistic and extensible: it’s written in Guile Scheme, the language also used by Guix, and its configuration file is a Scheme snippet that declares services.  Want a special type of service?  It may be that you can implement it right in your config file!
In this talk, I’ll focus on gems of the Shepherd’s internals.  Not only is it written in a high-level functional language in a space where C is dominating, it also follows an actor-style architecture powered by Fibers.  These choices bring a level of flexibility and elegance likely to bring happiness to anyone who dives in the code, as we will see.  It also brings its own challenges, sometimes even sweat and tears; I’ll also reflect on them in this talk.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ASUKDJ/feedback/)

---

### Shepherd with Spritely Goblins for Secure System Layer Collaboration

- **Speakers:** Juliana Sims
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 13:50 - 14:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5315-shepherd-with-spritely-goblins-for-secure-system-layer-collaboration/)

#### Abstract

The GNU Shepherd is being ported to Spritely's Goblins object-capability security library.  This talk will expound the project's vision, roadmap, and status.
Sharing the computational, memory, and storage resources of multiple distinct computers has been a goal in computer science for decades.  The domain has seen entries from the OS level, such as plan9, up to application-level abstractions of all kinds.  The Goblins Shepherd sits at the system layer, allowing secure collaboration across arbitrary network transport mechanisms while also providing greater security for machine-local collaboration.  While the project is still in early days, its path forward is clear.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BEZMZA/feedback/)

---

### Goblins: The framework for your next project!

- **Speakers:** Jessica Tallon
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 14:10 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5239-goblins-the-framework-for-your-next-project-/)

#### Abstract

Building peer-to-peer decentralised applications remains difficult and error-prone. Most attempts at this either abandon collaborative features entirely or fall back on centralised architectures. The Spritely Institute is working on this challenge by creating (among other things) Goblins, a Guile framework that makes secure, fault-tolerant peer-to-peer applications accessible to developers. These tools are especially valuable for developers building secure collaborative applications that aim to foster healthy online communities. This talk walks you through Goblins’ most powerful features, including the actor model, object capability security, networking, time travel debugging, and persistence.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TBPUDR/feedback/)

---

### Spritely and a secure, collaborative, distributed future

- **Speakers:** Christine Lemmer-Webber
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 14:30 - 15:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5123-spritely-and-a-secure-collaborative-distributed-future/)

#### Abstract

Spritely's vision is a world where everyone can access secure collaboration tools without gatekeepers. This requires building a new technical foundation upon which decentralized systems naturally arise. And that's exactly what we're doing! This presentation is going to look at the roadmap of what we have now, what we want for our end-users, and how we're going to get there.
Spritely's tools are also built on top of Guile Scheme. We'll take a look at how this relationship is reciporically helpful for Spritely and Guile both.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DXUBYY/feedback/)

---

### What should Teal be? - musings on FOSS project directions

- **Speakers:** Hisham Muhammad
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 15:20 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6147-what-should-teal-be-musings-on-foss-project-directions/)

#### Abstract

Here at the Declarative and Minimalistic Computing devroom, we discuss several FOSS projects -- some very small, often a wild idea being pursued by an individual (Teal started this way!), some actually pretty big, with large repositories of contributions by many people (such as Guix). The idea of minimalism is a common thread, but this can be understood as different things for different people. As a project evolves and changes to meet the needs of their users, how are the original design goals affected? 
In past talks we have discussed the origins of Teal, a programming language that aims to bring static typing to Lua programmers, while keeping a minimalist ethos, and we have also discussed its evolution. This time, let's catch up with recent developments that shipped in Teal 2024, consider the nature of user feedback received so far, and talk about in which direction should Teal 2025 and beyond go.

#### Related Links

- [Teal language](https://teal-language.org)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WFKBGJ/feedback/)

---

### Don't stand there and gawk, extend it!

- **Speakers:** Efraim Flashner
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 15:50 - 16:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4191-don-t-stand-there-and-gawk-extend-it-/)

#### Abstract

Awk was first included in Version 7 Unix in 1977 and then got a major upgrade in 1985 for Unix System V Release 3.1. After this GNU awk (gawk) was first released in 1988 and other versions of awk have also been written. It is part of the Single Unix Specification and part of the Linux Standard Base specification, so it is pretty much everywhere.
Awk uses a pattern-action structure to manipulate numbers and strings and has a lot more power than many people really use it for. With a simple, C inspired syntax it is easy to prototype larger projects or to create self-contained scripts.
Starting around gawk version 4.1.0 in 2013 the AWKPATH and AWKLIBPATH environment variables were introduced to allow adding external scripts and compiled libraries to be used to extend gawk without needing to vendor functions. Come see how easy it really is to extend gawk and create your own scripts and plugins.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NQUMZQ/feedback/)

---

### Resurrecting the minimalistic Dillo web browser

- **Speakers:** Rodrigo Arias Mallo
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 16:10 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4100-resurrecting-the-minimalistic-dillo-web-browser/)

#### Abstract

Dillo is a very fast and minimalistic graphical web browser that runs well on small computers. It has its own rendering engine and it supports a substantial subset of HTML and CSS, but it doesn't support JS. Unfortunately, the development ceased in 2017 but in late 2023 I decided to resurrect the project.
In this talk I will give a quick summary of the resurrection process and what is the current state of the project. Then, I will demonstrate live how fast is Dillo using an old netbook and explore what is capable of. This includes a tour of the new plugins for gemini, gopher, manual pages and others, some performance measurements with perf(1), energy and memory usage, as well as new features that were included recently like the new page navigation mode or zoom level.
I will also show some examples of websites that are well designed so you can read them without much difficulty on Dillo, and also the opposite.
The objective of this talk is to show that a simple web and web browser is possible.
Finally, to force ourselves to keep the browser small and simple, the next releases will continue to fit inside a floppy disk (1.44 MB) (which is monitored by the CI) and will be made available in physical format.

#### Related Links

- [Dillo Website](https://dillo-browser.github.io/)
- [Dillo repository](https://github.com/dillo-browser/dillo)
- [Mastodon](https://fosstodon.org/@dillo)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7HVXSB/feedback/)

---

### Crystal: A language for humans and computers

- **Speakers:** Johannes Müller
- **Room:** H.1308 (Rolin)
- **Day:** Sunday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6306-crystal-a-language-for-humans-and-computers/)

#### Abstract

Crystal focuses on developer happiness while still providing strong safety guarantees. It goes to great lengths to make complex concepts easy to use, taking away a lot of complexity.
For example, static typing and compilation to native code make it intrinsically type safe and blazingly fast. Yet built-in type inference makes most type annotations unnecessary, resulting in easy to read and clean code. Crystal’s runtime allows the programmer to write I/O operations as if they were blocking, but they're actually non-blocking under the hood.

#### Related Links

- [Crystal Homepage](https://crystal-lang.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-declarative:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-declarative:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DSWEQH/feedback/)

---

## Digital Wallets and Verifiable Credentials (8)

### Welcome from the OpenWallet Foundation

- **Speakers:** Digital Wallets and Verifiable Credentials FOSDEM team
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 09:00 - 09:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6213-welcome-from-the-openwallet-foundation/)

#### Abstract

Welcome session for the DevRoom by the OpenWallet Foundation (Torsten Lodderstedt)

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-wallets:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-wallets:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KKD8WR/feedback/)

---

### Utilising EUDI Wallet ecosystems in your legacy systems

- **Speakers:** Digital Wallets and Verifiable Credentials FOSDEM team, Michael Vognsen Nielsen, Thomas Rysgaard Christiansen
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 09:30 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6215-utilising-eudi-wallet-ecosystems-in-your-legacy-systems/)

#### Abstract

Many organizations within both the public sector and private sector will both see benefits and requirements in utilizing EUDI ecosystems. This includes both as issuers and relying party. Many of them operate large system landscapes that include older systems that might be hard to extend with modern prototols. They might also have a system landscape design that does not 1:1 fit the data model schemes of EUDI both in business flows and data ownership. We will describe a concept and patterns to ease implementation for large organizations that have a somewhat complex existing system landscape.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-wallets:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-wallets:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NU9APW/feedback/)

---

### We need Disposable Digital Identities for a more secure and resilient digital society

- **Speakers:** Digital Wallets and Verifiable Credentials FOSDEM team, Rob Van Kranenburg, Lorna Goulden, Friedger Müffke, Andrea D’Intino
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 10:00 - 10:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6217-we-need-disposable-digital-identities-for-a-more-secure-and-resilient-digital-society/)

#### Abstract

This presentation and demo will focus on core ideas, challenges and
developments in the area of Disposable Identities; a technical branch of Self
Sovereign Identity. We discuss core principles and requirements of Disposable
Identities and why we believe this development direction is imperative for Europe.
We will cover how this translates to EUDI ARF and Digital Wallets and touch
upon some major security issues. We demonstrate the open-source DIDroom
EUID wallet and briefly sneak preview other open-source work-in-progress to
explain why a ‘no-wallet’ approach to identity management for users should also
be considered.

#### Related Links

- [wallet implemented in/with dyne/forkbomb tech](https://didroom.com/)
- [Disposable identities; enabling trust-by-design to build more sustainable data driven value](https://www.researchgate.net/publication/354392538_Disposable_identities_enabling_trust-by-design_to_build_more_sustainable_data_driven_value)
- [Disposable Identities website](https://disposableidentities.eu)
- [Problems in the Euroepan Digital Identity](https://news.dyne.org/the-problems-of-european-digital-identity)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-wallets:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-wallets:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TLYARZ/feedback/)

---

### Are current standards enough? Towards Verifiable Credentials with expressive zero knowledge query

- **Speakers:** Jesse Wright
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5970-are-current-standards-enough-towards-verifiable-credentials-with-expressive-zero-knowledge-query/)

#### Abstract

Verifiable Credentials are quickly cropping up in a wide array of government frameworks, including across Europe, the UK, and Australia.
In this talk, we present our proposed approach to embedding the signature and selective disclosure features available in Verifiable Credentials, as a feature of specialized SPARQL-star APIs. This improves, amongst other things, the query API available.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-wallets:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-wallets:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/R8WAFN/feedback/)

---

### DarkFi: Zero-Knowledge Cryptography for Anonymous Uncensored Organizations

- **Speakers:** Amir Taaki
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 11:00 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6632-darkfi-zero-knowledge-cryptography-for-anonymous-uncensored-organizations/)

#### Abstract

ZK proofs allow us to prove a statement such as "the majority of participants has voted to approve the proposal" without revealing any information about any single person. This allows us to recreate services we commonly use but in a strongly privacy-preserving way.
In all spheres of free software, this cryptographic technique has been under-utilized but enlocks untapped design spheres. For free software to innovate, it should explore this realm of strong p2p & anonymous software using modern cryptography.
Our project has created:

Strong anonymous & p2p chat with no linkability between messages providing plausible deniability.
Anon & p2p organizations able to manage a treasury.
Task management and other p2p org software replacing GitHub and other source control systems
Anonymous payments

This talk is about ZK with a focus on applications.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-wallets:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-wallets:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QN3WNQ/feedback/)

---

### Trustchain - Trustworthy Decentralised Public Key Infrastructure

- **Speakers:** Tim Hobson, Pamela Wochner, Sam Greenbury
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 11:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5283-trustchain-trustworthy-decentralised-public-key-infrastructure/)

#### Abstract

The sharing of public key information is central to the digital credential security model, but the existing Web PKI with its opaque Certification Authorities and synthetic attestations serves a very different purpose. We propose a new approach to decentralised public key infrastructure, designed for digital identity, in which connections between legal entities that are represented digitally correspond to genuine, pre-existing relationships between recognisable institutions. In this scenario, users can judge for themselves the level of trust they are willing to place in a given chain of attestations. Our proposal includes a novel mechanism for establishing a root of trust in a decentralised setting via independently-verifiable timestamping. We also present an open source reference implementation built on open networks, protocols and standards. The system has minimal setup costs and is freely available for any community to adopt as a digital public good.

#### Related Links

- [Trustchain docs](https://alan-turing-institute.github.io/trustchain/)
- [Trustchain repository](https://github.com/alan-turing-institute/trustchain/)
- [Trustchain Mobile repository](https://github.com/alan-turing-institute/trustchain-mobile)
- [Trustchain journal article (open access)](https://arxiv.org/abs/2305.08533)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-wallets:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-wallets:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AVSHJR/feedback/)

---

### Sample implementation of OpenId 4 Verifiable Presentation over Bluetooth Low Energy

- **Speakers:** Sebastian Kałuzinśki
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 12:00 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6575-sample-implementation-of-openid-4-verifiable-presentation-over-bluetooth-low-energy/)

#### Abstract

This talk will demonstrate sample integration of OpenId 4 Verifiable Presentation over Bluetooth Low Energy using Nordic Semicondutor's BLE library with protobuf as a medium of transportation. 
Expected length:
Short - 20 min

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-wallets:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-wallets:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XTZZZY/feedback/)

---

### Challenges for Wallets and Digital Trust Services following EUDI Wallet Architecture Reference Framework

- **Speakers:** Digital Wallets and Verifiable Credentials FOSDEM team, Vangelis Sakkopoulos, Connor Fitzmaurice
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 12:30 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6220-challenges-for-wallets-and-digital-trust-services-following-eudi-wallet-architecture-reference-framework/)

#### Abstract

Featuring DG CNECT and NiScy, this is a deep dive into the Reference Implementation for digital identification, authentication and electronic signatures based on common standards across the European Union.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-wallets:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-wallets:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TTJBRZ/feedback/)

---

## Distributions (16)

### Boot from network attached devices using mkosi-initrd (or why systemd distributions should really start considering mkosi-initrd)

- **Speakers:** Antonio Alvarez Feijoo
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 09:00 - 09:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4644-boot-from-network-attached-devices-using-mkosi-initrd-or-why-systemd-distributions-should-really-start-considering-mkosi-initrd-/)

#### Abstract

mkosi-initrd is a wrapper built on top of mkosi to build initrds using distribution packages (i.e., without picking files from the host filesystem or injecting custom functionality during the boot process). While booting from local devices mostly works out of the box, this talk aims to demonstrate that it is also possible to boot from network attached devices, setting up Network Manager and using NFS and iSCSI as examples. We want to show how the complex (and sometimes hacky) functionality implemented in traditional initrd generators can be translated using a systemd-only approach, and prove that these features can be shipped (and thus maintained) by their respective packages, and not by the initrd generator.
This work is part of the mkosi-initrd enablement on openSUSE (https://en.opensuse.org/Mkosi-initrd).

#### Related Links

- [mkosi](https://github.com/systemd/mkosi)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RXN3G7/feedback/)

---

### Flatcar and Gentoo sitting in a tree - A collaboration of distributions

- **Speakers:** James "Chewi" Le Cuirot
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 09:30 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4763-flatcar-and-gentoo-sitting-in-a-tree-a-collaboration-of-distributions/)

#### Abstract

Flatcar is a Linux distribution for running container workloads that was originally derived from CoreOS, ChromiumOS, and Gentoo. Today, its maintainers not only draw directly from Gentoo, but also contribute directly back to Gentoo as well. Come and learn about how this relationship has evolved, how we've already benefited from each other's work, and what we plan to work on next. This ever-growing synergy has even led to us sharing a stand together at FOSDEM this year.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TU9UTL/feedback/)

---

### Rust, RPMs, and the Fine Art of Dependency Bundling

- **Speakers:** Daniel Mellado, Mikel Olasagasti
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 10:00 - 10:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5570-rust-rpms-and-the-fine-art-of-dependency-bundling/)

#### Abstract

Managing Rust dependencies in linux distributions packaging often involves navigating a tangled web of missing packages, mismatched versions, and the need to patch vendored crates manually. In this talk, we’ll explore a solution to simplify this process in RPM based distros by enhancing the rust2rpm tool to automate the patching and repackaging of vendored dependencies.
Even though the main approach is to have every dependency packaged, it often becomes really difficult to achieve that goal as you may find yourself out in a dependency hell situation where you'll have to deal with an outstanding number of them. Even if its a compromise you can bundle dependencies, but that comes with some drawbacks.
When packaging, you may often find yourself in a situation where you'll  have to patch rpm's on the fly to fix out issues, but that's not really doable when you're working with bundled dependencies.
We'll discuss about introducing a new -p flag in rust2rpm, which enables users to easily apply patches to vendored crates (like fiat-crypto), modify dependencies, and repackage them without the need for manual steps.
We’ll also discuss a more flexible approach using a new helper tool, rust2rpm-vendor, that allows maintainers to prepare and patch vendor tarballs independently, automating the entire workflow from patch application to repacking.
This talk will show how these enhancements can help alleviate "dependency hell" in Fedora’s Rust ecosystem, making it easier for maintainers to handle vendored crates and improve the overall Rust packaging experience.
Links
- rust2rpm on Pagure

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/Z3U7M3/feedback/)

---

### Fedora Silverblue With Disk Encryption: How I Almost Lost Everything But Gained Much Wisdom (Side Story: Bmaptool And Ddrescue: Why One Should Never Ever Use Dd)

- **Speakers:** Marcel Ziswiler
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6348-fedora-silverblue-with-disk-encryption-how-i-almost-lost-everything-but-gained-much-wisdom-side-story-bmaptool-and-ddrescue-why-one-should-never-ever-use-dd-/)

#### Abstract

While testing different RADXA ROCK 5B board boot options, I inadvertently typed sudo dd of=/dev/nvme0n1 on my notebook! While recovering I learned one too many things which one supposedly should know when running a modern distro like Fedora Silverblue with disk encryption. This talk covers some lessons learned from using Fedora Silverblue as a daily driver and outlines what modifications might make sense during installation and what parts you might want to have backed up to avoid a similar disastrous shocking moment from happening. As a side story, I cover why using dd is a really bad idea and what better options to consider.

#### Related Links

- [Disk Encryption User Guide](https://docs.fedoraproject.org/en-US/quick-docs/encrypting-drives-using-LUKS/)
- [Bmaptool](https://github.com/yoctoproject/bmaptool)
- [Ddrescue](https://www.gnu.org/software/ddrescue/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XBKK7M/feedback/)

---

### Packit: Bridging the Gap Between Fedora and openSUSE

- **Speakers:** František Lachman, Dan Čermák
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 11:00 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5794-packit-bridging-the-gap-between-fedora-and-opensuse/)

#### Abstract

The Linux world thrives on collaboration, yet distribution-specific tooling can create barriers. Packit, a CI/CD solution originally created for Fedora, is tearing down these walls by now supporting other distributions as well. Thanks to Google Summer of Code contributions, Packit now integrates with the Open Build Service (OBS), enabling support for openSUSE and other distributions.
We’ll dive into the new capabilities possible thanks to the OBS integration and demonstrate how openSUSE developers can now take full advantage of Packit's automation features — whether you're maintaining packages or managing the CI/CD pipeline for an upstream project.
Whether you're a Fedora maintainer, an openSUSE contributor, or simply curious about next generation CI/CD solutions, this talk will give you insights into the practical advantages and real-world applications of Packit's growing toolset!

#### Related Links

- [Official packit Website](https://packit.dev/)
- [packit git repository](https://github.com/packit/packit)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CQREMD/feedback/)

---

### CentOS Stream and the Power of SIGs: KDE, Hyperscale, and Beyond

- **Speakers:** Troy Dawson
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 11:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5616-centos-stream-and-the-power-of-sigs-kde-hyperscale-and-beyond/)

#### Abstract

CentOS Stream is a unique Linux distribution built by Red Hat Enterprise Linux (RHEL) engineers, serving as a preview of the next minor version of RHEL and a contribution path to RHEL itself. But CentOS Stream is much more than just a stepping stone to RHEL. CentOS Project's Special Interest Groups (SIGs) are expanding the platform in all sorts of interesting ways, including live KDE images, tweaks for hyperscale deployments, immutable CoreOS builds, and so much more.
Come and learn how CentOS relates to Fedora, how it's built, how it's tested and released, the new CentOS Stream 10 release (yay!), and how you can get involved!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JJBMYM/feedback/)

---

### From Manul to Kitten: 4 years of AlmaLinux development evolution

- **Speakers:** Andrew Lukoshko
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 12:00 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5472-from-manul-to-kitten-4-years-of-almalinux-development-evolution/)

#### Abstract

On the dates of FOSDEM 2025, we get to celebrate exactly 4 years since the release of the very first beta version of AlmaLinux. All this time, the development process has been constantly improving, new ideas have been incorporated, and our tools have been replaced with more efficient and advanced ones. In this presentation, I will share our experience in developing our distribution and related services around it, and tell you how we made certain decisions depending on emerging needs and external factors in order to continue to deliver and improve a high-quality distribution that is trusted by both small firms and large corporations in more than 70 countries, and on more than 1 million devices around the world.

#### Related Links

- [AlmaLinux website](https://almalinux.org)
- [AlmaLinux wiki](https://wiki.almalinux.org)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RVYFT7/feedback/)

---

### a tale of several distros joining forces for a common goal: reproducible builds

- **Speakers:** Jelle van der Waa, Holger Levsen, kpcyrd
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 12:30 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6479-a-tale-of-several-distros-joining-forces-for-a-common-goal-reproducible-builds/)

#### Abstract

For more than ten years the Reproducible Builds project has worked towards reproducible builds of many projects and for ten years we have build many packages twice, with maximal variations applied, to see if they can be build reproducible still.
But that's just theory. In practice we want to rebuild and try to match the packages a distro distributes. rebuilderd is the tool to do this and has been in use for Arch Linux since 2020 and for Debian since 2024.
This talk will explain what's shared between reproducing Arch Linux and Debian, what's different and what challenges are still laying ahead until users of either distro will benefit from reproducible builds.
Developers from Debian and Arch Linux will present this talk together.

#### Related Links

- [Reproducible Builds website](https://reproducible-builds.org)
- [Arch Linux rebuilderd instance](https://reproducible.archlinux.org/)
- [Debian rebuilderd instance](https://reproduce.debian.net)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KXZKQL/feedback/)

---

### openSUSE: Engineering Stable Rolling Releases with OBS and openQA

- **Speakers:** Dan Čermák
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 13:00 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5671-opensuse-engineering-stable-rolling-releases-with-obs-and-openqa/)

#### Abstract

The openSUSE project stands out in the Linux ecosystem by offering a diverse range of distributions: the rolling release distribution openSUSE Tumbleweed, the stable/fixed release openSUSE Leap distribution and Slowroll, a slowed down version of Tumbleweed. While all openSUSE distributions are RPM-based, their tooling is vastly different to all other RPM-based distributions. What enables the project to deliver a stable rolling distro along with many spins, container images and more given its limited resources? Is it the different build systems? Or maybe it's a different approach to packaging? Or is it the automated testing pipeline or something else entirely?
This talk dives into the unique build system, automated testing pipeline and general workflows that empower openSUSE. We'll explore the Open Build Service (OBS) and openQA, demonstrating how they enable a small team to achieve impressive results.

#### Related Links

- [openSUSE Homepage](https://www.opensuse.org/)
- [openSUSE Download Page](https://get.opensuse.org/)
- [Open Build Service git repository](https://github.com/openSUSE/open-build-service/)
- [openQA Homepage](https://open.qa)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VH87VK/feedback/)

---

### Being different takes Aeons - a tale of the endless RC?

- **Speakers:** Richard Brown
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 13:30 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5895-being-different-takes-aeons-a-tale-of-the-endless-rc-/)

#### Abstract

Aeon Desktop is an exciting new take on Desktop Linux, aiming to provide a fully functioning Desktop OS without the need for hands on management, tinkering, or any of the other distractions that come with 'traditional' Linux desktops.
However, getting this exciting new take into a quality that can be considered "Released" is taking it's sweet time, with Aeon now beginning it's 3rd year of being in a "Release Candidate" Stage.
This talk will share tales of that journey, exploring how distribution projects can start with relatively simple, tightly defined goals, and yet still find themselves challenged to adapt as technologies shift around them.
It will also discuss how the influence of existing distributions can both help and hinder new distributions and challenge the audience to perhaps reevaluate how they interact with distribution projects as a result.
Finally, it will question what does "Release Quality" mean really in the context of community distributions and end with an open discussion for the audience to share their expectations and opinions as to when a community-driven distribution can consider itself 'Ready' vs 'In Development'

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7FU8X8/feedback/)

---

### How to push your testing upstream

- **Speakers:** Sam Thursfield
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 14:00 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4805-how-to-push-your-testing-upstream/)

#### Abstract

Quality assurance is the final stage of testing a distro release, where you boot a real OS image, and use the keyboard and mouse to navigate the system. Several distributions have adopted openQA and os-autoinst which can automate much of this work, allowing QA testing to happen every time a package updates, instead of just at release time.
Increased downstream testing is great for upstreams, but for developers to work efficiently, we need quick feedback between publishing a change and discovering what broke. In many cases we still don't get issue reports upstream until weeks or months after a merge request landed.
What's missing? Let's look at the remaining pain points around QA in the Linux OS world. Then we’ll look at research happening in the GNOME project to bring QA testing all the way to the merge request pipelines in GNOME Gitlab, so we can find integration issues as they happen.
We’ll also touch on how systemd-sysext allows testing built artifacts in an OS in a distro-independent way. And we’ll look at how changes in openQA could mean that QA teams in different companies can join forces to build testsuites once, instead of everyone working separately to maintain their own.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7KFESF/feedback/)

---

### Fixing CVEs on Debian: _almost_ everything you should know about it

- **Speakers:** Carlos Henrique Lima Melara
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 14:30 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6354-fixing-cves-on-debian-almost-everything-you-should-know-about-it/)

#### Abstract

Have you ever asked yourself how your free and open source operating system keeps you safe from known security vulnerabilities? Should you proactively do something about it? Actually, is your operating system safe? Can you help making it more secure?
Let's talk about how Debian deals with security vulnerabilities in order to keep its users safe, how security fixes are applied and how these fixes get to users' machine. The idea is to give a general overview of how vulnerability management is conducted in Debian and why one can feel safe using Debian.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7JH8HF/feedback/)

---

### Enabling Architectural Features in Debian: PAC and BTI on arm64

- **Speakers:** Emanuele Rocca
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 15:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5517-enabling-architectural-features-in-debian-pac-and-bti-on-arm64/)

#### Abstract

Arm processors provide two security features called Pointer Authentication
(PAC) and Branch Target Identification (BTI). They are designed to mitigate
Return-Oriented Programming (ROP) and Jump-Oriented Programming (JOP) security
exploits respectively. Enabling features such as PAC and BTI in a Linux
distribution entails modifications all across the board, from the Kernel to the
C library and compiler. Further, all packages need to be rebuilt with a
specific compiler flag in order for the features to be enabled.
This talk presents the integration work done so far in Debian, how we are
monitoring enablement progress, and the tasks ahead.

#### Related Links

- [PAC/BTI on the Debian Wiki](https://wiki.debian.org/ToolChain/PACBTI)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FFE3AJ/feedback/)

---

### Rhino Linux and Pacstall: Towards a Rolling Ubuntu

- **Speakers:** Oren Klopfer, A. Salt
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 15:30 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4398-rhino-linux-and-pacstall-towards-a-rolling-ubuntu/)

#### Abstract

What if Ubuntu embraced a Rolling Release model? This might seem contradictory: Ubuntu typically follows a long-term support model with fixed, point-based releases, where packages remain stable at certain versions. In contrast, a rolling release model, commonly used by distributions based off of Arch Linux, requires ongoing, continuous package updates. While Ubuntu's standard model adheres to stability, it maintains a development branch called devel, akin to Debian's sid branch, on which it is based, and often even receiving updates sooner. While long-term support models prioritize security, rolling release models often cater more to user customization and development needs.
The idea to create a rolling release variant for Ubuntu first manifested in the form of the Rolling Rhino script in 2020, which allowed users to convert/upgrade their existing installs of Ubuntu to the devel branch, turning their familiar Ubuntu environments into Rolling Rhino ones. This concept was taken a step further in 2022, when a group of young developers turned it into a full-fledged fan flavour for Ubuntu, Rolling Rhino Remix, which included the notable addition of two utilities: rhino-config, which allowed users to switch from Ubuntu’s LTS kernel to the mainline or real-time kernels, and rhino-update, which served as a wrapper script for updating all APT and Snap packages on the system.
Rolling Rhino Remix evolved rapidly that year, undergoing numerous upgrades and integrations, with a particular focus on enhancing package management capabilities. The rhino-update utility added support for components such as Nala (a libapt-pkg front-end alternative), Flatpak, and most importantly, the Pacstall package manager. As the project evolved, it outgrew the simple Ubuntu flavour concept, transforming into a dynamically designed developer distribution, which led to the creation of Rhino Linux.
One of the key distinctions between Rhino Linux and its predecessors is the full integration of the Pacstall package manager for handling much of the distribution’s core utilities and applications, such as the kernel, web browser, and IDE. Additionally, the distribution ships with the rhino-pkg utility, the successor to rhino-update, which serves as a wrapper script for Pacstall, APT, Flatpak, and Snap, while also extending beyond just updates, allowing users to search and install from all at once.
Pacstall brings the package flexibility of Arch Linux’s AUR to Ubuntu and Debian, using pacscripts (similar to Arch's PKGBUILDs) to build .deb packages. With Pacstall, users can install from the community-maintained repository or source out-of-repository .deb packages, effectively making a stable Ubuntu base more adaptable to a rolling model. While Pacstall is available for almost all Ubuntu and Debian based distributions, Rhino Linux is built with Pacstall in mind from the ground up - and in consequence, the developer teams for Rhino Linux and Pacstall have largely crossed over.
In this talk, two core team members will explore the history and technical foundation of both Rhino Linux and the Pacstall package manager, outline future directions, and, perhaps most importantly, share the challenges faced and insights gained from developing these projects as a small, student-led team.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DWKMZB/feedback/)

---

### The Ubuntu patch pilot program

- **Speakers:** Athos Ribeiro
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 16:00 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6270-the-ubuntu-patch-pilot-program/)

#### Abstract

The Ubuntu patch pilot program is designed to make contributing to Ubuntu a welcoming and inspiring experience while fostering community knowledge and maintaining ongoing contributions. Through this program we provide the community with mentoring and support in getting patches into Ubuntu.
Join some Ubuntu core developers in this session to get an overview of the Ubuntu development process and understand how patches land in the distribution. We will discuss the differences between changing a stable and a development version of Ubuntu and how those are done through the patch pilot program.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MBQPME/feedback/)

---

### Building the Future: Understanding and Contributing to Immutable Linux Distributions

- **Speakers:** Jorge Gomez
- **Room:** H.1302 (Depage)
- **Day:** Sunday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5027-building-the-future-understanding-and-contributing-to-immutable-linux-distributions/)

#### Abstract

Immutable Linux distributions are transforming how we think about system stability and security. This talk explores four such distributions: Fedora Silverblue, NixOS, rde, and Vanilla OS. Attendees will learn how immutable operating systems enhance system reliability through atomic updates and rollback capabilities, while understanding the trade-offs in terms of flexibility and customization. We'll examine how each distribution approaches package management, system configuration, and developer workflows. Whether you're a system administrator, developer, or Linux enthusiast, you'll come away understanding which immutable distribution might best suit your needs and how to contribute to these projects through code, documentation, or community support.

#### Related Links

- [Fedora Silverblue](https://fedoraproject.org/atomic-desktops/silverblue/)
- [rde](https://trop.in/rde/)
- [Vanilla OS](https://vanillaos.org/)
- [NixOS](https://nixos.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-distributions:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-distributions:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UFNPHT/feedback/)

---

## DNS (9)

### getaddrinfo sucks, everything else is much worse

- **Speakers:** Valentin Gosu
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 15:00 - 15:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4229-getaddrinfo-sucks-everything-else-is-much-worse/)

#### Abstract

Historically, Firefox has relied on the getaddrinfo API for DNS resolution on most platforms. However, due to inherent limitations — such as the missing Time-To-Live (TTL) information — we sometimes had to resort to alternative APIs like DNSQuery_A on Windows.
When implementing DNS over HTTPS (DoH), we developed our own DNS parser, which allowed Firefox to also resolve TXT and HTTPS records. But DoH isn't available to all our users.
With HTTPS records becoming increasingly important, we decided to resolve HTTPS queries using system APIs like DNSQuery_A, res_query, res_nquery, and android_res_query, with the expectation that this would cover all supported platforms. This talk will delve into the lessons learned from this journey and explain why these platform specific APIs often fall short of expectations.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-dns:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-dns:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PMRZ9A/feedback/)

---

### Catalog Zones in the PowerDNS Recursor (TALK REPLACES CANCELLED TALK)

- **Speakers:** Otto Moerbeek, Kevin P. Fleming
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 15:25 - 15:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6804-catalog-zones-in-the-powerdns-recursor-talk-replaces-cancelled-talk-/)

#### Abstract

Catalog Zones in the PowerDNS Recursor

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-dns:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-dns:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZCQUVD/feedback/)

---

### DNS for enterprise domains: FreeIPA and Samba AD experience

- **Speakers:** Alexander Bokovoy
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 15:50 - 16:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4307-dns-for-enterprise-domains-freeipa-and-samba-ad-experience/)

#### Abstract

Active Directory-like deployments rely heavily on working DNS infrastructure. FreeIPA project handles this by providing an integrated DNS server based on Bind 9. Samba Active Directory also uses Bind 9, although in a different style. While both are capable to use an external DNS server infrastructure, ability to kickstart a whole enterprise environment from scratch with an integrated DNS server is valuable to administrators, as practice does show.
The talk will reflect on FreeIPA and Samba teams' experience on DNS requirements these Kerberos-dependent and certificate-heavy environments do have.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-dns:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-dns:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3Y7DNA/feedback/)

---

### NetBox DNS - Single source of truth for DNS

- **Speakers:** Peter Eckel
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 16:15 - 16:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4245-netbox-dns-single-source-of-truth-for-dns/)

#### Abstract

I started with the question "how can I make managing DNS more user friendly for a customer" and the discovery of a small plugin for NetBox and ended up as the maintainer of a moderately complex and increasingly powerful DNS management tool.
The talk will touch the core features of the plugin:
* Validation of names and values
* Automatic generation of NS, SOA and PTR records
* Zone and record templates
* Handling of RFC2317 zones
* Automatic generation of DNS address records for IPAM IP addresses

#### Related Links

- [Project Page in GitHub](https://github.com/peteeckel/netbox-plugin-dns)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-dns:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-dns:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YD8JNN/feedback/)

---

### rDNS Map In Your Hands

- **Speakers:** Alexey Milovidov
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 16:40 - 17:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6466-rdns-map-in-your-hands/)

#### Abstract

I've created an rDNS map, available at https://reversedns.space/, and I want to tell you how.
It was not hard to do, but there was a lot of unusual and amusing stuff in the process.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-dns:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-dns:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BB8UDC/feedback/)

---

### Prove website, domain, and network ownership

- **Speakers:** Mark Overmeer
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 17:05 - 17:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6572-prove-website-domain-and-network-ownership/)

#### Abstract

In an attempt to increase security and reduce spam, website services ask for more proofs.  Most services require you to confirm your email address, but nowadays, some services also demand a proof of domain ownership.  Sometimes you need to prove write access to a website.  Registration gets much harder, and we have to do it so often.  Time to rethink.
We have been used to creating usernames for three decades by now, but the practice has reached it limits: users need to do much more to get access to a service.  A tiny simplification is offered via OpenID ("Login via Google"), but the new Open Console project offers a more integrated solution to build a trust relation between a person and a service provider.
In Open Console, a person (or group) collects personal (and group) facts, and can share them with the requirements of the service.  When the service only needs a proven email-address, it only gets that email address, not your name.  The negotiation about which data is delivered is totally transparent and far more diverse.
Besides personal facts, many different kinds of proofs can be maintained, like a proof of website-ownership.  You only need to prove ownership once, and this can be shared with any service which requires it.
Proving website ownership is not easy. The focus of this talk is on the process of establishing this proof. There are many complications in checking the validity of a website. We implemented different approaches for this proof (via DNS, HTML-meta, and file).  We would also like to discuss the possible proofs of domain and network (ip-range) ownership with the participants: how to express them in DNS.
Open Console received support from NGI OpenWebSearch.EU and the NLnet Foundation.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-dns:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-dns:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/J3EQFS/feedback/)

---

### Modern zone replication using LMDB and Lightning Stream

- **Speakers:** Kevin P. Fleming
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 17:30 - 17:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4197-modern-zone-replication-using-lmdb-and-lightning-stream/)

#### Abstract

As a follow up to my award-winning FOSDEM 2023 talk "Hosting your own DNS for 'fun' and zero profit", I'll provide an update covering my experiences using Lightning Stream for zone replication between PowerDNS authoritative servers.
Lightning Stream offers significant advantages over traditional database-style replication (typically using relational databases like MariaDB and PostgreSQL), including simpler configuration, easier troubleshooting, and the ability to add/remove cluster members without having to reconfigure existing cluster members (providing a very loosely coupled 'cluster').
PowerDNS
Lightning Stream
MinIO
LMDB

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-dns:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-dns:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/URSSGT/feedback/)

---

### How to make BIND 9 fast(er)

- **Speakers:** Ondřej Surý
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 17:55 - 18:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4626-how-to-make-bind-9-fast-er-/)

#### Abstract

This talk will be focused on the software engineering techniques that we are using or plan to use to bring the BIND 9 into 21 century to scale better, use less memory and overall have improved design to utilize the modern CPU architecture.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-dns:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-dns:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TEM77G/feedback/)

---

### Honey, I shrunk DNSdist

- **Speakers:** Remi Gacogne
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 18:20 - 18:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4991-honey-i-shrunk-dnsdist/)

#### Abstract

As a DNS proxy with extensive support for DNS encryption protocols, DNSdist seemed like a very good choice to support DoT, DoH and DoQ on embedded devices running OpenWrt.
This is the story of how we completely underestimated the challenges of the embedded world, and managed in the end to make DNSdist's footprint small enough to provide end-to-end, encrypted DNS service to your home.

#### Related Links

- [DNSdist's website](https://dnsdist.org/)
- [DNSdist's code in the PowerDNS repository](https://github.com/PowerDNS/pdns/tree/master/pdns/dnsdistdist)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-dns:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-dns:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XXMVZZ/feedback/)

---

## eBPF (12)

### The state of eBPF docs

- **Speakers:** Dylan Reimerink
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 15:00 - 15:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4641-the-state-of-ebpf-docs/)

#### Abstract

eBPF is a big and complicated topic. For years it was common that the people using and writing eBPF programs were also the people involved in the development of eBPF. Those days are somewhat behind us now, eBPF is more popular than ever, and the number of non-kernel experts wanting to use eBPF is growing rapidly.
A lot of new people means a lot of learning to be done. There is a small but strong community of people to talk to, if you know how to find them. The internet is full of outdated articles that have aged like milk. The kernel has docs for a handful of subjects and man pages that are correct for some kernel versions but not others.
I started the eBPF docs project about two years ago out of frustration for the lack of comprehensive documentation. These docs are now hosted at docs.ebpf.io. Lets take a look at the state of these docs, what it took to get here and where they are going next.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ebpf:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ebpf:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7G7Y8P/feedback/)

---

### bpftrace: a path to the ultimate Linux tracing tool

- **Speakers:** Viktor Malik
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 15:20 - 15:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4967-bpftrace-a-path-to-the-ultimate-linux-tracing-tool/)

#### Abstract

We present bpftrace [1], a tracing tool for Linux based on eBPF which comes with a simple domain-specific language, "bpfscript". The language offers a convenient way to write eBPF tracing programs, without the need to dive deep into the complexities of eBPF. This makes bpftrace suitable as the entry point into the eBPF world. In addition, the terse nature of the language facilitates on-the-fly writing of very powerful short programs (so-called "one-liners") specifically tailored at the user's immediate tracing purposes.
Where bpftrace has struggled in the past, is writing complex tools which are intended to run and be maintained for a prolonged period of time. This has recently started to change with the introduction of many new bpfscript features such as variable and type declarations, user-defined functions, and more.
Ultimately, our goal is to make bpftrace the number one choice for most tracing tasks on Linux. In this talk, I will guide you through our way to achieve that - the current state of the project, the latest significant additions, and the planned future work.
No prior knowledge of eBPF or bpftrace is required for this talk. A basic understanding or a prior experience with Linux tracing is helpful.
[1] https://github.com/bpftrace/bpftrace/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ebpf:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ebpf:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DZTHS3/feedback/)

---

### Bpftrace OOM Profiler

- **Speakers:** Samuel Blais-Dowdy
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 15:40 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4402-bpftrace-oom-profiler/)

#### Abstract

Scuba, a real-time data ingestion system similar to Elasticsearch, is often experiencing memory pressure as part of normal operations. The pressure is sometimes overwhelming, leading to OOM (out-of-memory) issues. These are difficult to track in user space as the symptoms of such issues are only visible in kernel space (SIGKILL, kernel oom killer). This talk will highlight how we leveraged bpftrace to monitor our service and help bridge our observability gap.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ebpf:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ebpf:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZXD83F/feedback/)

---

### Auto-instrumentation for GPU performance using eBPF

- **Speakers:** Annanay Agarwal, Marc Tuduri
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 16:00 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5162-auto-instrumentation-for-gpu-performance-using-ebpf/)

#### Abstract

Modern AI workloads rely on large GPU fleets whose efficient utilisation is crucial due to high costs. However, gathering telemetry from these workloads to optimise performance is challenging because it requires manual instrumentation and adds performance overheads. Further, it does not produce telemetry in a standardised format for commonly used visualisation tools like Prometheus.
This talk explores the potential of leveraging eBPF to capture CUDA calls made to GPUs, including kernel launches and memory allocations. Data from these probes can be used to export Prometheus metrics, facilitating detailed analysis of kernel launch patterns and associated memory usage. This approach offers significant benefits as eBPF imposes minimal overhead and requires no intrusive instrumentation. Our implementation is also open-source and available on GitHub.

#### Related Links

- [Grafana Beyla (eBPF instrumentation) Github Link](https://github.com/grafana/beyla/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ebpf:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ebpf:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ANQMYV/feedback/)

---

### Extracting reliable data for short-lived processes using eBPF for Linux Security Threat Analysis

- **Speakers:** Ankit Garg, Meghna Vasudeva, Lakshmy A V
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 16:20 - 16:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6173-extracting-reliable-data-for-short-lived-processes-using-ebpf-for-linux-security-threat-analysis/)

#### Abstract

Endpoint Detection and Response (EDR) solutions continuously monitor the events occurring on an endpoint, create detailed process timelines, and analyse these data, to reveal suspicious patterns that could indicate threats such as ransomware. To create these detailed timelines, EDR solutions collect a variety of information about each process running on the endpoint, such as timestamp, PID, process name, path, command line, etc. On Linux systems, this is often done using the proc filesystem provided by the operating system, which provides rich information for each process currently running on the system.
However, if a process is short-lived and exits quickly, the proc filesystem entries for it get cleared out before the EDR solution can read them, leading to incomplete timelines. To take a simple example, suppose a malicious actor runs a script that downloads a binary from the network and then executes it. This downloaded binary quickly spawns a bunch of long-running malicious processes and exits itself. If EDR solution is unable to extract the complete process information about the execution of the downloaded binary from proc filesystem (being a short-lived process), it'll miss details about the creator of the malicious process in the system. Hence, EDR solution will have visibility gaps about the downloaded binary required for Security Threat Analysis. 
We propose a solution to address the gaps by attaching extended Berkeley Packet Filter (eBPF) programs dynamically to the Linux kernel system calls (such as fork, exec and exit) and extracting all the required information directly from the kernel hooks using BPF Type Format (BTF). These hooks use fundamental task structure in kernel representing a process or thread to extract variety of information about the process. Our proof of concept shows that eBPF-based process data extraction provides process timelines with near 100% reliability, compared to proc filesystem-based approaches which have a reliability of only around 83% for short lived processes.

#### Related Links

- [GitHub Repo holding the Proof of Concept for the work done in proposal](https://github.com/mevasude/ebpf-short-lived-processes-data-extraction)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ebpf:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ebpf:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QD33DF/feedback/)

---

### Latest kprobe and uprobe development

- **Speakers:** Jiri Olsa
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 16:40 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6260-latest-kprobe-and-uprobe-development/)

#### Abstract

I'll give an update on the latest development from kprobe and uprobe
world including new session feature and uprobe performance enhancements
that already got merged and those that are still being worked on.

#### Related Links

- [linux kernel](https://kernel.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ebpf:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ebpf:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GXNJ8C/feedback/)

---

### Performance evaluation of the Linux kernel eBPF verifier

- **Speakers:** Julia Lawall, Maxime Derri
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 17:00 - 17:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6453-performance-evaluation-of-the-linux-kernel-ebpf-verifier/)

#### Abstract

Integrated in the Linux kernel since 2014, eBPF has allowed the creation of a large variety of projects (observability, security, network, etc.). Unlike kernel modules, eBPF programs can be loaded by unprivileged users. The Linux kernel is protected by a static analyzer, called the eBPF verifier, which verifies that eBPF programs cannot harm the kernel and respect required security properties. Recently, several research works have shown that the eBPF verifier, which is a critical component, is not sound. This means that programs which should be rejected are accepted by the verifier, allowing unprivileged users to run malicious programs (e.g [1,2,3,4,5]). In this talk, we propose to evaluate the performance of the eBPF verifier through the measurement of three main aspects:


Performance evaluation: to understand the evolution of the eBPF verifier versions, we evaluated the verification time and consumed memory of six eBPF verifier versions (Linux kernel 5.0 to 6.8, both included). The results show that for some eBPF programs, the verifiers have nearly the same verification times (except for the conditional jumps, where the verification time has decreased since the introduction of the bounded loops in the Linux kernel 5.3). Consumed memory remains also stable.


Comparative evaluation with PREVAIL: as the eBPF verifier is not sound, we compared it to PREVAIL, which is another verifier proposed in 2019 at the PLDI conference. PREVAIL is a sound verifier that runs in user space and is used in the eBPF infrastructure of Windows. On the one hand, we were interested in the implementation differences between the two verification solutions and on the other hand, we observed the performance difference between the two verifiers. We observed that, although PREVAIL's performance has improved, it remains less efficient than the eBPF verifier. Nevertheless, PREVAIL showed that it can efficiently verify programs containing a lot of paths (implied by conditional jumps) thanks to the join operator and the fixpoint computation used for the bounded loops, where the eBPF verifier would have created a lot of paths, trying to reduce them with pruning.


Impact of compilers: beyond the verification mechanisms, there are external constraints such as the compilers: An eBPF program is first compiled into eBPF bytecode and then analyzed. However, we observed that for the eBPF verifier with a specific eBPF program, which varies only by its number of loop iterations, Clang-8 produced more programs accepted by the eBPF verifier and these programs are verified faster than those produced by Clang-14.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ebpf:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ebpf:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RZGAB3/feedback/)

---

### Mitigating Bugs in the Linux eBPF Verifier using Rust- or PREVAIL-based Layered Verification

- **Speakers:** Luis Gerhorst
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 17:20 - 17:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5095-mitigating-bugs-in-the-linux-ebpf-verifier-using-rust-or-prevail-based-layered-verification/)

#### Abstract

The eBPF verifier has repeatedly suffered from bugs in its verification
algorithm which enable malicious applications to perform container escapes and
privilege escalation. To improve upon this, existing work applies fuzzing (Chaignon'24)
and formal methods (Agni) to the verifier in order to find and fix bugs. However,
in the mid-term, these approaches are unlikely to result in a verifier that is
fully bug-free. While academic works have proposed the use of hardware-based
isolation (MOAT, Hive, SafeBPF) and software-fault isolation (BeeBox) to mitigate verifier bugs,
these approaches suffer from portability issues, require significant
design-changes with unclear consequences, or have runtime overheads.
Motivated by the shortcomings of the existing approaches, this talk discusses an
alternative approach to prevent verifier-bugs from being exploited. By requiring
eBPF bytecode to be compiled from safe Rust source code by a trusted systems
service, program-safety would effectively be checked twice by two very different
static analyzers (i.e., rustc's compiler passes and the eBPF verifier). Therefore, a bug in one of
the analyzers will no longer directly result in a kernel exploit as the other
analyzer is unlikely to exhibit the same buggy behavior and therefore still
catch malicious programs. This approach is appealing as it is unlikely to result in runtime
overheads and does not require significant changes to the kernel.
We analyze whether this is a viable approach to mitigate bugs in the eBPF
verifier, taking runtime-overheads, expressiveness, and security into
consideration. Specifically, we analyze whether past bugs in rustc and the eBPF
verifier could have been chained together in order to exploit the proposed
design as a whole.
We find that the fundamental flexibility of the Rust-IR-to-eBPF mapping allows attackers to still exploit the system as a whole. We also investigate whether using the alternative PREVAIL eBPF verifier would prevent a similar attack, but find that there exists a simple construction that allows attackers to combine exploits for the individual verifiers into an exploit that works for the verifiers when chained together.

#### Related Links

- [Safe Rust program that circumvents the checks in rustc and the Linux eBPF verifier](https://github.com/luisgerhorst/sust)
- [Discussion on layered verification using PREVAIL](https://github.com/vbpf/ebpf-verifier/discussions/824)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ebpf:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ebpf:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/P99QYK/feedback/)

---

### Building your eBPF Program with Rust and Aya

- **Speakers:** Daniel Mellado
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 17:40 - 18:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5534-building-your-ebpf-program-with-rust-and-aya/)

#### Abstract

eBPF (Extended Berkeley Packet Filter) is revolutionizing the way developers interact with the Linux kernel, enabling them to run user-defined programs in a highly efficient and safe manner. 
This session will introduce you to Aya, a modern Rust-based eBPF library. Unlike traditional eBPF libraries such as libbpf and bcc, Aya is built entirely in Rust and leverages the libc crate for syscalls, offering a clean, lightweight, and efficient interface for eBPF development.
In this session, we’ll explore how Aya simplifies the eBPF programming workflow, including features like BTF (BPF Type Format) support, which enables programs to run across different kernel versions without needing recompilation.
You’ll learn how Aya’s architecture ensures fast deployment and builds, with no need for a kernel build, compiled headers, or even a C toolchain. The result is a streamlined, "compile once, run everywhere" solution that allows you to easily deploy a single self-contained binary across different Linux distributions and kernel versions.
We'll cover that by using a sample XDP program  where we'll be covering aya we'll go across and explain how to use  aya components such as aya_log_ebpf or aya_ebpf to bootstrap the code and how our dev and build environment looks like.
Whether you’re new to eBPF or an experienced kernel developer, this session will provide you with the tools and insights to leverage the full power of eBPF using Rust and Aya in your next project.
Links:

Aya on GitHub
bpfman on GitHub

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ebpf:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ebpf:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XVN8YY/feedback/)

---

### Five silly things to do when benchmarking your BPF program

- **Speakers:** Dmitrii Dolgov
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 18:00 - 18:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4294-five-silly-things-to-do-when-benchmarking-your-bpf-program/)

#### Abstract

The Hitchhiker's Guide to the Galaxy has following to say about benchmarking:
avoid, if at all possible. One of the reasons is that it's hard and often
counterintuitive, another -- it attracts Ravenous Bugblatter Beasts.
Despite all those dangers it's still an important and underappreciated topic, and
in this talk I would like to discuss cases when unexpected results arise from
benchmarking of BPF programs and why they could be important. Kernel selftest
benchmarks would serve as an example, but we will vary the load generation to
produce different arrival distributions, introduce contention on tracepoints,
or simulate swarm of network connections in user space. To make it easier, we
will use home-grown tool Berserker,
which was created with an intent to exercise real world BPF applications.

#### Related Links

- [Project URL](https://github.com/stackrox/berserker/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ebpf:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ebpf:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RZFFVW/feedback/)

---

### Writing a Minimal Scheduler with eBPF, sched_ext, and C

- **Speakers:** Johannes Bechberger
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 18:20 - 18:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4458-writing-a-minimal-scheduler-with-ebpf-schedext-and-c/)

#### Abstract

Today, eBPF is used for software-defined networking, observability, monitoring tools, and more. Previously, creating these was labor-intensive and had a high barrier to entry. With the new scheduler extensions, we can now add custom schedulers to this list. Sched_ext allows us to write schedulers with custom policies directly in eBPF.
In this talk, we’ll develop a basic FIFO (First-In-First-Out) scheduler in C to show you how to get started with writing your own. If you’re interested in diving deeper into eBPF, join us for a quick hands-on intro to custom scheduling!

#### Related Links

- [sched-ext tutorial](https://github.com/sched-ext/scx/wiki)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ebpf:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ebpf:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RMQUJW/feedback/)

---

### An Introduction to Netkit: The BPF Programmable Network Device

- **Speakers:** Mike Willard
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 18:40 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4045-an-introduction-to-netkit-the-bpf-programmable-network-device/)

#### Abstract

Introduced in kernel v6.7, the Netkit device is an eBPF-programmable network device designed with containers in mind. In this talk, I will go over the the basics of the Netkit device, and discuss the performance gains we have realized and challenges we faced when rolling out Netkit across millions of containers at Meta.
Open-source projects used in this talk: Linux Kernel. View the netkit driver source code here.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ebpf:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ebpf:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9KRQGV/feedback/)

---

## Educational (14)

### Towards a Block-Oriented Visual Programming Paradigm

- **Speakers:** Jens Mönig
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 09:00 - 09:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5332-towards-a-block-oriented-visual-programming-paradigm/)

#### Abstract

Education typically prepares young people for professional life, equipping them with the skills to meet industry demands. Occasionally, however, the flow is reversed - educational research reshapes the industry itself. Historically, work on educational programming languages has sparked innovations like personal computing, graphical user interfaces, and the object-oriented programming paradigm.
In recent years, visual programming languages - where scripts are built by snapping together graphical blocks - have become a powerful tool for introducing programming to novices. But could there be more to these blocks than just their use in education? Could they point to a broader, transformative approach to programming itself?
In this talk, I’ll explore the Snap! visual programming language and showcase its recent developments, where blocks become first-class citizens of the language. By treating blocks as a computational domain, Snap! demonstrates how blocks can surpass their textual counterparts in expressiveness and versatility. This shift may offer new ways to form mental models of computation, potentially laying the groundwork for a new programming paradigm.
Join me as we examine the exciting possibilities of a block-oriented approach to programming and consider whether this marks the beginning of something much bigger.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3R7SLF/feedback/)

---

### Approaches to Open Source Embroidery

- **Speakers:** Richard Millwood
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 09:35 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5612-approaches-to-open-source-embroidery/)

#### Abstract

Open-source software makes it possible to create embroidery designs and stitch them onto clothing, bags, and patches. Learn how to create beautiful designs that can be stitched onto fabric using an embroidery machine.  There are two approaches, one is via programmatic embroidery (TurtleStitch), the other is using design software (Ink/Stitch, based on Inkscape).  The different approaches taken by both software packages will be discussed, and how the resulting output is stitched on an embroidery machine will be demonstrated.
www.turtlestitch.org
www.inkstitch.org
@megjlow@fosstodon.org

#### Related Links

- [TurtleStitch](https://www.turtlestitch.org)
- [InkStitch](https://www.inkstitch.org)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DRFPH9/feedback/)

---

### Youth Hacking 4 Freedom 2025

- **Speakers:** Bonnie Mehring
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 10:10 - 10:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4164-youth-hacking-4-freedom-2025/)

#### Abstract

The fourth round of the FSFE's programming competition “Youth Hacking 4 Freedom” is open for registration. "Youth Hacking 4 Freedom" is a programming competition for European teenagers from 14 to 18 years old. The participants have the chance to work on their own project idea with the guidance of experts from the Free Software universe. There are no limitations for the projects as long as they are published under a Free Software license. In this competition young people can test their skills, learn how to work on a project under a deadline, and most importantly have fun while meeting different people from Europe. Hear all about the competition and how to participate in this talk.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9WUVBS/feedback/)

---

### FOLL-E: open source educational tool to stimulate logical reasoning

- **Speakers:** Simon Vandevelde
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 10:45 - 11:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4076-foll-e-open-source-educational-tool-to-stimulate-logical-reasoning/)

#### Abstract

FOLL-E is an interactive tool designed to stimulate and sharpen the logical reasoning skills of children ages 8-12. Inspired by languages such as Scratch and Blockly, we have developed a blocks-based interface for pure logic. Crucially, we have proceeded to turn our blocks physical: children are given tangible "puzzle pieces" instead of a keyboard and mouse. This physical nature makes the tool more inviting and fun to play with, yet can still express everything we want.
The setup consists of a camera attached to a Raspberry Pi, which is connected to a computer screen. On the computer screen, children are presented with two groups of three robots each. A logic rule separates both robot groups (e.g., in one, all robots have a green arm, compared to none in the other). The goal is for the children to figure out this rule, and compose it by assembling the "puzzle pieces" into the correct configuration representing this rule. The Raspberry Pi then detects the blocks and verifies their correctness using an open-source logic engine. If correct, it continues on to the next level. If incorrect, it explains to the children where they went wrong, so that they can try again. In this sense, FOLL-E is meant to be very interactive.
From the get-go, we wanted FOLL-E to be freely available to everyone. As such, all aspects of FOLL-E are open source and available online for free, including among others the code and the design plans for the blocks. Furthermore, we are working on a detailed step-by-step building guide, aimed at e.g. schools. In a sense, anyone with access to a laser cutter and a Raspberry Pi can make their own setups -- which we strongly encourage you to do. :-)
Feel free to check out https://FOLL-E.com for pictures/videos of FOLL-E or https://gitlab.com/Vadevesi/foll-e to take a look at the source code.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LFJZKE/feedback/)

---

### Public values and FOSS for education

- **Speakers:** Geert-Jan, Raoul Kramer
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 11:20 - 11:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6042-public-values-and-foss-for-education/)

#### Abstract

The current digital educational system is dominated by tech giants. Fundamental rights, like the privacy, freedom, and sovereignty of children, parents, and educators are insufficiently secured. Ed-tech is mainly closed source and full of vendor lock-ins. Products are either overpriced, harvesting data, or both. The time to replace surveillance capitalist based Ed-tech by ethical open source alternatives is now.
We would like to build a European movement to create a free, sovereign alternative to the proprietary clouds offered by Big Tech that many kids are now forced to use.  We know that there are many beautiful initiatives in several places, but mostly independent of each other. We would like to reach out to our international colleagues, join forces together and help each other to make serious impact.
With this group, we would like to:
Build and improve educational tools
Integrate existing FOSS tools to create a complete suite for schools
Develop deployment methods
Take legal action
Lobby at the EU

In this presentation, we want to share our strategy and what we have been working on in the Netherlands to get attention for public values in educational software and show FOSS alternatives.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WLFQK3/feedback/)

---

### ZIMjs.com make javascript app

- **Speakers:** Karel Rosseel
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 11:55 - 12:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4345-zimjs-com-make-javascript-app/)

#### Abstract

ZIMjs.com/devs 2D + 3D/VR is a general Canvas Framework to create PWA (progressive Web Apps) for free, with simple, powerful JavaScript that lets everyone, from beginners to professionals, code creativity.
Hello developers, teachers, we celebrate ZIM 10 years! Made by https://ZIMjs.com/syno Dr. Abstract! You can use ZIM in different cases ( https://zimjs.com/history to have an overview started in 2014)
We now can use AI to generate apps with updates at https://zimjs.com/017 and with speechtechnolgy https://Zimjs.com/016 and much more, to create apps for kids and even by kids with https://zimjs.com/slate

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7QSJQE/feedback/)

---

### Free software teaching materials

- **Speakers:** Miriam Bastian
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 12:30 - 12:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4438-free-software-teaching-materials/)

#### Abstract

In this talk, Miriam will present some of the Free Software Foundation's teaching materials for high schools and will share her experience how students usually respond to them, what questions they ask and what topics they are interested in. The materials include videos, presentations, and handouts. The last five minutes of the talk are reserved for a Q&A.

#### Related Links

- [Teaching materials](https://libreplanet.org/wiki/Teaching_Materials)
- [Videos](https://framatube.org/a/fsf/video-channels)
- [More materials](https://www.fsf.org/resources/materials)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/K8YAKY/feedback/)

---

### Free your games: Luanti!

- **Speakers:** Zughy
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 13:05 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5795-free-your-games-luanti-/)

#### Abstract

Videogames are part of our daily life. They allow us to unplug, to relax, to compete, simulating a reality that puts us at the centre of a new digital world. However, if we go deeper into the way videogames are made, we’ll learn that their market can be brutal and the ethics of their business models highly debatable – if not plain intolerable. Nowadays, playing a videogame usually means having to renounce your privacy and shake hands with realities that we might not condone if we knew what they conceal. Free software allows us to reject this premise and grants people access to these experiences and the means to create games in ways that do no harm. Join us and discover Luanti, the voxel libre game platform that is widely used for both entertainment and education without ever compromising on the premise of total respect for all human beings.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JUPCWK/feedback/)

---

### The Hedy Programming Language

- **Speakers:** Jesús Pelay, Annelies Vlaar
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 13:40 - 14:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5098-the-hedy-programming-language/)

#### Abstract

Hedy is a programming language that aims to teach textual programming to kids. Hedy's unique approach involves gradual changes in the  syntax of the programming language, so students are not overloaded with information right away. Hedy is also built with teachers in mind and offers a multilingual approach, being available in over 50 languages, offering unique possibilities of learning for students who don't know english.

#### Related Links

- [Website of Hedy](https://hedy.org)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HNDJQN/feedback/)

---

### MicroBlocks 2.0: a complete makeover

- **Speakers:** Bernat Romagosa, John Maloney
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 14:15 - 14:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4304-microblocks-2-0-a-complete-makeover/)

#### Abstract

MicroBlocks  is a free (MPLv2) VM-based programming language for microcontrollers, with a graphical programming environment inspired in the Scratch and Snap! educational languages, and a virtual machine inspired in the Squeak Smalltalk-80 virtual machine.
In this talk, we present the new 2.0 version of the language and its IDE, with a completely redesigned UI, a new virtual machine with a smaller instruction footprint, lots of bug fixes, a whole new set of libraries and functionalities, and a new community-friendly translation system.

#### Related Links

- [The MicroBlocks website](https://microblocks.fun)
- [The MicroBlocks Git repository](https://bitbucket.org/john_maloney/smallvm/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/79ZLEJ/feedback/)

---

### Open Source in Education of Neurodiverse Students

- **Speakers:** William Jones, Ian Potter
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 14:45 - 15:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5624-open-source-in-education-of-neurodiverse-students/)

#### Abstract

Schools have an increasing number of students with learning needs. Demand grows to meet need for the high proportion of those students with neurodiversity. This is especially so in the most socio-economically deprived communities.
In this talk we present our experience in a program teaching open source AI technology to school students aged 12-14 years. This program has been run in collaboration with Redbridge School, Southampton and the Electronics and Computer Science department of Southampton University. 
We have been able to introduce these students to practical open source AI development. Through a range of projects they have been able to create their own gesture recognition systems and developed their own neural networks to solve a range of tasks. Open source has significantly driven this program, both in how it has been created, and in how it has shaped the students experience. 
We believe this approach is a template that could be widely adopted.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3LSZ3D/feedback/)

---

### Programming 3D Geometry in Snap!

- **Speakers:** Bernat Romagosa
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 15:20 - 15:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4303-programming-3d-geometry-in-snap-/)

#### Abstract

Based on our previous work on the now deprecated Beetle Blocks Snap! fork, we now present a new extension for Snap! that lets users generate 3D geometry programmatically. By giving instructions to a beetle, users can create surfaces and volumes based on simpler lower-dimensional objects. These 3D shapes can then be exported and printed on a 3D printer, or further manipulated in 3D modelling software.
The fact that these volumes are generated programmatically makes this extension an ideal tool to explore algorithmic and fractal structures, but we have also found it rather convenient to generate more mundane and functional geometry, such as toy replacements or simple home improvement parts.

#### Related Links

- [The Snap! website](https://snap.berkeley.edu)
- [The Snap! Git repository](https://github.com/jmoenig/Snap/)
- [The 3D Beetle Extension Documentation](https://beetleblocks.com)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NUNNVE/feedback/)

---

### How could open source in vocational education work?

- **Speakers:** Simone Weiß
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 15:50 - 16:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4687-how-could-open-source-in-vocational-education-work-/)

#### Abstract

Vocational Education is often not considered when it comes to open source as it neither happens in Schools or in Universities. Yet today over 300,000 IT specialists alone have completed their vocational education in Germany. In this talk, we will explore the reasons for integrating open source into vocational programs and delve into the specific content of vocational education for IT specialists and the options to add education about open source in the curriculum. I will also share practical examples of our own efforts to incorporate open source learning, providing insights into what works – and what doesn't!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8WCMZW/feedback/)

---

### Building Apps and Extensions with MIT App Inventor

- **Speakers:** Evan Patton
- **Room:** UD6.215
- **Day:** Sunday
- **Time:** 16:25 - 16:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6588-building-apps-and-extensions-with-mit-app-inventor/)

#### Abstract

Anyone can create iPhone and Android apps with global impact. MIT App Inventor is an intuitive, visual programming environment that allows everyone – even children – to build fully functional apps for Android and iOS devices. Those new to MIT App Inventor can have a simple first app up and running in less than 30 minutes. Our blocks-based tool also facilitates the creation of complex, high-impact apps in significantly less time than traditional programming environments. We will briefly discuss the platform and its design philosophy, build a simple app, and show how to build an extension for Android apps.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-educational:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-educational:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AA93CM/feedback/)

---

## Embedded, Mobile and Automotive (19)

### SatNOGS-COMMS: An Open-Source Communication Subsystem for CubeSats

- **Speakers:** Manolis Surligas
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 10:30 - 10:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6024-satnogs-comms-an-open-source-communication-subsystem-for-cubesats/)

#### Abstract

SatNOGS-COMMS is an open-source, open-hardware communications subsystem for CubeSats, developed by the Libre Space Foundation in collaboration with the European Space Agency (ESA). This innovative system combines advanced hardware and software to meet the challenges of CubeSat missions while promoting accessibility and flexibility through an open ecosystem.
The subsystem features an STM32H743 microcontroller as its main processor, complemented by a ZYNQ-7020 FPGA accelerator for computationally intensive tasks. SATNOGS-COMMS is built on Zephyr RTOS, with the firmware written entirely in C++17. Notably, its hardware control interfaces follow a platform-agnostic architecture, enabling users to adapt the firmware to their preferred RTOS with minimal effort.
This presentation will delve into the software engineering decisions, challenges encountered, and the advantages of an open-source approach for CubeSat missions and space exploration. Key topics include:
  * The benefits of using C++ in embedded systems, particularly in the context of resource constraints.
  *  How the use of exceptions improves firmware safety and reliability.
  * Fault-tolerant mechanisms designed to ensure reliable operation in the harsh environment of space.
Additionally, we will highlight our approach to enabling user-defined code integration without modifying the original codebase, comparing it with other commercial and non-commercial solutions.
The complete project, including hardware designs, software, simulations, and documentation, is freely available at the project’s GitLab repository: https://gitlab.com/librespacefoundation/satnogs-comms.

#### Related Links

- [Project repository](https://gitlab.com/librespacefoundation/satnogs-comms/)
- [Main firmware repository](https://gitlab.com/librespacefoundation/satnogs-comms/satnogs-comms-software-mcu)
- [Hardware repository](https://gitlab.com/librespacefoundation/satnogs-comms/satnogs-comms-hardware)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CGNYQS/feedback/)

---

### The road to open source General Purpose Humanoids with dora-rs

- **Speakers:** Tao xavier
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 11:00 - 11:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5525-the-road-to-open-source-general-purpose-humanoids-with-dora-rs/)

#### Abstract

Progress in both hardware and software ( such as dora-rs ) makes using Humanoids easier than ever!
Yet, one of the key feature required for humanoids to be truly useful is to be able to be able to behave in full autonomy!
A lot of company such as Tesla, 1X, Figure, are working on just this at the moment. But, it seems that most of this work is not going to be Open Source.
This is where dora-rs comes to the rescue!
We have a plan for 2025 to make General Purpose Humanoids accessible to anyone.
Please come to the talk and we'll share how!
Website: https://dora-rs.ai
Github; https://github.com/dora-rs/dora

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7AAA3G/feedback/)

---

### Exploring Open Source Dual A/B Update Solutions for Embedded Linux

- **Speakers:** Leon Anavi
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 11:30 - 11:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6299-exploring-open-source-dual-a-b-update-solutions-for-embedded-linux/)

#### Abstract

Regular software updates are essential for fixing common vulnerabilities and exposures (CVEs), addressing bugs, and adding new features, all while maintaining security and increasing the lifespan of embedded Linux devices. Over the past decade, the landscape has changed significantly, with many high-quality and reliable open source solutions now available, making the development of in-house update solutions unnecessary. During this time, several SOTA solutions using different strategies have come and gone. Open source options based on the dual A/B redundant update scheme have become widely adopted in the industry. This session will focus on three such solutions: Mender, RAUC, and swupdate. We will analyze their strengths and weaknesses, offering guidance on selecting the best solution for different use cases and industries. Additionally, we will explore advanced features such as HTTP streaming, which allows direct installation of updates without the need to download and store the update file locally. We will also discuss the potential of adaptive and delta updates, which are additional features built on top of A/B update schemes. These features minimize data transfer by sending only the changes, rather than the full update files.
The hands-on examples will demonstrate the integration of three different open source solutions: Mender, RAUC, and swupdate - on two different devices: Raspberry Pi 5 and the open source hardware Olimex I.MX8MP SoM, using the Yocto Project and OpenEmbedded. The demonstrations will highlight the differences in setup, configuration, and update management for each solution. Additionally, we will explore support for other build systems such as Buildroot, PTX dist, and distributions like Debia and Ubuntu, emphasizing how each solution integrates with these environments.
This talk is suitable for engineers and developers looking to implement an open source update solution for embedded Linux devices. It will provide a deeper understanding of the technical challenges and available open source solutions, empowering attendees to address these challenges more effectively and focus on enhancing the unique features of their products.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JELYDN/feedback/)

---

### Vulnerability Management at a Scale for the Yocto Project

- **Speakers:** Marta Rybczynska, Samantha Jalabert
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 12:00 - 12:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5519-vulnerability-management-at-a-scale-for-the-yocto-project/)

#### Abstract

The Yocto Project offers the cve-check class to allow users to check
for known vulnerabilities in the packages they include in their
distribution. However, the CRA (Cyber Resilience Act) and changes
around vulnerability databases require a different approach. The move
to multiple databases and more dynamic vulnerability checking is in
progress.
In this talk, we will explain the ongoing move to external checking
for vulnerabilities in the Yocto Project. This will allow users to
verify their distribution years after the release without the original
build directory.
As the future of the NVD (National Vulnerability Database) is unknown,
we are also considering using other databases, starting with raw data
from the CVE (Common Vulnerability Enumeration) program.
The audience will also discover VEX (Vulnerability Exchange), allowing
per-product annotations of vulnerabilities: you can finally say, "Not
affected, we disabled the vulnerable configuration option!"
This talk is 25 minutes; if we have 50, we can add more content and examples.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3ZZVHB/feedback/)

---

### Booting blobs between U-Boot and Linux

- **Speakers:** Marek Vasut
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 12:30 - 12:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6084-booting-blobs-between-u-boot-and-linux/)

#### Abstract

Various blobs like PSCI provider or TEE are currently started between BootROM and the U-Boot bootloader. This has multiple downsides, the blobs are difficult to update and the blobs may configure the platform in a way that prevents U-Boot from accessing all system resources, thus making it less useful as a debug tool. This talk explains how to start U-Boot before most of the blobs, thus giving it full unrestricted access to the platform, and how to start the blobs from U-Boot afterward, so Linux can still access the services like PSCI provided by the blobs. Finally, the talk hints at how to perform a safe A/B update of the blobs.
Project link: https://www.u-boot.org/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZFQE3W/feedback/)

---

### usb9pfs: network booting without the network

- **Speakers:** Ahmad Fatoum, Michael Grzeschik
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 13:00 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6103-usb9pfs-network-booting-without-the-network/)

#### Abstract

Linux v6.12 adds usb9pfs as a new USB gadget function, which can be used to
mount a filesystem provided over USB.
Booting from an external rootfs in the form of NFS is already a staple
in embedded systems development, but multiple issues complicate its usage:

network interface required , which may not always be available
Interference with normal network setup, especially in existence of switches
Requires setup of multiple services: DHCP, TFTP, NFS...

By using usb9pfs for the rootfs, these limitations can be avoided
on all devices that feature a USB gadget port.
This talk will discuss the design of 9p and usb9pfs and showcase how
streamlined development on a Yocto root file system can be with both
barebox and Linux making use of usb9pfs.

#### Related Links

- [usb9pfs patch series](https://lore.kernel.org/all/20240116-ml-topic-u9p-v12-0-9a27de5160e0@pengutronix.de)
- [NFS exporter for Yocto rootfs](https://github.com/ejoerns/poky-nfsroot)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HPG9SM/feedback/)

---

### Adopting BlueZ in production: challenges and caveats

- **Speakers:** George Kiagiadakis
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 13:30 - 13:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6203-adopting-bluez-in-production-challenges-and-caveats/)

#### Abstract

In 2024, I worked with a small team to bring up BlueZ as the Bluetooth stack of a real-world automotive In-Vehicle Infotainment (IVI) system. In this talk, I am going to discuss the steps that we went through, the challenges that we faced, the caveats of BlueZ in contrast with closed-source alternatives and also present the contributions that we made to BlueZ and PipeWire as part of this process.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/K3LYTP/feedback/)

---

### All Open Source Toolchain for ZYNQ 7000 SoCs

- **Speakers:** Yimin Gu
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 14:00 - 14:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4850-all-open-source-toolchain-for-zynq-7000-socs/)

#### Abstract

Zynq 7000 SoCs are popular devices widely used in embedded scenarios when both CPU power and flexible logic are required. However, the ARM (processing system, PS) + FPGA (programmable logic, PL) combo makes developments reply on an even heavier set of propriety toolchains. 
In this talk, I'll introduce the recently developed GenZ, a free software BSP generator for the Zynq 7000 PS register configuration. Together with OpenXC7, the free and open source FPGA toolchain for Xilinx 7-series chips, and a enlarging amount of open-source IP cores, development on Zynq 7000 SoCs can be done without a single piece of propriety tool. 
The speed and ease of GenZ + OpenXC7 will be demonstrated on site with an ARM laptop and Zynq boards.

#### Related Links

- [GenZ](https://github.com/regymm/GenZ/)
- [OpenXC7](https://github.com/openXC7/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LRKVBZ/feedback/)

---

### Getting more juice out from your Raspberry Pi GPU

- **Speakers:** José María Casanova Crespo, Maíra Canal
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 14:30 - 14:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5553-getting-more-juice-out-from-your-raspberry-pi-gpu/)

#### Abstract

Unleashing the power of 3D graphics on the Raspberry Pi is an ongoing effort at Igalia. We are constantly exploring new opportunities to maximize the GPU's potential. The process of identifying applications that can be optimized is highly rewarding. Every so often, we uncover a breakthrough, enabling us to boost application performance up to ~70%.
The graphics stack for the Raspberry Pi 4 and 5 is built on the Mesa user-space drivers (V3D/V3DV) and the Linux kernel driver V3D. These drivers are fully mature, with the upstream Mesa Vulkan driver V3DV having already achieved Vulkan 1.3 conformance, and the OpenGL/ES driver V3D exposing desktop OpenGL 3.1.
However, just having working, conformant drivers isn't enough for us. In this talk, we will demonstrate how we go the extra mile to extract the maximum performance from the Raspberry Pi's GPU, proving that a more performant embedded GPU is possible.
In addition to explaining where we currently stand, we will showcase several cases where optimizations in the Mesa user-space drivers led to significant performance improvements. We will also review recent developments in the kernel driver, including support for Huge Pages in the GPU kernel driver and our experience using Transparent Huge Pages (THP) on an embedded device.
By the end of this talk, we hope the audience will have a better understanding of the graphics stack for embedded GPUs and how to start getting more juice out of an embedded board.

#### Related Links

- [Recent work on V3D OpenGL/OpenGL-ES user space driver for Raspberry Pi 4/5](https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests?scope=all&state=merged&label_name[]=v3d)
- [Recent work on V3DV Vulkan user space driver for Raspberry Pi 4/5](https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests?scope=all&state=merged&label_name[]=v3dv)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XPPVHP/feedback/)

---

### The status of removing /sys/class/gpio and the global GPIO numberspace from the kernel

- **Speakers:** Bartosz Golaszewski
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 15:00 - 15:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5288-the-status-of-removing-sys-class-gpio-and-the-global-gpio-numberspace-from-the-kernel/)

#### Abstract

The GPIO sysfs interface for user space has been deprecated for many years. Its alternative, the GPIO character device and the associated libgpiod project, has been available since 2017. The library, along with its numerous bindings, has become the de facto standard tool for interacting with GPIOs from user space. Recently, it was supplemented by a D-Bus API and a reference implementation, addressing the long-standing issue of maintaining GPIO state persistence across different processes.
The sysfs interface is the primary user of the global GPIO number space in the kernel. Unlike other legacy components of the GPIO codebase, we cannot remove it without user space agreeing to stop using it. However, there remains a group of users who, for various reasons, refuse to migrate to the new uAPI. It has become evident that, without providing them with a 100% compatible experience, we will be stuck with the old interface indefinitely.
To address this, the latest addition to the family of user-space GPIO utilities is gpiod-sysfs-proxy[1] - a libfuse-based user-space compatibility layer for the GPIO sysfs interface under /sys/class/gpio, using libgpiod to talk to the kernel.
This talk will cover why we aim to remove /sys/class/gpio (along with the in-kernel legacy APIs), progress made so far, an introduction to gpiod-sysfs-proxy and the libgpiod D-Bus API, and a discussion of future plans.
[1] https://github.com/brgl/gpiod-sysfs-proxy

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DLRXQZ/feedback/)

---


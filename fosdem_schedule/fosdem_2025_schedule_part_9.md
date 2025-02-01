# FOSDEM 2025 Schedule - Part 9 of 11

*Generated on 2025-02-01*

## Table of Contents

- [Open Source In The European Legislative Landscape and Beyond (34)](#open-source-in-the-european-legislative-landscape-and-beyond-34)
- [PostgreSQL (8)](#postgresql-8)
- [Python (16)](#python-16)
- [Quantum Computing (10)](#quantum-computing-10)
- [Radio (10)](#radio-10)
- [Railways and Open Transport (10)](#railways-and-open-transport-10)
- [Real Time Communications (RTC) (12)](#real-time-communications-rtc-12)
- [Retrocomputing (13)](#retrocomputing-13)
- [RISC-V (13)](#risc-v-13)
- [Robotics and Simulation (14)](#robotics-and-simulation-14)

## Open Source In The European Legislative Landscape and Beyond (34)

### Wrap up by Open Source in the policymaking process block organisers and Rapporteur feedback

- **Speakers:** Jordan Maris, Sebastian Raible
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 16:50 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6705-wrap-up-by-open-source-in-the-policymaking-process-block-organisers-and-rapporteur-feedback/)

#### Abstract

Wrap up by Open Source in the policymaking process block organisers and Rapporteur feedback

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GCRETV/feedback/)

---

## PostgreSQL (8)

### PostgreSQL Performance - 20 years of improvements

- **Speakers:** Tomas Vondra
- **Room:** UA2.220 (Guillissen)
- **Day:** Sunday
- **Time:** 09:00 - 09:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4615-postgresql-performance-20-years-of-improvements/)

#### Abstract

Let's do some basic benchmarks (both OLTP and OLAP) on releases since PostgreSQL 8.0, and see how the performance changed over the years. It's unexpectedly difficult to realize how much has the performance changed over many releases, because we usually test and measure only the two releases. But the incremental improvements can compound pretty quickly, and the hardware and applications change too. So let's do some testing and look at numbers ;-)
You will not learn about how to use cool new features during this talk, but hopefully you'll learn how far we got in the past ~20 years.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-postgresql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-postgresql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YDHXGH/feedback/)

---

### Logical Replication Live Session - Keep on Streaming

- **Speakers:** Boriss Mejías
- **Room:** UA2.220 (Guillissen)
- **Day:** Sunday
- **Time:** 10:00 - 10:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5787-logical-replication-live-session-keep-on-streaming/)

#### Abstract

Logical replication in PostgreSQL is great for multiple use cases such major upgrades with nearly-zero downtime, consolidation of multiple databases into a warehouse, and more recently, bi-directional replication for geo-redundancy, with the promise of an active-active architecture. All these possibilities are evidence that logical replication is far richer than physical replication. However, that richness comes with higher complexity and nuances that makes it challenging. Oh yeah, and that’s fun, isn’t it?
In this presentation we will not just discuss in theory the nuances and challenges, we will have a live session analysing different scenarios, reviewing best and worst practices, breaking the replication and fixing it, so that the publisher database keeps on streaming, keeping the beat.
Logical replication is complex, but as the Zen of Python says, “better complex than complicated”.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-postgresql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-postgresql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TBMJGR/feedback/)

---

### Tuning Postgres for Analytics

- **Speakers:** Karen Jex
- **Room:** UA2.220 (Guillissen)
- **Day:** Sunday
- **Time:** 11:00 - 11:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5242-tuning-postgres-for-analytics/)

#### Abstract

Imagine the following, common scenario:
Your database is configured for the needs of your day-to-day (OLTP) application activity; many concurrent user connections each performing multiple short select, insert and update statements.
This OLTP activity constantly generates data, which has built up in your database over time, and is now seen as a valuable business resource. The organisation wants to use this data to answer real-world business questions such as “what percentage increase in sales did we see as a result of this marketing campaign?”.
This means you need to run analytics queries (OLAP activity) against the data; complex queries that work on large data sets and are therefore very resource intensive.
How can you do that without compromising the performance of your application?
Let’s look at some of the ways that you can design your environment and tune your database to work with this hybrid (OLTP + OLAP) workload. The goal is to make sure you've got performant analytics queries that have minimal impact on your day-to-day database activity.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-postgresql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-postgresql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/M9C88J/feedback/)

---

### From Queries to Pints: Building a Beer Recommendation System with pgvector

- **Speakers:** Andrzej Nowicki
- **Room:** UA2.220 (Guillissen)
- **Day:** Sunday
- **Time:** 12:00 - 12:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5531-from-queries-to-pints-building-a-beer-recommendation-system-with-pgvector/)

#### Abstract

Discover how easily you can create a recommendation system from scratch using modern AI and database technologies.
In this session, we’ll build a beer recommendation system using advanced language models and PostgreSQL's pgvector extension. By leveraging the capabilities of pgvector, we can seamlessly store high-dimensional embeddings generated from beer descriptions and perform similarity search with user preferences.
Whether you're a seasoned database administrator or just starting to explore the potential of AI, this presentation will equip you with practical insights and hands-on techniques to integrate machine learning into your database workflows. Join to learn how to turn complex data into intuitive recommendations! No prior ML knowledge required.
Links to projects used in this talk: PostgreSQL, pgvector extension, all-MiniLM-L6-v2 model, beer dataset

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-postgresql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-postgresql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GRSSHV/feedback/)

---

### Anatomy of Table-Level Locks in PostgreSQL

- **Speakers:** Gulcin Yildirim Jelinek
- **Room:** UA2.220 (Guillissen)
- **Day:** Sunday
- **Time:** 13:00 - 13:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4603-anatomy-of-table-level-locks-in-postgresql/)

#### Abstract

Short abstract
Understanding table-level locks in Postgres is a quite useful skill as almost all DDL operations require acquiring one of the different types of table-level locks on the object being manipulated. If not managed well, schema changes can result in downtime. In this talk we will explain fundamentals of table-level locking, covering how different types of locks are applied and queued during schema changes. Attendees will learn how to identify and manage lock conflicts to minimize downtime, avoid deadlocks, and maintain smooth database operations, even during high-concurrency schema changes.
Long abstract
In PostgreSQL, managing schema changes without downtime can be a challenging task. Table-level locks, which control access during Data Definition Language (DDL) operations like ALTER or DROP TABLE, can result in unintended application slowdowns or even service interruptions when not fully understood. This talk will provide a comprehensive dive into table-level locking and lock queueing in PostgreSQL, helping attendees gain the insights they need to perform efficient schema changes.
We’ll start by explaining the various types of table-level locks in PostgreSQL such as Access Share, Exclusive, and Access Exclusive and how they are automatically managed during common DDL operations. Then, we’ll break down lock queuing: how PostgreSQL organizes lock requests, what happens when transactions wait for locks, and how deadlocks can arise in complex environments.
Next, we’ll focus on practical approaches to managing table-level locks for near-zero downtime. Attendees will learn techniques to minimize locking impact, including understanding lock conflicts, using online schema migration patterns, and identifying lock-heavy queries. We’ll introduce open-source tools like pgroll, which utilizes the expand/contract pattern to make schema changes in small, lock-free steps.
By the end of this session, attendees will be equipped with practical strategies and knowledge to control lock behavior during schema changes, ensuring data integrity and reducing operational disruptions. This talk will provide the tools needed to manage PostgreSQL schema changes with confidence and minimal impact on production environments.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-postgresql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-postgresql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/98HQJG/feedback/)

---

### Stats roll, baby, stats roll.

- **Speakers:** Cédric Villemain
- **Room:** UA2.220 (Guillissen)
- **Day:** Sunday
- **Time:** 14:00 - 14:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4496-stats-roll-baby-stats-roll-/)

#### Abstract

PostgreSQL 18 will offer extension developers support for defining new statistics, using the native PostgreSQL Cumulative Statistics
We're talking about stats similar to what's in pg_stat* views and functions, and how you will be able to define your own views and functions in the future.
Using the PACS (PostgreSQL Advanced Cumulative Statistics) extension, we will explore what is offered by PostgreSQL as well as how to define your own new kind of statistics. We will also see how to benefit from the C and SQL API provided by PACS to setup your own gauge, counters, buckets and histogram.

#### Related Links

- [pg_pacs git repositery](https://git.data-bene.io/cedric/pg_pacs)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-postgresql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-postgresql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VLL9XB/feedback/)

---

### PostgreSQL Anonymizer and the battle for privacy

- **Speakers:** Damien Clochard
- **Room:** UA2.220 (Guillissen)
- **Day:** Sunday
- **Time:** 15:00 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4258-postgresql-anonymizer-and-the-battle-for-privacy/)

#### Abstract

Privacy is disappearing. From our morning coffee habits to our medical records, personal information flows freely between employers, businesses, government agencies, and social media platforms. Often without our knowledge or true consent. This isn't science fiction - it's our reality, and the databases are prime targets for breaches and abuse.
As Postgres administrators, we're on the front lines of this challenge. This talk introduces the PostgreSQL Anonymizer extension as a powerful solution for protecting sensitive data while maintaining its analytical value.
Through hands-on examples, we'll explore:

Creating and implementing effective masking policies
Applying dynamic masking for real-time data protection
Generating anonymized dumps for development environments
Producing privacy-preserving statistics

We'll conclude with cutting-edge developments, including:

Implementing differential privacy
Building a masking logical decoder
Addressing privacy challenges in AI vector storage

Join us to learn practical techniques for enhancing data privacy in your PostgreSQL deployments.

#### Related Links

- [PostgreSQL Anonymizer Extension](https://gitlab.com/dalibo/postgresql_anonymizer)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-postgresql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-postgresql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WEF7MV/feedback/)

---

### Row-Level Security sucks. Can we make it usable?

- **Speakers:** Jimmy Angelakos
- **Room:** UA2.220 (Guillissen)
- **Day:** Sunday
- **Time:** 16:00 - 16:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5282-row-level-security-sucks-can-we-make-it-usable-/)

#### Abstract

Row-Level Security (RLS) in PostgreSQL is awesome, as it allows you to isolate each user or tenant's data, lock it down and default to "deny access"... but it sucks because it makes assumptions about your application that are not applicable in many cases.
Especially if your applications were developed without RLS in mind and you use a single app user to connect to the database, it's impossible to use RLS in any meaningful way.
In this talk, we'll look at possible ways to roll out RLS that can let you take advantage of this powerful feature in the real world.
PostgreSQL Documentation: https://www.postgresql.org/docs/current/ddl-rowsecurity.html

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-postgresql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-postgresql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BSJSCZ/feedback/)

---

## Python (16)

### Advanced parsing of structured data using Python's new match statement

- **Speakers:** Marc-André Lemburg
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 09:00 - 09:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5301-advanced-parsing-of-structured-data-using-python-s-new-match-statement/)

#### Abstract

The match statement was introduced in Python 3.10, but has not yet seen wide adoption.
In this talk, I'd like to showcase a few more advanced use cases to demonstrate it's expressiveness and versatility, compared to classic parsers using if-elif-else chains, in the hope of attracting a few more Python users to the new concept in Python.
We will have a look at parsing JSON, XML and ASTs, and also compare performance to the classic parsing strategy.
Knowledge of how the match statement works and familiarity with at least one of JSON, XML and ASTs are prerequisite for this talk.

#### Related Links

- [PEP 636 – Structural Pattern Matching: Tutorial](https://peps.python.org/pep-0636/)
- [Python documentation for the match statement](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8T7UD7/feedback/)

---

### Python Monorepos: The Polylith Developer Experience

- **Speakers:** David Vujic
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 09:30 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4772-python-monorepos-the-polylith-developer-experience/)

#### Abstract

What if writing software could be more like building with LEGO bricks? A more playful and productive developer experience. For me, that is all about writing code - without the hassle. A productive setup should also let us make design decisions while learning what to actually build, and allow changes during the way. Polylith solves this in a nice and simple way. I am the developer of the Open Source Python-specific tooling for Polylith. I’ll walk through the simple Architecture & the Developer friendly tooling for a joyful Python Experience.

#### Related Links

- [Repository: The Python tools for the Polylith Architecture](https://github.com/DavidVujic/python-polylith)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/S9GXPF/feedback/)

---

### make python devex: Towards Red-Green-Refactor in 1 Command with an Old Tool

- **Speakers:** Colin Dean
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 10:00 - 10:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6426-make-python-devex-towards-red-green-refactor-in-1-command-with-an-old-tool/)

#### Abstract

Getting productive with a Python codebase, especially when unfamiliar with the ecosystem or setting up a new workstation for the first time, can be daunting. Building a cohesive strategy with widely available tooling shortens the time-to-productivity for new contributors to projects internal and open-source, demonstrating that the maintainers care about onboarding and the developer experience. I'll introduce how my team solved this problem using a nearly 50-year-old program and push the audience toward better developer experiences, starting at the greatest common denominator of tooling. Some newer tooling makes some of this easier, but corporate Python projects and open source projects alike benefit from this approach.

#### Related Links

- [Slides sources](https://github.com/colindean/talks/tree/master/make_python_devex)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NUUV33/feedback/)

---

### FawltyDeps: Finding undeclared and unused dependencies in your notebooks and projects

- **Speakers:** Johan Herland
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5072-fawltydeps-finding-undeclared-and-unused-dependencies-in-your-notebooks-and-projects/)

#### Abstract

Reproducibility is a cornerstone of science. However, most data science projects and notebooks struggle at the most basic level of declaring dependencies correctly. A recent study showed that 42% of the notebooks executed failed due to missing dependencies.
FawltyDeps is a dependency checker that finds imports you forgot to declare (undeclared dependencies), and packages you declared, but that are not imported in your code (unused dependencies).
This talk will guide you through integrating FawltyDeps in your manual or automated workflows and how this can improve the reproducibility of your notebooks and projects.

#### Related Links

- [FawltyDeps project](https://github.com/tweag/FawltyDeps/)
- [Slides](https://docs.google.com/presentation/d/1qVmYzQHzCQv4ieUaAddIWg-8Gw497rb43ClGg9gJqtM/edit?usp=sharing)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7L9ZRE/feedback/)

---

### What can PyArrow do for you - Array interchange, storage, compute and transport

- **Speakers:** Rok Mihevc, Alenka
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 11:00 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6092-what-can-pyarrow-do-for-you-array-interchange-storage-compute-and-transport/)

#### Abstract

PyArrow is a powerful tool for Python developers seeking high-performance data processing and interchange. This talk will provide a pragmatic overview of some of PyArrow's capabilities, demonstrating data interchange, storage, manipulation and transport using a single Python library. 
We'll explore four key capabilities:
Array Interchange: Seamless data exchange between NumPy, pandas, and other libraries using zero-copy
Storage: Efficient serialization and file format support (Parquet, ORC, Feather) with advanced compression
Compute: High-performance in-memory computation and data transformation capabilities
Transport: Leveraging Arrow Flight RPC for distributed data movement and processing

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9GF8WB/feedback/)

---

### Python MonkeyPatch: Debugging Python Applications + Production Hotfix

- **Speakers:** Safwan Rahman
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 11:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5489-python-monkeypatch-debugging-python-applications-production-hotfix/)

#### Abstract

Monkeypatching is a very powerful technique to dynamically modify program at the runtime. Even though it is very powerful, using it without proper method can leads to unintentional behavior. In this talk, I am going to talk about how it is possible to use monkeypatching functionality of Python to debug bug and other issues. Moreover, how can we effectively use it for making emergency hotfix into production systems.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8MPL7L/feedback/)

---

### Understanding programming peculiarities

- **Speakers:** Katie McLaughlin
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 12:00 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4764-understanding-programming-peculiarities/)

#### Abstract

Designing a programming language is not something you can do in a day*. Like many programming languages, Python builds on lessons learnt from other languages, as others build from Python. As you explore programming beyond Python, you'll start to encounter interesting edge cases and peculiarities that may take some time to understand. Some may inherit from Python, but some may also be something that Python explicitly prevents -- once you understand the reasoning, of course. 
In this presentation, you will be introduced to several novel examples of programming quirks, learn the language-specific reason behind them, and then discover how the problem doesn't (or also) exist in Python. 
By the end of this talk, you'll have a deeper understanding of not only some of Python's implementation details, but also learned some nuances around several other programming languages.

JavaScript took a whole eight days.

#### Related Links

- [Talk resources](https://github.com/glasnt/wat-references/#turning-wat-into-why)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LMEKGD/feedback/)

---

### Anatomy of a Python OpenTelemetry instrumentation

- **Speakers:** Riccardo Magliocchetti
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 12:30 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4282-anatomy-of-a-python-opentelemetry-instrumentation/)

#### Abstract

OpenTelemetry Python instrumentations may seem indistinguishable from magic: they can be bootstrapped from your installed dependencies, they are able to patch your code without even noticing and most often they work out of the box automatically! Fortunately there's no magic spell involved and they are mostly the combination of not well known Python features, standing on the shoulders of powerful libraries and work done by the community to improve the reach and the quality of the code. Let's dig a bit into the code to see what's inside the black box.

#### Related Links

- [OpenTelemetry Python repository](https://github.com/open-telemetry/opentelemetry-python)
- [OpenTelemetry Python Contrib repository](https://github.com/open-telemetry/opentelemetry-python-contrib)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/U8FQP8/feedback/)

---

### Nim for Pythonistas (and Open Source Lovers)

- **Speakers:** Pietro Peterlongo
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 13:00 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6414-nim-for-pythonistas-and-open-source-lovers-/)

#### Abstract

You might have heard of Nim as a fast and statically typed language with a Python-like syntax that compiles to compact executables and you are curious to hear more about it. Or you might have never heard of Nim and you might be curious what a talk about another programming language (that is not Rust) has anything to do with a Python devroom. Or maybe you are someone who loves Open Source (possibly even contributed to some open source projects) but does not feel like you will ever be able to contribute a project of your own that might interest others. If you connect with one of these three descriptions, I have prepared this talk for you. Even if you do not see yourself in any of those, please keep reading to see if you should consider joining the Python devroom for this talk.
This talk is divided in three parts:

What is Nim?
Why Nim made me a better Pythonista
How Nim can help you getting more involved in Open Source

In the first part I will give a quick introduction to Nim emphasizing similarity and differences with Python. I will explain that Nim can be used as a fast and easy to use complement to Python with a great interoperability and metaprogramming superpowers. Nim has also a powerful type system, functional features and can compile to Javascript.
In the second part I will tell you a bit about my story on how I got attracted to Nim coming from Python, the benefits of a niche community, and how I came out with a deeper appreciation for the Python project and community.
In the third part, I will show you how easy it is to create your own open source project with Nim and share it with the world (maybe even a Python version of it), and I will tell you a little bit about my own open source project, called Nimib, a literate programming tool for interactive explanations.
The talk is kept approachable for beginners while trying to be interesting also for experts. It does not have any specific pre-requisites on Nim, Python or Open Source but a familiarity and interest with at least one of those will help you take the most out of it.

#### Related Links

- [Link to repository of Nim Language](https://github.com/nim-lang/Nim)
- [Link to talk slides (new version to be updated)](https://github.com/pietroppeter/nim-for-pythonistas)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UGKK39/feedback/)

---

### Skip the Overhead: Lean Web Development with Django

- **Speakers:** Jochen Wersdörfer
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 13:30 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6174-skip-the-overhead-lean-web-development-with-django/)

#### Abstract

Do we really need complex JavaScript frameworks to build interactive websites? This talk argues we don’t. By combining Django, HTMX, and web components, we can create fast, interactive sites without unnecessary complexity.
To showcase how these advantages come together in practice, we’ll explore a small example. Introducing django-resume, a lightweight third-party Django app that adds a resume and CV section to your site—with no dependencies besides Django itself. It demonstrates:

Achieving SPA-like behavior using HTMX with server-side rendering.
Storing all data in a single JSONField to simplify database interactions and data export.
Enabling inline editing with contenteditable elements and web components.
Adding features through plugins without database migrations.
Using JSON data with Large Language Models (LLMs) for content creation.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GPUTXW/feedback/)

---

### Shifting DX expectations: keeping Django relevant 😬

- **Speakers:** Thibaud Colas
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 14:00 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5824-shifting-dx-expectations-keeping-django-relevant-/)

#### Abstract

Django is a big, slow-moving object. Lots of people worry about how much traction the framework still has, and its long-term outlook. Today, together, we get to review its existential threats – and opportunities 🌈!
We’ll start with a data-driven review of emerging trends in the web development ecosystem, with a particular focus on Python. We’ll look at specific Python considerations (types, tooling, package discovery) that are relevant for all projects, and specific indicators of the project health for contributors, and underlying usage trends.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MNWNTV/feedback/)

---

### PyScript - Python in the Browser

- **Speakers:** Chris Laffra
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 14:30 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4468-pyscript-python-in-the-browser/)

#### Abstract

Zero Installation, massive scalability, mobile support, and more. This talk will cover the superpowers of running Python in the Browser and how to best use PyScript.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AYJHQG/feedback/)

---

### Building Context-Aware Recommendation Systems With Python and Keras

- **Speakers:** Brayan Kai Mwanyumba
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 15:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4778-building-context-aware-recommendation-systems-with-python-and-keras/)

#### Abstract

This Talk will cover how to build Context-Aware Recommendation Systems using both text and image data. We will explore techniques to extract context from textual content, such as user posts or reviews, and visual content, like images shared by users. By integrating these diverse context sources into recommendation algorithms, we can significantly enhance the relevance and personalization of recommendations. 
Participants will engage in hands-on implementation, utilizing NLP tools for text and computer vision techniques for images through Python and Keras. By the end of the session, you’ll be equipped to create robust, context-aware recommendation systems that leverage text and image data to drive user engagement. 
Key Takeways 
- Understand the principles of context-aware recommendation systems
- Learn basic techniques for extracting context from textual content using NLP
- Discover how to analyze visual content using computer vision methods
- Gain insights into integrating text and image features for enhanced recommendations

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/F7UZRD/feedback/)

---

### Effortless Distributed Computing in Python

- **Speakers:** Raphael Javaux
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 15:30 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4835-effortless-distributed-computing-in-python/)

#### Abstract

In this talk, Raphael will share his experience taking part to the development of 3 new packages dedicated to the parallelization of distributed Python workloads:

Scaler, a light-weight and resilient distributed task scheduler for Python;
Parfun, an easy to use map-reduce decorator for Python;
Pargraph a battle-tested distributed graph engine for Python.

The talk will show examples on how to leverage these three projects for efficient distributed computations.

#### Related Links

- [Scaler](https://github.com/Citi/scaler)
- [Parfun](https://github.com/Citi/parfun)
- [Pargraph](https://github.com/citi/pargraph)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WULPLC/feedback/)

---

### Create A Custom Linux Init in Python

- **Speakers:** Hugo Herter
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 16:00 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5260-create-a-custom-linux-init-in-python/)

#### Abstract

On Linux, init is the first process started by the kernel during system boot. This talk will show how to write your own init in Python and why you might want to do so.
The Linux init process bootstraps user space and starts system processes. This is typically managed by Systemd, OpenRC, or the older System V. While these provide many useful features for modern desktops and servers, virtual machines and embedded devices can benefit from a more minimalist approach and precise control over userspace.
This talk will explore the steps required to create a new init in Python and the common patterns to achieve this:

Setting up a minimal filesystem.
Managing child processes and signals.
Handling system tasks like rebooting.
Interfacing with the host system.

We will demonstrate this process using Firecracker microVMs, the open-source virtualization tool that powers AWS Lambda and can start virtual machines in a few hundred milliseconds.
By the end of this talk, attendees will have a clear understanding of how to build and customize their own init processes, enabling them to create tailored environments for their specific needs, particularly in resource-constrained or specialized applications.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/F7WCWV/feedback/)

---

### Rewriting pyc files for fun and reproducibility

- **Speakers:** Zbigniew Jędrzejewski-Szmek
- **Room:** UD2.218A
- **Day:** Sunday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4072-rewriting-pyc-files-for-fun-and-reproducibility/)

#### Abstract

Python writes bytecode files (*.pyc) to speed up module imports. It's been known for a while that those are not reproducible: on different architectures, the bytecode for exactly the same sources ends up slightly different. Fedora is working on making all package builds reproducible, and with 8500 Python source packages, we quickly found out that differences in bytecode give us grief. One source of the difference (reference flag numbering) has been known for a while. But after cleaning that up, we found that there are at least two other ways in which bytecode is irreproducible: one related to reference use (also solved), one related to object order (still unsolved). In this talk we'll describe the problem and report how Fedora rewrites bytecode files in package builds to make them smaller and reproducible.

#### Related Links

- [Fedora Change page](https://fedoraproject.org/wiki/Changes/ReproduciblePackageBuilds)
- [Post-build cleanup program used in Fedora](https://github.com/keszybz/add-determinism)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-python:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-python:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RVGXDT/feedback/)

---

## Quantum Computing (10)

### Welcome to the Quantum Computing devroom

- **Speakers:** Alessandro Cosentino
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 13:10 - 13:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5444-welcome-to-the-quantum-computing-devroom/)

#### Abstract

Quantum computing promises to solve problems that are out of reach for classical systems, but today's quantum computers are still experimental, noisy, and lack scalability. So why are we already building software for them?
We will give a concise introduction to the field of quantum software for FOSDEM attendees that are not too familiar with it. Covering the full stack—from algorithms to hardware—we'll make the case for how software (and open-source software in particular) plays a critical role in advancing quantum computing and helping scientists turn potential into reality.
Following that, we will introduce the schedule of the Quantum Computing devroom.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-quantum:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-quantum:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BHRDGE/feedback/)

---

### Qlafoutea: Baby steps towards compiling a programming language to analog quantum computer

- **Speakers:** David "Yoric" Teller
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 13:25 - 13:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4269-qlafoutea-baby-steps-towards-compiling-a-programming-language-to-analog-quantum-computer/)

#### Abstract

Implementing a programming language for a classical computer is considered a solved topic, to the point that it's the kind of homework that can easily be handed out to CS students.
Implementing a programming language for an analog computer, now? Or for an analog quantum computer? That's a different story. How can you compiler or interpret a set of instructions on a machine that is defined not by memory and a machine language, not even by a circuit, but by physical laws?
Qlafoutea is an ongoing experiment at Pasqal, hoping to bring us one step closer to answering this question. We'll take a look under the hood at the physical limitations, the various compilation steps and what we can do so far.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-quantum:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-quantum:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BUPCVA/feedback/)

---

### No-one used my software: a tale of quantum software engineering

- **Speakers:** Aleksander Wennersteen
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 13:50 - 14:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5829-no-one-used-my-software-a-tale-of-quantum-software-engineering/)

#### Abstract

Quantum software engineering sounds complicated. Nevertheless, my experience is that the hard part of quantum software is not quantum, but software and engineering.
Paraphrasing a famous quote one might say that “quantum software engineering is a journey, not a destination”, a mantra that also fits this talk. As such rather than focusing on the destination I can divulge that the chapters of this story includes “How multiple inheritance killed my SDK” and its sequel  “The return of the SDK” which will outline some the development process that led to Pasqal's latest open-source SDK Qadence, a and a recurring entr'acte: “the GPU strikes back”, wherein the lure of GPU accelerated compute frequently leads our hero astray.
Building on the experience of over 3.5 years building software across teams at the full-stack quantum company Pasqal the presenter intends to bring a high-level view with concrete examples and demystify quantum software in a way that is accessible to the wider open-source community yet interesting and informative for practitioners.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-quantum:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-quantum:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TGP8XG/feedback/)

---

### Bridging the Gap: Quantum Computing for Classical Software Engineers

- **Speakers:** Veronica Lopez
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 14:15 - 14:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6529-bridging-the-gap-quantum-computing-for-classical-software-engineers/)

#### Abstract

Quantum computing is opening doors for software engineers to contribute in ways that complement their existing expertise. But how do we bridge the gap between quantum mechanics and practical software development?
In this talk, I’ll draw on my background in physics and my work as a staff software engineer in distributed systems to show how quantum concepts can translate into software challenges and solutions. Whether you're curious about quantum computing or wondering how your engineering skills apply, this talk will provide insights and strategies to help you get started and make meaningful contributions to the quantum computing ecosystem.
We’ll explore how quantum mechanics translates into practical software challenges and solutions, with a focus on tools and techniques that connect classical and quantum worlds.
This session is ideal for developers curious about quantum computing, those working in open-source, and anyone wondering how their existing skills in classical computing can help drive innovation in quantum technologies.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-quantum:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-quantum:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7YJD8E/feedback/)

---

### Quantum type system in H-hat quantum programming language

- **Speakers:** Eduardo Maschio (Dooms)
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 14:40 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4154-quantum-type-system-in-h-hat-quantum-programming-language/)

#### Abstract

In this talk, the H-hat quantum type system is presented. H-hat is a high-level abstraction quantum programming language designed to close the gap between software development and quantum resources, by using familiar programming concepts in a hybrid paradigm. Its quantum type system introduces quantum types that can hold both classical and quantum types, define the number of indexes (qubits) that a quantum variable is able to use, as well as define the rules in which a quantum type can be cast into a classical type. The casting process causes the quantum variable to execute its context at runtime, compile the quantum instructions to be executed and measured in a quantum simulator or hardware, and provide the appropriate conversion method from bits sampling to the desired classical type.

#### Related Links

- [H-hat GitHub page (in development at the time of the talk)](https://github.com/hhat-lang/hhat_lang/tree/dev/python)
- [H-hat Docs page](https://docs.hhat-lang.org)
- [H-hat GitHub page (official - but not up-to-date)](https://github.com/hhat-lang/hhat_lang)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-quantum:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-quantum:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SN73YF/feedback/)

---

### Quantum Distance Bounding: Achieving Secure Proximity

- **Speakers:** Kevin Bogner
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 15:05 - 15:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4623-quantum-distance-bounding-achieving-secure-proximity/)

#### Abstract

Have you ever considered how we can securely confirm someone's physical proximity in our digital world? In this talk, we'll explore Quantum Distance Bounding—an approach that uses the principles of quantum physics to determine an upper limit on the distance between two parties. This method enhances security by using qubits instead of traditional signals like radio waves or ultrasound, offering robust protection against various types of attacks. We'll discuss the fundamental concepts, potential applications, and how this technology could influence the future of secure communications.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-quantum:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-quantum:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GXVHRH/feedback/)

---

### Introducing Qumat! (An Apache Mahout Joint)

- **Speakers:** Trevor Grant, Andrew Musselman
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 15:30 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5298-introducing-qumat-an-apache-mahout-joint-/)

#### Abstract

There seem to be as many quantum computing languages as there are quantum computers. IBM’s qiskit attempts to address this by providing interfaces to multiple backends, but do we really want a vendor owning the coding ecosystem? What could go wrong? Lulz. Apache Mahout’s Qumat project allows users to write their circuits once and then run the same code on multiple vendors. In this talk we’ll discuss how Apache Mahout’s Samsara project introduced the idea of avoiding vendor lock-in by allowing machine learning experts to author algorithms in a vendor-neutral language that would then run everywhere. This spirit is living on in the Qumat project which allows user to write quantum circuits and algorithms (in a vendor-neutral Python library), which are then transpiled to run on IBM’s qiskit, Google cirq, Amazon Braket, or to extend the library to run on other hardware.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-quantum:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-quantum:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VAMQJK/feedback/)

---

### Opensource Tools for Platform Agnostic Quantum Computing

- **Speakers:** Harshit Gupta
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 15:55 - 16:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4410-opensource-tools-for-platform-agnostic-quantum-computing/)

#### Abstract

Our mission at qBraid is to make quantum computing broadly accessible, supported by the qBraid Lab platform. Additionally, we're committed towards building an open-source ecosystem that provides essential tools and resources, helping developers and researchers enter the field with minimal friction. This talk will showcase three key tools that make quantum programming more approachable for developers - 

qBraid-runtime simplifies quantum software pipelines, providing a streamlined workflow that allows developers to build and execute applications efficiently. 
qBraid-transpiler, part of our qBraid-SDK, enables seamless conversion of quantum programs across different quantum computing packages, such as Qiskit and Cirq, making it easier for users to work with various frameworks without compatibility issues. 
PyQASM offers semantic analysis and compilation support for OpenQASM, equipping developers with tools to write, debug, and optimize quantum code.

Together, these tools support a global, platform-agnostic, open-source ecosystem, empowering anyone to explore, innovate, and contribute to quantum computing. This talk will demonstrate how qBraid’s tools enable users to better think about "what" they want to do, without worrying about the implementation details, thereby paving a path to a more accessible future for quantum technologies.
References - 
1. qBraid-SDK : https://github.com/qBraid/qBraid
2. PyQASM : https://github.com/qBraid/pyqasm
3. Transpiler Documentation : https://docs.qbraid.com/sdk/user-guide/transpiler
4. Runtime Documentation : https://docs.qbraid.com/sdk/user-guide/runtime/components

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-quantum:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-quantum:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WNVUPK/feedback/)

---

### On-Chip Verified Quantum Computation with an Ion-Trap Quantum Processing Unit

- **Speakers:** Cica Gustiani
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 16:20 - 16:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4481-on-chip-verified-quantum-computation-with-an-ion-trap-quantum-processing-unit/)

#### Abstract

We introduce ocvqc-py (On Chip Verified Quantum Computation - Python), a Python library for constructing verifiable measurement-based quantum computation (MBQC) patterns. Verifiable quantum computation ensures that the output of a quantum computation can be relied upon even if the quantum device may be faulty or untrusted. Supported by pytket, the library is compatible with the Quantinuum ion-trap backend, enabling the construction of verifiable MBQC patterns compatible with near-term noisy quantum hardware. Building on the principles of quantum verification, ocvqc-py implements a novel approach to on-chip verification, allowing users to generate verifiable MBQC patterns without the need for quantum communication between client and server, which is typical in traditional verifiable MBQC setups. ocvqc-py has been used to construct measurement patterns with up to 52 vertices, demonstrated on the Quantinuum H1-1 ion-trap quantum computer, which is the largest verified MBQC pattern implemented to date.
The full paper can be found here: https://arxiv.org/abs/2410.24133
The code: https://github.com/CQCL/ocvqc-py

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-quantum:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-quantum:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3NJKME/feedback/)

---

### Unitary Compiler Collection

- **Speakers:** nate stemen
- **Room:** K.4.401
- **Day:** Sunday
- **Time:** 16:45 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6531-unitary-compiler-collection/)

#### Abstract

Compilers are vital tools for turning code into efficient executables that run on machines, making them a key part of classical computing infrastructure. While classical computing benefits from a wealth of sophisticated compiler tools, the quantum computing landscape is young in its software tooling development. In this talk I'll motivate the need for a new, cross-platform quantum circuit compiler which goes beyond existing tools.
At Unitary Fund, we are developing the Unitary Compiler Collection (UCC)—a Python library designed for frontend-agnostic, high-performance compilation of quantum circuits. Think of it as GCC, but for quantum computers. We’ll share benchmarking results comparing UCC to current quantum circuit compilers across real-world applications and explore future directions to push the boundaries of quantum compilation.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-quantum:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-quantum:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7YRXDN/feedback/)

---

## Radio (10)

### Welcome to the Radio Devroom

- **Speakers:** Bastien Cabay
- **Room:** UB2.147
- **Day:** Saturday
- **Time:** 10:30 - 10:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6592-welcome-to-the-radio-devroom/)

#### Abstract

5-10 minutes talk with devroom co-owner to introduce devroom.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-radio:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-radio:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KWZ8TK/feedback/)

---

### Using AI hardware accelerators for real-time DSP on embedded devices - NPU, TPU etc,

- **Speakers:** Sylvain AZARIAN
- **Room:** UB2.147
- **Day:** Saturday
- **Time:** 10:45 - 11:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6189-using-ai-hardware-accelerators-for-real-time-dsp-on-embedded-devices-npu-tpu-etc-/)

#### Abstract

While we presented last year what could be achieved using NVIDIA GPU, the hardware market has seen a lot of new comers following the need to have AI running locally on devices. Google has the Coral, Rockchip is adding a AI coprocessor on their ARM CPU, and now we have the Copilot PC coming with additional power focused on running Deep Learning models.
In this talk I will present how these accelerators can also be useful for SDR realtime processing, showing some results and presenting the first beta of a new open source library.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-radio:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-radio:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZLDBHW/feedback/)

---

### M17 and OpenRTX: one year later

- **Speakers:** Marc Balmer, Silvano Seva
- **Room:** UB2.147
- **Day:** Saturday
- **Time:** 11:40 - 12:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5723-m17-and-openrtx-one-year-later/)

#### Abstract

Following the FOSDEM 2024 presentations about M17 and OpenRTX, this talk will provide an insight into the developments carried out by both projects throughout the past year: the first commercial device supporting M17, the support of OpenRTX by the trx-control software, and M17Netd, a Linux daemon that enables the creation of IP links over RF.

#### Related Links

- [M17 project home page](https://m17project.org/)
- [OpenRTX project home page](https://openrtx.org/#/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-radio:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-radio:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LDNFDV/feedback/)

---

### The AFF3CT framework for building numerical communication chains

- **Speakers:** Olivier Aumage
- **Room:** UB2.147
- **Day:** Saturday
- **Time:** 12:35 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4250-the-aff3ct-framework-for-building-numerical-communication-chains/)

#### Abstract

The AFF3CT framework (https://aff3ct.github.io/) is a free and open-source environment under MIT license for building numerical communication chains in the context of software-defined radio applications. It has been developed over about a decade by Inria and the IMS and LIP6 research labs to enable the design, simulation, validation and production-oriented exploitation of building blocks, such as error correction code modules, in chains such as satellite DVB-S2 video transmission or 5G communications. AFF3CT has been designed with a focus on efficiently using the hardware parallelism available in modern multicore processors. This talk will present a brief overview of AFF3CT's capabilities and architecture.
The AFF3CT open source repositories are available at the following links:
- AFF3CT GitHub repo:
  - https://github.com/aff3ct/aff3ct.git
- AFF3CT's task-based runtime system StreamPU repo: 
  - https://github.com/aff3ct/streampu.git
- AFF3CT's SIMD intrinsics wrapper library MIPP repo:
  - https://github.com/aff3ct/MIPP.git
- AFF3CT's DVB-S2 SDR example repo:
  - https://github.com/aff3ct/dvbs2

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-radio:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-radio:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AZWFK9/feedback/)

---

### HAMNET - Status Update

- **Speakers:** Jann Traschewski, DG8NGN
- **Room:** UB2.147
- **Day:** Saturday
- **Time:** 13:30 - 14:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6523-hamnet-status-update/)

#### Abstract

Over the last 15 years, HAMNET (Highspeed Amateur Radio Multimedia NETwork) has developed from an experiment into a stable infrastructure, particularly in German-speaking regions.
It generally connects unmanned amateur radio stations via microwave links using the IP- and BGP-protocol and provides a platform for networking amateur radio applications.
This talk will show how HAMNET has evolved and how it could evolve (challenges in deployment, expansion in Europe, densification of the backbone, higher speeds, access technologies for non-line-of-sight propagation).

#### Related Links

- [HAMNET Database](https://hamnetdb.net)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-radio:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-radio:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MDCPMT/feedback/)

---

### RF Swift: A Swifty Toolbox for All Wireless Assessments

- **Speakers:** Sébastien Dudek
- **Room:** UB2.147
- **Day:** Saturday
- **Time:** 14:25 - 15:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4301-rf-swift-a-swifty-toolbox-for-all-wireless-assessments/)

#### Abstract

In an increasingly connected world, securing wireless communication is vital for protecting critical infrastructure and personal data. Traditional tools for Radio Frequency (RF) assessments, while effective, often lack flexibility, cross-platform compatibility, and adaptability for diverse environments and architectures. RF Swift addresses these limitations by providing a streamlined, modular toolbox tailored for RF Security assessments and HAM radio enthusiasts alike.
RF Swift is a multiplatform solution, seamlessly running on Windows, Linux, and a wide range of architectures. This versatility empowers users to conduct RF assessments in virtually any environment without hardware constraints. Designed with adaptability in mind, RF Swift enables security professionals and radio enthusiasts to deploy, manage, and analyze RF communications with unprecedented speed and efficiency.
Attendees will discover how RF Swift empowers both rapid assessments and deep analysis, simplifying complex tasks such as spectrum monitoring, signal detection, protocol analysis, and signal generation. Join us to explore how RF Swift redefines RF security assessment, offering a robust, scalable, and flexible approach to tackle modern wireless security challenges.

#### Related Links

- [Official RF Swift website and documentation](https://rfswift.io/)
- [The impossible being possible with RF Swift by running a GPRS station on Windows](https://www.youtube.com/watch?v=oOUrT6G0ECg&feature=youtu.be)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-radio:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-radio:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PRZXHL/feedback/)

---

### SDR++, a modular, cross-platform SDR utility

- **Speakers:** Alexandre Rouma
- **Room:** UB2.147
- **Day:** Saturday
- **Time:** 15:20 - 16:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4043-sdr-a-modular-cross-platform-sdr-utility/)

#### Abstract

This talk is would be a presentation of the SDR++ project with roughly  the following sections:
1) A small history segment about the project and its origins
2) An in-depth explanation of the architecture and design choices of the software
3) A short demo showcasing the features of the software

#### Related Links

- [SDR++ Website](https://www.sdrpp.org)
- [SDR++ Github Page](https://github.com/AlexandreRouma/SDRPlusPlus)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-radio:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-radio:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/N9ZB7G/feedback/)

---

### Broadband data transfer over USB for GNU/Linux: 1-2 GHz (L-band) SDR receiver dedicated to GNSS (and other) reception, interfacing with PocketSDR, GNU Radio and gnss-sdr

- **Speakers:** Jean-Michel Friedt
- **Room:** UB2.147
- **Day:** Saturday
- **Time:** 16:15 - 17:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4150-broadband-data-transfer-over-usb-for-gnu-linux-1-2-ghz-l-band-sdr-receiver-dedicated-to-gnss-and-other-reception-interfacing-with-pocketsdr-gnu-radio-and-gnss-sdr/)

#### Abstract

A dual-MAX2771 radiofrequency frontend fitted on a FX2LP parallel to USB interface is presented as an update to Tomoji Takasu's PocketSDR. Having understood the underlying operating principles of the FX2LP configured through its 8051 microcontroller core using the opensource sdcc compiler, we configure the MAX2771s to collect samples up to 44 MS/s in the L-band ranging from 1 to 2 GHz. We first demonstrate proper operation by collecting and decoding Iridium messages using gr-iridium, despite the 2 or 3-bit resolution of the IQ ADCs, before demonstrating post-processing and real time processing of GNSS data. Both real time data collection, processing and streaming using GNU Radio and GNSS signal decoding using gnss-sdr are demonstrated. Tomoji Takasu's PocketSDR software provides invaluable insight and our contribution is porting the firmware to sdcc to get rid of any proprietary tool for developing the PocketSDR-like board.
The coherent multi-receiver architecture allows for processing the same L-band with two antennas for Controlled Radiation Pattern Antenna (CRPA) processing and detecting spoofing by inconsistent direction of arrival ; or processing two bands (e.g. L1/L5 or L1/L2) simultaneously.
See https://github.com/jmfriedt/max2771_fx2lp/: the subject of this presentation was the core project of the opensource tools for embedded systems development ELISE Master teaching at University of Franche-Comté is Besançon, France.

#### Related Links

- [Project repository](https://github.com/jmfriedt/max2771_fx2lp/)
- [slides of the presentation](http://jmfriedt.free.fr/fosdem2025.pdf)
- [Dataset recorded for the demonstation and GNU Radio flowchart](http://jmfriedt.free.fr/fosdem_galileo.tar.gz)
- [Associated article (1/2)](https://github.com/jmfriedt/max2771_fx2lp/blob/main/hackable_max2771_1eng.pdf)
- [Associated article (2/2)](https://github.com/jmfriedt/max2771_fx2lp/blob/main/hackable_max2771_2_eng.pdf)
- [Video of the demonstration](https://www.youtube.com/watch?v=9ugML8JjXIQ)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-radio:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-radio:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PE97XJ/feedback/)

---

### Meshtastic - off-grid communication for everyone

- **Speakers:** Thomas Göttgens
- **Room:** UB2.147
- **Day:** Saturday
- **Time:** 17:10 - 18:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4375-meshtastic-off-grid-communication-for-everyone/)

#### Abstract

Meshtastic is an open source, off-grid, decentralized, mesh network built to run on affordable, low-power devices. A bit of history, a bit of the future and lots of hands-on action, running on the ISM and SRC frequencies below and above 1GHz. It uses Lora-P2P with dedicated radio chips and forms ad-hoc meshes. In HAM mode the encryption is switched off and the ISM airtime restrictions are lifted.

#### Related Links

- [Meshtastic Homepage and Documentation](https://meshtastic.org/)
- [Github Project Space](https://github.com/meshtastic)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-radio:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-radio:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UW3GYJ/feedback/)

---

### Yet another new SDR runtime?

- **Speakers:** Daniel Estévez
- **Room:** UB2.147
- **Day:** Saturday
- **Time:** 18:05 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5499-yet-another-new-sdr-runtime-/)

#### Abstract

I will present some work-in-progress/experiments on a high-performance graph-based SDR runtime that differs from popular runtimes such as GNU Radio and FutureSDR in that instead of using circular buffers to connect adjacent blocks, the data travels in packets through closed circuits encompassing multiple blocks of the flowgraph. I show benchmarks comparing GNU Radio 3.10, GNU Radio 4.0, FutureSDR, this new runtime, and a hand-written ad-hoc implementation, for a class of certain simple flowgraphs. These show that popular runtimes often have a high overhead and that there is much room for improvements in performance. This project focuses on ARM Cortex-A53 CPUs, found in AMD RFSoC/MPSoC and other embedded platforms, but most ideas are applicable to other systems, including fast x86_64 machines.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-radio:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-radio:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/S9BXNL/feedback/)

---

## Railways and Open Transport (10)

### Opening Railways and Open Transport Devroom

- **Speakers:** Max Mehl, Cornelius Schumacher, Simon Clavier, Loic HAMELIN, Brede Dammen, Peter Keller, Tu-Tho Thai
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 13:15 - 13:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6654-opening-railways-and-open-transport-devroom/)

#### Abstract

Welcome and setting the stage for the Railways and Open Transport Devroom by the co-organizers of the Devroom

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-railways:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-railways:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MZKBUU/feedback/)

---

### European standards to serve both public transport and rail, demystification of NeTEx, SIRI and TOMP API 2.0

- **Speakers:** Brede Dammen, Tu-Tho Thai, Edwin van den Belt
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 13:20 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5345-european-standards-to-serve-both-public-transport-and-rail-demystification-of-netex-siri-and-tomp-api-2-0/)

#### Abstract

The updates in the EU regulations, especially TSI Telematics, reinforced the role of European standards from passenger information to ticketing. This talk will:
* quickly brush over the EU regulations impacts and introduce European standards
* demystify how to use NeTEx and SIRI for both rail and public transport
* showcase how to use TOMP-API 2.0 to create integrated booking and ticketing systems
The objective is to highlight all the upcoming opportunities for open-source software development in this specific field. We hope that it wil inspire the room to create open-source solutions to bridge public transport and rail even further.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-railways:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-railways:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LJRVDL/feedback/)

---

### Netzgrafik-Editor - a human-centric timetable planning approach

- **Speakers:** Adrian Egli
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 14:00 - 14:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5023-netzgrafik-editor-a-human-centric-timetable-planning-approach/)

#### Abstract

Netzgrafik-Editor (NGE) is an open-source software that enables the creation, modification, analysis and optimization of integrated interval timetables at a macroscopic level of detail, developed by Swiss Federal Railways (SBB CFF FFS). 
Source Code: Netzgrafik-Editor (github)
User Manual: Netzgrafik-Editor
Demo: Netzgrafik-Editor
Free Public Accessible Online Demo - Application
Netzgrafik-Editor tackles a significant business problem by providing a robust solution for long-term timetable planning. A live demonstration will showcase the functionality and the excellent interactive user interface of the Netzgrafik-Editor.
Why a Human-Centric Approach Matters
Netzgrafik-Editor - together with our users we developed a novel approach for interactive timetable planning - user research, user involvement and usability testing were done among others to increase the user experience of the tool.
The result of this human-centered approach is that the Netzgrafik-Editor is not only technically sophisticated but also intuitive and user-friendly. Planners can now create, adjust, and optimize schedules with ease. The tool adapts to their workflows, not the other way around. Users feel heard and taken seriously, which significantly increases their satisfaction and engagement.
This story impressively demonstrates why a human-centered approach is so important. It ensures that technology serves people, not the other way around. The users like to use the Netzgrafik-Editor. This fosters innovation by putting actual needs at the forefront and users like to contribute and help to improve the tool which they have developed together with IT specialists. 
Open Source As an Enabler
The Netzgrafik-Editor exemplifies a successful open-source project within the public transportation sectors. By embracing open collaboration, we leverage diverse expertise to address internal needs more effectively. This approach fosters a dynamic environment where building, sharing, and profiting from collective efforts become feasible. Open-source strategies enable us to reconsider traditional architecture principles, transitioning from a buy-versus-build mindset to one where open-source solutions empower us to build, share, and profit together.
Open Source is Not Enough - Attention Is All You Need
Our journey in the open-source realm has taught us valuable lessons, particularly in enhancing the visibility of our projects. Merely opening the source code is insufficient; we must also bridge the gap between software developers and end-users. By making our application freely accessible online, we ensure that it reaches a broader audience, demonstrating that open-source success relies not just on code availability but also on user engagement and accessibility.
Netzgrafik-Editor's Software - Some Insights
We have implemented much of the logic in the frontend (TypeScript) rather than the backend because performance and interactivity are crucial. Low latency and maximum responsiveness are thus ensured in the frontend.
Open Issues
One of our current key challenges is preventing forks in our open-source projects. We aim to benefit from all contributions, ensuring that enhancements and innovations made today and in the future remain integrated within the main project.
Additionally, we seek ways to derive and share novel interaction design patterns that can be freely used, promoting consistency across open-source tools in similar application domains. By doing so, we hope to create a more cohesive and user-friendly ecosystem. For more information, visit digital.sbb.ch and sbb-design-systems.
How Can You Contribute

Issue, documentation, ... , Source Code (bug fixes, ... , features), pull request.
Share data, data importers to improve data exchange (converters).
Roadmap: What next?

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-railways:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-railways:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/L3ZAQ8/feedback/)

---

### Enhancing OSRD with NGE’s Macroscopic Visualization

- **Speakers:** Louis Greiner
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 14:20 - 14:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5221-enhancing-osrd-with-nge-s-macroscopic-visualization/)

#### Abstract

OSRD (Open Source Railway Designer) is a an open source web application, supported by SNCF Réseau, for operational studies (railway infrastructure design, simulations, capacity analysis, timetabling) and also last-minute train slot design! Operational studies' scope is microscopic, however, OSRD aims to cover a wider scope, including more long term studies, aka macroscopic studies. Also, OSRD is missing a graphic tool, to visualize and work on timetables, which can be tough to read on bigger scales.
Source code: https://github.com/OpenRailAssociation/osrd
NGE (Netzgrafik-Editor) is another open source web application, supported by SBB CFF FFS, that enables the creation, modification, and analysis of regular-interval timetable, through a network graphic visualization. It has been designed to work on macroscopic studies.
Source code: https://github.com/SchweizerischeBundesbahnen/netzgrafik-editor-frontend
This talk is about the integration of NGE in OSRD:
- open source collaboration
- microscopic / macroscopic concepts
- integration of an Angular application in a React application
By providing an editor tool, NGE enables OSRD to work on macroscopic studies as well, creating opportunities and saving crucial development time, that can be used to focus on a model that can support both microscopic and macroscopic levels of detail.
Also, the choices made for the integration should allow OSRD to benefit NGE development, and in return, OSRD should contribute to NGE, in order to drive each other forwards.
Thanks to the open source, OSRD gained a powerful and well designed component, and NGE gained not only users, but also developers that contribute to the project. The two teams work alongside, redefining the working experience in big organizations, proving that the open source approach works!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-railways:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-railways:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/V3DLNT/feedback/)

---

### The Flatland Framework: Enabling Machine Learning Research for Railway Rescheduling and Beyond

- **Speakers:** Manuel Schneider
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 14:40 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5890-the-flatland-framework-enabling-machine-learning-research-for-railway-rescheduling-and-beyond/)

#### Abstract

The Flatland Framework is a multi-purpose simulation framework to tackle problems around resilient resource allocation under uncertainty with a focus on railway networks. The framework provides a flexible, method-agnostic simulation environment to support research into novel approaches from operations research and machine learning, particularly for solving real-time vehicle rescheduling and dispatching challenges.
In this presentation, we will dive into Flatland's development as an open research framework, from its origins in addressing practical railway challenges to its current role in the transportation research community. The talk will demonstrate the framework's key capabilities and explore how the open source approach sparked a rich community and ecosystem around open transport research.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-railways:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-railways:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AHLFLV/feedback/)

---

### Post processing GNSS train positions

- **Speakers:** Mathias Vanden Auweele
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 15:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4319-post-processing-gnss-train-positions/)

#### Abstract

Trains run on tracks, so intuitively, if we know the location of the rails, we should be able to adjust any measured position to align more closely with reality, right?
Right! But it's not that simple...
Measurement trains play a crucial role in ensuring railway safety and maintenance. They collect vital data on various parameters, including track gauge and catenary height. When these measurements fall outside acceptable limits, technicians are dispatched to address the issues. Over time, certain parameters can degrade, making predictive analysis essential for anticipating maintenance needs and enhancing operational efficiency. However, both timely interventions and accurate predictive analytics hinge on precise positioning of the measurement data.
In this talk, we will delve into the inner workings of an open-source library developed as part of the Openrail initiative. This library leverages rail network topology, train detection data, and GNSS/IMU/ODO information to post-process train positions effectively.
As an added bonus, we’ll explore how open-source hardware, specifically a Raspberry Pi, contributes to the positioning of measurement trains.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-railways:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-railways:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KGAXJU/feedback/)

---

### NeTEx and SIRI: Show me the code

- **Speakers:** Alban Peignier
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 15:30 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5113-netex-and-siri-show-me-the-code/)

#### Abstract

NeTEx and SIRI are described as complex and painful. But what if they only require a few lines of code ?

Read a NeTEx file
Invoke a SIRI API
How to find NeTEx datasets ?
How to find SIRI APIs ?
One is missing ?
Create a NeTEx file
Create a SIRI server
What's missing ?

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-railways:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-railways:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HJLYLR/feedback/)

---

### Explorative Routing

- **Speakers:** Katharina Rasch
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 16:00 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6205-explorative-routing/)

#### Abstract

When planning long train trips across Europe (e.g. Brussels -> Sicily), standard routing criteria such as travel time and number of transfers become less relevant. I want a comfortable connection, with enough buffers, in particular when operators change. If I need to stop somewhere overnight on long trips, let’s make it a place I haven’t visited yet! But please, let’s arrive there early enough so that I have time for some touristing. Aha, there is a (non-optimal) route through Munich? That’s a chance to visit an old friend I haven’t seen in a while! Oh, I see, I have to change trains in Rome anyway? Lunch out in the sun on the piazza, that sounds fantastic. In short, for such trips, the journey can often feel as part of the destination.
The criteria listed above are quite personal and often only emerge while planning the trip. Sure, existing routing tools allow me to change my search settings and re-run the search. But what I really want is to interact with the proposed travel plans, to change them how I see fit. Move connections here and there, use drag&drop to try out what would happen if I did take time for that lunch in Rome, how much later would I arrive at my destination? To explore on a map what possible routes there even are, and perhaps add a little detour to a place I’ve been wanting to visit.
In my project Trans-Europe-Planner (funded by prototypefund/German Ministry of Education and Research), I am building such a user interface, testing out different UX mechanisms for interactively exploring, moving connections around, trying things out, comparing options. How that all works and how users respond to it, that is what I want to discuss in my talk.

#### Related Links

- [Code repo](https://github.com/krasch/trans-europe-planner)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-railways:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-railways:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KMPJD8/feedback/)

---

### GNOME Maps meets Transitous meets MOTIS

- **Speakers:** Felix Gündling, Marcus Lundblad, Jonah Brüchert
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 16:30 - 16:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4105-gnome-maps-meets-transitous-meets-motis/)

#### Abstract

Transitous is an open, community-run provider-neutral international mobility platform. Using openly available GTFS and GTFS-RT public transport data and MOTIS, a FOSS real-time routing engine, we operate a free to use global routing service that does not stop at borders. Our mission is to offer a provider-neutral, international, cross-border, and privacy friendly routing that focuses on the interest of the user. In the future, this work can serve as a building block for open Google Maps alternatives. In this talk we will show you how our crowdsourced data collection process works and how you can join us and contribute. We will present clients such as GNOME Maps and their integration with Transitous. Finally, we will have a look at the technical innovations in MOTIS that enable planet sized routing (including geocoding, street and indoor routing, and map tiles) on affordable hardware.

#### Related Links

- [transitous.org](https://transitous.org)
- [MOTIS GitHub](https://github.com/motis-project/motis)
- [GNOME Maps](https://gitlab.gnome.org/GNOME/gnome-maps)
- [motis:matrix.org](https://matrix.to/#/#motis:matrix.org)
- [transitous:matrix.spline.de](https://matrix.to/#/#transitous:matrix.spline.de)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-railways:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-railways:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LCDABM/feedback/)

---

### HackerTrain to FOSDEM 2025 (a.k.a. the beta run)

- **Speakers:** Matija Šuklje
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 16:50 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5311-hackertrain-to-fosdem-2025-a-k-a-the-beta-run-/)

#### Abstract

At this point, the first HackerTrain to FOSDEM has – hopefully 🤞 – arrived!
In this talk we will present :

what was/is the HackerTrain to FOSDEM
how the idea came about and who was involved
the rollercoaster ride that was the different plans we tried
the actual train ride that followed (hopefully with pictures!)
lessons learnt
what are the long-term goals for this project

Through this beta run of the HackerTrain to FOSDEM we hope to uncover also the potential for (massive) group travel to (FOSS) events, as well as the hurdles that we still need to overcome to make affordable, easy, comfortable and engaging cross-border public travel possible.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-railways:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-railways:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FEVNFB/feedback/)

---

## Real Time Communications (RTC) (12)

### Engaging the Open-Source Community: Exploring the OpenSIPS Community Edition Projects

- **Speakers:** Răzvan Crainea
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 15:00 - 15:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5063-engaging-the-open-source-community-exploring-the-opensips-community-edition-projects/)

#### Abstract

The OpenSIPS Community Editions are the community effort to produce real-life SIP solutions (as platforms) already configured to fulfill precise SIP scenarios. OpenSIPS based solutions – acting as SoftSwitch or SBC – that are ready to use and simple to deploy.
This presentation offers a detailed look at the OpenSIPS Community Edition projects, exploring their capabilities, current status, and development roadmaps. It delves into the innovative ideas driving these projects and emphasizes the critical role of the open-source community in their evolution. To conclude, a brief showcase using Docker Compose will effectively demonstrate the practical utility of the OpenSIPS Community Edition projects.

#### Related Links

- [OpenSIPS Project](https://opensips.org)
- [OpenSIPS Community Editions](https://ce.opensips.org)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rtc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rtc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZCRRBA/feedback/)

---

### OAuth Authentication and Identity Validation in SIP Systems

- **Speakers:** Jehan Monnier, jehan.monnier@belledonne-communication.com
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 15:15 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5508-oauth-authentication-and-identity-validation-in-sip-systems/)

#### Abstract

User authentication in real-time communication systems using SIP (Session Initiation Protocol) is evolving with the adoption of OAuth 2.0, as outlined in RFC 8898, published by the IETF in 2020. This protocol secures user access through authentication tokens (instead of traditional methods like Digest). This "Single Sign-On" approach allows for the use of a unified identity verification source across the entire information system, and is now being extended to VoIP.
In this conference, we will explore how OAuth 2.0 and OpenID Connect are integrated into a modern SIP environment, with a focus on managing and validating access tokens. To illustrate this, we will use our Flexisip server solution.
Key Topics:
- OAuth 2.0 and OpenID Connect: Introduction and benefits for authentication in modern SIP systems.
- JWT for Authentication: Token signature validation and extracting user identity.
- Integration in Flexisip: Demonstration of OAuth-based authentication with Flexisip, and token validation in a SIP environment.
- Authorization Management: Controlling requests based on identity information extracted from access tokens.
This conference will provide an overview of how to implement and secure user authentication with OAuth 2.0 and JWT in a SIP server, using Flexisip as a concrete example.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rtc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rtc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/L39VWE/feedback/)

---

### Enabling AI-Powered Conversations at Scale with Kamailio, FreeSwitch, and RTPEngine

- **Speakers:** Nuno M Reis
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 15:35 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6285-enabling-ai-powered-conversations-at-scale-with-kamailio-freeswitch-and-rtpengine/)

#### Abstract

In a call center environment, this talk will explore how to leverage the power of Kamailio, FreeSwitch, and RTPEngine to enable AI-driven real-time conversations at scale.
We will dive deep into how to integrate AI copilots, providing real-time call transcriptions and conversational context, as well as AI autopilots, enabling call conversations with specialized bots.
By taking advantage of well-defined standards like SIPREC, and leveraging the capabilities of Kamailio, FreeSwitch, and RTPEngine, along with some additional custom code, we will demonstrate ingenious ways to enable these AI-powered capabilities for any VoIP environment, even legacy proprietary systems.
Attendees will learn practical techniques and best practices for building scalable, AI-enhanced call center solutions that can improve customer experience, increase agent productivity, and drive business outcomes.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rtc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rtc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3ZSGXG/feedback/)

---

### RTCP, Racecars, video and 5g

- **Speakers:** Tim Panton
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 15:55 - 16:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5586-rtcp-racecars-video-and-5g/)

#### Abstract

We have built a low latency 5g Video camera for race cars using linux and WebRTC.
We use RTCP (RTP's companion protocol) to help cope with the variability in quality and bandwidth of a 5g connection.
The talk will describe the problems we encountered, how we used data from RTCP to solve them.
We will present experimental data from tests run with and without RTCP at varying speeds (30->160km/h).
We will also describe the opensource java (S)RTP/RTCP library we developed and used for this work
https://github.com/steely-glint/srtplight as well as an LGPL demo program that uses srtplight implement the WebRTC based WHIP protocol
(https://github.com/pipe/whipi)

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rtc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rtc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DSKEPM/feedback/)

---

### SIP-V+T=❤️? Tales of taking VoIP out of SIP and adding TCP instead, or Proxy All Things

- **Speakers:** Maksym Sobolyev
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 16:15 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4161-sip-v-t-tales-of-taking-voip-out-of-sip-and-adding-tcp-instead-or-proxy-all-things/)

#### Abstract

Our exploratory quest of previously uncharted territory of real-time TCP/TLS media over SIP RFC4145 (hey don't confuse it with TCP as a SIP transport!) and all the fun and possibly profit that can be had from it potentially. As part of the presentation I would announce the SIP Proxima project implementing this functionality and do a demo of various application protocols (e.g. postgresql, mysql, rrdcache, thrift, https etc) operating over it.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rtc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rtc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BSFDMJ/feedback/)

---

### WebRTC support in WebKitGTK and WPEWebKit with GStreamer: Status update

- **Speakers:** Philippe Normand
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 16:35 - 16:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4651-webrtc-support-in-webkitgtk-and-wpewebkit-with-gstreamer-status-update/)

#### Abstract

The WebKit WPE and GTK ports are aiming to leverage GstWebRTC as their WebRTC backend. Over the years we made progress towards this goal both in WebKit and in GStreamer. During this talk we will present the current integration status of GstWebRTC in WebKit and the plans we have for the coming months.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rtc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rtc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NRP3HQ/feedback/)

---

### Kamailio 6.0 (development) update

- **Speakers:** Henning Westerholt
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 16:55 - 17:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5978-kamailio-6-0-development-update/)

#### Abstract

Kamailio is one of the most widely used open source SIP servers for large VoIP and real-time communication platforms. The talk will give an overview of the key topics of the newly released version 6.0, describing the improvements in the UDP worker architecture, asynchronous processing, the new build system and other important changes. The presentation is aimed at people who are interested in developing high-performance VoIP platforms, developers who want to extend or improve Kamailio, and operations experts who run Kamailio infrastructures.

#### Related Links

- [Kamailio homepage](https://kamailio.org)
- [Kamailio github](https://github.com/kamailio/kamailio)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rtc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rtc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VU8JGT/feedback/)

---

### A long, short history of realtime AI agents

- **Speakers:** Rob Pickering
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 17:10 - 17:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6180-a-long-short-history-of-realtime-ai-agents/)

#### Abstract

Until a few months ago, the only working approach for connecting realtime AI agents to WebRTC streams and phone calls was to use lengthy pipelines of speech to text, agent orchestration, and text to speech, often using multiple machine learning models from commercial vendors.
That has changed with new realtime speech to speech models, most famously the (closed) OpenAI advanced voice, but what are the open source ways to build these kind of systems?
This talk walks through my experience with using 4 different projects to build functional systems which can use open source (open weights) models at their core. We will talk about how we have integrated Jambonz, Livekit, and Ultravox (Fixie.AI) within our Aplisay framework and what this allows us to do.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rtc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rtc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WP8KEA/feedback/)

---

### Chatting on IRC in 2025: grandpa, what's up?

- **Speakers:** Simon Ser, Thomas Flament
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 17:30 - 17:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6407-chatting-on-irc-in-2025-grandpa-what-s-up-/)

#### Abstract

IRC is a venerable 37 year old chat protocol used by many open-source software projects, technical experts happily lending their help and other discussion groups. However, the historic IRC protocol is not always well-suited to modern usage, such as connecting from multiple devices with unreliable connectivity, or connecting from battery-constrained mobile devices.
In this talk, Simon and Thomas will explain how IRC has evolved in the last few years to address these challenges through efforts like the IRCv3 working group and new software (soju, senpai, gamja, goguma). We've been working on adding new features such as easily accessing message history, sharing files and pictures and searching through messages. Some of the architectural design decisions may be interesting to people working on other open protocols, for instance secure and interoperable push notifications or OAuth integration.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rtc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rtc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/Z3FXQY/feedback/)

---

### Call fraud prevention through traffic trends monitoring using CGRateS

- **Speakers:** Dan Christian Bogos
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 17:50 - 18:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5884-call-fraud-prevention-through-traffic-trends-monitoring-using-cgrates/)

#### Abstract

In this talk we will review together TrendS, a newly implemented subsystem within CGRateS to help you build your own traffic trends analysis as well as react to unexpected behaviour through automatic actions available.
CGRateS is a battle-tested Open-Source Enterprise Billing Suite with support for various prepaid and postpaid billing modes.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rtc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rtc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BGPVXX/feedback/)

---

### AI for Meetings

- **Speakers:** Tudor Avram, Răzvan Purdel
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 18:05 - 18:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5061-ai-for-meetings/)

#### Abstract

This is the story of how Jitsi's AI evolved and expanded its features while keeping it all open source: from half-botched PoCs in a weekend to features our customers use in production on a daily basis. Razvan will walk you through some of the implementation details and gotchas of the near-real-time transcription system, while Tudor will guide you through all the other goodies which rely and expand on it.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rtc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rtc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VXZF3X/feedback/)

---

### A Universal and Stable API to Everything: XMPP

- **Speakers:** Jérôme Poisson (Goffi)
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 18:25 - 18:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5721-a-universal-and-stable-api-to-everything-xmpp/)

#### Abstract

Nowadays, most services provide APIs with their own formats, and sometimes multiple versions, which may change over time. But there is a universal API, with an excellent track record of stability and backward compatibility: XMPP! 
In this talk, I'll show how XMPP can be more than just an Instant Messaging protocol, and how it can be an extremely powerful tool to access almost anything, from third-party networks (IM, microblogging, etc.) to file sharing, automation (IoT), and more. 
I'll briefly explain how the XSF (XMPP Standards Foundation) is organized, how specifications are created, and why having a large number of XEPs (we are now in the 500 series) is not a bad thing—quite the opposite. 
Next, I'll discuss some mechanisms of XMPP and demonstrate how they can be applied to a wide range of use cases. 
I'll also show that you can use XMPP without having to deal with XML—you can use JSON from your software or other layers. 
XMPP is a fantastic toolbox that can help you do almost anything. Let's dive into it and explore how it can help you achieve things simply, efficiently, and quickly.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rtc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rtc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LWNXCN/feedback/)

---

## Retrocomputing (13)

### Welcome to Retrocomputing Devroom

- **Speakers:** Sebastian Eggermont
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 13:10 - 13:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4183-welcome-to-retrocomputing-devroom/)

#### Abstract

Welcome to Retrocomputing Devroom

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PNBEL8/feedback/)

---

### Error correction for Dragon Quest passphrases

- **Speakers:** Raphaël Zumer
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 13:15 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4221-error-correction-for-dragon-quest-passphrases/)

#### Abstract

Learn about the structure of the passphrases ("fukkatsu no jumon") used for saving progress in the Famicom versions of Dragon Quest and Dragon Quest II, and about a new open source tool, ReJumon, designed to find and correct transcription errors.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PPMHAF/feedback/)

---

### Bildschirmtext - Reeenacting an ancient communication system using Javascript and Common Lisp

- **Speakers:** Hans Hübner
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 13:25 - 13:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4783-bildschirmtext-reeenacting-an-ancient-communication-system-using-javascript-and-common-lisp/)

#### Abstract

The German Bildschirmtext system was an early large-scale public access information service established in 1983.  Using telephone connections, users would dial in to a central system which offered them with access to commercial and non-commercial offerings.  Television sets were used as display devices, with a set top box or built-in decoder proving the terminal functionality.  Communication was bi-directional with a low-speed back channel that allowed typing in text messages.
The introduction of Bildschirmtext overlapped with the home computing era, but for regulatory reasons, home computers could not easily be used as Bildschirmtext terminals.  This, among other technical and non-technical reasons, caused the service to fail to reach its full potential.  It remained in use as a carrier system for home banking and other high security applications until it was finally switched off in 2007.
As Bildschirmtext was a centralized system operated by the federal Deutsche Bundespost on mainframe systems, much of the content that was available has been lost.  A couple of the original data files of the Chaos Computer Club have survived, however, and as the CCC became notorious in the context of Bildschirmtext, that content made for an entertaining exercise in re-engineering.
In the talk, I will present my journey as a recent Bildschirmtext enthusiast. I will describe how the service was organized, how content providers edited content and put it into the system and how users would access it.  I will also dive into my implementation of a Bildschirmtext terminal emulator in Javascript and a central service system written in Common Lisp, providing the audience with an insight of the challenges, constraints and possibilities of the system.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7TSQCE/feedback/)

---

### Keeping a hand on the evolution of cursor controls:  important mice of the past and what to do if you get one today

- **Speakers:** Dmitriy Kostiuk
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 13:45 - 14:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5153-keeping-a-hand-on-the-evolution-of-cursor-controls-important-mice-of-the-past-and-what-to-do-if-you-get-one-today/)

#### Abstract

The talk tracks the evolution of the peripheral devices that transmit their motion to a cursor - namely mice and trackballs. The analysis covers motion detection methods, the way signals are transmitted to the computer, ergonomics, and ways to test the device with a modern computer. The pre-commercial phase is covered, which includes early marine radar trackballs, Douglas Engelbart's wheel mouse, and Rollkugel ball mouse. The commercial phase is tracked through the following personally studied devices, including early Xerox mice with mechanical and optical encoders, Mouse Systems' design with a simplified optical encoder and reflective mouse pad, Depraz and Apple mice that commercialized the optomechanical encoder, the returns to  Engelbart's original approaches in 1980s analog mice for home computers and wheel mice such as Torrington/Numonics Manager mouse and Hawley DEC mouse, and, finally, the ProAgio Scroll mouse that started the wheel scrolling revolution. Considered connection methods include parallel, serial, serial bus, and analog ones. Surprisingly, all mice and trackballs covered in the talk can be connected to modern computers using open-source converters, which are also examined and discussed.

#### Related Links

- [Detailed info on the reviewed mice (and a number of other “mouses”)](https://mouses.info)
- [Interface converter to use Amiga mice as USB HID (perfectly usable for other quadrature mice)](http://github.com/BleuLlama/AmigaInputToUSB)
- [Dedicated USB converter for Depraz mice](https://github.com/floren/depraz-arduino)
- [Retronics USB converter for various joysticks and mice](https://github.com/retronicdesign/USBJoystickAdapter_v3.3)
- [Converter coming as a part of the TMK keyboard firmware (useful for HP HIL, ADB and serial mice)](https://github.com/tmk/tmk_keyboard/tree/hphil/converter/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EHTQ9U/feedback/)

---

### A PID control system based on the MOS 6502 - CANCELLED, replaced by panel discussion

- **Speakers:** Mark Meyer
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 14:05 - 14:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4656-a-pid-control-system-based-on-the-mos-6502-cancelled-replaced-by-panel-discussion/)

#### Abstract

I'll be showcasing the design of a (originally) MOS 6502 based PID (proportional-integral-differential) control system. This system has been in productive use until a couple of years ago in the mechanical engineering department in the HAW Hamburg. The purpose of the system was to educate students.
The system is equipped with DAC, ADC I/O functions, CPU, and a variety of interesting controls.
This is a multi chassis system, that used to fit in a standard 19" rack.
I'll chronicle my journey to survey, inspect, and get the system into operational state.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NZGQ7V/feedback/)

---

### Supersonic retro development with Docker

- **Speakers:** Steven Goodwin
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 14:25 - 14:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4235-supersonic-retro-development-with-docker/)

#### Abstract

The beauty of retro computers, especially in the 8-bit era, is that you develop for the computer on the computer, with it’s default prompt being a BASIC interpreter from which you can load any of the original native tools. But who wants to develop like it’s 1979?
Cross-compiling for one architecture, while sat in the comfort of another, is nothing new. But these modern tools are specialised, and not always general enough to be packaged with every distribution. Or if they are available today, will they tomorrow? Or do they require extensive dependencies, specific versions, or changes to the host OS and libraries that are incompatible with your day-to-day?
Docker, first introduced in 2013 (which almost makes it retro itself!), lets us run these tools in a safe  containerised environment that act like a virtual time capsule, providing fully reproducible builds and super-fast turn-around so you can stay in the creative flow.
In this talk we see two similar projects, ZXDocker and Dragon Docker, to see how simply retro development tools like cross-compilers, assemblers, BASIC→binary converters, and emulators can be combined into a Docker image that results in a one-click workflow.
Perhaps this will future-proof the retro development process for another 40 years!

#### Related Links

- [Dragon Docker](https://github.com/MarquisdeGeek/DragonDocker)
- [ZX Docker](https://github.com/MarquisdeGeek/ZXDocker)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KXKDHU/feedback/)

---

### (General) Electric Dreams: restoring the GE-120, a milestone in transistor-based computing

- **Speakers:** Daniele Lacamera, Antonio Malara - Biappi
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 14:40 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5866--general-electric-dreams-restoring-the-ge-120-a-milestone-in-transistor-based-computing/)

#### Abstract

We are the Museo Interattivo di Archeologia Informatica (MIAI) and the Museo dell’Informatica Funzionante (MusIF), two Italian cultural organizations dedicated to preserving and exploring the history of computing and its societal impact. We focus on creating engaging, interactive exhibits that highlight vintage hardware and software, offering hands-on experiences to captivate visitors of all ages.
One of our signature events, Electric Dreams, is an annual gathering for members, supporters, and enthusiasts. In its first four editions, the event centered on the restoration of a General Electric GE-120, a historic computer that represents one of the early successors to Olivetti’s groundbreaking ELEA 9000 series—the first solid-state transistor-based computer in history.
The computer was used at the Zurich Airport until its decommissioning in 1984. This machine played a key role in early aviation systems and its restoration offers a window into the technological evolution of the 20th century.
Thanks to the fact that the donor preserved the original manuals—written in four languages, and partially hand written—  our archival team has fully digitalized 57 binders worth of documentation. Meanwhile, the restoration team has focused on following the original testing procedures to validate the components of the CPU.
Reconstructing the self-test rig has been a critical milestone, enabling efficient identification and replacement of all the parts that tested as defective.
To complement this effort, we are also developing a full emulator for the GE-120, creating a bridge between its historical operation and modern exploration.
This talk will trace the journey of the restoration project, detailing achievements to date and setting the stage for the future.
With a look ahead to Electric Dreams 2025, usually occurring during the last weekend of July, we invite the audience to join us in sunny Calabria for a hands-on experience with this exciting challenge.
https://github.com/MusIF-MIAI/ge-120-test-rig/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/J3YDAB/feedback/)

---

### Pac-Man for the DEC VT420

- **Speakers:** Francois Laagel
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 15:00 - 15:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5990-pac-man-for-the-dec-vt420/)

#### Abstract

Pac-Man is a graphical game designed in 1979 by a team of five people and
implemented in Z80 assembly language over the course of seventeen months.
This presentation will be an evolutionary account of my own Forth implementation
in ANS94 Forth for the Digital VT420 text terminal over a three month period.
The C port of the resulting application to Linux and OpenVMS 9.2 will also
be briefly covered. 
Stress will be laid upon the value of standards throughout this talk.
Various development/prototyping tools were required for this implementation
to be successful. In essence, this paper is a first person account of an
experience in retrocomputing.

#### Related Links

- [Z79Forth Project Repository](https://github.com/frenchie68/Z79Forth/tree/REL-ANS94)
- [Relevant Application Software](https://github.com/forth2020/frenchie68)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9TBYTF/feedback/)

---

### Raiders of the lost hard drive

- **Speakers:** Michal Pleban
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 15:20 - 15:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5479-raiders-of-the-lost-hard-drive/)

#### Abstract

In 1984 Commodore introduced the C900, a budget Unix workstation with an obscure Zilog Z8000 processor. Unfortunately, when hey bought the Amiga, the Commodore 900 project was canceled and today only a few dozen prototypes exist.
A few years ago I happened to get one of these prototypes. Without a working power supply, monitor, keyboard and with the hard drive giving a mysterious 0xFF error, I was left puzzling on how to make the machine run. 
This talk documents my successful effort to bring the machine back to life. It is a continent-spanning tale of digital archaeology, which included, among others, disassembling the Z8000 BIOS, reverse-engineering the keyboard interface and figuring out the hard disk low level format. After I figured out how to make the machine run, I have helped two other Commodore 900 owners with the same problems to make their machines fully working.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3U8BKK/feedback/)

---

### Rediscovering the fun of programming with the Game Boy

- **Speakers:** Eldred HABERT, Sylvie Oukaour
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 15:35 - 15:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4605-rediscovering-the-fun-of-programming-with-the-game-boy/)

#### Abstract

The Game Boy is a handheld video game console released by Nintendo in 1989. Together with its Color successor, they sold nearly 120 million units, the fourth best-selling game console ever. Homebrew games (i.e. not made by professional studios) started being created for it in the late 90's, and still are today, thanks to constantly improved tooling and resources.
Thirty-five years later, the amateur/hobbyist video game community has changed drastically, with smartphone and web apps dominating the space. In this talk, we will explain how the Game Boy is refreshingly simpler than modern development platforms, discuss why this is (mostly) a good thing, and showcase many ways to use this old system in modern ways to just have fun, even for rookie programmers and non-programmers!

#### Related Links

- [Homebrew Hub](https://hh.gbdev.io)
- [Game Boy demoscene](https://www.pouet.net/prodlist.php?platform%5B%5D=Gameboy&platform%5B%5D=Gameboy+Color)
- [Pan Docs](https://gbdev.io/pandocs/)
- [RGBDS assembler](https://rgbds.gbdev.io)
- [RGBDS-live](https://gbdev.io/rgbds-live)
- [RGBenv](https://github.com/gbdev/rgbenv)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/73EAZE/feedback/)

---

### The Small Device C Compiler targeting Z80, MOS 6502 and their derivatives

- **Speakers:** Philipp K. Krause
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 15:55 - 16:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4899-the-small-device-c-compiler-targeting-z80-mos-6502-and-their-derivatives/)

#### Abstract

The Small Device C Compiler (SDCC) is a free C compiler targeting 8-bit architectures, including the Z80, MOS 6502 and their derivatives, such as Z80N, Z180, Rabbit, eZ80, TLCS-90, SM83 (Gameboy CPU), R800, 65C02. It supports standard C up to current ISO C23.
We discuss the current state of SDCC, its use in retrocomputing, and relevant plans for the near future.

#### Related Links

- [SDCC website](https://sdcc.sourceforge.net/)
- [SDCC repository](https://sourceforge.net/p/sdcc/code/HEAD/tree/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9HQ9MK/feedback/)

---

### Silicium occitel mini

- **Speakers:** rene speranza, ben*.*
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 16:15 - 16:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4622-silicium-occitel-mini/)

#### Abstract

Discover how association Silicium, a French retro-computing non-profit, created a mini console to commemorate the Occitel, a gaming console from 1976 by a French company, Société occitane d’électronique.
From accurate software emulation through bit-banged video with low-cost hardware to solving hardware design mistakes without forgetting iterative adjustment of the 3d-printed case, we will tell the story and lessons of a team project that will be open-sourced on the day of the conference.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VYTYPB/feedback/)

---

### Writing a dynarec, step by step

- **Speakers:** Paul Cercueil
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 16:35 - 16:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6079-writing-a-dynarec-step-by-step/)

#### Abstract

Emulators for computers or consoles that came out in the 21st century are generally built around a Just-In-Time (JIT) compiler, more often called dynamic recompiler or "dynarec" in the emulation scenes. They are very complex pieces of software that take years to create, and get more and more complex the faster they become.
In 2014 I started to work on my own dynarec for the well-known Playstation emulator, PCSX. In this talk, I will walk through the steps of creating Lightrec, from the original concept idea of a cross-platform dynarec, all the way to running it on the Sega Dreamcast.

#### Related Links

- [Lightrec repo on Github](https://github.com/pcercuei/lightrec)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-retrocomputing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-retrocomputing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8EXJKT/feedback/)

---

## RISC-V (13)

### Welcome to the FOSDEM 2025 RISC-V DevRoom

- **Speakers:** Björn Töpel
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 10:30 - 10:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6256-welcome-to-the-fosdem-2025-risc-v-devroom/)

#### Abstract

Welcome session.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PG9XCH/feedback/)

---

### RISC-V Hardware - Where are we?

- **Speakers:** Emil Renner Berthing
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 10:40 - 11:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6031-risc-v-hardware-where-are-we-/)

#### Abstract

I'll talk about the current landscape of available RISC-V hardware powerful enough to run Linux and hopefully give a better overview of what to buy if you want to get into developing software for RISC-V. I'll talk about the difference between cores, SoCs and boards, who makes them, their performance and how well they're supported under Linux.

#### Related Links

- [Slides](https://esmil.dk/fosdem2025.pdf)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BPWST3/feedback/)

---

### Unstoppable Force Behind Linux on RISC-V

- **Speakers:** Yuning Liang
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 11:20 - 11:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4722-unstoppable-force-behind-linux-on-risc-v/)

#### Abstract

This talk will delve into how DeepComputing and Fedora have strategically collaborated to address the chicken-and-egg challenges in the RISC-V ecosystem, and to achieve Fedora official running on DeepComputing's DC-ROMA series laptops and pads, as well as upcoming workstation and server products.
Overcoming the complex barriers involved in this process required seamless collaboration among multiple partners. DeepComputing has played a pivotal role—not only in mass-producing RISC-V-powered devices but also in driving the implementation of proposed solutions. This includes close coordination with SoC partners, product solution providers, and active engagement with the Fedora team to ensure the best outcomes.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TJW3TD/feedback/)

---

### ABI Extractor - Understanding ABI compatibility between compilers targeting RISC-V

- **Speakers:** Luis Silva
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 12:00 - 12:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4838-abi-extractor-understanding-abi-compatibility-between-compilers-targeting-risc-v/)

#### Abstract

How to ensure that object files from two compilers are ABI (Application Binary Interface) compatible?
This talk presents a tool capable of extracting ABI properties for a RISC-V compiler. This human readable summary can be compared to another version, be it a reference version or one created for a different compiler or with different options, exposing where compatibility problems can pop up.
While the topic may not receive extensive attention, certain methods for ABI validation do exist, most of which focus on libraries. This tool, however, adopts a unique approach by focusing on extracting ABI properties to ensure compatibility between object files produced by different compilers. It covers aspects from data type sizes/alignment to the organization of data in registers and on the stack. For example, it identifies which registers or stack locations are used for variable/struct argument passing and distinguishes caller-saved from callee-saved registers.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/73HX7L/feedback/)

---

### Add RISC-V support to your favorite Operating System

- **Speakers:** Adrian Vladu
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 12:40 - 13:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6036-add-risc-v-support-to-your-favorite-operating-system/)

#### Abstract

This presentation focuses on the perspective of an Operating System maintainer - how easy it is to add RISC-V support to a Linux based operating system nowadays.
The case study is done on a FOSS Operating System - Flatcar Container Linux.
Flatcar Container Linux (https://flatcar.org) is a Container-optimized Linux distribution, CNCF incubated project, which has Gentoo as an upstream distribution.
We will go through the steps required to add RISC-V support, from the Linux Kernel quirks, the bootloader paradigms, and to the generic software support from the wider community: systemd, Docker, Kubernetes.
An important part that will be thoroughly presented is the current state of the art hardware availability combined with virtualization support, very much needed for testing and faster iteration.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/URVXG3/feedback/)

---

### RISC-V Unified Database: Streamlining the Ecosystem with a Centralized Source of Truth

- **Speakers:** Afonso Oliveira
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 13:20 - 13:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5386-risc-v-unified-database-streamlining-the-ecosystem-with-a-centralized-source-of-truth/)

#### Abstract

The RISC-V ecosystem currently relies on multiple disconnected repositories and specifications, including the assembly manual, opcode database, formal specifications like Sail and the non-machine readable ISA manual. This fragmentation of information is error prone and makes it hard for hardware designers, researchers, and tool developers to efficiently find, modify, and verify essential data. To address these challenges, we introduce the RISC-V Unified Database (UDB), a single, machine-readable source that consolidates and cross-validates RISC-V specifications against established resources like binutils and riscv-opcodes. Built through collaboration between engineers at industry-leading companies, the UDB already generates version-specific ISA manuals, instruction indexes, and standardized opcode definitions. Ongoing work extends to generating simulator configurations for QEMU and other instruction set simulators. The UDB's YAML-based format ensures broad compatibility and positions it as a foundation for next-generation RISC-V tools. This approach is starting to gain traction with official RISC-V working groups, including the Certification Steering Committee, which already uses the UDB for generating certification requirements. This talk explores UDB’s architecture, showcases its use cases, and invites you to contribute to this transformative project for the RISC-V community.

#### Related Links

- [UDB Active Repository](https://github.com/riscv-software-src/riscv-unified-db)
- [Automatically generated HTML manual](https://riscv-software-src.github.io/riscv-unified-db/manual/html/isa/20240411/index.html)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9KWUTS/feedback/)

---

### Towards seamless Python package installation on riscv64

- **Speakers:** Mark Ryan
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 14:00 - 14:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5659-towards-seamless-python-package-installation-on-riscv64/)

#### Abstract

Have you ever wondered why certain Python packages fail to install on riscv64 devices?  Why, instead of pleasing "Successfully installed" messages, riscv64 users are often presented with bleak screens full of errors?  How, in the face of all of these errors, are those users supposed to run Python based AI or data analytic workloads?  To the curious who have briefly pondered such things as the package names and errors go scrolling by, this talk is aimed at you!  It will explain how Python packages are built and why upstream projects do not provide versions of their packages for riscv64 devices.  It will discuss the progress being made in adding riscv64 support to the Python packaging ecosystem.  Finally, it will explain how RISE is mitigating the current lamentable situation by building and distributing riscv64 wheels for a select set of popular Python packages.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DHXYG3/feedback/)

---

### How to quickly build an AI startup on open source RISC-V Cores

- **Speakers:** Jeremy Bennett, Florian 'Flo' Wohlrab, Frédéric Desbiens
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 14:40 - 15:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5921-how-to-quickly-build-an-ai-startup-on-open-source-risc-v-cores/)

#### Abstract

AI is everywhere and especially open source is accelerating capabilities and delivering new breakthroughs in Models, making them smaller yet more powerful. While there is a big focus on the next big thing in Software, many overlook the goldrush in Hardware.
You may have heard of companies like Nvidia, AMD or Axelera.AI, they are some of the ones selling the shovels to the diggers for a great profit margin. Have you ever wondered what it take to make your own chip? 
So how to get started on your AI startup? The good news is: there is RISC-V, an open standard for CPUs, so everyone cam implement their own CPU and use common library software (in theory).  The even better news is there is an non profit open source organization called OpenHW Foundation offering high quality Apache 2.0 (or Solderpad) CPU Cores you can take as is, modify as needed and collaborate with a big community.
Even better, the OpenHW Foundation is offering small platforms to debug on FPGA's but also has QEMU support and various other Models for example system Verilog cycle accurate SystemC Models. On top of this we also provide the Software eco system you need to brign your chip up and running quickly and sell it to one of the big Datacenter Companies, or just keep it running in your basement, heating your house and providing awesome AI edge capabilities for you and your family!
In this talk Flo will highlight the current trends in chip development and how open source is accelerating this from the Cores to the EDA tools for designing but also open source tapeouts and then focus a little more on some of the Cores in OpenWH and how you can utilize it. Dr Jeremy Bennett world famous for his 45min overviews on "how to get GNU GCC ported on a totally new Architecture" is joining to deliver an overview which Software you need to run on your Chip, to develop your Chip and why it is easy with the OpenHW Group.
Last but not least we will spill the beans on how the European Union is supportign our work as a non profit (and also for profits in that context) to guarantee sovereignty and enable academic but also research and industrial to build and innovate on a common platform via the Chips JU and programs like TRISTAN and how you can benefit, no matter if you quickly develop a MCU in your Master, need to do some measurements on real RISC-V Cores for your PhD and prove how to boost performance or if you join the real business selling shovels to all the diggers.
Believe us, this talk will be a wild ride deep into the Hardware realm of RISC-V and OpenHW and make you start your own Chip while you are still listening!

#### Related Links

- [Slides (Google Slides)](https://docs.google.com/presentation/d/1GKU8hHYr0nLv4dX46MHJ92RYh0Elu5bE7hOg8n2xCe)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SWCEAR/feedback/)

---

### From Rust-VMM to KataContainers: THE DEVELOPMENT OF H EXT. BASED SOFTWARE ECOSYSTEM

- **Speakers:** Ruoqing He
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 15:20 - 15:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4156-from-rust-vmm-to-katacontainers-the-development-of-h-ext-based-software-ecosystem/)

#### Abstract

Our efforts to develop a complete Rust-based software stack for secure, cloud-native applications on the emerging RISC-V architecture. Despite the unavailability of current-generation hardware with H Extensions, Advanced Interrupt Architecture (AIA), and IOMMU support, we are proactively building and testing our stack in preparation for future hardware releases. Centered around the rust-vmm framework, we enable lightweight hypervisors like Dragonball, StratoVirt, Cloud-Hypervisor, and Firecracker—all designed to provide high performance, strong isolation, and virtualization-based security. Integrating these hypervisors with Kata Containers, we explore virtualization-based isolation of containerized workloads on RISC-V. By simulating hardware environments and leveraging forward-compatible software designs, we aim to be fully prepared for the introduction of real RISC-V hardware that meets RVA23 standard and RISC-V Server Platform specification, ensuring a seamless deployment path for confidential computing and secure cloud-native platforms.

#### Related Links

- [Works Done in RustVMM](https://github.com/search?q=is%3Amerged+author%3ATimePrinciple+org%3Arust-vmm&type=pullrequests)
- [Works Done in Cloud-Hypervisor](https://github.com/search?q=is%3Amerged+author%3ATimePrinciple+org%3Acloud-hypervisor&type=pullrequests)
- [Works Done in Kata-Containers](https://github.com/search?q=author%3ATimePrinciple+org%3Akata-containers+is%3Aopen&type=pullrequests)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FYTT3A/feedback/)

---

### RISC-V Linux bug hunting

- **Speakers:** Ben Dooks
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 16:00 - 16:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5719-risc-v-linux-bug-hunting/)

#### Abstract

Debugging issues with the Linux kernel and user space can be both interesting and challenging. This talk goes through looking at a couple of bugs we found while working with RISC-V in both kernel and user space.
The aim is to show multiple ways of approaching issues in both the kernel and user space, a run through why these happen, and how we fixed these problems. We will include taking an syzbot report and analysing what is going on during a strange kernel OOPS, and going through a user report of a crashing system where there was an issue with a Buildbot on a set of remote workers.
As part of this we will go into how to decode kernel OOPs, how to dump object code and attempt to decpher bug reports without the aid of attaching a debugger.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NEWTRB/feedback/)

---

### How good is RISC-V: Comparing benchmark results

- **Speakers:** Jeremy Bennett
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 16:40 - 17:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5678-how-good-is-risc-v-comparing-benchmark-results/)

#### Abstract

As RISC-V reaches maturity, we look at how RISC-V designs are performing.  We look at how performance has improved over the years and how performance compares to other cores, particularly those from Arm.  We'll explore the impact of different extensions and compilers on performance of compiled code.  We'll also look at how useful measuring performance using models is for predicting the performance of real silicon.
Throughout we will use mostly the Embench benchmark suites, with some use of SPEC CPU for application class cores.  We will present the first results from the new Embench IoT version 2.0 test suite.
Finally we will show how combining accurate benchmarking with simple machine learning can yield additional performance of compiled software.  This will be illustrated with the OpenHW CV32E40Pv2, where we were able to improve benchmarked code density by 7% in just 24 hours.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XCRNP8/feedback/)

---

### Open-Source CPU: Deep-dive into RISC-V CFU and Zephyr

- **Speakers:** Mohammed Billoo
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 17:20 - 17:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4482-open-source-cpu-deep-dive-into-risc-v-cfu-and-zephyr/)

#### Abstract

RISC-V's instruction set architecture (ISA) has enabled seasoned embedded software engineers to experiment with FPGAs since numerous open-source RISC-V cores can be flashed onto an FPGA.
The Zephyr Project is rapidly emerging as a leading real-time operating system (RTOS). Zephyr integrates open-source and security best practices to ensure a vendor-neutral, secure, and reliable platform.
One of the exciting features of the RISCV ISA is the Custom Function Unit (CFU), which enables a framework to support custom operations in hardware, which is accessible from software. In this talk, Mohammed will provide an in-depth demonstration on how to add a CFU into a RISCV core on an FPGA, how to make the appropriate calls from Zephyr, and the possibilities that the CFU enables for hardware acceleration in embedded systems.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/APZVXE/feedback/)

---

### Upstream Embedded Linux on RISC-V: The Good, the Bad and the Ugly

- **Speakers:** Marcel Ziswiler
- **Room:** H.1309 (Van Rijn)
- **Day:** Saturday
- **Time:** 18:00 - 18:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6342-upstream-embedded-linux-on-risc-v-the-good-the-bad-and-the-ugly/)

#### Abstract

This talk looks at the state of upstream U-Boot, Linux kernel, FreedesktopSDK, and Yocto Project for the powerful SpacemiT K1-based Banana Pi BPI-F3. Nothing has been merged yet, but I took the various pieces posted on mailing lists or available as merge requests and gave them a spin. As a reference for comparison, I also looked at the vendor downstream stuff available from Banana Pi Team/SpacemiT.

#### Related Links

- [Banana Pi BPI-F3](https://wiki.banana-pi.org/Banana_Pi_BPI-F3)
- [[PATCH v4 0/2] riscv: spacemit: add support for bananapi-f3](https://lore.kernel.org/all/20241129-pickup-bpif3-v4-0-e99fabf66e33@gmail.com)
- [[PATCH v5 00/10] riscv: add initial support for SpacemiT K1](https://lore.kernel.org/all/20240730-k1-01-basic-dt-v5-0-98263aae83be@gentoo.org)
- [[FreedesktopSDK] Draft: bpi-f3: Initial support for BPi-F3](https://gitlab.com/freedesktop-sdk/freedesktop-sdk/-/merge_requests/23075)
- [RISC-V Architecture Layer for OpenEmbedded/Yocto](https://github.com/riscv/meta-riscv)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-risc-v:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-risc-v:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XEUDG9/feedback/)

---

## Robotics and Simulation (14)

### Welcome to the Robotics and Simulation devroom

- **Speakers:** Arnaud Taffanel
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 13:15 - 13:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6590-welcome-to-the-robotics-and-simulation-devroom/)

#### Abstract

Welcome session.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/B7RVD7/feedback/)

---

### PyCRAM - A Framework for Cognitive Robot Control

- **Speakers:** Jonas Dech
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 13:20 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6268-pycram-a-framework-for-cognitive-robot-control/)

#### Abstract

With the increased use of small robots in human households like vacuum robots the next logical step is the introduction of more complex robots which are capable of manipulating objects. Introducing such robots into human household poses a multitude of new challenges, they need to operate in dynamically changing environments while being aware of their surrounding to avoid accidents. Furthermore, they need to be able to reason about the outcome of actions and change their behavior accordingly, to name a few. 
PyCRAM is a framework to design high-level cognition enabled robot behavior, designed to address the aforementioned challenges of deploying robots in human households. This is done by providing tools to define a robot control plan, which is written as high-level human instructions like "go to the table" or "pick up the cup". PyCRAM is then able to translate these instructions to instructions for a robot while taking the current context the robot is operating in into account. Resulting in robot behavior which is constantly adapting to the current state of the environment and context.
You can find the framework on GitHub: PyCRAM

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WS9HPH/feedback/)

---

### All my frustrations with ROS summed up in 5 minutes

- **Speakers:** Roland Meertens
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 13:25 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4951-all-my-frustrations-with-ros-summed-up-in-5-minutes/)

#### Abstract

Although ROS is an amazing platform it can also be frustrating, especially for a hobby-roboticist like me. From packages only being available in one specific ROS version, to dependencies which don’t compile on your specific linux version, some problems already start when trying to install your software. But that is just the start for the hobby-roboticist. The flexibility of ROS theoretically allows for cheap robots to be built, but in practice it’s hard to get your odometry, mapping, and movements in general set up correctly if you don’t have any of the more standard supported platforms. 
In this talk I will go over my experience with ROS as a hobby roboticist, give tips to the developer community, and will introduce a new ROS package to make it more affordable to get started with robotics.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MKLNTP/feedback/)

---

### Building a robot powered with Raspberry pis and Arduinos from a super fast Traxxas RC car

- **Speakers:** Loïc Vigneron
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 13:30 - 13:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4975-building-a-robot-powered-with-raspberry-pis-and-arduinos-from-a-super-fast-traxxas-rc-car/)

#### Abstract

Loïc has been playing with robotics since the beginning of a side project converting a full size car into and autonomous EV. However, some features can't be tested directly on the full size car. This talk describes the building process of a robotics-ready small scale car made for initial testing, including:
- Designing the scaffold to hold the components and printing them
- Designing and creating PCBS for the custom hats
- Creating firmwares for each components
- Creating bridges to control the car remotely with Mavlink and using ROS2
- The challenges met along the way

#### Related Links

- [Github](https://github.com/open-vehicle-control-system)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FSJPHM/feedback/)

---

### Accelerating robotics development through simulation

- **Speakers:** Ignacio Davila Gallesio, Agustin Alba Chicar
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 13:40 - 14:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6252-accelerating-robotics-development-through-simulation/)

#### Abstract

In the world of robotics, simulations have become an essential tool for developing, testing, and deploying robotic systems. But what exactly is simulation, and why is it so transformative? A simulation is a virtual environment that emulates robot behavior and interactions with the world, using mathematical models to replicate physics, sensors, and actuators. By eliminating the need for expensive or inaccessible hardware, simulation empowers developers everywhere to create, refine, and scale their robotics applications.
This talk explores how open-source general-purpose simulators (like Gazebo, Webots, O3DE, etc.) are breaking barriers in robotics development. From reducing costs and improving safety to accelerating development cycles and enabling large-scale testing, simulations are revolutionizing the field. Importantly, they are fostering inclusivity by providing accessible tools for regions with limited access to robotics hardware, such as Argentina and other less than well-resourced areas.
We’ll discuss the critical factors to consider when choosing a simulator, including its focus, community support, and compatibility with open-source tools. We’re excited to invite you to join us and discover how open-source simulations are democratizing robotics, empowering developers, and shaping the future of this exciting field.
Plan for the talk (20 minutes + 5 minutes of discussions and questions):

Introductions
Robots and simulators
   2.1 What is a robotic system?
   2.2 What is a robotic simulator?
   2.3 What can I do with a robotic simulator?
Picking the right tool for the job
   3.1 How to pick a robotic simulator?
   3.2 One robot, many simulators: Gazebo, Webots, O3DE, MuJoCo, Flatland
Discussion and questions

#### Related Links

- [Andino Webots: An open-source diff drive robot simulation in Webots integrated with ROS 2](https://github.com/Ekumen-OS/andino_webots)
- [Andino Gz: An open-source diff drive robot simulation in Gazebo integrated with ROS 2](https://github.com/Ekumen-OS/andino_gz)
- [Andino O3DE: An open-source diff drive robot simulation in O3DE integrated with ROS 2](https://github.com/Ekumen-OS/andino_o3de)
- [Andino MuJoCo: An open-source diff drive robot simulation in MuJoCo](https://github.com/Ekumen-OS/andino_mujoco)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VHLWHT/feedback/)

---

### O3DE: Creating realistic simulations with open-source game engine

- **Speakers:** Jan Hanca
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 14:10 - 14:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6035-o3de-creating-realistic-simulations-with-open-source-game-engine/)

#### Abstract

A variety of simulation platforms are available to support research and development in robotics and biomechanics, with popular open-source options like Gazebo, Webots, and MuJoCo, as well as proprietary alternatives such as NVIDIA Isaac Lab, which provide end-to-end solutions for simulation and machine learning. Additionally, tools integrating game engines like Unity and Unreal into robotic simulations have been developed to leverage their advanced rendering capabilities.
O3DE (Open 3D Engine) is a versatile, open-source, real-time 3D engine designed for creating high-fidelity games, robotic simulations, and immersive 3D environments. Its modular architecture supports seamless integration with robotics systems through ROS 2 middleware, while its AAA-quality renderer produces photorealistic visuals ideal for machine learning training and evaluation.
Governed by the Open 3D Foundation, part of the Linux Foundation, O3DE’s codebase is freely available on GitHub under the Apache 2.0 and MIT licenses, making it a powerful and accessible tool for advancing robotics simulation and development.
Talk Plan (20 Minutes):


Introduction to O3DE (3 minutes)

Provide an overview of O3DE.
Highlight its strengths and weaknesses.



Getting Started with O3DE (5 minutes)

Explain the installation process and how to build O3DE from source.
Share available resources, including robotic project templates and ready-to-test projects (e.g., open-source demos from ROSCon 2022, 2023, and 2024).



O3DE and the ROS 2 Ecosystem (5 minutes)

Discuss O3DE's integration with the ROS 2 ecosystem.
List built-in implementations, such as ROS 2 sensors, joint control, and robot control features.
Provide examples of use cases supported by the existing codebase, including importing robots from Gazebo.



C++ Code Examples for ROS 2 (5 minutes)

Demonstrate C++ code snippets for implementing ROS 2 topic subscribers and publishers.



Conclusion (2 minutes)

Share information on contributing to O3DE.
Highlight communication channels and ways to get involved with the community.



Resources:
O3DE website
O3DE repository
O3DE repository with ROS2 integration and templates
ROSCon2021 Demo using O3DE
ROSCon2022 Demo using O3DE
ROSCon2023 Demo using O3DE
ROSCon2024 Demos using O3DE

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MSD9L3/feedback/)

---

### Repurposing Valve's SteamVR 2.0 Technology to Develop an Open-Source, Low-Cost Motion Capture System for Robotics

- **Speakers:** Said Alvarado-Marin
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 14:40 - 15:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5013-repurposing-valve-s-steamvr-2-0-technology-to-develop-an-open-source-low-cost-motion-capture-system-for-robotics/)

#### Abstract

The Lighthouse Localization System V2, originally designed by Valve/HTC Vive, was developed for motion tracking in virtual reality headsets. In this talk, we will introduce the operational principles of this system and present a lighthouse decoding and tracking algorithm implemented on a low-power wireless microcontroller, with hardware designed in a compact, centimeter-scale form factor. Our open-source implementation achieves an accuracy of 7.25 mm RMS for 2D motion tracking and 11.2 mm RMS for 3D motion tracking. We believe this system offers a low-cost alternative to expensive, camera-based motion capture systems.

#### Related Links

- [LH2 driver for the RP2040](https://github.com/DotBots/lh2_on_rp2040)
- [Scientific Paper](https://hal.science/hal-04589717)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XZN9BL/feedback/)

---


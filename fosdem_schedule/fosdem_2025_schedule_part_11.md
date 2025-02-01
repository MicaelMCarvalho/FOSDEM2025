# FOSDEM 2025 Schedule - Part 11 of 11

*Generated on 2025-02-01*

## Table of Contents

- [Testing and Continuous Delivery (19)](#testing-and-continuous-delivery-19)
- [Tool the Docs (8)](#tool-the-docs-8)
- [Virtualization and Cloud Infrastructure (16)](#virtualization-and-cloud-infrastructure-16)
- [WebAssembly (7)](#webassembly-7)
- [Web Performance (6)](#web-performance-6)
- [BOF - Track A (15)](#bof---track-a-15)
- [BOF - Track B (13)](#bof---track-b-13)
- [BOF - Track C (15)](#bof---track-c-15)

## Testing and Continuous Delivery (19)

### Unlocking the Power of Property-Based Testing

- **Speakers:** Merlin Pahic
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 13:00 - 13:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6232-unlocking-the-power-of-property-based-testing/)

#### Abstract

Most developers approach unit testing by manually defining specific examples to verify the expected behaviour. With this approach, catching all the edge cases can be tricky – or tedious.
Property-based testing offers an alternative, by emphasizing general properties or rules that should hold true across a wide range of inputs. By automatically generating test cases, property-based testing provides broader coverage and can uncover issues that are difficult to find with conventional techniques.
In this talk, we'll explore property-based testing, breaking down how it works and when to use it. We'll cover:

Core principles of property-based testing and how it differs from example-based approaches.
Practical techniques for identifying useful properties in various domains, including algorithms, data structures and APIs.
Tools and libraries that enable property-based testing in popular programming languages.
Real-world examples of how this approach has uncovered critical bugs and improved test coverage.

This session is designed for developers curious about expanding their testing toolbox. Whether you're new to property-based testing or looking for ways to apply it in your work, this talk will provide practical guidance and resources to help you get started.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XADXYM/feedback/)

---

### Zap the Flakes! Leveraging AI to Combat Flaky Tests with CANNIER

- **Speakers:** Daniel Hiller
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 13:15 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5200-zap-the-flakes-leveraging-ai-to-combat-flaky-tests-with-cannier/)

#### Abstract

Flakes aka tests that don’t behave deterministically, i.e. they fail sometimes and pass sometimes, are an ever recurring problem in software development. This is especially the sad reality when running end-to-end tests where a lot of components are involved. There are various reasons why a test can be flaky, however the impact can be as fatal as CI being loaded beyond capacity causing overly long feedback cycles or even users losing trust in CI itself.
Ideally we want potential flakes to be flagged at the earliest stage of the development lifecycle, so that they do not even enter the end-to-end test suite. We want a gate that acts as a safeguard for developers, pointing out to them what kind of stability issues a test has. This reduces CI user frustration and improves trust in CI. At the same time it cuts down on unnecessary waste of CI system resources.
This talk will explore the CANNIER approach, which aims to reduce the time cost of rerunning tests. We will take a closer look at the feature set used to create training data from existing test code of the KubeVirt project, enabling us to predict probable flakiness of a certain test with an AI model.  
We will cover how a subset of the CANNIER feature set is implemented, how it is used to generate training data for an AI model, and how the model is used to analyze flakiness probability, generating actionable feedback for test authors. 
Attendees will gain insight on how the CANNIER approach can help them improve test reliability, ultimately enhancing overall software quality and team productivity.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JQMHD9/feedback/)

---

### Breaking things for fun and profit

- **Speakers:** Marcos Albe
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 13:30 - 13:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4095-breaking-things-for-fun-and-profit/)

#### Abstract

A disk full, a saturated or lossy network, too-few CPU cores, an unexpected IO error… how will your software handle such scenarios? 
In this talk we present a collection of tools that can be used to systematically "break" things, so you can write test cases and make sure that these unexpected situations will be handled gracefully by your software: ToxiProxy, charybdefs, tc qdisc, strace --inject, taskset, numactl, cgroups and syscall overloading, all can be used to emulate a wide array of failures.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZDKPNP/feedback/)

---

### Fuzzing databases is difficult

- **Speakers:** Pedro Ferreira
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 14:00 - 14:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6478-fuzzing-databases-is-difficult/)

#### Abstract

After fuzzing databases for the last 3 years, I learned that simple design decisions on a fuzzer impact on the issues it can ever find. In this talk I would to address some of those 
decisions. As an example, I would to discuss about the design of BuzzHouse, a new database fuzzer to test ClickHouse.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/R7JTYZ/feedback/)

---

### Advanced Test Harness Infrastructure for Validating ARM and FPGA-based Systems

- **Speakers:** Stefan Raus
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 14:30 - 14:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5708-advanced-test-harness-infrastructure-for-validating-arm-and-fpga-based-systems/)

#### Abstract

Designed to cater to a wide range of peripheral devices and platforms, Analog Devices' Kuiper Linux distribution is built with more than 1000 Linux device drivers compatible with Xilinx and Intel FPGAs, Raspberry Pi boards, and several other platforms.  
To ensure its quality, a test harness infrastructure must be in place to carry out continuous testing on actual hardware. This talk covers the design and implementation of such a fully automated test harness. The implemented architecture leverages the use of readily available components/technologies such as Jenkins, Docker, NetBox, and JFrog Artifactory and, at the same time, includes custom-built tools that can be tailored and extended to support existing or new devices and platform types.  
By using an advanced resource locking mechanism, the hardware setups are also remotely available to others for development and debugging, when there are no automated tests running.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HJ8BRP/feedback/)

---

### Squashing the Heisenbug with Deterministic Simulation Testing

- **Speakers:** Dominik Tornow
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 15:00 - 15:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4279-squashing-the-heisenbug-with-deterministic-simulation-testing/)

#### Abstract

Modern, distributed systems are complex and present numerous challenges: concurrency, process crashes, message loss, duplication, or reordering.
How can developers confidently test distributed systems instead of continuously dreading the next hard-to-catch and hard-to-reproduce Heisenbug?
Deterministic Simulation Testing is a powerful testing technique that eliminates uncertainty－or rather non-determinism－and ensures that your system is tested exhaustively and every single test is reproducible.
Using a systems modeling approach, we will accurately and concisely discuss Deterministic Simulation Testing. In addition, we will explore real-world implementation of this technique in production in projects such as FoundationDB, TigerBeetle, and Resonate.
Gain actionable insights for crafting your own Deterministic Simulation Testing strategy. Confidently open Schrödinger's Box of testing in distributed systems.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KWW9SX/feedback/)

---

### Testing Support for Multiple Authentication Methods in ClickHouse Using Combinatorics and Behavioral Models

- **Speakers:** Alsu Giliazova
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 15:30 - 15:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6027-testing-support-for-multiple-authentication-methods-in-clickhouse-using-combinatorics-and-behavioral-models/)

#### Abstract

In this talk, I’ll share how combinatorial testing and behavioral modeling helped uncover tricky edge cases while testing ClickHouse’s (open-source column-oriented DBMS) multiple authentication methods feature. I’ll demonstrate how these methodologies can systematically identify gaps in testing, validate complex features, and improve software quality.
Attendees will learn practical steps for applying combinatorial testing to define comprehensive test scenarios, as well as how behavioral modeling can simplify result validation and solve the test oracle problem. This session is for QA engineers, testers, and developers looking to adopt smarter, more effective testing strategies.

#### Related Links

- [Merged pull request for multiple authentication methods feature in Clickhouse Github repository](https://github.com/ClickHouse/ClickHouse/pull/65277)
- [Code of behavioral model for multiple authentication methods feature](https://github.com/Altinity/clickhouse-regression/blob/main/rbac/tests/multiple_auth_methods/model.py)
- [Combinatorial test for multiple authentication methods feature](https://github.com/Altinity/clickhouse-regression/blob/main/rbac/tests/multiple_auth_methods/combinations.py)
- [Testflows - open-source software testing framework that was used for testing this feature](https://testflows.com/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JXPHKJ/feedback/)

---

### Accelerating CI Pipelines: Rapid Kubernetes Testing with vCluster

- **Speakers:** Hrittik Roy, Saiyam Pathak
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 16:00 - 16:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5569-accelerating-ci-pipelines-rapid-kubernetes-testing-with-vcluster/)

#### Abstract

Continuous Integration (CI) workflows often encounter bottlenecks when testing Kubernetes applications. Traditional methods of building and tearing down full clusters, whether locally or in the cloud, can be both time-consuming and resource-intensive. vCluster, an open-source virtual cluster solution, offers a game-changing alternative by enabling lightweight Kubernetes clusters to be created on demand and quickly
This talk will guide you through integrating vCluster into your CI pipelines and the benefits you get from it. Virtual Cluster enables rapid application testing in production-like environments, including support for custom resource definitions (CRDs) without the overhead of traditional cluster setups. By the end of this session, you'll be equipped to reduce build times, accelerate testing cycles, and enhance the overall developer experience, as your clusters will take less time to build and you will have more time to test.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DJT3F7/feedback/)

---

### Advanced Build Tools and Remote Execution API

- **Speakers:** Son Luong Ngoc
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 16:30 - 16:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4249-advanced-build-tools-and-remote-execution-api/)

#### Abstract

In this talk, we will walk through different scalability challenges various modern CI setups encounter today: caching, distributed computing, reproducibility, telemetry... and how advanced build tools such as Bazel, Buck2, Pants,... addressed them at scale at big enterprises. We will then drill down into the common Remote Build Execution protocol that these tools all have in common. Finally, we shall reflect upon the current state of the build tool ecosystem and highlight key areas to improve upon.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CYKTZ9/feedback/)

---

### Streamlining package testing with Molecule and Jenkins

- **Speakers:** YASH PANCHAL
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 17:00 - 17:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4807-streamlining-package-testing-with-molecule-and-jenkins/)

#### Abstract

Testing packages across diverse environments often involves integrating legacy setups like bash scripts with modern frameworks such as testinfra. For many testing teams, traditional Jenkins setups rely on pre-provisioned worker nodes managed exclusively by DevOps, Build and Release, or Operations teams. This reliance often creates a bottleneck, as testing teams are restricted from modifying infrastructure directly, limiting their ability to adapt environments dynamically to meet specific testing requirements.
In this talk, we will demonstrate how Molecule, an open-source testing tool, provides a robust framework for overcoming these challenges. By decoupling test environment management from pre-configured nodes, Molecule empowers testing teams to independently define and execute their tests across multiple environments. We’ll discuss how this approach integrates seamlessly with Jenkins pipelines and supports both legacy and modern testing frameworks.
Attendees will learn how to use Molecule to reduce infrastructure dependencies, streamline testing workflows, and increase flexibility in testing.

#### Related Links

- [Molecule](https://github.com/ansible/molecule)
- [Jenkins](https://www.jenkins.io/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JBEVXW/feedback/)

---

### Infra for Drones: Lessons learned from 15 years of open source robotics.

- **Speakers:** Ramon Roche
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 17:30 - 17:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6384-infra-for-drones-lessons-learned-from-15-years-of-open-source-robotics-/)

#### Abstract

The Dronecode Foundation hosts an ecosystem of open-source projects, developers, and contributing organizations. Dronecode is an umbrella foundation (part of The Linux Foundation) hosting open-source projects that offer solutions to robotics developers looking to build Aerial solutions. 
The PX4 Autopilot is an open-source flight controller project that offers developers a stable foundation for building drones. The project sustains a community of thousands of robotics developers and hundreds of companies building complex drone solutions on top of PX4, including everything from wedding photography to package delivery for Walmart.
Our humble open-source project has supported an ever-growing community of contributors at times with little to no resources. With the growing complexity of demanding robotics workflows, proving reliable and reproducible testing to guarantee the safety of our codebase has been a constant challenge.
I will share the cautionary tale of how not to run CI for a robotics project, the scary times when we wanted to delete our whole infra and start fresh, and how we found the strength to move on. I will also share the gory details behind running an open-source robotics project and the supporting tooling needed to support our complex workflows and demanding community.
Our Continuous Integration pipeline is far from sophisticated, but it is responsible for supporting thousands of developers and is the backbone of our infrastructure. Some of the topics I will be discussing:
Maximizing containers for reproducible builds
Running a hardware-in-the-loop service with embedded hardware connected to the cloud.
Moving from Jenkins to GitHub Actions
Hosting our own GitHub Actions runners
Build patterns for better GitHub Actions development across distributed teams.
Building an array of upwards of 60 builds per pull request in GitHub Actions

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EUKFEE/feedback/)

---

### Refining the Release Strategy of a Custom Linux Distro

- **Speakers:** Andreea Daniela Andrisan
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 18:00 - 18:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5699-refining-the-release-strategy-of-a-custom-linux-distro/)

#### Abstract

As with many stages of the software development lifecycle, the release process needs to be constantly improved, iteration by iteration. This way, the software product gets delivered faster and more reliably to customers. This paper focuses on different techniques that have shortened the release cycle of the Kuiper Linux distribution. 
The new release process involves creating a stabilization branch from main which is dedicated to the new release.  Previously, the software components were built and installed during the image creation. Now they are released independently as Debian packages which are uploaded on Analog Devices' Linux Package Repository. This is an easy, user-friendly method that facilitates the distribution and installation of ADI software packages. Each software component has its own release cycle so that one component's bugs won't affect the other components' release. 
The software components are tested both separately and integrated into the Kuiper image. The latter required creating a Kuiper Docker image. This ensures that each software component is compatible with the target system as early as possible in the development process.

#### Related Links

- [Kuiper image repo](https://github.com/analogdevicesinc/adi-kuiper-gen/tree/main)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LDZPPF/feedback/)

---

### Enhancing delivery using Kubernetes Gateway API and Istio

- **Speakers:** Sachin Kumar Singh
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 18:30 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5791-enhancing-delivery-using-kubernetes-gateway-api-and-istio/)

#### Abstract

At DigitalOcean's internal platform team, we use a tool called docc to make deploying apps easier for our teams. It’s designed to hide the complexity of Kubernetes so teams can focus on getting their apps running without needing to understand Kubernetes itself.
When we deploy updates to applications, we usually use a simple method where old versions are replaced with new ones, one by one, over a short time. This works fine most of the time, but if the new version has bugs—causing slower performance or errors for users—this method doesn’t have a built-in way to catch those problems early or quickly switch back to the previous version.
To solve this, we’ve added safer deployment strategies like canary and A/B testing. These allow us to release updates more cautiously by directing only a small percentage of user traffic to the new version first. If everything looks good, we slowly increase the traffic. If not, we can automatically roll back quickly.
We achieved this by using tools like the Kubernetes Gateway API, Envoy proxy, and Istio to manage and control how traffic flows between different versions of an app. These tools work together to create a "service mesh," which helps us balance traffic and make deployment smoother and safer.
In this talk, we’ll share what we learned while setting this up and how it’s helping us ensure more reliable application updates at DigitalOcean.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XF9GQM/feedback/)

---

## Tool the Docs (8)

### Org mode witchcraft at Spritely

- **Speakers:** Amy Grinn
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5139-org-mode-witchcraft-at-spritely/)

#### Abstract

Since joining Spritely as technical administrator, I've made a number of improvements to our public documents that some people have described as Org mode 'witchcraft'. This form of witchcraft is not just magical though, it's necessary in an age of increasingly-centralized and proprietary note-taking software. I hope this presentation demystifies some of the tooling we use and inspires others to think bigger about how to write documents and how to improve accessibility.
I will talk about our Org export process, working with multiple src-block languages, and integrating Emacs with GNU Make. I'll also discuss the built-in features of Org mode that we rely most heavily on, and how to get started in your organization.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-docs:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-docs:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WGJBBJ/feedback/)

---

### CLI Magic Tricks for Docs Projects

- **Speakers:** Lorna Mitchell
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 11:00 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5206-cli-magic-tricks-for-docs-projects/)

#### Abstract

Why should coders have all the fun? The command line isn't just for programming wizards—it’s a magic box of tools that can supercharge how you tackle large documentation projects. In this talk, we’ll demystify the command line and share how to use it for wrangling text and images with ease. You’ll learn about regular expressions, how to chain single-purpose commands into clever pipelines, and tricks to manage complex project structures. From handling vast text files in various formats to taming sprawling docs projects, this session is packed with practical tricks to make your work a little easier and more magical. Recommended for anyone managing the written word at a scale that’s outgrown a single file, and who has a readiness to unleash your inner CLI magician!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-docs:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-docs:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZY9HSA/feedback/)

---

### Patterns for maintainer and tech writer collaboration

- **Speakers:** Daniel D. Beck
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 11:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5983-patterns-for-maintainer-and-tech-writer-collaboration/)

#### Abstract

Users and developers demand more and better documentation but, as a FOSS maintainer, you’re an expert in making software, not documentation. Technical writers are docs experts, but it can be hard to collaborate across that gap of expertise. It’s especially challenging to define and scope the work to be done, leading to misunderstandings and disappointing outcomes, for maintainers and writers alike.
Wouldn’t it be nice to have clear expectations of what your next documentation project would look like and to pull together as a team from the start? In this talk, you’ll get a preview of a new open-source resource for maintainers to help recognize archetypal documentation projects, the skills you’ll need to successfully complete them, and common pitfalls to avoid. And across documentation projects—whether you’re adopting new docs tools, rewriting tutorials, or deleting out-of-date materials—you’ll learn some important themes that will lead maintainers and tech writers to make the docs that users and developers want.

Daniel D. Beck is a documentation consultant who helps software engineering teams make tools, processes, and content that reach developer audiences. His talk draws from experience as a longtime contributor and maintainer of open source software and documentation, including as a current maintainer of Baseline, a browser compatibility tool, and a past role as technical content lead for MDN Web Docs.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-docs:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-docs:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TV9JTQ/feedback/)

---

### Evolving real-world AsciiDoc into a specification and how it will help the ecosystem

- **Speakers:** Alexander Schwartz
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 12:00 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5779-evolving-real-world-asciidoc-into-a-specification-and-how-it-will-help-the-ecosystem/)

#### Abstract

Lots of open-source projects use documentation as code to collaborate on web sites and documentation. But how do you integrate the different parts of a documentation pipeline to provide a great contributor and user experience? 
AsciiDoc is a popular plain text markup language for writing technical content, and lots of open-source projects use it. It’s loved for its rich features and its ability to modularize and reuse content. The AsciiDoc Working Group at the Eclipse Foundation has recently published the AsciiDoc Language documentation, and it is continuing to work on the AsciiDoc Language Specification that is the foundation to define standard parsing rules for the language.
This talk showcases different AsciiDoc tools in real-world project documentation pipelines to show what is possible today when you author, verify, convert, and publish content. It also highlights what challenges will be solved with the evolving AsciiDoc Language Specification.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-docs:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-docs:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HM7UCV/feedback/)

---

### Docs Straight from the Code: AST-Powered Automation

- **Speakers:** James (purpleidea)
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 12:30 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6143-docs-straight-from-the-code-ast-powered-automation/)

#### Abstract

Mgmt is a cutting-edge, real-time, automation tool designed to be fast, safe, and revolutionary.
Our goal wasn't just to replicate legacy tools but to surpass them-- and we believe we've done exactly that.
Mgmt is now powering real production workloads, showcasing its potential to redefine what's possible in automation.
Empowering our users starts with great documentation! To achieve this, we aimed to minimize the time spent maintaining our docs while ensuring they stay perfectly in sync with the code. So we developed custom AST parsing code that automatically converts code into a structured data format.
We then use a GoHugo templating system to publish it in a polished and user-friendly way.
All of this code is open source, making it available for others to use and benefit from! We'll also show how even a small project could do this.
I'll deliver live demos throughout, ensuring the concepts come to life.
You'll also get a glimpse of how mgmt can revolutionize your workflows-- it might just become your go-to tool for managing documentation pipelines!
For those who want a head start, check out our blog posts. Reading a few before the talk will provide a great background of the topic!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-docs:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-docs:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7SGHSV/feedback/)

---

### No more broken docs: keep docs accurate with Doc Detective

- **Speakers:** Ariel Kaiser, Jake Cahill
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 13:00 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4928-no-more-broken-docs-keep-docs-accurate-with-doc-detective/)

#### Abstract

Documentation often struggles to keep up with development cycles. Your users become testers of inaccurate information, which leads to a poor experience. But what if you could test your documentation for accuracy and catch breaking changes before your users do?
This short talk shows how you can improve your docs-as-code workflows with automated testing. Attendees will hear an explanation of Doc Detective and its testing framework. We will also show off some implementation strategies and automation to help keep your docs current.

#### Related Links

- [Project home page](https://doc-detective.com/)
- [Project repository](https://github.com/doc-detective/doc-detective)
- [Slides](https://docs.google.com/presentation/d/1btkevKY_ba3Ms2XFHI9mHIh48JsiW6ZcIousiRyiuXA/edit?usp=sharing)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-docs:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-docs:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QWLVQ7/feedback/)

---

### API documentation testing with AI user simulation

- **Speakers:** Lisa Driukova
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 13:30 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4912-api-documentation-testing-with-ai-user-simulation/)

#### Abstract

In open-source projects, contributors often wear many hats—developer, tester, writer—and resources are typically stretched thin. This multitasking environment can make it challenging to maintain comprehensive and accurate API documentation. Yet, high-quality documentation is vital for the usability and adoption of any open-source project.
This talk focuses on how AI can help simplify one aspect of documentation development: testing. By using AI to simulate user interactions, we can efficiently identify gaps and inconsistencies in API documentation that a contributor might miss due to exceptional knowledge of the topic.
By integrating AI-driven user simulations into your workflow, you can improve the quality of your documentation while managing multiple responsibilities more effectively. This approach not only benefits individual contributors but also strengthens the overall success and sustainability of open-source projects.

#### Related Links

- [Code sample](https://gist.github.com/driukova/77c1d6b83264ee6020125017c85ce964)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-docs:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-docs:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RL79MY/feedback/)

---

### 9,800 Sandboxes and Counting: Transforming Documentation with Interactive Learning Environments

- **Speakers:** Jay Clifford
- **Room:** K.4.201
- **Day:** Saturday
- **Time:** 14:00 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4978-9-800-sandboxes-and-counting-transforming-documentation-with-interactive-learning-environments/)

#### Abstract

One of the reasons why Go is easy to learn is due to the interactive examples all through the documentation, we wanted to emulate this success. Six months later, we now manage 26 sandbox tutorials and totalled over 9,800 unique instances.  They transformed our documentation by letting users run commands, deploy sample projects, and see real-world use cases come alive. 
Scaling the concept to support over 10 products brought unique challenges for us. How could we streamline the creation of new sandbox tutorials? How could we maintain a single source of truth between our sandboxes and evolving documentation?
In this session, we’ll dive into:
*What an interactive sandbox is and how it enhances developer experiences
* How we created an open-source tool to automatically synchronize our documentation and sandboxes via CI/CD pipelines
This talk will help you get started integrating interactive sandboxes into your documentation and arm you with the tools you need to scale them effectively!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-docs:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-docs:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SMB7FS/feedback/)

---

## Virtualization and Cloud Infrastructure (16)

### Introducing FUKI, guest firmware in a UKI for confidential cloud deployments

- **Speakers:** Anirban (Ani) Sinha
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 09:00 - 09:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4661-introducing-fuki-guest-firmware-in-a-uki-for-confidential-cloud-deployments/)

#### Abstract

We described our idea of a guest virtual machine driven firmware update mechanism for confidential cloud deployments (where tenant and cloud providers are two different entities) in our KVM Forum talk 2024 titled “Empowering confidential VMs in the cloud to use their own firmware upon instantiation.” [1] . We already demoed a prototype in action at KVM Forum [4]. In this talk, we will briefly describe our motivation for this work for the benefit of those not present in the KVM Forum. Then, we will argue how signed UKIs can be a simple, easier and guest OS agnostic means of deploying the trusted and measured firmware images for tenants in the cloud. We will also describe how UKIs can trigger an update of the firmware using our proposed simple hypervisor interface. Discussions around implementing this have already started within the systemd community [2][5]. We will describe some of the details around our design decisions. We will also seek inputs from the community on implementing the hypervisor specific support needed in UKI for interacting with the hypervisor by proposing some initial ideas.
This talk is mostly UKI/systemd focussed. We will not describe QEMU specific details. For QEMU details, those interested may please refer to our 2024 KVM Forum talk and other future presentations at the KVM Forum or other conferences.
This work is being driven within Red Hat in collaboration with AWS. Other members besides the presenter Ani Sinha(Red Hat) [3] are:  Alex Graf (AWS), Vitaly Kuznetsov(Red Hat), Paolo Bonzini(Red Hat), Gerd Hoffmann (Red Hat), Harald Hoyer (Matter Labs).
References:
1. https://pretalx.com/kvm-forum-2024/talk/HJSKRQ/
2. https://github.com/systemd/systemd/pull/35091
3. https://people.redhat.com/~anisinha
4. https://drive.google.com/file/d/1m6vkH-AENIt6pM9Onb98jyjloR1NP0lQ/view?usp=drive_link
5. https://github.com/systemd/systemd/pull/35281

#### Related Links

- [Our KVM Forum presentation](https://www.youtube.com/watch?v=VCMBxU6tAto)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/W9DHWM/feedback/)

---

### Confidential VMs on public clouds and on-premise: a long way towards zero trust

- **Speakers:** Vitaly Kuznetsov
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 09:30 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5182-confidential-vms-on-public-clouds-and-on-premise-a-long-way-towards-zero-trust/)

#### Abstract

Confidential VMs are generally available on popular public clouds today and on-premise hypervisor solutions are trying to catch up. The main selling point of the technology is the assumed ability to isolate guests from the owner of the infrastructure thus gaining true confidentiality. Are we there yet? In the talk I will try to describe (from a general purpose Linux based operating system perspective) what would it take to build full chain of trust. In particular, I'd like to discuss the following parts: why/how can we trust 
the hardware, the firmware, the bootloader, the kernel, and the userspace; how we can ensure confidentiality and integrity of the workload.
The talk is supposed to be fairly high level with the main purpose to provide an overview of the current state of affairs; highlight parts of the chain where the required solutions are already there, parts, which are 'work and progress', and parts where we've just scratched the surface.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/U8CJJ8/feedback/)

---

### Hunting Virtio Specification Violations

- **Speakers:** Matias Vara Larsen
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 10:00 - 10:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5930-hunting-virtio-specification-violations/)

#### Abstract

In the rust-vmm project, we implement VirtIO devices in Rust by following the VirtIO specification that defines how devices and driver interact. For example, the specification outlines the steps that drivers must follow to initialize a device. If a driver makes any incorrect sequence, the device returns an error.
While the driver or device may not always conform to the spec, deviations can lead to unexpected behaviors or bugs. In this presentation, we introduce two tools to check whether a VirtIO device conforms to the specification. Firstly, we present Kani - a tool developed by Amazon that is used to verify conformance in devices implemented in Firecracker. Secondly, we discuss an experimental tool that validates conformance during the execution of the device. This is a Rust tracer that developers can add to an existing device to ensure its implementation conforms to the specification. Traces are compared with the specification at runtime to detect any violations that may have occurred.

#### Related Links

- [Kani Rust Verifier](https://github.com/model-checking/kani/)
- [Rust Tracer that accepts an spec as input (formal)](https://github.com/MatiasVara/tracing-formal)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/R3TXQN/feedback/)

---

### Migrating from VMware to Kubernetes

- **Speakers:** Martin Necas
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5549-migrating-from-vmware-to-kubernetes/)

#### Abstract

Forklift is an open-source project designed to facilitate the migration of virtual machines (VMs) from platforms such as Red Hat Virtualization (RHV), OpenStack, VMware, and OVA to Kubernetes KubeVirt. This presentation will provide an overview of the migration process, with a specific focus on VMware migrations and the techniques employed by Forklift to minimize downtime during these transitions. Additionally, it will explore the rationale behind selecting specific technologies, highlighting their respective benefits and limitations. The session will conclude by discussing Forklift's current objectives and future goals. After the session, you will have a solid understanding of the Forklift migration workflow, the challenges involved, and the strategic decisions that shape the project https://github.com/kubev2v/forklift.

#### Related Links

- [Forklift](https://github.com/kubev2v/forklift)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LQFPHV/feedback/)

---

### Can QEMU and vhost-user devices be used on macOS and *BSD?

- **Speakers:** Stefano Garzarella
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 11:00 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5100-can-qemu-and-vhost-user-devices-be-used-on-macos-and-bsd-/)

#### Abstract

The vhost-user protocol is used to offload the emulation of a virtio device to a process that is external to the Virtual Machine Monitor (VMM). This approach offers several advantages: it enhances the isolation of device emulation, reducing the attack surface of the VMM; it allows for the use of different programming languages, enables daemon restarts in case of failures, and reduces the VMM's dependency on external libraries used just for the device emulation.
Originally developed for QEMU and Linux, the vhost-user protocol's flexibility has led to its adoption by other VMMs, facilitated particularly by the crates provided by the rust-vmm community. These crates have also been very useful for developing deamons for device emulation such as virtiofsd, vhost-device-vsock, and many others.
So far these devices have been developed to run only on Linux. This raises the question: can we extend their functionality to other POSIX systems, such as macOS or FreeBSD/OpenBSD?
In this talk, we will try to answer this question by analyzing the core components of vhost-user, the changes needed to QEMU, and the adjustments required for rust-vmm crates. We will also see some details about the work needed for some specific devices such as virtiofsd and vhost-user-vsock.

#### Related Links

- [QEMU](https://www.qemu.org/)
- [vhost user devices from rust-vmm community](https://github.com/rust-vmm/vhost-device/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9UMBJ9/feedback/)

---

### The IaC Tooling Multiverse and the Future of IaC

- **Speakers:** Ronny Orot
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 11:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6057-the-iac-tooling-multiverse-and-the-future-of-iac/)

#### Abstract

With Infrastructure as Code becoming the de facto way we manage our infrastructure today, a lot of excellent tools have become widely adopted that each have a different set of strengths. In this talk we'd like to take a look at the evolution of the IaC landscape over the past decade, and where we're heading.
We'll examine some of the biggest Ops - DevOps / SRE / Platform - engineering challenges through the lens of IaC including disaster recovery, security, cost, performance and even where complexity factors in when choosing your tooling of choice. While many of us have already chosen our tooling, we may also like to consider migration and integration of multiple tools for different use cases and stacks. In this interactive talk, we'll allow you to decide which tools we explore - from CDK to Pulumi, Terraform, OpenTofu, Helm, ArgoCD to learn about how they stack up versus modern cloud native challenges.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VXMXLW/feedback/)

---

### Enhancing KubeVirt workload scheduling patterns (controversial)

- **Speakers:** Simone Tiraboschi
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 12:00 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5741-enhancing-kubevirt-workload-scheduling-patterns-controversial-/)

#### Abstract

In the KubeVirt architecture, scheduling as well as network and storage management is completely delegated to the underlying Kubernetes cluster, with KubeVirt extending it with virtualization functions.
When developing KubeVirt, we are often faced with a dilemma: should we solve a problem in KubeVirt in a way that is best optimized for VMs, or should we take a more general path and develop or rely on solutions that are also suitable for generic pod-based workloads?
The KubeVirt razor that states "if something is useful for Pods, we should not implement it only for VMs” is our guiding principle and has proven to be a wise and smart idea over the years.
However, we still frequently receive questions from experienced users coming from other more traditional virtualization solutions who want to know how they can perform certain scheduling/maintenance activities following patterns that have proven successful for them in the past.
An example of these questions is live migrating one of my VMs to a named node as and when I wish bypassing the cluster scheduler decision, or how to automatically and regularly rebalance the cluster according to the real-time resource consumption of my long-lived VMs. In the past, such questions have not found an easy answer in KubeVirt.
In this session, we will discuss how to extend the VirtualMachineIstanceMigration object to allow the cluster administrator to specify a desired target node.
We will then move on to a more advanced use case and discuss why PSI (Pressure Stall Information) metrics collected at node and workload level (cgroupv2) are like barometers that provide fair warning of impending resource shortages (memory, CPU, IO), and how we can proactively leverage this information by using a novel load-aware plugin for the Kubernetes descheduler that can trigger evictions and live migrations (for VMs) to automatically manage and balance resource utilisation on cluster nodes.
Please note that these novel proposals are still controversial and the subject of an interesting discussion between KubeVirt developers. So this talk may be an interesting opportunity for discussion to influence the future development of your preferred virtualization solution.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VKCYSJ/feedback/)

---

### A Highly Distributed Cloud Architecture for Telco NFV Deployments

- **Speakers:** Nicolae-Madalin Neag
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 12:30 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5943-a-highly-distributed-cloud-architecture-for-telco-nfv-deployments/)

#### Abstract

The nature of 5G RAN and disaggregated edge computing architectures are forcing EU telecom operators to transform themselves into IT savvy companies and deploy remote management solutions where the different business domains are all consumers of a shared underlying telco cloud platform. This presentation will describe a new distributed open architecture based on OpenNebula with a single NOC management cloud front-end instance to operate and maintain tens to hundreds of geo-distributed clusters (PoPs with edge nodes) with minimal hardware infrastructure. This European open source alternative enables operators to use the same software stack to deploy different cloud platforms for their 5G and fixed access network, core network, edge computing, private, and third-party cloud needs.
In this session you will learn from someone with more than 20 years experience at Telefónica about telco cloud considerations compared to enterprise cloud environments, and about the specific technical challenges associated with the deployment of 5G/edge use cases based on open source technologies, including support to distributed User Plane Function (UPF) in 5G Core Networks, CDN or O-RAN, Enhanced Platform Awareness (EPA) for the fine-grained matching of processor capabilities for Virtual Machine (VM) and Kubernetes workloads, exposing low-level CPU and NIC acceleration components for Network Function Virtualization (NFV), DPDK and SR-IOV support, GPU hardware support, native multi-tenancy, bare-metal automation, and multi-cluster management.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BPJMJP/feedback/)

---

### Simplifying KubeVirt: New tools for easier VM management

- **Speakers:** Felix Matouschek
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 13:00 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5121-simplifying-kubevirt-new-tools-for-easier-vm-management/)

#### Abstract

KubeVirt brings the power of virtual machines to Kubernetes, but its complexity can pose challenges for new users. This talk focuses on recent improvements to two essential tools: virtctl, the CLI for managing KubeVirt resources, and the kubevirt.core Ansible collection, designed for automating virtual machine operations. These enhancements introduce features that simplify workflows, enhance usability, and make managing virtual machines on Kubernetes more approachable.
We’ll explore how these tools streamline tasks like managing the virtual machine lifecycle in conjunction with instancetypes and leveraging existing Ansible automation content to reduce manual effort. Attendees will discover how these improvements make KubeVirt more accessible and practical. This session is ideal for Kubernetes enthusiasts, DevOps, and virtualization engineers looking to integrate hybrid workloads into their cloud-native environments.

#### Related Links

- [KubeVirt.io](https://kubevirt.io/)
- [KubeVirt on GitHub](https://github.com/kubevirt/kubevirt)
- [kubevirt.core Ansible Collection on GitHub](https://github.com/kubevirt/kubevirt.core)
- [kubevirt.core in the Ansible Community Documentation](https://docs.ansible.com/ansible/devel/collections/kubevirt/core/index.html)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZF8G7L/feedback/)

---

### Free my Kubernetes network! Breaking away from the Kubernetes networking model

- **Speakers:** Miguel Duarte, Doug Smith
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 13:30 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4059-free-my-kubernetes-network-breaking-away-from-the-kubernetes-networking-model/)

#### Abstract

KubeVirt is transforming the integration of containers and virtual machines (VMs) within Kubernetes environments. By enabling VMs to run as processes in Kubernetes pods, KubeVirt allows seamless operation of VMs alongside containerized workloads. However, the existing Kubernetes networking model, while offering simplicity and cost-effectiveness through a unified approach, presents challenges for diverse user groups.
Traditional virtualization users face difficulties meeting their Layer 2 isolation needs, while Kubernetes-savvy users seek a managed networking experience. Importantly, both groups running virtualization workloads require stable IP addresses for their VMs throughout their lifecycle, including during live migration and restart/shutdown operations. This requirement adds complexity to the already challenging Kubernetes networking landscape, and brings into focus the needs for network isolation in Kubernetes, questioning the fundamental decisions for networking in Kubernetes.
To address these multifaceted issues, the user-defined networks OVN-Kubernetes feature has emerged as a powerful solution. This feature integrates natively with the Kubernetes API, supporting services and network policies while providing the necessary tools for effective traffic isolation and NATed egress implementation. Crucially, it also offers the capability to maintain consistent IP addresses for virtualization workloads, ensuring stability during VM lifecycle events.
Through a live demonstration, attendees will learn practical steps to implement traffic isolation using OVN-Kubernetes User Defined Networking functionality. Including NATed egress and stable IP addressing for VMs on their clusters. By the session's end, participants will understand how to tailor Kubernetes networking to meet their organization's specific requirements, bridging the gap between Kubernetes' flexible architecture and the stringent networking needs of both traditional virtualization and managed Kubernetes environments. This knowledge will empower attendees to create more effective and secure networking solutions, enabling them to fully leverage cloud-native technologies while maintaining operational security and compliance across diverse deployment scenarios.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CYQ8DA/feedback/)

---

### Portability and Interoperability across a Pan-European Virtualized Cloud-Edge Continuum

- **Speakers:** Jordi Guijarro
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 14:00 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5955-portability-and-interoperability-across-a-pan-european-virtualized-cloud-edge-continuum/)

#### Abstract

To ensure a competitive market in the EU, customers of data processing services, including cloud and edge services, must be able to switch seamlessly between providers. This benefits customers by allowing them to choose services that best meet their needs, while also benefiting providers by expanding their potential customer base. However, significant barriers currently hinder this flexibility, including high costs for data egress, lengthy switching procedures, and a lack of interoperability between providers, which can lead to the loss of data and applications.
The Data Act, coming into force on 12 September 2025, aims to address these challenges by ensuring that switching between providers is free, fast, and seamless. This presentation will describe and demonstrate a new open-source virtualization layer developed within the IPCEI-CIS project to further facilitate smooth transitions between data processing services.
This integrated virtualization system ensures interoperability by providing a control plane that manages distributed resources, virtual machines, and Kubernetes clusters across multiple cloud providers. It also guarantees portability, enabling applications to run seamlessly on any provider without the need for conversion. Additionally, it supports efficient migration of applications between providers with minimal downtime.
The demo will showcase a testbed combining resources from six EU cloud providers and resources from U.S. providers to illustrate the migration of workloads. This initiative demonstrates how the new virtualization layer enables true flexibility and portability in the cloud ecosystem, driving the vision of a competitive and interoperable cloud market in Europe.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BL9SPV/feedback/)

---

### Unlocking the Hybrid Cloud: An Open Source Approach

- **Speakers:** Victor Palma
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 14:30 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5940-unlocking-the-hybrid-cloud-an-open-source-approach/)

#### Abstract

The hybrid cloud has become a cornerstone of modern infrastructure, offering the flexibility to seamlessly integrate on-premises environments with public cloud resources. However, building and managing a hybrid cloud that is efficient, scalable, and vendor-neutral requires powerful automation tools grounded in open source principles.
This talk introduces OpenNebula Formation (a.k.a. oneform), an open-source tool designed to automate the deployment and configuration of cloud resources across diverse public cloud environments. We’ll explore how oneform simplifies the process of extending private clouds to public providers, enabling dynamic and scalable hybrid cloud setups tailored to specific use cases.
Through a practical demonstration, we’ll showcase how oneform can define and provision complex infrastructures, emphasizing its ability to ensure seamless automation and a consistent operational model across platforms. We’ll also highlight how oneform enables the combination of U.S.-based providers like Equinix and AWS with European providers such as ScaleWay, offering true multi-cloud flexibility and fostering compliance with regional data regulations. Additionally, we’ll discuss its compatibility with other open-source tools and its capacity to avoid vendor lock-in by leveraging community-driven custom drivers.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SAZPJH/feedback/)

---

### Running QEMU Inside Browser

- **Speakers:** Kohei Tokunaga
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 15:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6290-running-qemu-inside-browser/)

#### Abstract

"QEMU Wasm" is a QEMU system emulator experimentally ported to the browser with enabling TCG. It allows running QEMU's variety of emulated CPUs (including x86_64 and AArch64) and machines inside browsers.
In this session, Kohei will show the overview of QEMU Wasm and how it works. The talk will also cover its possible use cases, including running Linux-based containers inside browsers and web-based playgrounds, etc. Its integration with tools in the community will also be shared.

#### Related Links

- [QEMU Wasm repo](https://github.com/ktock/qemu-wasm)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HU3MTV/feedback/)

---

### Building AI Factories with Open Source Tools

- **Speakers:** Aleksejs Petrovs
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 15:30 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5952-building-ai-factories-with-open-source-tools/)

#### Abstract

The growing demand for AI-powered solutions has led to the emergence of specialized cloud infrastructures optimized for AI workloads. This talk introduces the concept of "AI Factories"—dynamic, open source-driven architectures designed to streamline the processing of complex AI workloads in a scalable, multi-tenant environment.
We will explore how open source technologies like OpenNebula enable the seamless integration of advanced features, including GPU passthrough and SR-IOV for high-performance compute capabilities, hybrid cloud deployment for scalability and flexibility, and pre-configured AI appliances to accelerate development pipelines. Together, these components deliver an “AI as a Service” model, providing users with a robust and vendor-neutral foundation for training, deploying, and managing AI workloads efficiently.
Through practical examples and architectural insights, attendees will gain a clear understanding of how to build and deploy these AI Factories using open source tools. The session will also highlight the role of hybrid cloud strategies in balancing on-premises and public cloud resources, showcasing how to create cost-effective, high-performance environments tailored for AI innovation.
Join us to discover how to harness open source technologies to power the next generation of AI services.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WB3Z7G/feedback/)

---

### Enabling AMD SEV technology in Xen Hypervisor.

- **Speakers:** Andrei Semenov
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 16:00 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5451-enabling-amd-sev-technology-in-xen-hypervisor-/)

#### Abstract

In this talk we’re presenting our work at Vates Company of enabling Secure Encrypted Virtualization (SEV) technology for Xen Project open-source hypervisor. SEV is an extension of AMD-V technology and allows to run encrypted virtual machines on the top of “untrusted” hypervisor. Even though the hypervisor still controls the lifecycle of virtual machines, it’s up to SEV enabled guest to decide whether its memory is encrypted or not. The SEV enabled hardware ensures that the hypervisor nor other software (VMs) running on the platform can’t access (decrypt) this memory. 
In the heart of the SEV technology is the “AMD Secure Processor” hardware component which offers an interface to the system software (hypervisor or guest kernels) allowing to manage virtual machines and the whole platform, so these pieces of software can run and communicate without compromising each other’s security.  X86 instruction set was also enriched to fully benefit from SEV technology.
We will present our project which targets to integrate SEV extension to Xen hypervisor, the necessary developments and adaptions that have been done, where we are with this project and our future work.

#### Related Links

- [Xen Project Site](https://xenproject.org/)
- [XCP-ng  Github Xen repository](https://github.com/xcp-ng/xen)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EC8383/feedback/)

---

### On-Prem Kubernetes at Scale With metal-stack.io

- **Speakers:** Stefan Majer, Gerrit Schwerthelm
- **Room:** UB4.132
- **Day:** Sunday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4665-on-prem-kubernetes-at-scale-with-metal-stack-io/)

#### Abstract

Now that Kubernetes has gained a reputation as the de facto standard for running applications in a scalable and secure way, organizations are struggling to decide where to get Kubernetes from and how to run it.
Most take the seemingly easiest route and go to one of the hyperscalers like Google, Amazon, or Azure. This works for most companies, but it comes with additional costs and loss of control over their data.
For this reason, we will show you how to build, run, and operate Kubernetes on your own hardware in your own data center without losing the performance and elegance your developers are used to from the hyperscalers.
metal-stack.io is a fully open source Metal as a Service API that can be used either by gardener.cloud or our Cluster API driver to create clusters in minutes, but on bare metal. We believe that strengthening the independence of European industry is more necessary than ever. With metal-stack.io, which is developed in Germany, we hope to contribute to this goal.
It was designed with the financial industry in mind, but is also well suited for any application that requires performance, high levels of tenant separation, best-in-class networking and high availability. It has been in production for over 5 years in many different data centers.
There is also a public offering at metalstack.cloud where customers can try and see how Kubernetes feels when not running on VMs.
We will give a deep dive into all aspects including a demo.

Relevant Open Source Projects we are talking about:

metal-stack website
metal-stack github repos
gardener kubernetes orchestration
kubernetes

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-virtualization:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-virtualization:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CARLND/feedback/)

---

## WebAssembly (7)

### Moving Beyond Containers - Introducing Boxer

- **Speakers:** Dan Phillips
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 09:00 - 09:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6115-moving-beyond-containers-introducing-boxer/)

#### Abstract

While containers have been pivotal in cloud computing, offering isolated environments for applications, they bring notable drawbacks. These include substantial overhead, resulting in larger, less efficient deployments and startup times, and a dependency on the underlying OS for security, posing potential vulnerabilities. 
WebAssembly (Wasm) addresses these challenges, and this talk will introduce the open-source project Boxer (https://boxer.dev), which offers tooling for taking existing containerized workloads and definitions, and creating near-universally deployable Wasm distributions (“Boxes”) offering roughly the same environment, with all the benefits of the WebAssembly target. Wasm, a compact binary instruction format, enables lightweight, sandboxed execution,  significantly reducing overhead compared to traditional containers. This leads to enhanced performance and smaller, more efficient deployments, ideal for cloud computing. Additionally, Wasm's memory-safe, isolated execution environment provides superior security, independent of the OS. Thus, Wasm, with its blend of efficiency and security, emerges as not just an alternative, but a substantial improvement over container technology for cloud deployments.
With the main tools built in Rust, importantly, Marcotte (https://github.com/dphilla/marcotte) -- the underlying tool for virtualizing layers of system functionality -- allows us to make safe, sandboxed, discrete, and composable system functionality, by leveraging Rust's memory safety model, and the inherent properties of WebAssembly. 
This talk will critically examine this new technology, its approach, benefits, and existing limitations compared with containers, and its path forward as a new standard in cloud infrastructure.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-webassembly:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-webassembly:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SLZRUZ/feedback/)

---

### Wazero vs Chicory: An In-Depth Comparison Between Two Language-Native Wasm Runtimes

- **Speakers:** Edoardo Vacchi
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 09:30 - 09:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4961-wazero-vs-chicory-an-in-depth-comparison-between-two-language-native-wasm-runtimes/)

#### Abstract

Today there are several mature, state-of-the-art, general-purpose WebAssembly runtimes, but they are generally released as architecture- and OS-specific native binaries. 
Native binaries are the most general way to distribute a Wasm implementation; however, any programming language with a significant runtime environment faces some degree of friction when interfacing with native code. For instance:
native code might make assumptions about memory management, which could conflict with automatic garbage collection, 
and it tends to assume ownership over threaded code, which won’t play well with abstractions over the operating system threads, such as user-space task schedulers.
With “language-native runtime”, we mean a Wasm implementation that has been developed using the language of the host platform.
Arguably, wazero was among the first language-native runtime environments for Wasm. wazero provides a pure-Go Wasm interpreter and a pure-Go just-in-time compiler for arm64 and amd64. But, even though this might be surprising, there are many similarities between the Go runtime and the Java runtime. 
We will compare how the two relate to each other while presenting Chicory, a fairly new language-native runtime written in pure-Java, featuring a Wasm interpreter and an ahead-of-time bytecode translator.
By comparing wazero and Chicory, we propose language-native runtimes as a great solution to further spread Wasm for cross-platform software delivery.

#### Related Links

- [wazero](https://wazero.io)
- [Chicory](https://chicory.dev)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-webassembly:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-webassembly:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LCXYXK/feedback/)

---

### WASM meets unikernels: Secure and Efficient Cloud-Native Deployments

- **Speakers:** Charalampos Mainas, Anastassios Nanos
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 10:00 - 10:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6292-wasm-meets-unikernels-secure-and-efficient-cloud-native-deployments/)

#### Abstract

This talk explores the intersection of WebAssembly and unikernels to create a flexible, powerful and secure deployment. On one hand, WASM offers unprecedented portability across platforms with almost near-native execution. On the other hand, unikernels can achieve extremely fast boot times, truely strong isolation with low CPU overhead and memory footprint. The presentation covers the development of a tool that builds and packages WASM unikernels as OCI-compliant images. Additionally, the talk demonstrates the seamless integration of WASM unikernels with Kubernetes through urunc, a unikernel container runtime, which treats them as standard containers. This end-to-end solution facilitates the building, deployment, and execution of WASM applications in a purely cloud-native manner, achieving a level of security and efficiency that surpasses the traditional container model.

#### Related Links

- [Container runtime repository](https://github.com/nubificus/urunc)
- [Building tool repository](https://github.com/nubificus/bunny)
- [Blogpost](https://blog.cloudkernels.net/posts/wasm-urunc/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-webassembly:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-webassembly:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/THJVDU/feedback/)

---

### Cyber-Physical WebAssembly: Interfacing with USB and I2C Hardware

- **Speakers:** Merlijn Sebrechts, Michiel Van Kenhove
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 10:30 - 10:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6068-cyber-physical-webassembly-interfacing-with-usb-and-i2c-hardware/)

#### Abstract

Did you know you can use WebAssembly on IoT devices and microcontrollers? In this talk, we explain why anyone would do such a thing, and how to connect WebAssembly applications to hardware using USB and I2C interfaces.
WebAssembly allows embedded developers to use modern toolchains, diverse programming languages and sandboxing technology on truly tiny devices like ESP32 microcontrollers. Support for these use-cases is improving with the newly formed Embedded SIG and new interfaces for connecting WebAssembly applications to underlying hardware via USB and I2C.
We will cover the WASI-USB and WASI-I2C proposals and explains how to embed a device driver in WebAssembly. The session also takes a look at the overhead of these interfaces and embedded WebAssembly in general. The session closes with a demo of a USB device driver running inside of WebAssembly.

#### Related Links

- [wasi-usb standard proposal](https://github.com/WebAssembly/wasi-usb)
- [wasi-i2c standard proposal](https://github.com/WebAssembly/wasi-i2c)
- [Demo showing off wasi-usb and a USB device driver in WebAssembly](https://github.com/idlab-discover/usb-wasm)
- [Demo showing off wasi-i2c](https://github.com/idlab-discover/i2c-wasm-components)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-webassembly:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-webassembly:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HGBS7V/feedback/)

---

### The current state of debugging in WebAssembly

- **Speakers:** Artem Kobzar
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 11:00 - 11:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6415-the-current-state-of-debugging-in-webassembly/)

#### Abstract

During the talk, we will explore the implementation details of how different languages (such as Rust, C/C++, Kotlin, and Dart) provide a debugging experience in and outside the browser. We will cover approaches such as SourceMap, DWARF, and Dart VM Service Protocol and explore their pros and cons from the end-user perspective. Additionally, we will discuss what improvements we will have in the standards shortly.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-webassembly:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-webassembly:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/K7VMSQ/feedback/)

---

### WebAssembly-powered game console

- **Speakers:** gram
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 11:30 - 11:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4509-webassembly-powered-game-console/)

#### Abstract

Firefly Zero is the first in the world handheld game console powered by WebAssembly. It's fully open-source (both software and hardware), has peer-to-peer multiplayer, and is easy to program in any WebAssembly-targeting programming language.
Come to hear why we've picked WebAssembly for the job, how we've run a web-centric technology on microcontrollers, and what crazy challenges we've conquered along the way.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-webassembly:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-webassembly:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8GENRW/feedback/)

---

### Seeing Eye To Eye: Computer Vision using wasmVision

- **Speakers:** Ron Evans
- **Room:** K.4.601
- **Day:** Sunday
- **Time:** 12:00 - 12:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5902-seeing-eye-to-eye-computer-vision-using-wasmvision/)

#### Abstract

Creating a computer vision application so it can run on many different machines and different types of hardware has historically been very difficult. Sounds like an excellent use case for WebAssembly!
wasmVision (https://wasmvision.com/) is a new project for high-performance computer vision applications based on WebAssembly.
It uses the wasmCV interface (https://wasmcv.org/) which provides guest bindings for computer vision applications based on OpenCV. Any language that can compile to WASM can then use these interfaces to create processors to do tasks like image filtering, object detection, communicate with vision models, and more.
In this talk, I will show several demonstrations using code written in Rust, Go, and C to perform a number of visually interesting tasks, including displaying live video from a drone.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-webassembly:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-webassembly:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/M8VJPP/feedback/)

---

## Web Performance (6)

### Welcome to the web performance dev room

- **Speakers:** Dave Hunt, Peter Hedenskog
- **Room:** UA2.220 (Guillissen)
- **Day:** Saturday
- **Time:** 15:00 - 15:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5491-welcome-to-the-web-performance-dev-room/)

#### Abstract

A five minute introduction to the dev room.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-web-performance:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-web-performance:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XPVKKQ/feedback/)

---

### How browsers REALLY load Web pages

- **Speakers:** Robin Marx
- **Room:** UA2.220 (Guillissen)
- **Day:** Saturday
- **Time:** 15:10 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4852-how-browsers-really-load-web-pages/)

#### Abstract

When browsers load a Web page and its subresources, A LOT happens under the hood. They need to take into account render/parsing blocking resources, use a preload scanner, listen to resource hints (like preload/preconnect), loading modifiers (async/defer/module), fetchpriority, responsive images, and much more. Based on all those signals, they then need to somehow decide when to load which resources, to make optimal use of the modern HTTP/2 and HTTP/3 connections. And, as you might have guessed, none of the browsers do this in quite the same way (understatement alert!). Several even intentionally delay requesting some resources until others have been downloaded (shocked face emoji here). 
This talk is a deep dive into how browsers decide when to load a specific resource, and some ways in which you can influence them to modify their behaviour (so you can make sure that important LCP image is definitely one of the first things to come in!). We will look at A LOT of different waterfalls and discuss why each looks the way it does, why browsers often make different decisions, and how to solve common problems (no, don’t just preload everything with fetchpriority=high, you monster!).
You will walk away with a deeper understanding of what happens under the hood, which will allow you to better deal with the various gotchas and quirks present in today’s browsers and resource loading features.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-web-performance:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-web-performance:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CRLJNA/feedback/)

---

### Making Sense of the Long Animation Frames (LoAF) API

- **Speakers:** Andy Davies
- **Room:** UA2.220 (Guillissen)
- **Day:** Saturday
- **Time:** 15:55 - 16:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6376-making-sense-of-the-long-animation-frames-loaf-api/)

#### Abstract

Over time the web has become more reliant on JavaScript… but we've very little information on how its growth is affecting our visitors' experience.
Some believe JavaScript is the only way to build the modern web and dismiss the performance concerns, while others hold opposing views.
Wouldn't it be great if we had data on how scripts actually perform in our visitor's browsers – when they delay loading, cause jankiness and slowdown interactions, and perhaps more importantly which scripts are responsible?
After all, if we can't measure it, how can we improve it?
The W3C Long Tasks API was a first attempt at providing this data but it only helped us to understand when the Main Thread was busy and couldn't answer the question of why it was busy.
The W3C Long Animation Frames (LoAF) API aims to overcome the weaknesses of the Long Tasks API and provides both information on when there were long frames during rendering the process, and where possible, details on what Main Thread activity caused the long frame.
In this talk we'll explore:


What data the API provides and how it relates to the Main Thread activity we see when profiling pages using Chrome DevTools


How we can use this data to get a better understanding of our visitors experience in the wild and identify scripts that are having a harmful impact on our visitors experience


What data the API doesn't currently provide and how some of these gaps might be filled in the future


At the end of this talk you'll have a good understanding of the Long Animation Frames API and how to  use the data to identify scripts that need improvement.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-web-performance:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-web-performance:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DYPMWU/feedback/)

---

### Scheduling HTTP streams

- **Speakers:** Alexander Krizhanovsky
- **Room:** UA2.220 (Guillissen)
- **Day:** Saturday
- **Time:** 16:40 - 17:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4903-scheduling-http-streams/)

#### Abstract

Scheduling problem arise in many subsystems such as the CPU scheduler, disk IO or Qdisc. Despite extensive research during several decades, this problem remain challenging to solve due to varying workload requirements, diversity of scheduled resources, latency versus throughput considerations, scheduler overhead and many others. For instance, the Linux CPU scheduler continues to evolve.
In this talk, we’ll explore another scheduling scenario: HTTP streams prioritization. Having that a busy web server can manage millions of TCP connections, each potentially containing hundreds of HTTP/2 or HTTP/3 streams, a pretty efficient stream is essential. It should be fair, say, for progressive JPEGs, but it should prioritize shorter load times for PNG images. It should also be smart enough, particularly if browsers don’t adequately prioritize streams (which is still could be an issue for mainstream browsers in 2024). Additionally, it must be resilient against DDoS attacks.
This talk will cover the following topics:


The different nature of resources, their relationships, and how these factrors affect streams scheduling used for delivering these resources


Fair O(logN) and fast O(1) scheduling algorithms


Discussions on underlying data structures to optimize the scheduler for a large number of streams


HTTP/2 streams prioritization in servers such as Nginx, H2O, nghttp2 (Envoy, Apache HTTPD) and Tempesta FW


Differences between stream prioritization in HTTP/2 and HTTP/3, along with corresponding RFCs


How modern browsers construct stream priority trees


Server-side optimizations for streams scheduling in Cloudflare and Tempesta FW


Known vulnerabilities exploiting the HTTP/2 prioritization mechanisms

#### Related Links

- [Tempesta FW repository](https://github.com/tempesta-tech/tempesta)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-web-performance:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-web-performance:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UUDJYM/feedback/)

---

### Chromium on Android: How we doubled Speedometer & developed the LoadLine benchmark

- **Speakers:** Eric Seckler, Gurj Bahia
- **Room:** UA2.220 (Guillissen)
- **Day:** Saturday
- **Time:** 17:25 - 18:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5253-chromium-on-android-how-we-doubled-speedometer-developed-the-loadline-benchmark/)

#### Abstract

Chrome's Speedometer scores have more than doubled in the last ~two years. We'll outline major improvements and dig deeper into build optimizations and their impact on CPU microarchitecture bottlenecks. We'll also discuss the relevance of benchmarking end-to-end user journeys in the lab, and how we approached building a page load benchmark (bit.ly/loadline) to allow optimizing across the software/hardware stack.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-web-performance:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-web-performance:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3NLQGX/feedback/)

---

### Collaborate using the Firefox Profiler

- **Speakers:** Nazım Can Altınova
- **Room:** UA2.220 (Guillissen)
- **Day:** Saturday
- **Time:** 18:20 - 18:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6738-collaborate-using-the-firefox-profiler/)

#### Abstract

Tracking down performance issues can be tough, especially when you're not quite sure how to fix them and need to reach out to someone on your team for help. In this talk, we’ll explore how the Firefox Profiler not only helps identify performance bottlenecks but also makes it easy to collaborate with your team to find solutions faster.
We’ll show how to collect and analyze profiling data, spot key issues, and share your findings, so everyone can work together more effectively. We’ll go through real-world examples of how using the Firefox Profiler can streamline your debugging process and improve teamwork.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-web-performance:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-web-performance:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZZ97DZ/feedback/)

---

## BOF - Track A (15)

### Weblate BoF

- **Speakers:** Benjamin Alan Jamie
- **Room:** AW1.121
- **Day:** Saturday
- **Time:** 10:00 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6731-weblate-bof/)

#### Abstract

Gathering feedback, discussing Weblate plans, features, bugs, collaboration within the community, and anything Weblate. Like every year, everybody is welcome! Michal Čihař, Weblate Founder and Benjamin Jamie, Community Manager will be there for sure.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RVV7C8/feedback/)

---

### WebExtensions BoF

- **Speakers:** Rob Wu, Danny Colin
- **Room:** AW1.121
- **Day:** Saturday
- **Time:** 11:00 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5916-webextensions-bof/)

#### Abstract

An extension adds features and functions to a browser. It's created using familiar web-based technologies — HTML, CSS, and JavaScript. 
We’ll be meeting here to discuss the current state of WebExtensions (new APIs, toolings, and more). Whether you’ve authored several web extensions or a newbie working on your first extension, all are welcome to join and share about your experiences of building web extensions!
This session will be hosted by Danny Colin, with representatives from Mozilla Firefox’s add-ons team (Rob Wu & Simeon Vincent), from Google Chrome's extensions team (Oliver Dunk), and other extension community members ready to answer your questions.

#### Related Links

- [WebExtensions Documentation](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions)
- [W3C WebExtensions Community Group](https://github.com/w3c/webextensions)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DZHJEH/feedback/)

---

### Foreman Community discussion

- **Speakers:** Nofar Alfassi
- **Room:** AW1.121
- **Day:** Saturday
- **Time:** 12:00 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6745-foreman-community-discussion/)

#### Abstract

Join us for a Foreman community BoF session to connect with fellow contributors, users, and enthusiasts. This is an opportunity to discuss the future of Foreman, share experiences, address challenges, and brainstorm ideas for improving the ecosystem. Whether you're a developer, system administrator, or simply curious about Foreman, your input and participation are valuable!

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/R9TB7M/feedback/)

---

### NGI Zero network meetup BOF

- **Speakers:** Ronny Lam
- **Room:** AW1.121
- **Day:** Saturday
- **Time:** 13:00 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6561-ngi-zero-network-meetup-bof/)

#### Abstract

NLnet is inviting (prospect) NGI Zero projects to meet & greet, and have a discussion about the Next Generation Internet.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VNTNDY/feedback/)

---

### Global Voices, Inclusive Orgs: How Open-Source Sets the Standard for Inclusivity and How You Can Too BOF

- **Speakers:** Apoorv garg
- **Room:** AW1.121
- **Day:** Saturday
- **Time:** 15:00 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6630-global-voices-inclusive-orgs-how-open-source-sets-the-standard-for-inclusivity-and-how-you-can-too-bof/)

#### Abstract

Open Source thrives on the diversity of its global contributors, which has driven the creation of some of the most inclusive practices in the industry. Yet, nearly 80% of the global tech community remains underrepresented and faces numerous inclusivity barriers beyond just language. In this session, we'll see how open-source organizations have harnessed their diverse voices to craft a community that includes all identities, gender representations, and multilingual accessibility. By the end of this session, attendees will gain practical insights to implement these inclusive standards in their work, ensuring their community is welcoming and accessible to all.
This session highlights a critical issue in the tech industry - THE LACK OF INCLUSIVITY. While this problem spans multiple sectors, we will focus specifically on community practices. We'll explore how language barriers, gender biases, and accessibility gaps have historically excluded many from fully engaging with Community. We'll also look at how some of the most successful open-source communities, such as Kubernetes, and Django have faced inclusivity challenges before, how they have tackled them head-on, and what we can learn from their experiences.
This session is also to hear the voices of those who have faced issues and could share their experiences. So We can get more ideas and as an Open Source, be more inclusive.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FWPPS3/feedback/)

---

### OpenStack Community Meetup BOF

- **Speakers:** Amy Marrich
- **Room:** AW1.121
- **Day:** Saturday
- **Time:** 16:00 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4885-openstack-community-meetup-bof/)

#### Abstract

In this Birds of a Feather session, members of the OpenStack Community will have the opportunity to get together to discussion issues ranging from development to operations. It is also a goal of this session to welcome potential contributors and users who might want to learn more about the project and how they can get involved.
The OpenStack project is part of the OpenInfra Foundation. Code for the project is hosted at opendev.org

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SKXMGC/feedback/)

---

### How to Become a Contributor? An Open Source Masterclass BOF

- **Speakers:** Xavier Antoviaque, Rémi SHARROCK, Marc Jeanmougin
- **Room:** AW1.121
- **Day:** Saturday
- **Time:** 17:00 - 18:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6578-how-to-become-a-contributor-an-open-source-masterclass-bof/)

#### Abstract

Want to get more involved in open source and understand better how to contribute? Making your first contributions can be a daunting prospect, regardless of technical background. But fear not! This burd of a feather welcomes those who want a gentle introduction to the topic, and will equip you with what you need to get up to speed. 
We will demystify the process of contributing to an open source project, offering insights from the Open Source Masterclass MOOC https://opensourcemasterclass.org/ and several major open source projects and contributors. Whether you're aiming to submit code, improve documentation, or participate in discussions, you'll learn key strategies for making your first contribution meaningful and accepted by the community.
Open source projects are the backbone of innovation in today's technology landscape, and contributing to them can be a fulfilling and career-enhancing experience. However, taking that first step into an active project can seem overwhelming. 
We will explore the different types of contributions valued by open source communities: from code and documentation to community support and quality assurance. You will gain knowledge about the importance of communication, how to interact with project maintainers, and ways to align contributions with the current needs and priorities of the project.
Furthermore, this session will touch upon the practical aspects of the open source contribution lifecycle, including how to stay motivated, deal with feedback or rejection, and find mentorship opportunities within the community.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KQUXFY/feedback/)

---

### Version control is changing! BOF

- **Speakers:** Raphaël Gomès
- **Room:** AW1.121
- **Day:** Saturday
- **Time:** 18:00 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5414-version-control-is-changing-bof/)

#### Abstract

Let's chat about Git, Mercurial, Pijul, Jujistu... what makes them great or not so great and what they're currently doing to improve. Present in the room will be two Mercurial developers, the creator of Pijul and other people invested in this space, feel free to come, ask questions and bounce ideas!

#### Related Links

- [Pijul's website](https://pijul.org/)
- [The Mercurial changeset evolution concept](https://wiki.mercurial-scm.org/ChangesetEvolution)
- [Jujustu's repository](https://github.com/martinvonz/jj)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/D7GQ9P/feedback/)

---

### FSFE Upcycling Android Workshop BOF

- **Speakers:** Darragh Elliott
- **Room:** AW1.121
- **Day:** Sunday
- **Time:** 09:00 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4277-fsfe-upcycling-android-workshop-bof/)

#### Abstract

A workshop on installing custom Android ROM's in line with the FSFE's Upcycling Android Campaign.
Demonstration phones are available.
https://fsfe.org/activities/upcyclingandroid/upcyclingandroid.en.html

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ERSPVW/feedback/)

---

### FOSS apps on Android BoF

- **Speakers:** Michael Opdenacker
- **Room:** AW1.121
- **Day:** Sunday
- **Time:** 10:00 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6219-foss-apps-on-android-bof/)

#### Abstract

While on the GNU/Linux desktop, people can rely on mostly Free and Open Source applications, that's less the case on Android, which is still teeming with applications that serve other interests than ours. Let's share our experience trying to replace as many proprietary applications as possible with FOSS ones. This can be a very rewarding journey and we are not so far from something "the masses" can use!

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TCLRVQ/feedback/)

---

### Overcoming Ceph challenges at scale - CERN, IBM & Ceph community BOF

- **Speakers:** Abhishek Lekshmanan
- **Room:** AW1.121
- **Day:** Sunday
- **Time:** 11:00 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5790-overcoming-ceph-challenges-at-scale-cern-ibm-ceph-community-bof/)

#### Abstract

Ceph is a distributed storage system known for its scalability & flexibility. 
Ceph is also a complex system with lots of features, so it also comes with challenges. 
CERN relies heavily on ceph as building block for many IT, physics analysis & other services.
In this Birds of a Feather session, we will bring together engineers from CERN,  IBM and the community in a discussion for the challenges faced with tuning, running and using the correct features for the evolving scientific & business use cases.  Some discussion topics include multisite Ceph clusters, CephFS for diverse scientific/AI/ML workloads, the many RGW features for object safety, tiering strategies etc.  We will look at some pain points and solutions available as well as being developed to address these.
We expect a colloborative discussion with attendees, and would like everyone to share their experiences, ask questions and discuss improving Ceph as a solution for scientific as well as enterprise storage needs.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8FLW3H/feedback/)

---

### Social Web BOF

- **Speakers:** 
- **Room:** AW1.121
- **Day:** Sunday
- **Time:** 12:00 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6617-social-web-bof/)

#### Abstract

The Social Web, also known as the Fediverse, is an network of independent social software platforms. In this BOF, we will discuss some of the cool software being used in the Fediverse today.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MFVKPQ/feedback/)

---

### NLnet office hour

- **Speakers:** Ronny Lam
- **Room:** AW1.121
- **Day:** Sunday
- **Time:** 13:00 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6560-nlnet-office-hour/)

#### Abstract

Ask NLnet everything you want to know about Open Source (NGI0) grants. What are the requirements, how you can apply, and more... Current active grants are NGI0-Core, NGI0-Commons, and NGI0-Review.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BSMGH3/feedback/)

---

### Building Bridges: Exploring the Future of Developer Relations BOF

- **Speakers:** Nadia Jiang
- **Room:** AW1.121
- **Day:** Sunday
- **Time:** 15:00 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6568-building-bridges-exploring-the-future-of-developer-relations-bof/)

#### Abstract

Developer Relations (DevRel) is at the crossroads of community building, developer advocacy, and product growth. In this BoF session, we invite DevRel practitioners, software developers, and community managers to come together and discuss the evolving role of DevRel in the tech ecosystem. From fostering authentic relationships with developers to measuring the impact of DevRel initiatives, we'll explore best practices, common challenges, and emerging trends in the field.
Whether you're a seasoned DevRel professional, a developer curious about the field, or someone looking to build meaningful connections with your developer community, this session is for you. Join us for an open, informal discussion where we’ll share insights, exchange ideas, and shape the future of DevRel together.
Topics for discussion include:

How to balance advocacy, community building, and business goals in DevRel.
Innovative ways to engage and grow developer communities.
Challenges in measuring the success and ROI of DevRel efforts.
The impact of AI and other emerging technologies on DevRel strategies.
Sharing stories: successes, failures, and lessons learned.
Let’s collaborate to build stronger bridges between developers, communities, and organizations.

Who should join:
Anyone passionate about developer relations, including DevRel professionals, open source contributors, developers, community managers, and tech enthusiasts.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XXZWRJ/feedback/)

---

### Arch Linux meetup BOF

- **Speakers:** Jelle van der Waa
- **Room:** AW1.121
- **Day:** Sunday
- **Time:** 16:00 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6706-arch-linux-meetup-bof/)

#### Abstract

Arch Linux is a rolling release Linux distribution of which it’s staff have always attended FOSDEM. This BoF session gives a status update on the distribution, adjacent projects and future plans.
There will be a short presentation and a following Q&A session with distro maintainers and project developers.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9KWAES/feedback/)

---

## BOF - Track B (13)

### Future of the Arrow ecosystem BOF

- **Speakers:** Antoine Pitrou
- **Room:** H.3242
- **Day:** Saturday
- **Time:** 10:00 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5096-future-of-the-arrow-ecosystem-bof/)

#### Abstract

Apache Arrow has become a critical foundation for the data science and data analytics FOSS communities. It is also a large project, with a number of official specifications, even more implementations, and common grounds with other projects such as Parquet.
This session will gather Arrow maintainers, contributors and interested parties (such as maintainers of other FOSS data analytics projects) to discuss the Arrow project, its continued sustainability and possible directions for the future.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YCY3KX/feedback/)

---

### Offering paid services (contract work, SaaS) - from first steps BOF

- **Speakers:** Andriy Utkin
- **Room:** H.3242
- **Day:** Saturday
- **Time:** 11:00 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6615-offering-paid-services-contract-work-saas-from-first-steps-bof/)

#### Abstract

Making a living as a FOSS contractor or entrepreneur, or want to try? Come!
In the FOSDEM Job Corner and elsewhere there are opportunities to work on FOSS and get paid.
Unless you get employed by a company, there are some other things to deal with besides writing code. Let's share experience and get better at it!

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LSQX7F/feedback/)

---

### Digital Accessibility : Enhancing user experiences for persons with disabilities

- **Speakers:** Raashi Saxena
- **Room:** H.3242
- **Day:** Saturday
- **Time:** 12:00 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6163-digital-accessibility-enhancing-user-experiences-for-persons-with-disabilities/)

#### Abstract

We invite open-source maintainers, testers,  designers, developers, human rights defenders, researchers, activists, community organizers, digital security experts working, and others currently working within FOSS communities in the Global Majority, to join our gathering.
This gathering focuses on exchanging perspectives, sharing insights, and identifying both challenges and opportunities in designing usable and accessible open source internet circumvention technologies for underrepresented and historically marginalized communities. Through open and collaborative dialogue, we’ll share best practices and collectively strategize inclusive and contextually relevant approaches. In doing so, we hope to foster a practice of mutual support and care, sustaining our effort in contributing to a safer, more equitable, and resilient digital space for those at risk.
We'll facilitate our session like a circle where each participant will get to contribute and share their stories. The outline will roughly be like this:

Goal of the session
Individual Introduction
Questions for group discussion
Note-taking and sharing

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TJRJX9/feedback/)

---

### NetworkManager and Nmstate community meetup  BOF

- **Speakers:** Fernando Fernandez Mancera
- **Room:** H.3242
- **Day:** Saturday
- **Time:** 14:00 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4699-networkmanager-and-nmstate-community-meetup-bof/)

#### Abstract

Let's meet and talk about NetworkManager and Nmstate!
There is no fixed agenda or schedule. Everybody is welcome, and we will have an open discussion about problems, improvements, use cases and ideas for NetworkManager and Nmstate. Bring a topic you'd like to discuss, or just join to meet people.
See https://networkmanager.dev/community/ for how reach the community.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AHBS7Q/feedback/)

---

### AT Protocol developer meet and greet

- **Speakers:** Dietrich Ayala
- **Room:** H.3242
- **Day:** Saturday
- **Time:** 15:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6742-at-protocol-developer-meet-and-greet/)

#### Abstract

The AT Protocol aka @proto is a protocol designed for decentralized social applications, the inaugural example being Bluesky - a social network application.
If you're developing with @proto or for Bluesky, join to meet others doing the same.
Learn more at:

https://atproto.com/
https://bsky.app/
https://bsky.social/
https://atprotocol.dev/
https://lexicon.community

You can sign up at https://lu.ma/7a0p68nw to be notified about this and other @proto events around FOSDEM.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YGWJKD/feedback/)

---

### Hachyderm @ FOSDEM!

- **Speakers:** Preston Doster -- @esk@hachyderm.io
- **Room:** H.3242
- **Day:** Saturday
- **Time:** 15:30 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6748-hachyderm-fosdem-/)

#### Abstract

Kris Nova first announced Hachyderm -- a Mastodon instance that's a safe space for LGBTQIA+, BLM, and other historically marginalized communities -- on the FOSDEM stage in 2023. While Nova is no longer with her vision and spirit for bringing people together through tech and hacking the system is still with us. Today, Hachyderm is about 50,000 users (with about 10,000 monthly active users) strong.
We would like to host an in-person gathering for members of the Hachyderm community who are attending FOSDEM, but anyone is welcome. Come join us to talk about your favorite Nova stories, Hachyderm moments, or the Fediverse in general.  Several members of the Nivenly & Hachyderm teams will be joining us as well.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XR8PJT/feedback/)

---

### Debian BoF

- **Speakers:** Paulo Henrique de Lima Santana
- **Room:** H.3242
- **Day:** Saturday
- **Time:** 16:30 - 17:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6744-debian-bof/)

#### Abstract

Every year there are a lot of Debian community members at Fosdem,  so let's gather Debian Developers, contributors and enthusiasts to talk about Debian, their contributions, answer questions and talk about DebConf25 (The Debian Conference will take place in France  this year).

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RPH8RH/feedback/)

---

### MPTCP community meetup BoF

- **Speakers:** Matthieu Baerts
- **Room:** H.3242
- **Day:** Saturday
- **Time:** 17:30 - 18:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6750-mptcp-community-meetup-bof/)

#### Abstract

Let's meet and talk about Multipath TCP (MPTCP)!
Everybody is welcome! There is no fixed agenda or schedule. We will have open discussions about problems, improvements, use cases and ideas for MPTCP. Feel free to come with a topic, or simply join to meet people.
It is also possible to talk about kernel development, and continuous integration in the Linux kernel, e.g. the way MPTCP is continuously validated using Virtme-NG on public CI instances.
See https://www.mptcp.dev/#communication for how reach the community.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/L8M9DB/feedback/)

---

### Applying the "Do No Harm" Principle to Open Source Practices and Technology BOF

- **Speakers:** Malvika Sharan
- **Room:** H.3242
- **Day:** Sunday
- **Time:** 10:00 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6597-applying-the-do-no-harm-principle-to-open-source-practices-and-technology-bof/)

#### Abstract

The "Do No Harm" principle, well-established in fields like medical research, healthcare, and humanitarian aid, has significant potential to enhance ethical approaches and reduce the negative effects of open research practices and technology. 
As open source/science practices become a norm across different disciplines, it is important to identify, improve awareness of, and reduce its potential negative effects. While efforts like ethical source licenses (like the Do No Harm and Hippocratic License) are yet to become an acceptable legal pathway to enforcing responsible practices in open source, more general adoption and use of the "Do No Harm" will help account for societal and environmental implications of research and technology.
This Birds of a Feather session aims to engage the community in an interactive discussion about the implications of adopting the "Do No Harm" principle within open source projects and practices. I will start by introducing a simple framework designed to identify and develop actionable plans to mitigate the negative impacts of open research practices and technology. This framework examines the development and deployment of technology across four critical areas: the actors involved or affected, the dynamics and relationships within impacted communities, the economic realities faced by researchers, and environmental impact. Additionally, I will highlight practical methods for addressing the potential negative consequences of our work, inviting participants to share examples from their work.
This session is designed to be interactive and will engage participants involved in open source/science, including researchers, designers, contributors, developers, maintainers, and community members who seek to better understand and navigate the ethical challenges of open research and technology. Attendees will gain insights into global disparities in technology and explore how they can share responsibility to ensure their work promotes more equitable benefits by combining open practices with the do-no-harm principle.
Desired Outcomes:
1) Increased awareness of the ethical dimensions of open source.
2) Identification of practical steps for integrating the "Do No Harm" principle into open source products and practices.
3) Formation of a network of stakeholders interested in advancing ethical frameworks in open science.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TJTHDC/feedback/)

---

### FOS 4 Bioinformatics & Computational Biology

- **Speakers:** Alexis Praga, Jim Procter, Freek van Hemert
- **Room:** H.3242
- **Day:** Sunday
- **Time:** 12:00 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6747-fos-4-bioinformatics-computational-biology/)

#### Abstract

This BoF is to bring together FOSDEMers involved in or interacting with others doing computational biology and bioinformatics, and anyone interested in learning more about how open source powers computational biology research around the world.
Open source and free software has long history in the computational biology community, forming the backbone of many high-quality tools. However, their adoption in research, industry, and healthcare settings is not yet universal. FOSDEM provides the ideal platform to bridge this gap by drawing upon best practices in computer science and applying them to the biological context.
Currently, bioinformatics is underrepresented at FOSDEM. This BoF seeks to change that by creating a space to share insights, demonstrate projects, and discuss the future of open-source bioinformatics.
Goals

Establish the foundation of a bioinformatics community at FOSDEM.
Explore effective and emerging practices for open-source software, systems, and infrastructure in computational biology across public, private, and academic sectors.
Showcase projects and spread the word about upcoming events.

Proposed Outline of the session

Intros
Open HPC infrastructure stack 
Demo: Snakemake on the Dutch Tier 1 (SLURM powered) supercomputer Snellius (10min)
Discussion: schedulers (e., Slurm), HPC file systems (Gluster, SaunaFS), containers (Nix, docker...)


Workflow systems and reproductibilty
Demo: Nextflow and the nf-core initiatve (10min)
Discussion: choosing a workflow language (snakemake, nextflow, common Workflow Language), ensuring reproducibility


Open Web facing infrastructure and APIs
Demo: Slivka-Bio (https://compbio.dundee.ac.uk/slivka) and friends (10min)
Discussion: Galaxy, Jupyter, and local, national, and international platforms for computational biology


Closing Discussion
Keep in contact at https://matrix.to/#/#fosdembioinformatics:matrix.org

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BAUW8H/feedback/)

---

### Automotive BOF

- **Speakers:** Walt Miner, Jan-Simon Möller
- **Room:** H.3242
- **Day:** Sunday
- **Time:** 13:00 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6762-automotive-bof/)

#### Abstract

Meet and chat about open source in automotive !
This Birds of a Feather (BoF) session at FOSDEM will focus on the growing intersection of open source and the automotive industry, highlighting the latest advancements, challenges, and opportunities for collaboration. As the automotive sector increasingly adopts open-source software, it is driving innovation in areas such as in-vehicle systems, autonomous driving, and vehicle connectivity. Key projects like Automotive Grade Linux (AGL) and the ELISA (Enabling Linux in Safety Applications) initiative are at the forefront of this transformation, providing open-source frameworks for developing scalable, secure, and reliable automotive software. This session will bring together developers, engineers, and enthusiasts to discuss how these initiatives are shaping the future of mobility and explore how open-source communities can work together to solve the unique challenges of the automotive domain.
Attendees will have the opportunity to share experiences, discuss key technical topics such as real-time operating systems, safety-critical systems, and compliance with automotive standards (e.g., ISO 26262), and explore potential new collaborations. The session will delve into the importance of open standards, the growing need for security in connected vehicles, and how projects like AGL and ELISA enable safer, more efficient automotive software development. By fostering cross-industry dialogue and strengthening the automotive open-source ecosystem, this session aims to inspire future collaborations that can help define the next generation of smart, connected, and autonomous vehicles.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SJS93M/feedback/)

---

### Coordinating a Windows 10-to-Linux upcycling campaign across Free Software communities worldwide

- **Speakers:** Joseph P. De Veaugh-Geiss
- **Room:** H.3242
- **Day:** Sunday
- **Time:** 14:00 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6779-coordinating-a-windows-10-to-linux-upcycling-campaign-across-free-software-communities-worldwide/)

#### Abstract

Windows 10 security updates end on 14 October 2025, KDE's 29th birthday and also, ironically, International E-Waste Day (you cannot make these things up!). Hundreds of millions of functioning devices will become e-waste. This means manufacturing and transporting new ones, which is perhaps the biggest waste of all: hardware production alone can account for over 75% of a device's CO2 emissions over its lifespan.
Free Software is a solution, and if we work together Windows 10 could truly be the last version of Windows users ever use! Let's take this opportunity to coordinate a global, unified Free Software campaign over the next year to raise awareness about the environmental harm of software-driven hardware obsolescence, at the same time upgrading users from Windows 10 to GNU/Linux directly to keep those devices in use and out of the landfill. Let's think big and act boldly! Campaign organization has already begun, but there is still time to get involved. Help decide what the campaign will look like and how we can best reach our target audience! Let's brainstorm what obstacles for new users exist and how our communities can best address them! Join the BoF to co-ordinate, together.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7BYUY8/feedback/)

---

### Making the Financial World Open Source With FINOS

- **Speakers:** Manik Surtani, Gabriele Columbro
- **Room:** H.3242
- **Day:** Sunday
- **Time:** 15:00 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6780-making-the-financial-world-open-source-with-finos/)

#### Abstract

Open Source is becoming a first class citizen in a traditionally closed industry like Financial Services, and FINOS.org (The Fintech Open Source Foundation), a project of the Linux Foundation, is helping some all the constituencies of the financial sector collaborate in the open.
Come talk about further breaking down the walled gardens of fintech and finance at the FINOS BOF room. 
We’ll discuss:
- Building interoperable systems with open standards
- Open source tools for payments, investment banking, regulation & compliance, and risk management
- Collaboration between developers, institutions, and regulators
- Addressing challenges like security, scalability, and adoption
- Open Source + AI + Financial Services

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EH3CEH/feedback/)

---

## BOF - Track C (15)

### Special-Purpose Operating Systems Meetup BOF

- **Speakers:** Mauro Morales
- **Room:** H.3244
- **Day:** Saturday
- **Time:** 10:00 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6716-special-purpose-operating-systems-meetup-bof/)

#### Abstract

The Special-Purpose Operating Systems (SPOS) Working Group is a collaborative initiative under the CNCF TAG Runtime, bringing together developers, maintainers, and adopters focused on operating systems designed for specific workloads—cloud-native, edge, embedded systems, and more.
In this Birds of a Feather (BoF) session, we aim to connect in person for the second time at FOSDEM, a pivotal event for the open-source operating system community. This meetup will provide a space for SPOS enthusiasts, contributors, and representatives from major Linux distributions to exchange insights, share experiences, and discuss the future direction of specialized operating systems.
https://tag-runtime.cncf.io/wgs/spos/charter/

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/A9JTUG/feedback/)

---

### Organizing sponsor free conferences BOF

- **Speakers:** Rabbit
- **Room:** H.3244
- **Day:** Saturday
- **Time:** 11:00 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6721-organizing-sponsor-free-conferences-bof/)

#### Abstract

Organizing conferences is a challenging but rewarding experience, and keeping them free from conflicts of interest makes it even more meaningful. At NixCon 2024, we took the bold step of going completely sponsor-free—and it turned out to be a great success, with 400 attendees, making it the largest NixCon to date.
In this BOF session, I’ll share my experiences as a core organizer, including the challenges, lessons learned, and tips for anyone looking to organize their own sponsor-free events without breaking the bank. Let’s discuss how to prioritize community and make it work without sponsorship.
https://2024.nixcon.org/

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NH8FRK/feedback/)

---

### Lets discuss performance and scale related challenges BOF

- **Speakers:** Imaanpreet Kaur, Pravin Satpute
- **Room:** H.3244
- **Day:** Saturday
- **Time:** 12:00 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6567-lets-discuss-performance-and-scale-related-challenges-bof/)

#### Abstract

We are planning to kick off this BoF by discussing the Continuous Performance Testing (CPT) methodology. At Red Hat, We are implementing this approach to ensure that our projects and products consistently meet the minimum performance and scalability standards with each update.
After that, participants will have the opportunity to discuss the performance and scalability challenges they are encountering, as well as the strategies they are employing to address these issues prior to the final release of their projects or products.
Following these discussions, We intend to arrange dedicated talks later with attendees that will concentrate on the specific performance and scalability challenges they are facing.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QZL8K3/feedback/)

---

### DevOpsDays meetup

- **Speakers:** Katie McLaughlin
- **Room:** H.3244
- **Day:** Saturday
- **Time:** 12:30 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6784-devopsdays-meetup/)

#### Abstract

DevOpsDays is a global series of technical conferences run entirely by local volunteers, started in Ghent in 2019.
This BOF is a space for DevOpsDays organizers and volunteers to collaborate and discuss future plans for their events, and share lessons learnt during their events.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SQFZZ7/feedback/)

---

### Mozilla Contributors: Newcomers and Old timers Meetup

- **Speakers:** Danny Colin
- **Room:** H.3244
- **Day:** Saturday
- **Time:** 13:00 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6755-mozilla-contributors-newcomers-and-old-timers-meetup/)

#### Abstract

Come learn about contribution opportunities across all Mozilla. We have opportunities for both developers and non-developers (user support, localization, documentation). It's a great opportunity for newcomers to ask questions and for old timers to have a casual chat with other contributors about their works; or help newcomers to get started.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RLDFJU/feedback/)

---

### Multicore & Concurrency: Algorithms, Performance, Correctness

- **Speakers:** Diogo
- **Room:** H.3244
- **Day:** Saturday
- **Time:** 14:00 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6757-multicore-concurrency-algorithms-performance-correctness/)

#### Abstract

In this BOF session, we'll discuss the application of concurrent algorithms in system software (operating systems, system libraries, database systems, runtime systems, etc).  Practical requirements, techniques and trends from the industry as well as research results and limitations are interesting areas of discussion. The goal is to connect with concurrency enthusiasts and to figure out whether a critical mass exists to form a "Multicore & Concurrency" devroom next year.
Planned agenda:

Introduction round
Talk 1: Concurrent cat on a Raspberry Pi - Diogo Behrens
Talk 2: Modern Concurrency Made Easy(ier) - Hernan Ponce de Leon
Talk 3: Evaluate All the Things with benchkit - Antonio Paolillo
Discussion: How to evolve this to a devroom?

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7KFSJ7/feedback/)

---

### Cloud Autonomy and Interoperability: The Eclipse Cloud

- **Speakers:** Gaël Blondelle, Jean-Baptiste Piacentino
- **Room:** H.3244
- **Day:** Saturday
- **Time:** 15:00 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6760-cloud-autonomy-and-interoperability-the-eclipse-cloud/)

#### Abstract

Join us at  for an engaging session on the Eclipse Cloud Interest Group! This session will explore our mission to foster cloud autonomy and interoperability, offering insights into the group’s objectives and ongoing efforts. We’ll also feature presentations from key technical projects associated with the Interest Group, such as Xpanse, Biscuit, Conformity Assessment Profile, and XCP-ng, highlighting their contributions to creating an open, resilient, and interoperable cloud ecosystem. You are interested in cloud interoperability? This session is your chance to connect, collaborate, and contribute. Join us to learn more about the Interest Group, get involved in the projects, and help shape the future of cloud services!

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FSVVC9/feedback/)

---

### Open-Hardware E Ink Devices with Modos: Discussion & Demos

- **Speakers:** Alexander Soto
- **Room:** H.3244
- **Day:** Saturday
- **Time:** 16:00 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6753-open-hardware-e-ink-devices-with-modos-discussion-demos/)

#### Abstract

Modos is an open-hardware and open-source company, building an ecosystem of e-ink devices to re-imagine personal computing with a focus on creating calm, inclusive, and humane technology.
Join us for an informal BoF session to discuss open-hardware e-paper projects, come and try our Caster development board and Paper Monitor, and discuss improvements and ideas. There’s no fixed agenda—just a chance to share use cases, get feedback, and build a community around e-paper and open hardware. Bring your questions or come meet others in the community.

#### Related Links

- [Talk: Modos: Building an Ecosystem of Open-Hardware E Ink Devices](https://archive.fosdem.org/2024/schedule/event/fosdem-2024-3052-modos-building-an-ecosystem-of-open-hardware-e-ink-devices/)
- [Modos: 2024 Year In Review](https://www.modos.tech/blog/2024-year-in-review)
- [NLnet; Caster](https://nlnet.nl/project/Modos/)
- [Github: Modos Labs](https://github.com/Modos-Labs)
- [Contribute to our Development](https://db.modos.tech/form/Sbzu4X9wXg-FikIie0yBVCwSRdhPfLIL9ropUdMttSQ)
- [Talk: Reimagining Personal Computing with E ink: Community Insights and Design Challenges](https://archive.fosdem.org/2024/schedule/event/fosdem-2024-3049-reimagining-personal-computing-with-e-ink-community-insights-and-design-challenges/)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/Q7V3PQ/feedback/)

---

### Patchouli: Open-Source EMR Drawing Tablet

- **Speakers:** Alexander Soto
- **Room:** H.3244
- **Day:** Saturday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6754-patchouli-open-source-emr-drawing-tablet/)

#### Abstract

Patchouli is an open-source electro-magnetic drawing tablet hardware implementation, including a coil array, an RF front end built using commercially available parts, and digital signal processing algorithms. The design is compatible with most commercial pens from different vendors, offering an ultra-low-latency pen input experience for your customized hardware projects.
Join us for an informal BoF session to discuss and try out Patchouli and discuss improvements and ideas. There’s no fixed agenda—just a chance to share use cases, get feedback, and build a community around Patchouli. Bring your questions or meet others in the community.

#### Related Links

- [Project Patchouli Documentation](https://patchouli.readthedocs.io/en/latest/)
- [GitLab: Project Patchouli](https://gitlab.com/yukidama/patchouli)
- [Project Patchouli Presentation](https://docs.google.com/presentation/d/1czwQGQsdwWLSjI47rnOqcgozgKpyf986XkGZxYL4NJc/edit#slide=id.p)
- [NLnet; Patchouli](https://nlnet.nl/project/Patchouli/)
- [Discord: Patchouli](https://discord.gg/EGKbpjMyaB)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RBTZ38/feedback/)

---

### Let's huddle around Nextcloud BOF

- **Speakers:** Jos Poortvliet
- **Room:** H.3244
- **Day:** Saturday
- **Time:** 17:00 - 18:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4516-let-s-huddle-around-nextcloud-bof/)

#### Abstract

Nextclouders, unite!
We don't have a booth this year, so let's instead get together for an hour and talk about all the good stuff in one place and time. Come with your questions, ideas, feature requests, bugs and hugs and share them!
Next-what? Oh, you're in for a treat. Sick of Big Tech owning your data? We have the answer. You can share and work on documents, participate in video calls, have chats, automate stuff or even talk endlessly and uselessly to an artificial intelligence - WITHOUT having to hand over your data. Yes. it is possible. And fully open source too. You just have to host it yourself, as we only make software. No real clouds here!

#### Related Links

- [Our project](https://nextcloud.com)
- [The Code!](https://github.com/nextcloud)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JADCGH/feedback/)

---

### Bevy: Rustlang Game Engine

- **Speakers:** Thierry Berger
- **Room:** H.3244
- **Day:** Sunday
- **Time:** 10:00 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6751-bevy-rustlang-game-engine/)

#### Abstract

Meet up with Rustaceans, talk about https://bevyengine.org/, Rustlang, game development and open source development.
An open sourced Rustlang-themed card game will be available to play as a social ice-breaker (see https://github.com/Vrixyz/techycards).

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/C9ZY38/feedback/)

---

### Software patents in Europe v3.0: 20 years anniversary and further actions

- **Speakers:** Benjamin Henrion
- **Room:** H.3244
- **Day:** Sunday
- **Time:** 11:00 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6759-software-patents-in-europe-v3-0-20-years-anniversary-and-further-actions/)

#### Abstract

20 years ago in 2005, large corporations asked the European Parliament to reject the software patents directive to better push for a central patent court instead, the Unified Patent Court (UPC). They shielded patent law from any intervention of the European Court of Justice (CJEU), meaning the final word over software patents will be made by pro-patent courts. Those large corporations (Nokia, Airbus) also managed to get their attorneys as part time judges.
We will discuss with the interested people what to do, including further legal actions.

#### Related Links

- [FFII: Unified Patent Court has an EU treaty legality problem, said ex-CJEU judge Melchior Wathelet](https://ffii.org/unified-patent-court-has-an-eu-treaty-legality-problem-says-ex-cjeu-judge-melchior-wathelet/)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YGQEBZ/feedback/)

---

### Sailfish OS Community BoF

- **Speakers:** David Llewellyn-Jones, Raine Mäkeläinen
- **Room:** H.3244
- **Day:** Sunday
- **Time:** 11:30 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6773-sailfish-os-community-bof/)

#### Abstract

Sailfish OS has been providing daily-usable Linux on phones for over a decade, with its unique blend of gesture-based mobile interface, Android AppSupport and enthusiastic community. Join the Sailfish OS Community Birds of a Feather event to talk about Sailfish OS, meet the Sailfish community, share experiences and ask questions.
The Jolla Team will be present to answer your questions and share insights about future developments, including the new Jolla Mind2, a privacy-first AI computer that connects with your phone and also runs Sailfish OS.
The Sailfish OS BoF has been running for many years at FOSDEM and always attracts an enthusiastic community. We look forward to seeing you there!

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EYBDBH/feedback/)

---

### RIOT-OS: Embedded/IoT OS meetup

- **Speakers:** Benjamin Valentin
- **Room:** H.3244
- **Day:** Sunday
- **Time:** 13:00 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6776-riot-os-embedded-iot-os-meetup/)

#### Abstract

RIOT is a free operating system for 8/16/32 bit microcontrollers (AVR, MSP430, STM32, ESP32, nRF5x SAM Dx, …).
It comes with a networking stack, a hardware abstraction layer and many drivers out of the box while focusing on ease of use.
Join this session if you are interested in IPv6/6LoWPAN and CoAP on MCUs, want to meet with other RIOT developers or discuss new developments in this space.
https://github.com/RIOT-OS/RIOT

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LUB3B3/feedback/)

---

### Making you embedded product CRA compliant

- **Speakers:** Marta Rybczynska
- **Room:** H.3244
- **Day:** Sunday
- **Time:** 14:00 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6764-making-you-embedded-product-cra-compliant/)

#### Abstract

This BoF will be a place to discuss technical details of making embedded products (using open source) compliant with the CRA (Cyber Resilience Act).
We can chat about:
- the technical blueprints (secure defaults, hardening, logging, updates...)
- processes (risk assessment, vulnerability reporting)
- tools (SBOM, CVEs...)

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CWVVVF/feedback/)

---


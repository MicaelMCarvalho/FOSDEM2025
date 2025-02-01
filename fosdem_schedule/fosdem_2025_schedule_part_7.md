# FOSDEM 2025 Schedule - Part 7 of 11

*Generated on 2025-02-01*

## Table of Contents

- [Microkernel and Component-Based OS (10)](#microkernel-and-component-based-os-10)
- [Modern Email (17)](#modern-email-17)
- [Monitoring and Observability (13)](#monitoring-and-observability-13)
- [Mozilla (12)](#mozilla-12)
- [MySQL (14)](#mysql-14)
- [Network (21)](#network-21)
- [Nix and NixOS (10)](#nix-and-nixos-10)
- [Open Hardware and CAD/CAM (19)](#open-hardware-and-cad/cam-19)

## Microkernel and Component-Based OS (10)

### Celebrating kernel diversity with Genode

- **Speakers:** Alexander Boettcher
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 15:30 - 15:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5768-celebrating-kernel-diversity-with-genode/)

#### Abstract

The Genode OS framework is an open-source tool kit for building component-based
operating systems. It scales from rather static embedded appliances to highly
dynamic general-purpose computing as showcased by Sculpt OS. Nowadays Sculpt OS
is mature, in daily use, and supports PCs, ARM notebooks and the PinePhone.
Since its inception, the Genode framework supports various microkernels and
Linux at the lowest layer. Even so Genode leveraged the characteristic features
of the underlying kernels, each kernel called for different trade-offs.
All the requirements and expectations by the Genode framework towards the kernel
are institutional knowledge of Genode's core developers and implicitly documented
in Genode's foundation book.
As I'm currently in the process to enable another kernel, let's take a
look back, review our experiences, re-iterate challenges we had
to surmount, and draw the connection to the ongoing endeavor of broadening
Genode's kernel landscape even more.
It goes without saying that no Genode talk is without a demo!
https://www.genode.org
https://www.genodians.org
https://genode.discourse.group
https://github.com/genodelabs

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-microkernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-microkernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GLKVYX/feedback/)

---

### MACHINA: Lessons and Insights from Reimplementing the Mach Microkernel

- **Speakers:** Gianluca Guida
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 16:00 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5490-machina-lessons-and-insights-from-reimplementing-the-mach-microkernel/)

#### Abstract

Mach, famous for its complex IPC and VM subsystems, remains to this day an influential and historically significant Microkernel.
This talk introduces MACHINA, a new microkernel for AMD64 and RISCV64 modelled after the Mach 3 Microkernel. Currently in prototype stage, MACHINA aims to create a modular architecture for experimenting with "Mach-like" systems, reinterpreting Mach’s  principles for modern hardware and software environments.
The talk will describe Mach 3’s abstractions and architecture—with a particular focus on its IPC and VM subsystems—and explore the process, design choices, and challenges of reimplementing them from scratch.

#### Related Links

- [Github Sources](https://github.com/glguida/machina)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-microkernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-microkernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EKGPWS/feedback/)

---

### CMRX: Microkernel-based RTOS with memory isolation on MMU-less architectures

- **Speakers:** Eduard Drusa
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 16:25 - 16:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4390-cmrx-microkernel-based-rtos-with-memory-isolation-on-mmu-less-architectures/)

#### Abstract

Despite memory isolation being used for decades now; a typical contemporary low-power IoT embedded system does not use this technique. One of reasons might be that in virtually all available systems memory isolation is an afterthought. We proposed, designed and implemented CMRX real-time operating system targeted towards devices without MMU which takes memory isolation as non-negotiable feature.
Achieving usable memory isolation on such constrained hardware has its challenges and there are compromises to be made. In this talk I will outline high-level design decisions and overall system design of the CMRX RTOS. Why micro-kernel design is suitable in this situation, what advantages does it bring? I will tackle benefits and potential drawbacks of proposed architecture and finally cybersecurity point of view will be discussed.

#### Related Links

- [CMRX source code:](https://github.com/ventZl/cmrx.git)
- [CMRX documentation:](https://ventzl.github.io/cmrx/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-microkernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-microkernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/993TJZ/feedback/)

---

### Obtaining Safety & Security Certifications for L4Re

- **Speakers:** Marcus Hähnel
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 16:50 - 17:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6039-obtaining-safety-security-certifications-for-l4re/)

#### Abstract

In this talk I will share some details on the path towards the recently obtained Security (EAL4+, German GEHEIM) and Safety (ISO26262 ASIL-B, SIL-2) certifications that have been achieved for the L4Re Operating System Framework. I will show some details on where generic software development, operating systems, and third-party code clash with the expectations of the safety norms. I will also shed some light on the challenges we face in maintaining these certifications while staying true to the open source nature of the system with contributions form a multitude of actors from various fields. I will conclude with an outlook of the things to come and how we want to ensure that open source microkernel-based operating systems can be a vital cornerstone to safe & secure systems.

#### Related Links

- [L4Re Homepage](https://www.l4re.org)
- [L4Re Github Repositories](https://github.com/kernkonzept/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-microkernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-microkernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/J8JMUU/feedback/)

---

### A Formal Specification of the NOVA Microhypervisor

- **Speakers:** Hoang-Hai Dang
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 17:20 - 17:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5083-a-formal-specification-of-the-nova-microhypervisor/)

#### Abstract

We present a formal specification of NOVA that captures its complex concurrent and architectural behavior. Our specification combines an operational specification for unprivileged user code with a separation logic specification of privileged state and operations. The specification precisely captures the subtle behaviors of NOVA such as address translation and user faults. Separation logic’s small footprint and open world nature makes the specification highly modular and reasonably high level, allowing us to abstract architectural details that are encapsulated by NOVA and evolve the formal specification as NOVA evolves. Using the specification, we have carried out proofs of the NOVA source code as well as of applications running on top of NOVA.

#### Related Links

- [Formal proof development (in Rocq) of the NOVA formal specification (2024-04-16)](https://github.com/bedrocksystems/fm-releases/tree/main/nova_interface.2024-04-16)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-microkernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-microkernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UYUQPR/feedback/)

---

### Cancelling POSIX syscalls in Managarm - an asynchronous microkernel-based OS

- **Speakers:** Geert Custers
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 17:50 - 18:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4938-cancelling-posix-syscalls-in-managarm-an-asynchronous-microkernel-based-os/)

#### Abstract

One of the most idiosyncratic parts of POSIX compliance is signal support. On microkernels the implementation can prove to be quite difficult. One especially tricky part is the cancellation of POSIX syscalls when they are interrupted by signals, and the intricacies of EINTR side effects. Monolithic kernels inheritely have the bookkeeping required to implement this without  extra overhead. In contrast, due to the generally distributed nature of microkernels, properly cancelling syscalls requires extra work. This is especially the case for Managarm, where (1) POSIX is implemented in a userspace server, (2) syscalls are asynchronous and (3) can involve multiple servers.
In this talk, we will explore the process of implementing syscall cancellation on Managarm. A brief overview of signal delivery is given, followed by a deep dive into the new lifetime of a Managarm POSIX request. Finally, we give a summary of the lessons learned while implementing cancellation in a fully asynchronous microkernel.

#### Related Links

- [Managarm Github repository](https://www.github.com/managarm/managarm)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-microkernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-microkernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GQZRY8/feedback/)

---

### POSIX Signals in User Space on the Redox Microkernel

- **Speakers:** Jacob Lorentzon
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 18:15 - 18:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5670-posix-signals-in-user-space-on-the-redox-microkernel/)

#### Abstract

Redox is a community-developed Unix-like operating system written in Rust, with the long term goal of being a microkernel-based alternative to its monolithic counterparts. To achieve this, Redox has been pursuing a "userspaceification" strategy of the POSIX-enabling logic in the kernel, into a runtime library. The most recent example of this is the ongoing POSIX Signals project, funded by NLnet.
This presentation will provide an overview of the Redox operating system and architecture. It will describe the technical details of the userspace signals implementation, challenges, and which parts that were kept in the kernel and why.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-microkernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-microkernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9HBPFE/feedback/)

---

### Trusted boot with the Genode OS Framework

- **Speakers:** Alice Domage
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 18:40 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4140-trusted-boot-with-the-genode-os-framework/)

#### Abstract

Alice will present Gapfruit's design of trusted boot in combination with a microkernel operating system built with the Genode OS framework on an i.MX8MP SoC. This presentation will cover the various building blocks involved, including TPM, u-boot, libraries, and supporting tools. It will also explore how these components integrate within a microkernel environment and the trade-offs we have faced.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-microkernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-microkernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YB7J7K/feedback/)

---

## Modern Email (17)

### Welcome to the Modern Email DevRoom 💌

- **Speakers:** 
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 10:30 - 10:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6662-welcome-to-the-modern-email-devroom-/)

#### Abstract

Introduction to the DevRoom

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3B3K9T/feedback/)

---

### aerc, an email client for the discerning hacker

- **Speakers:** Robin Jarry
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 10:35 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4084-aerc-an-email-client-for-the-discerning-hacker/)

#### Abstract

aerc is a modern email client for your terminal written in Go. aerc supports IMAP, SMTP, JMAP, Maildir, notmuch, mbox and has been designed with patch review and management in mind.
aerc is easy to setup with a new account wizard and has first class support for git+email based workflows.
In this talk, I will be making an introduction to aerc and its capabilities. I will also demonstrate some of the ways you can tweak it and configure it to suit your needs.
More information is available at https://git.sr.ht/~rjarry/aerc

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KRQSAB/feedback/)

---

### Parula - Presenting the new email client

- **Speakers:** Ben Bucksch
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 11:00 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4887-parula-presenting-the-new-email-client/)

#### Abstract

Parula is a new email application, calendar and chat app, for everybody - business use and private. It is Open Source, implemented in TypeScript, and runs on Linux, Mac, Windows and soon Android. This talk is presenting the app, and showing where we need help for implementation and testing.
We would like to bring fresh air into the email ecosystem and not leave it entirely to Microsoft Office365 and GMail. Let's make email enjoyable for everybody.
https://parula.beonex.com

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3CRMDM/feedback/)

---

### Structured Email: Building blocks and implementation guidance

- **Speakers:** Hans-Jörg Happel
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 11:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6386-structured-email-building-blocks-and-implementation-guidance/)

#### Abstract

Structured Email allows to extend common email messages with a machine readable representation. The talk describes available libraries and implementation experience with the Structured Email Plugin for Roundcube Webmail. The talk also explains ongoing work within the IETF Structured Email working group.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DKCJKT/feedback/)

---

### Stalwart Mail Server

- **Speakers:** Mauro De Gennaro
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 12:00 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4571-stalwart-mail-server/)

#### Abstract

Self-hosting an e-mail server is notoriously challenging. While privacy is a top concern for many individuals and businesses, the complexities of self-hosting a mail server often outweigh the benefits, leading many to choose to sacrifice some privacy and pay a third-party provider to manage their email instead. One of the key challenges of self-hosting an email server is the outdated and complex nature of most available open-source mail server software.
Stalwart Mail Server seeks to change this by providing a modern, open-source mail server built in Rust that prioritizes ease of use, security, and privacy. Designed to simplify self-hosting, Stalwart Mail Server enables individuals and businesses to reclaim their email autonomy with confidence. This talk will explore how Stalwart Mail Server democratizes email, promoting decentralization by making self-hosted email accessible, secure, and efficient. Join us to learn how Stalwart can empower you to take back control of your email in today’s digital landscape.

#### Related Links

- [Project Repository](https://github.com/stalwartlabs/mail-server)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PBBX8X/feedback/)

---

### Mox and simplifying mail server setup & management

- **Speakers:** Mechiel Lukkien
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 12:30 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5364-mox-and-simplifying-mail-server-setup-management/)

#### Abstract

Mox is a relatively young modern, all-in-one mail server. One of its goals it making it easy to setup a mail server, and keeping it up to date. In this talk, we'll look at how mox helps with setting up and running a mail server. From the original quickstart with its environment checks, setting up initial DNS records and modifying them later on, notifying about new mox releases and installing them, to a future easier guided setup process and automatic DNS management.

#### Related Links

- [mox website](https://www.xmox.nl)
- [mox source](https://github.com/mjl-/mox)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XPVQV8/feedback/)

---

### How to Deploy Full-Scale Secure On-Prem E-Mail Security Cluster as IaC

- **Speakers:** Carsten Rosenberg, Manu Zurmuehl
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 13:00 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6350-how-to-deploy-full-scale-secure-on-prem-e-mail-security-cluster-as-iac/)

#### Abstract

In times of complexity and easy cloud computing - is it still value-able to maintain an on-prem mail cluster with open-source tools?
We will showcase our approach to sizing and rolling out a complete and flexible mail infrastructures, highlight why we chose Ansible for IaC, our approach to template the configuration and automatic documentation generation. We continue to update and develop our roles to incorporate our best practices, develop new features and counter latest security threats. Our Ansible Playbooks and Roles to roll-out this full fledged E-Mail infrastructure are open-source and publicly available. The setups are maintained either by us, the customer with our support or also completely independent.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZLNFN3/feedback/)

---

### Enhancing Email Spam Detection with LLMs: Practical Experience with Rspamd and GPT

- **Speakers:** Vsevolod Stakhov
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 13:30 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5114-enhancing-email-spam-detection-with-llms-practical-experience-with-rspamd-and-gpt/)

#### Abstract

This talk explores the practical implementation of Large Language Models (LLMs) in email filtering, giving the example of the integration between Rspamd and various LLM services. We'll discuss how LLMs can complement traditional filtering methods, comparing supervised (Bayes) and unsupervised (LLM-based) approaches to spam detection.
We'll examine real-world results from different models (GPT-3.5, GPT-4, and alternatives via OpenRouter), analyzing their effectiveness, false positive rates, and cost implications. The presentation will cover advanced features such as content categorization, password extraction from archives, and message anonymization for privacy-preserving learning.
Special attention will be given to practical deployment considerations, including:

Cost-effective strategies for different scales of operation
Self-hosted models vs. cloud APIs
Privacy considerations and message anonymization techniques
Integration with existing email infrastructure
Extended message analysis capabilities

The talk will conclude with insights into future developments and best practices for implementing LLM-based email filtering in both personal and enterprise environments.
Target Audience: Email administrators, spam filtering specialists, and developers interested in modern email security solutions.

#### Related Links

- [Rspamd project website](https://www.rspamd.com)
- [Rspamd project repository](https://github.com/rspamd/rspamd/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RPKY3P/feedback/)

---

### Advanced mail security - our experience with automated reputation sharing in communities and pre-queue deep threat analyzers

- **Speakers:** Carsten Rosenberg
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 14:00 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6360-advanced-mail-security-our-experience-with-automated-reputation-sharing-in-communities-and-pre-queue-deep-threat-analyzers/)

#### Abstract

From out daily experience as Linux Mail Security Consultants, we see different groups of infrastructures like universities and government authorities getting similar spam and threats. We have implemented automated ways to share this information among these clusters. We will introduce the techniques used in our Rspamd implementations and we will point at some pitfalls that should be avoided. We also like to talk about our experience with pre-queue deep threat second stage security analysis like sandboxing.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AWX8SP/feedback/)

---

### TLSRPT comes to Open Source

- **Speakers:** Patrick Ben Koetter
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 14:30 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5776-tlsrpt-comes-to-open-source/)

#### Abstract

My talk will introduce you to TLSRPT and it will show you how to configure Postfix to send TLSRPT datagrams to a TLSRPT report service. TLSRPT is to TLS security what DMARC is to anti-phishing: it allows you not only to establish standards like STARTTLS, MTA-STS or DANE for secure message transport, but to verify via reports those security levels are being uphold.
It allows a sender platform to inform receiving platforms how often a TLS connection from the sender to the recipient had been successful and if not why. It is a major improvement over self-monitoring your MTA service, because it creates - in contrast to self-monitoring - a world-wide view how others „see“ your platform. It allows e.g. to make areas in the network visible, where TLS fails, to investigate and ideally to fix the problem in order to keep communication secure.
Previously the capability to create and send TLSRPT reports had been limited to a few major platforms running their own or a commercial MTA. This will change early 2025. The Postfix MTA will be the first Open Source MTA to implement functionality that permits to send TLSRPT-relevant DATA to a TLSRPT report service. The service will collect the DATA, create a report and pass it on to an MTA for delivery or submit it directly via HTTP.
Postfix’ new feature is the result of a collaborative effort between Wietse Venema, the creator of Postfix, and my company sys4 as we want to foster TLSRPT (also because it hinders German providers to qualify to become BSI approved „Secure E-Mail Platforms“).
We created an Open Source low-level C-library that can be used by any MTA - not only Postfix - and the service required to create TLSRPT reports. Both can be downloaded at github. And we hope many other Open Source projects will use the library and the service to implement TLSRPT reporting in their MTA.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AMH7MQ/feedback/)

---

### DMARCaroni: where do DMARC reports go after they are sent?

- **Speakers:** Vint Leenaars
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 15:00 - 15:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6451-dmarcaroni-where-do-dmarc-reports-go-after-they-are-sent-/)

#### Abstract

In recent years DMARC has become one of the cornerstones of email deliverability. A large part of email is now protected by the combined efforts of SPF, DKIM and DMARC checks. However, the secret weapons of DMARC which are hardly used are its reports. Along with respecting the policy set by an email sender, the recipient also actively acknowledges how many emails have been sent, from which IP addresses and why some of them have been delivered and others not. This reporting is done by providing a xml file inside a zip attached to an email, which makes it rather hard to digest for humans. Imagine what happens if you get such a report every day for every internet domain you, all of your colleagues and anybody spoofing you send emails to...
Obviously this calls for a tool. Interestingly, even though DMARC is almost a decade old, no good FOSS tool was ever developed. This is why DMARCaroni was created: free and open source software (written in Haskell and Elm) to deliver all your DMARC monitoring needs. In this talk I will unveil this new tool which I wrote in the last 18 months, show off its features, and talk about the roadmap.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/93XLVK/feedback/)

---

### Authentication and autoconfig for email - Update on standardization efforts

- **Speakers:** Ben Bucksch
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 16:00 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4888-authentication-and-autoconfig-for-email-update-on-standardization-efforts/)

#### Abstract

The talk shows the status of the standarization efforts for autoconfiguration and 2FA authentication for email, for example based on OAuth2 or Passkeys. It shows the various Draft RFCs discussed at the moment, and the state of their standards efforts.
There are a few strategic choices to be made, and tradeoffs, which give advantage to certain parties, e.g. email providers or email clients or their users. The talk highlights these choices and it might ask the audience for an opinion poll of some of these choices.
https://datatracker.ietf.org/doc/draft-ietf-mailmaint-autoconfig/
https://datatracker.ietf.org/doc/draft-bucksch-mauth/
https://datatracker.ietf.org/doc/draft-jenkins-oauth-public/
https://benbucksch.github.io/sasl-passkey/draft-bucksch-sasl-passkey.html

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NUWDKK/feedback/)

---

### How email addresses are growing to support unicode

- **Speakers:** Arnt Gulbrandsen
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6235-how-email-addresses-are-growing-to-support-unicode/)

#### Abstract

This talk will include a presentation about changes that are happening to email address syntax, as well as recent developments to Unicode email addresses. In addition, IETF and W3C email syntax rules, which are primarily compatible, will be discussed. Both organizations have proposed updates to extend the rules (i.e., via an IETF draft and W3C Github pull request). There'll be brief information regarding the proposed changes, address validation and web browsers/forms and of course implementation progress

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YQ77GY/feedback/)

---

### (Avoid) Implementing STARTTLS

- **Speakers:** Damian Poddebniak
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 17:00 - 17:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4929--avoid-implementing-starttls/)

#### Abstract

I want to keep up my mission to make STARTTLS a technology of the past by recapping on the issues STARTTLS creates and providing advice how to (avoid) implementing (most of) it. The talk will be 5 to 10 minutes and is motivated by my research about real-world STARTTLS issues (https://nostarttls.secvuln.info/) and the implementations I (reluctantly) wrote (https://github.com/duesee/imap-next).

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/A9AJE8/feedback/)

---

### Post-Quantum Cryptography in OpenPGP

- **Speakers:** Daniel Huigens, Aron Wussler
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 17:30 - 18:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5992-post-quantum-cryptography-in-openpgp/)

#### Abstract

Quantum computers that are able to break classical cryptography are generally expected to appear in the coming decades. To prevent encrypted emails from being decryptable by an attacker at that point, we need to start using post-quantum cryptography as soon as feasible.
To that end, we're standardizing the use of post-quantum cryptography in OpenPGP. In addition, for long-term storage and archival, we're standardizing the use of persistent symmetric keys, which allows for more efficient encryption, while still being post-quantum secure as well.
In this talk, we'll present the state of the standardization and implementation efforts, and discuss how the transition might affect applications using OpenPGP, as well as their end users.

#### Related Links

- ["Post-Quantum Cryptography in OpenPGP" draft specification](https://datatracker.ietf.org/doc/draft-ietf-openpgp-pqc/)
- ["Persistent Symmetric Keys in OpenPGP" draft specification](https://datatracker.ietf.org/doc/draft-ietf-openpgp-persistent-symmetric-keys/)
- [Blog post on Post-Quantum Cryptography in OpenPGP and Proton Mail](https://proton.me/blog/post-quantum-encryption)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9N3FAA/feedback/)

---

### Delta Chat, from e-mail messaging to Peer-to-Peer realtime networking

- **Speakers:** Xenia
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 18:00 - 18:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5853-delta-chat-from-e-mail-messaging-to-peer-to-peer-realtime-networking/)

#### Abstract

Over the years, Delta Chat has matured to be an easy-to-use, secure, and even fast messenger for all platforms, based on the massive e-mail server network. We'll give an overview of the ways Delta Chat is used today and how it is developed by a dozen active contributors. This talk will highlight our recent introduction of realtime chat-shared apps that use e-mail OpenPGP-encrypted messaging to establish a private Peer-to-Peer network among chat group members. In this talk we will demonstrate how these apps work in real-time. We'll also report on several interesting situations where Delta Chat is used today in context of partial shutdowns or strict internet censorship.
Description:
In the beginning, Delta Chat was a fun little experiment, an experimental solution to the network effects problem: “nobody uses secure messengers! But everyone has E-Mail… 🤔" Since then it has come a long way. From a cross-platform set of messenger apps with freely chosen e-mail servers to using audited and well analyzed end-to-end encryption, our project is based on IETF and W3C approved protocols and specifications. We interoperate with the massively distributed SMTP e-mail routing network as well as other e-mail based apps or webmailers and socially are in collaborative relations with numerous other projects, including XMPP-based messengers and standardization specialists.
Delta Chat was among the first messengers to adopt Rust (2019) as its core implementation language and provide all-platform apps. Together with XMPP-projects like Cheogram and Monocles we are evolving a new paradigm and quasi-standard called "webxdc" that enables integration of web apps into chat groups, giving users full control over app distribution. Webxdcs provide a unique Peer-to-Peer model for deploying collaborative standards based software.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TS8TXH/feedback/)

---

### Chatmail server networks for anonymous end-to-end encrypted messaging

- **Speakers:** missytake
- **Room:** K.4.601
- **Day:** Saturday
- **Time:** 18:30 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5217-chatmail-server-networks-for-anonymous-end-to-end-encrypted-messaging/)

#### Abstract

In April 2024 Delta Chat introduced "instant onboarding" using chatmail servers leading to several 10K new users-per-day surges in geographies like Somalia, Russia, Mexico, Cuba and the US. There are currently 1-2 new chatmail servers per month and in 2025 we want to cover more of the planet, and will dicuss our plans for "zero-metadata" operations.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-modern-email:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-modern-email:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JPY3PJ/feedback/)

---

## Monitoring and Observability (13)

### Monitoring and Observability Devroom Opening

- **Speakers:** Richard "RichiH" Hartmann
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 09:00 - 09:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6715-monitoring-and-observability-devroom-opening/)

#### Abstract

Devroom opening

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LLHAV9/feedback/)

---

### Discovering the Magic Behind OpenTelemetry Instrumentation

- **Speakers:** Israel Blancas, Jose Gomez-Selles
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 09:10 - 09:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4146-discovering-the-magic-behind-opentelemetry-instrumentation/)

#### Abstract

Instrumentation is the secret ingredient that brings observability to life, revealing the intricate workings of applications in ways logs and metrics alone can’t match. In this talk, we’ll dive deep into the magic of OpenTelemetry instrumentation, exploring how to uncover hidden insights within your applications and services.
Join us as we break down the essentials of OpenTelemetry instrumentation, including setting up automatic instrumentation for popular libraries and frameworks, and crafting custom spans to track the most critical parts of your workflows. You’ll see how simple, well-placed instrumentation points can reveal complex system behaviors, helping you detect bottlenecks, trace errors, and understand end-to-end request flows.
Whether you’re new to observability or looking to master OpenTelemetry, this session will show you how to harness the full potential of instrumentation to transform your data into actionable insights. Discover the power of OpenTelemetry and bring clarity to your observability journey.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/W3URYR/feedback/)

---

### Apache Flink and Prometheus: better together to improve the efficiency of your observability platform at scale

- **Speakers:** Lorenzo Nicora, Hong Teoh
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 09:50 - 10:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5726-apache-flink-and-prometheus-better-together-to-improve-the-efficiency-of-your-observability-platform-at-scale/)

#### Abstract

Prometheus has become the go-to solution for monitoring and alerting, ingesting metrics from applications and infrastructure. The ability to efficiently store high volumes of dimensional time series also makes Prometheus a perfect fit broader operational analytics use cases. Examples are observing fleets of IoT devices, connected vehicles, media streaming devices, and any distributed resources. However, the high cardinality and frequency of events generated by these sources be challenging. Apache Flink can preprocess observability events in real-time before writing to Prometheus. Reducing cardinality or frequency, adding contextual information, calculating derived metrics, will improve the efficiency of your observability platform. In this talk, an Apache Flink committer and the maintainer of the new open source Flink-Prometheus connector, will illustrate potential use cases, key challenges, and how to leverage Flink and Prometheus together to supercharge your observability platform.

#### Related Links

- [Apache Flink Improvement Proposal (FLIP) for the Prometheus Connector](https://cwiki.apache.org/confluence/display/FLINK/FLIP-312%3A+Prometheus+Sink+Connector)
- [Apache Flink Prometheus Connector repository](https://github.com/apache/flink-connector-prometheus)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AECTFF/feedback/)

---

### Prometheus Version 3

- **Speakers:** Jan Fajerski, Bryan Boreham
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6571-prometheus-version-3/)

#### Abstract

Released in November 2024, 3.0 is the first major version of Prometheus in seven years.
Sporting a brand-new user interface, and offering new features such as UTF-8 character support, this release also enabled many small improvements that were previously behind feature flags.
Over 60 contributors worked for hundreds of hours to bring this release to completion. Join us to hear what is new and improved, how you can contribute, and to celebrate this milestone in a legendary Open Source project.

#### Related Links

- [Prometheus project](https://prometheus.io/)
- [Prometheus 3 release notes](https://github.com/prometheus/prometheus/releases/tag/v3.0.0)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DTBJE9/feedback/)

---

### The performance impact of auto-instrumentation

- **Speakers:** James Belchamber
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 11:10 - 11:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5502-the-performance-impact-of-auto-instrumentation/)

#### Abstract

Auto-instrumentation sounds like a free lunch - press buttons, get signals - but nothing is truly free. Auto-instrumentation requires resources just like any other process, and this requirement scales with the application it's automatically instrumenting.
So what's the cost? Well, I can't tell you what it will be in your application, but over the last year or so we’ve been auto-instrumenting quite a lot of code. So let's explore some performance testing experiments to learn more about how much you're paying for that free lunch.
Oh, and what are the benefits? Let me show you that too :)

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/Q7DP3E/feedback/)

---

### Zero-Code Distributed Traces for any programming language

- **Speakers:** Fabian Stäber, Rafael Roquetto
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 11:50 - 12:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5028-zero-code-distributed-traces-for-any-programming-language/)

#### Abstract

We live in a world of many programming languages, even more application development frameworks and many different versions of these technologies. Wouldn’t it be nice if we could automatically get OpenTelemetry distributed tracing to work for all of these applications, in a manner that’s performant, requires zero-code changes, low overhead and doesn’t need maintaining instrumentation support for every single application development framework or version?
We’d like to present two novel approaches of using eBPF to achieve OpenTelemetry trace context propagation across services residing on different nodes, without the need for any external services for trace matching or ordering.
The first approach uses TCP/IP Level 4 embedding of trace context information which works for any protocol, even when encryption is enabled. We’ll show you how metadata can be transmitted and embedded in various parts of the TCP/IP packet to send context to the other side, outside of the application protocol.
The second approach uses TCP/IP Level 7 protocol manipulation to embed the additional trace context information. We’ll show two different Level 7 protocol extension approaches we’ve implemented and describe some of their pros and cons.

#### Related Links

- [Opensource Project](https://github.com/grafana/beyla)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8WMK9D/feedback/)

---

### O11y-in-One: Exploring a Unified Telemetry Database

- **Speakers:** Josh Lee
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 12:30 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5960-o11y-in-one-exploring-a-unified-telemetry-database/)

#### Abstract

OpenTelemetry is often introduced as a way to send your metrics, traces, and logs to separate backend databases. But in reality, most organizations juggle at least half a dozen monitoring tools in production. What we really need isn’t just a standardized way to collect telemetry—it’s a unified datastore that brings all the backends together, much like how OpenTelemetry has unified telemetry collection.
Could ClickHouse be that solution? In this talk, Joshua will dive into the fundamental nature of telemetry and explore what we truly need from a unified telemetry datastore. He’ll break down the specific features of ClickHouse that make it an exceptional choice for tracing and logs today—and hint at its growing potential for time-series data in the future.
From there, he’ll highlight the seamless integrations between ClickHouse and open-source tools like OpenTelemetry, Prometheus, Grafana, and Kafka, showcasing how these technologies work together to enhance observability pipelines. Finally, we’ll take a closer look at cutting-edge, open-source observability platforms built on ClickHouse, including CoRoot, QRYN, and SigNoz.
Whether you’re building a complete observability platform or exploring how to simplify your own observability strategy, this session will equip you with insights into leveraging ClickHouse as a core part of your telemetry infrastructure. Join us to learn how to move beyond fragmented tools and unlock the power of unified observability.

#### Related Links

- [Past Recording](https://www.youtube.com/watch?v=uDY_EsE47sA&t=389s)
- [ClickHouse Homepage](https://clickhouse.com)
- [OpenTelemetry](https://opentelemetry.io)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AJPRCH/feedback/)

---

### Reducing observability cognitive load in KubeVirt

- **Speakers:** João Vilaça
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 13:10 - 13:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4224-reducing-observability-cognitive-load-in-kubevirt/)

#### Abstract

KubeVirt, which provides additional functionality to Kubernetes clusters, to perform virtual machine management, is a large multi-component project that, like many others, grew rapidly with a strong focus on delivering new features. In the beginning, observability was not a priority. Whenever necessary, the developers of each component would add Prometheus instrumentation in their code bases in very different ways.
As the project matured and observability became increasingly more important, we created a dedicated team. By then, there were high levels of intertwined observability and business logic code. It was challenging to keep a mental model of how different teams implemented observability across repositories and difficult to maintain them in sync with new features.
This presentation will outline and demo how we modularized the code and made it more readable, and maintainable. By encapsulating the Prometheus monitoring best practices and the common patterns into a library with a strict interface and using it as a dependency for all KubeVirt components, we reduced code complexity, made it easy to maintain and evolve, and reduced the risk of introducing errors. Our experience will give you a clear path forward on how to clean up and improve observability code in your projects.

#### Related Links

- [KubeVirt GitHub group](https://github.com/kubevirt)
- [Kubernetes Operator Observability Toolkit repository](https://github.com/machadovilaca/operator-observability)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZMBVNF/feedback/)

---

### What Can We Learn from Formula 1 Incident Management

- **Speakers:** Ricardo Castro
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 13:50 - 14:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6599-what-can-we-learn-from-formula-1-incident-management/)

#### Abstract

uly 18th 2020, Max Verstappen qualifies 7th for the Hungarian Grand Prix. With Red Bull fighting Mercedes for the Constructor’s championship and  Max fighting Lewis Hamilton and Vallteri Bottas for the Driver’s Championship, this wasn’t his best qualifying session. 
July 19th 2020, during the formation lap, Max crashed his car, damaging his front wing and suspension. In the next 22 minutes, Red Bull mechanics performed an absolute miracle.
How did they do it? How did they go from a crashed car to giving Max a chance to fight for a podium in under 23 minutes? And what can we learn about incident management from one of the most demanding engineering disciplines in the world?
Key Points

Importance of clear communication: During the incident, the crew communicated effectively to assess the damage, determine the necessary repairs, and track the time remaining.
Technical proficiency at the highest level. F1 is one the most complex engineering disciplines on the face of the Earth. What these people did in under 23min is nothing short of amazing.
Clear processes. Everyone new their place. Everyone knew exactly what they needed to do. Coordination was as close to perfection as it could be.
Clear communication. Clear messages between people (engineers, managers, etc). Zero confusion. Everyone focused on getting the job done.
The calmness on everyone's voice. No shouting. No need to emphasize urgency or pressure on requests. They know people will perform at their best if they're as calm as they possibly can.
Making quick decisions: The team had to rapidly decide whether to attempt a fix on the grid or forfeit Verstappen’s starting position.
Teamwork: The mechanics worked together efficiently to remove and replace damaged parts within a tight timeframe.
Postmortem: Formula 1 team debriefs are brutal but it’s the price to pay for excellence.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VYWQCP/feedback/)

---

### Mastering Observability with SigNoz -> Open-Source Alternative for Metrics, Logs, and Traces

- **Speakers:** Angeles Mora
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 14:30 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6640-mastering-observability-with-signoz-open-source-alternative-for-metrics-logs-and-traces/)

#### Abstract

In today’s increasingly distributed system architectures, observability has become a crucial aspect of maintaining system reliability and performance. SigNoz, an open-source observability platform, offers a seamless and cost-effective alternative to proprietary solutions for managing metrics, logs, and traces.
This talk will introduce SigNoz and its core features, demonstrating how it enables teams to gain deeper insights into their applications' performance. Attendees will learn how SigNoz integrates with popular observability standards like OpenTelemetry, supports advanced queries, and provides robust visualizations for debugging and monitoring modern systems.
By the end of this session, participants will have a clear understanding of how to set up SigNoz, explore real-world use cases, and leverage its capabilities to simplify and enhance observability in their tech stacks.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XUYNF3/feedback/)

---

### The Art of Fleet-Wide Kubernetes Observability: 3 Core Strategies

- **Speakers:** Mitali Bhalla, Pratik Kumar Panda
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 15:10 - 15:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5581-the-art-of-fleet-wide-kubernetes-observability-3-core-strategies/)

#### Abstract

Kubernetes is just magical! The solution and benefits it offers for running large scale applications is hidden from none of us. But, the same strengths in running applications on Kubernetes can be a huge hurdle when monitoring these same deployments.
A single pod can easily expose 25 different metrics, and each container can add another 20 metrics. So, for a minimal single node K8s cluster, even running a minimum of 10 pods can let your metrics volume to 5000 data points. Now imagine, running a multi node cluster in a multi cluster fleet , what a chaos it can be! This brings up a huge challenge of understanding and handling metrics that are actually useful.
It doesn’t really end at just understanding your metrics - How do you set up alerting? How do you correlate this enormous data? How do you develop or adopt the right tooling? 
This talk delves into the art and science of building a robust observability ecosystem tailored for large-scale environments. We'll focus on the key three fundamentals for managing observability at scale without sacrificing performance - Metrics, Alerts and Correlation.
Drawing from our daily experience managing a multi-cluster, complex fleet as SREs at Red Hat, we'll share our approach to effectively collecting and managing metrics, developing alerting strategies, and extracting valuable insights by properly correlating telemetry. These practices help establish a solid foundation for a strategic and robust cluster monitoring system.
Whether you're starting from scratch or optimising your existing setup, these insights will help you build a resilient, scalable observability framework. This session will deepen your understanding of monitoring capabilities and help enhance reliability across your fleet.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZJCRUU/feedback/)

---

### How to monitor the monitoring

- **Speakers:** Roman Khavronenko
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 15:50 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5388-how-to-monitor-the-monitoring/)

#### Abstract

Monitoring serves as a shield against the unknown, providing clarity through the complexity of distributed systems and hardware. However, monitoring itself can become a complex system, posing challenges when it fails.
In this talk, Roman Khavronenko explores the evolution of monitoring practices through numerous support cases encountered with VictoriaMetrics. He investigates Monitoring of Monitoring, engineer-friendly Grafana dashboard creation, alert optimization, and troubleshooting guide compilation.
Join Roman as he navigates through these monitoring-related questions, shedding light on effective strategies for enhancing monitoring practices.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8LAHJ7/feedback/)

---

### From Error to Alert using FOSS-Tools

- **Speakers:** Claudi Grimm
- **Room:** UD2.120 (Chavanne)
- **Day:** Sunday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6576-from-error-to-alert-using-foss-tools/)

#### Abstract

At Jointech, we identified the need for a scalable, multi-tenant capable monitoring stack, which led us to establish a production-ready system utilizing Grafana Mimir and Loki on Kubernetes. In this presentation, we will share best practices for setting up an LGTMA (Loki, Grafana, Tempo, Mimir, Alloy) stack using open-source tools. Mimir will be employed for multi-tenant metric collection, Loki for log aggregation, Alloy as a vendor-neutral metrics collector, and Grafana as the universal visualization tool.
To ensure that our infrastructure is optimal, we use tools such as OpenTofu, Ansible, and Flux. 
By integrating Grafana OnCall with Zammad, we have developed an efficient and scalable on-call solution. This enables our small team of Site Reliability Engineers (SREs) to rest assured while maintaining best-in-class uptime for our customers.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-monitoring:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-monitoring:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WLPBTA/feedback/)

---

## Mozilla (12)

### Mozilla Mythbusters: Separating Fact from Fiction

- **Speakers:** Sylvestre Ledru
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 13:15 - 13:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6199-mozilla-mythbusters-separating-fact-from-fiction/)

#### Abstract

Mozilla has long been a pioneer in the open web, privacy, and innovation, but over the years, myths and misconceptions about the organization have taken root. Is Mozilla just “Firefox”? Are we lagging in technology? What’s the truth about our business model and partnerships?
In this talk, we’ll tackle some of the most common rumors and misunderstandings about Mozilla head-on. From our role in shaping the internet’s future to our initiatives in privacy, AI, and open standards, you’ll gain an insider’s perspective on who we are, what we do, and where we’re headed.
Join us to separate fact from fiction and discover the truth about Mozilla's impact on the web and beyond. Whether you're a long-time supporter or just curious, this talk will challenge your assumptions and provide fresh insights.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mozilla:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mozilla:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/K7AP3P/feedback/)

---

### Mozilla Builders: Working with the OSS community to build the future of AI

- **Speakers:** Stephen Hood
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 13:35 - 13:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5934-mozilla-builders-working-with-the-oss-community-to-build-the-future-of-ai/)

#### Abstract

With AI already transforming how we use computers and the Web, Mozilla believes it's crucial that open source lead the charge. We cannot afford another Internet Explorer situation, where one or a handful of powerful corporations seize control of fundamental technology. Open source AI can and must offer a viable, competitive alternative to closed source commercial offerings.
To help this happen, Mozilla's Builders program sponsors and co-develops projects that advance the state of the art in open source AI. This session will showcase these projects (including Llamafile, sqlite-vec, Web Applets, LocalScore, and others), outline Mozilla's vision for open source AI, and describe how we seek to collaborate with independent developers and the open source community at large.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mozilla:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mozilla:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CHDJZQ/feedback/)

---

### Blueprints by Mozilla.ai - Empowering Devs to Build with Open-Source AI

- **Speakers:** Stefan French, Kostis Saitas Zarkias, David
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 13:55 - 14:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4974-blueprints-by-mozilla-ai-empowering-devs-to-build-with-open-source-ai/)

#### Abstract

Blueprints are customizable workflows that help developers build AI applications using open-source tools and models. Designed for developers without deep ML expertise, each Blueprint walks you through using open-source tools and models to create AI features that can be customized for your project. 
We believe Blueprints can help bring low-level AI innovations, like model quantization, into the hands of more developers, driving broader adoption within the open-source community. In this session, we’ll showcase the Blueprints we’ve created, discuss potential directions going forward, and share ways you can contribute your own expertise to help make open-source the standard for AI application development.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mozilla:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mozilla:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/C3GJS3/feedback/)

---

### ForkServer coming to Firefox on Linux

- **Speakers:** LISSY Alexandre
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 14:10 - 14:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6340-forkserver-coming-to-firefox-on-linux/)

#### Abstract

Firefox evolved over years from a single-process to a multi-process browser and while this brought nice improvements to the processing and latency, creating new processes has a cost both in time and in memory. This talk will introduce the solution that is coming to Linux and has already been enabled by default on Nightly for a few months: ForkServer, a process dedicated to making fork(). We will first go through a quick history of the landscape both in concurrent browsers as well as in previous attempts in Firefox and highlight the general architecture before sharing a few challenges met.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mozilla:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mozilla:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UAH8SA/feedback/)

---

### Community Insights: Best Practices for Open Datasets for LLM training

- **Speakers:** Kasia Odrozek
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 14:25 - 14:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6020-community-insights-best-practices-for-open-datasets-for-llm-training/)

#### Abstract

The landscape of AI training data stands at a critical crossroads. As large language models increasingly shape our digital ecosystem, the methods of data collection and curation have become a complex battleground of legal, ethical, and technical challenges.
Concerns from creators have spurred lawsuits and prompted AI companies to limit transparency about training datasets, undermining accountability, innovation, and research. While using open access or public domain data could address these issues, at the time of writing, no large-scale competitive models trained on such data exist yet due to challenges like unreliable metadata, digitization costs, the “consent crisis,” and the need for legal and technical expertise.
In this talk, we will discuss pioneering community efforts toward creating open and responsible AI training datasets that challenge the current opaque practices of major AI companies and chart a path toward open datasets as part of a larger public AI ecosystem that can address humanity's most pressing needs while distributing control among many stakeholders.
In June 2024, Mozilla and EleutherAI convened 30 open dataset builders from across the field—organizations such as Hugging Face, Pleias, Cohere4AI, LLM360, TogetherAI, and many more—to address these critical issues. Based on the insights from this gathering, we co-created a research paper titled "Towards Best Practices for Open Datasets for LLM Training". This paper outlines the challenges of navigating the production of open datasets and provides practical recommendations for sourcing, processing, governing, and releasing such datasets. These recommendations are rooted in on-the-ground experience and paired with examples of what is already being done. While the paper references OSI's Open Source AI definition, it goes further by outlining possible tiers of openness and offering avenues for more ethical data governance in AI datasets. 
This session will provide an in-depth exploration of the current landscape and its main players, unpacking the legal ambiguities surrounding AI training data and highlighting the critical importance of transparency and governance. We will share a practical roadmap for developing datasets that promote healthy openness, respect people and communities’ broadly defined rights, and advance the field of artificial intelligence from a digital public good perspective, as well as an overview of concrete policy and tech investments that would unlock the ecosystem.
Building a future where AI systems can be trained on openly licensed data that is responsibly curated and governed requires collaboration across legal, technical, and policy domains, and fostering a culture of openness. With this session, we hope to engage you in a discussion around the unique insights into this cutting-edge work and invite you to add your voice to the growing community of responsible open-source AI developers and advocates.

#### Related Links

- [Research Paper "Towards Best Practices for Open Datasets for LLM Training" by Mozilla and EleutherAI](https://arxiv.org/abs/2501.08365)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mozilla:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mozilla:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RN3ZSE/feedback/)

---

### The Firefox AI Platform

- **Speakers:** Tarek Ziadé
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 14:45 - 15:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4236-the-firefox-ai-platform/)

#### Abstract

Learn how the privacy-preserving local inference runtime works in Firefox Desktop, our current use cases and how to create your own features using the Experimental Web Extension API.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mozilla:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mozilla:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/A9JD8U/feedback/)

---

### The most fun you'll ever have dealing with Firefox crashes

- **Speakers:** Gian-Carlo Pascutto
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 15:05 - 15:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6389-the-most-fun-you-ll-ever-have-dealing-with-firefox-crashes/)

#### Abstract

Join us for the most fun you'll ever have dealing with Firefox crashes! We'll embark on a scenic tour through the lands of unexpected shutdowns, exploring how often they happen, why they occur, who suffers from them, and how to make sure that 'who' isn't you. Dive into the technical wizardry behind reporting, collecting, and analyzing these mishaps. We'll also showcase recent advancements in crash analysis and give you a sneak peek at upcoming features you'll wish you'll never need.

#### Related Links

- [Mozilla Firefox](https://github.com/mozilla/gecko-dev)
- [Rust Minidump - crash reporting tooling](https://github.com/rust-minidump)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mozilla:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mozilla:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DPDMDN/feedback/)

---

### An open source project never sleeps: Two decades of MDN

- **Speakers:** Pranshu Khanna
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 15:20 - 15:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5927-an-open-source-project-never-sleeps-two-decades-of-mdn/)

#### Abstract

I’ve grown within an open-source community, and one thing I’ve learned for sure is that managing a popular open-source project is incredibly challenging. Since stepping into my previous role and now at MDN, I’ve gained valuable insights into managing expectations—understanding who you are as an open-source project and how to foster growth both within and beyond it.
Running and growing an open-source project comes with many challenges, and MDN has successfully navigated them for nearly two decades. But what’s next? In this brief session, I’ll provide a status report on what MDN has achieved so far and where we’re headed. With almost 143,000 contributors from diverse backgrounds over our lifetime, we’ve built a community rooted in open principles that guide many aspects of our work.
Join me for a look inside MDN and discover what makes our journey so unique.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mozilla:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mozilla:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AGEG9B/feedback/)

---

### Lumigator: evaluating LLMs made simple

- **Speakers:** Davide Eynard
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 15:40 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5594-lumigator-evaluating-llms-made-simple/)

#### Abstract

Lumigator is a Python application designed for evaluating large language models. It provides an opinionated selection of models and evaluation metrics for specific use-cases (starting with summarization), but it also allows for extension and customization. It is built on an open stack that includes FastAPI and Ray and easily scales from private, self-hosted, local installations to bare metal servers and cloud providers. It can be used via web UI, programmatically with a python SDK, or directly via REST API.
In this talk we will show how Lumigator works, explore its architecture and design choices, and demonstrate how it can be deployed on different infrastructures, extended, and customized to meet your specific needs.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mozilla:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mozilla:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WZESWV/feedback/)

---

### QUIC vs. middleboxes

- **Speakers:** Lars Eggert
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 16:00 - 16:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6261-quic-vs-middleboxes/)

#### Abstract

Well take a look how implementations of the QUIC protocol can harden themselves against middlebox meddling.

#### Related Links

- [Neqo, the Mozilla Firefox implementation of QUIC in Rust](https://github.com/mozilla/neqo)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mozilla:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mozilla:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RAFW3N/feedback/)

---

### State of Firefox Add-ons

- **Speakers:** Simeon Vincent
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 16:15 - 16:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6619-state-of-firefox-add-ons/)

#### Abstract

2024 was a busy year for the Firefox Add-ons group. Attendees may be familiar with browser extension development but not up-to-date on every change across browsers, This talk examine some of the biggest changes that have landed in the past year including improvements to Manifest V3 support, add-on support in Firefox for Android, and a look at some cross-browser extension development patterns that have been unlocked. 
Attendees are encouraged to share feedback on these features with Add-ons team members after the talk and over the course of the event.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mozilla:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mozilla:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RSBPQV/feedback/)

---

### Mozilla Language Portal

- **Speakers:** Matjaž Horvat
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 16:35 - 16:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6145-mozilla-language-portal/)

#### Abstract

Mozilla is developing the Mozilla Language Portal — a centralized platform designed to empower translators and localization professionals worldwide. This innovative hub will integrate Mozilla’s localization technology and serve as a knowledge-sharing space for the global translation community, featuring searchable translation memories, terminologies, comprehensive documentation, best practices, and a dynamic blog space.
Join us to help shape this exciting project and advance the future of software localization!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mozilla:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mozilla:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CBQRWD/feedback/)

---

## MySQL (14)

### Atomic Honeypot: A MySQL Honeypot That Drops Shells

- **Speakers:** Alexander Rubin, Martin Rakhmanov
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 09:00 - 09:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4617-atomic-honeypot-a-mysql-honeypot-that-drops-shells/)

#### Abstract

Meet an attacking MySQL honepot which can “Attack the attackers”. In
2023 we have found a CVE (CVE-2023-21980) in MySQL that allows a rogue
MySQL “server” to attack a client connecting to it; attack meaning RCE
on the client side. Since then we were thinking on how to use it for
good. One obvious application is to create a honeypot which will
attack the attackers. In 2024 we have found another RCE in mysqldump
utility (CVE-2024-21096), so we have created a rogue MySQL server and
weaponized it with a chain of 3 vulnerabilities: 1/ arbitrary file
read 2/ RCE from 2023 (CVE-2023- 21980) 3/ the new RCE
(CVE-2024-21096). With this atomic honeypot we were able to discover 2
new attacks against MySQL server. Using arbitrary file read
vulnerability in MySQL we were able to download and analyze the
attackers' code and then execute an “attack against attackers” using a
chain of exploits.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/B3Y3WZ/feedback/)

---

### MySQL Vector and AI

- **Speakers:** Mattias Jonsson
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 09:35 - 10:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6100-mysql-vector-and-ai/)

#### Abstract

MySQL 9.0.0 introduces a powerful new Vector data type and associated functions, adding possibilities for AI applications to use your existing MySQL database directly, instead of yet another special datastore. This talk will explore how vectors enable similarity comparisons or semantic search functionality within MySQL. We will also dive into how vector based Retrieval Augmented Generation (RAG) can extend Large Language Models (LLMs) by using your domain-specific data already stored in MySQL. We will also have a short comparison of the different Vector implementations in the MySQL ecosystem. By the end of this talk you will understand how MySQL’s vector capabilities can be used for your AI workflows and applications.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TSYEFG/feedback/)

---

### Boosting MySQL with Vector Search: Introducing the MyVector Plugin

- **Speakers:** Alkin Tezuysal, Shankar Iyer
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 10:10 - 10:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4230-boosting-mysql-with-vector-search-introducing-the-myvector-plugin/)

#### Abstract

As the demand for vector databases and Generative AI continues to rise, integrating vector storage and search capabilities into traditional databases has become increasingly important. This session introduces the MyVector Plugin, a project that brings native vector storage and similarity search to MySQL. Unlike PostgreSQL, which offers interfaces for adding new data types and index methods, MySQL lacks such extensibility. However, by utilizing MySQL's server component plugin and UDF, the MyVector Plugin successfully adds a fully functional vector search feature within the existing MySQL + InnoDB infrastructure, eliminating the need for a separate vector database. The session explains the technical aspects of integrating vector support into MySQL, the challenges posed by its architecture, and real-world use cases that showcase the advantages of combining vector search with MySQL's robust features. Attendees will leave with practical insights on how to add vector search capabilities to their MySQL systems.

#### Related Links

- [MyVector Development Repository](https://github.com/p3io/myvector-dev)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HK8RPV/feedback/)

---

### Extending MySQL using components: Password breach check, broadcasting a service call and more..

- **Speakers:** Harin Vadodaria
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 10:45 - 11:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4982-extending-mysql-using-components-password-breach-check-broadcasting-a-service-call-and-more-/)

#### Abstract

MySQL’s component infrastructure provides a powerful way to extend server’s functionality. In this talk we will explore basics of component infrastructure followed by an example component that checks password against haveibeenpwned’s breached password database. We will also explore how a service call can be broadcasted to multiple implementations of a same service to achieve chained execution.

#### Related Links

- [Component to validate password against haveibeenpwned database](https://github.com/harinvadodaria/password_breach_check)
- [Library to broadcast MySQL component service calls](https://github.com/harinvadodaria/libservicebroadcast)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/V3WHEJ/feedback/)

---

### Upgrading to MySQL 8.4 at Booking.com

- **Speakers:** Simon Mudd
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 11:20 - 11:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4711-upgrading-to-mysql-8-4-at-booking-com/)

#### Abstract

A discussion of how we handle upgrades to major new versions of MySQL and the challenges we have to do this at scale.
Upgrading to MySQL 8.4 at Booking.com
- why we want to do this?  why NOT stay on 8.0?
- how to approach the process with a large fleet
- changes around automation and tooling
- testing of the changes and deployment
- compatibility issues
- new features?
- In many ways 8.4 is to allow us to test 9.X  --> Why should we care?

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XM8CBQ/feedback/)

---

### 30 Years of MySQL: Reflections on the Past, Present, and Future

- **Speakers:** Vinicius Grippa
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 11:55 - 12:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5928-30-years-of-mysql-reflections-on-the-past-present-and-future/)

#### Abstract

This session examines MySQL’s journey over the past 30 years, exploring how it has evolved into the most used open-source database. We will review the milestones in its development, key features introduced over time, and the tools that made MySQL a versatile choice for diverse applications.
The talk will cover areas such as backup (e.g., Percona XtraBackup, MyDumper/MyLoader, MySQL Shell utilities), security enhancements (LDAP integration, encryption), and performance optimizations through proxies like ProxySQL and caching solutions such as ReadySet. Clustering technologies like Galera Cluster and InnoDB Cluster will also be discussed for their role in enabling high availability and scalability.
Finally, we’ll conclude with a diagram of the open-source tooling available for MySQL examine recent advancements, and explore MySQL's direction in its upcoming releases. This session aims to provide a balanced perspective on MySQL’s history, current capabilities, and future potential.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JQLUWM/feedback/)

---

### Profiling MySQL from MySQL

- **Speakers:** Frédéric Descamps, Dimitri KRAVTCHUK
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 12:30 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4757-profiling-mysql-from-mysql/)

#### Abstract

Some memory allocator such tcmalloc and jemalloc provides information to profile the memory and sometimes CPU usage of a specific process. External tools are used and are not always very straightforward to use. During this session, we will show how we have hacked MySQL to include the profiling operations directly from the SQL interface.
Find where MySQL is spending time and memory by following this session.

#### Related Links

- [MySQL Source Code](https://github.com/mysql/mysql-server)
- [TCMalloc Source Code](https://github.com/google/tcmalloc)
- [jemalloc Source Code](https://github.com/jemalloc/jemalloc)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JATQA3/feedback/)

---

### What is new in MyRocks - RocksDB storage engine for MySQL

- **Speakers:** Yoshinori Matsunobu
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 13:05 - 13:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5168-what-is-new-in-myrocks-rocksdb-storage-engine-for-mysql/)

#### Abstract

MyRocks is an open source MySQL storage engine on top of RocksDB - a popular Log-Structured Merge Tree database library. We created at Meta in 2015 and since then we expanded use cases. 
Recently we added several interesting new features, and I would like to introduce to the MySQL community about them, and how they work. Notably, the following new features will be covered in the session.

Vector database support with Faiss (https://github.com/facebookresearch/faiss)
Accessing MyRocks tables directly with NoSQL/RPC calls with Thrift (https://github.com/apache/thrift)
User defined timestamp support for stronger consistency

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/S7BSYQ/feedback/)

---

### Routing Guidelines: Unlocking Smarter Query Routing in MySQL Architectures

- **Speakers:** Miguel Araújo
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 13:40 - 14:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5462-routing-guidelines-unlocking-smarter-query-routing-in-mysql-architectures/)

#### Abstract

Routing Guidelines is a new feature that makes query routing in MySQL Architectures more dynamic, flexible, and declarative. It enables rapid adaptation to changes, tailored routing for specific application needs, and seamless query distribution in MySQL InnoDB Cluster, ClusterSet, and ReplicaSet topologies. This talk introduces the concept and its technical details, offering practical insights and examples to give attendees a solid understanding of how Routing Guidelines enable smarter, scalable, and more resilient MySQL Database Architectures.

#### Related Links

- [MySQL Shell](https://github.com/mysql/mysql-shell)
- [MySQL Router](https://github.com/mysql/mysql-server/tree/trunk/router)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QRAAUW/feedback/)

---

### MySQL Network Protocol: A walkthrough

- **Speakers:** Daniël van Eeden
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 14:15 - 14:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4956-mysql-network-protocol-a-walkthrough/)

#### Abstract

This walkthrough gives you an idea about how the network protocol that MySQL uses functions.

Authentication: mysql_native_password, caching_sha2_password and more
Secure connections with TLS
Queries, Resultsets and Prepared statements
Compression with zlib and zstd
Connection attributes
Replication

This is based on work I have done on the MySQL protocol dissector in Wireshark

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GY9NFC/feedback/)

---

### schemadiff: in memory schema analysis, validation, normalization, diffing, and manipulation

- **Speakers:** Shlomi Noach
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 14:50 - 15:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4921-schemadiff-in-memory-schema-analysis-validation-normalization-diffing-and-manipulation/)

#### Abstract

schemadiff is a library within the Vitess project, which uses a programmatic approach to analyzing database schemas independently of a MySQL server. schemadiff powers Vitess' own internal schema management as well as the user facing Online DDL logic. In this session we take a deep dive into schemadiff's capabilities, and show how the community can use it to solve very common schema change and schema management tasks and problems. We discuss:

Parsing.
Per table and per database validations.
Normalization.
Diffing tables, diffing databases.
Schema change conflicts and dependencies.
Generating a successful sequential migration route.
In-memory schema manipulation.
Performance.
Extras: INSTANT DDL, Online DDL support, constraint analysis.

schemadiff is part of Vitess, a CNCF project released under the Apache 2 license. We illustrate some real-world scenarios from PlanetScale's (main sponsors of the Vitess project) schema deployment system.

#### Related Links

- [Vitess project page](https://github.com/vitessio/vitess)
- [Vitess documentation](https://vitess.io/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/E3NXNA/feedback/)

---

### The past, present and future of EXPLAIN

- **Speakers:** Norvald H. Ryeng
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 15:25 - 15:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5466-the-past-present-and-future-of-explain/)

#### Abstract

The EXPLAIN statement has been extended with a number of features the last years, both in MySQL 8.4 LTS and 9.x innovation releases. Some features are useful for scripts and tools, while others are more aimed at human users trying to understand the query plans. In this talk we'll go through it all and explain the direction of EXPLAIN development.

#### Related Links

- [MySQL](https://www.mysql.com/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VQPKZL/feedback/)

---

### Open-source support for JS stored programs in Percona Server

- **Speakers:** Dmitry Lenev
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 16:00 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4814-open-source-support-for-js-stored-programs-in-percona-server/)

#### Abstract

Support for stored programs written in JavaScript (often abbreviated
as JS) was added by Oracle to MySQL version 9.0. Unfortunately, this 
feature is only available in MySQL Enterprise Edition and not in 
Community version of MySQL.
Percona is working on an alternative, free and open-source implementation
of JS stored programs for its Percona Server for MySQL, based on widely 
used V8 engine (the latest version of code is available on Percona's GitHub
at https://github.com/percona/percona-server/tree/js-lang).
This talk will provide an overview of this alternative implementation.
We will discuss what features are supported, what are the limitations
and how this implementation is different from the one from Upstream.
We will also talk about performance results for this implementation, some
interesting implementation details and challenges we encountered while
working on it.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BB9ZAP/feedback/)

---

### MySQL InnoDB Data Recovery - the last resort

- **Speakers:** Frédéric Descamps
- **Room:** H.1301 (Cornil)
- **Day:** Sunday
- **Time:** 16:35 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4728-mysql-innodb-data-recovery-the-last-resort/)

#### Abstract

If you decide to live with the wildlife and never take backups of your MySQL, what happens when you delete idb files and realize you lost your data? 
In this session, we will see how InnoDB Data recovery can be done in 2025 and we will create our swiss army knife to realize this operation that was still very complex 10 years ago.

#### Related Links

- [ibsdi](https://github.com/mysql/mysql-server)
- [sdi2dll](https://github.com/altmannmarcelo/sdi2ddl)
- [innodb_sort](https://github.com/YukiHinana/innodb_sort)
- [MySQL Shell](https://github.com/mysql/mysql-shell)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mysql:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mysql:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HVL8XP/feedback/)

---

## Network (21)

### Fast UDP makes QUIC quicker - optimizing Firefox’s HTTP3 IO stack

- **Speakers:** Max Inden
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 09:00 - 09:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5449-fast-udp-makes-quic-quicker-optimizing-firefox-s-http3-io-stack/)

#### Abstract

QUIC is a new transport protocol on top of UDP, transporting a large portion of the Internet traffic today. UDP I/O performance is crucial for QUIC implementations, where e.g. system call overhead can significantly impact throughput at high network speeds. To improve QUIC throughput, Firefox is switching to a modern UDP IO stack in Rust, using mechanisms like recvmmsg, and GRO across Linux, Windows, and Android.
This talk gives a high level overview of Firefox’s HTTP3 / QUIC / UDP stack, followed by a deep dive into the various performance improvements landing in Firefox. Learn how we are making Firefox even faster and how you too can leverage these techniques to optimize your application.

#### Related Links

- [Firefox's HTTP3 / QUIC implementation](https://github.com/mozilla/neqo)
- [Rust UDP library](https://github.com/quinn-rs/quinn/tree/main/quinn-udp)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YNJQWA/feedback/)

---

### Building Peer-to-Peer QUIC

- **Speakers:** Floris Bruynooghe
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 09:25 - 09:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6053-building-peer-to-peer-quic/)

#### Abstract

QUIC is a network protocol with several interesting properties, like
cheap independent ordered streams without head-of-line blocking,
client connection migration or its datagram extension.  Another
interesting property is that it uses UDP as transport, making it very
appealing for NAT traversal.  To make a reliable p2p system out of
QUIC we add a few more components: a relay server which doubles as a
holepunching coordination server, a QUIC address discovery extension
draft [0], the Multipath QUIC draft [1], a QUIC NAT traveral extension
draft [2] and ed25519 keys for identity.
This talk will describe how to make a coherent p2p QUIC networking
stack out of all those components.  This is essentially topology the
iroh [3] project is providing, and is evolving its internal
architecture towards.
[0] https://datatracker.ietf.org/doc/draft-seemann-quic-address-discovery/
[1] https://datatracker.ietf.org/doc/draft-lmbdhk-quic-multipath/
[2] https://datatracker.ietf.org/doc/draft-seemann-quic-nat-traversal/
[3] https://iroh.computer

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ANBUES/feedback/)

---

### ProxyGuard - WireGuard behind a reverse proxy

- **Speakers:** Jeroen Wijenbergh
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 09:50 - 10:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4629-proxyguard-wireguard-behind-a-reverse-proxy/)

#### Abstract

WireGuard is a great protocol to set up a virtual private network (VPN). However, the challenge is to make it work on networks that block or mangle user datagram protocol (UDP) traffic. Certain hotspots, such as those at hotels, events, cafes & restaurants block UDP traffic and only allow web traffic over the transmission control protocol (TCP) usually port 80/443. Even if a network allows UDP traffic, there can be issues with certain packets not going through due to issues regarding maximum transmission units (MTU).
Supporting TCP is left explicitly out of scope for the WireGuard project and should be handled by an upper layer obfuscation tool [1]. There is a good reason for this: TCP-over-TCP has bad performance (e.g. website traffic over a TCP VPN). However, in these networks the choice has to be made between no VPN connectivity or at least something as a fallback. For this reason, there are some tools which aim to proxy UDP packets over TCP.
Many of these tools, however, do not directly allow you to put it behind a reverse proxy. The advantage of using a reverse proxy is that you can use your existing web server to (next to tunneling it over TCP) obfuscate the traffic with TLS and tunnel your WireGuard traffic through the same port that is serving normal websites. In this talk, I will introduce a tool called ProxyGuard which aims to solve this use case. I explain why I came up with this approach in the first place, what challenges I had implementing it and possible improvements for the future. The project homepage is at: https://codeberg.org/eduvpn/proxyguard
1: https://www.wireguard.com/known-limitations/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RMKP9H/feedback/)

---

### Unleashing SuperNIC's Superpowers

- **Speakers:** Alfredo Cardigliano
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 10:15 - 10:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5559-unleashing-supernic-s-superpowers/)

#### Abstract

In the ever-evolving landscape of network traffic monitoring and processing, the need for high-performance, flexible, and scalable solutions is critical. This talk explores how BlueField DPU-based SuperNICs, coupled with NVIDIA's DOCA Flow framework, offer a powerful platform for achieving these goals. We will delve into the architecture and capabilities of BlueField SmartNICs, demonstrating their potential (and limitations) when offloading tasks such as network traffic processing, inline security applications, traffic shaping. Shifting these workloads to the adapter is desirable as it frees up host resources, and enables more efficient and scalable network operations. Attendees will gain insights into the practical deployment of BlueField DPUs in modern network infrastructures and learn best practices for leveraging DOCA Flow to optimize network observability and control.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BW7WTB/feedback/)

---

### Passive Network Traffic Fingerprinting

- **Speakers:** Luca Deri
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 10:40 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5461-passive-network-traffic-fingerprinting/)

#### Abstract

Understanding network traffic fingerprints is crucial for enhancing cybersecurity and network performance. This talk concisely explores passive network traffic fingerprints, discussing their definition, identification methods, and practical applications. We will cover techniques including deep packet inspection and flow analysis to capture and analyze traffic patterns. Real-world examples based on nDPI, an open-source DPI toolkit, will illustrate their use in intrusion detection, anomaly detection, and network monitoring, as well as other open-source tools such as Wireshark and Suricata.

#### Related Links

- [nDPI Source Code](https://github.com/ntop/nDPI)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LEFAJN/feedback/)

---

### Every ISP Needs To Use A QoE Middle-Box On Their Network

- **Speakers:** Frantisek (Frank) Borsik_LibreQoS
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 11:05 - 11:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6051-every-isp-needs-to-use-a-qoe-middle-box-on-their-network/)

#### Abstract

Every Internet Service Provider on the face of the Earth needs to use a Quality of Experience middle-box on their network. A middle-box gives you visibility into your network: latency, jitter and bufferbloat only become apparent when you look. Spot congestion and latency spikes at every level of the network. A middle-box gives you proactive monitoring: identify the customers who are having problems before they call you. And most importantly, a middle-box gets rid of support calls. By actively managing bufferbloat, enhancing perceived latency and proactively pacing packets you can immediately improve your customers’ quality of experience. In our experience, this massively reduces the volume of support calls-and costs to service them. A Quality of Experience middle-box allows also for more aggressive but safer over-subscription rate. PS: Bandwidth is a lie.

#### Related Links

- [LibreQoS GitHub](https://github.com/LibreQoE/LibreQoS)
- [LibreQoS website](https://libreqos.io)
- [LibreQoS chat (Zulip)](https://chat.libreqos.io/join/fvu3cerayyaumo377xwvpev6/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/J33EB9/feedback/)

---

### grout # a graph router based on DPDK

- **Speakers:** Robin Jarry
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 11:30 - 11:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4083-grout-a-graph-router-based-on-dpdk/)

#### Abstract

grout stands for Graph Router. It is a DPDK based network processing application. It uses the rte_graph library for data path processing. It was recently accepted as a hosted project on dpdk.org.
Its main purpose is to simulate a network function or a physical router for testing/replicating real (usually closed source) VNF/CNF behavior with an opensource tool.
It comes with a client API to configure it over a standard UNIX socket and a CLI that uses that API. The CLI can be used as an interactive shell, but also in scripts one command at a time, or by batches.
This talk will present the project and my journey with writing a DPDK application from scratch using rte_graph. I will also make some demonstrations of its capabilities and performance.
Project link: https://github.com/DPDK/grout

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RWAAZD/feedback/)

---

### Unleashing 100 Mpps with FD.io VPP on GCP

- **Speakers:** Federico Iezzi, Jerome Tollet
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 11:55 - 12:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4774-unleashing-100-mpps-with-fd-io-vpp-on-gcp/)

#### Abstract

This session delves into the high-performance world of Telco packet processing. We'll explore foundational technologies like DPDK, system partitioning, and deterministic setups, showcasing how they enable lightning-fast network processing. Moving beyond theory, we’ll present a practical case featuring FD.io VPP, a standout example of a high-performance network function, and demonstrate how GCP and the Titanium architecture provide the infrastructure needed to build and deploy efficient, scalable, and robust Telco solutions-pushing the boundaries beyond 100 Mpps on commodity shared infrastructure.

#### Related Links

- [FD.io Vector Packet Processor](https://fd.io/)
- [Data Plane Development Kit](https://www.dpdk.org/)
- [Tuning Profile Delivery Mechanism for Linux](https://github.com/redhat-performance/tuned)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SEMY9H/feedback/)

---

### Levitation made handy: roll your own Maglev LB with VPP !

- **Speakers:** Nathan Skrzypczak
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 12:15 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5546-levitation-made-handy-roll-your-own-maglev-lb-with-vpp-/)

#### Abstract

Horizontal scaling is nice, but keeping state is not. Enters Maglev [0] 
that offers the best of both worlds ! But one does not get to run it 
without a fair supply of pain killers.
This talk claims otherwise !
We will cover how Malgev works, why it makes sense to use it, 
how to write a simple VPP [1] agent, and make run it on commodity hardware.
Packets will fly !
[0] https://research.google/pubs/maglev-a-fast-and-reliable-software-network-load-balancer/ 
[1] https://fd.io/technology/

#### Related Links

- [FD.io website](https://fd.io/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7WNNTV/feedback/)

---

### VPP: Monitoring 100Gbps+ with sFlow

- **Speakers:** Pim van Pelt
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 12:35 - 12:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4196-vpp-monitoring-100gbps-with-sflow/)

#### Abstract

This talk describes the author's work on an sFlow plugin for a popular userspace dataplane called VPP], and how it can be used to do statistical packet sampling with very high rates using the sFlow protocol.
An integration with ntopng and Akvorado will be demonstrated.

#### Related Links

- [Github repo](https://github.com/sflow/vpp-sflow)
- [VPP repo](https://gerrit.fd.io/r/q/status:open+-is:wip+repo:vpp)
- [Article about VPP and sFlow](https://ipng.ch/s/articles/2024/09/08/vpp-with-sflow-part-1/)
- [Article about VPP sFlow performance](https://ipng.ch/s/articles/2024/10/06/vpp-with-sflow-part-2/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SCEFD7/feedback/)

---

### VPP TLS Plugin: Enhancing Performance with Asynchronous Operations

- **Speakers:** Varun Rapelly, Venkata Ravichandra Mynidi
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 12:50 - 13:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5565-vpp-tls-plugin-enhancing-performance-with-asynchronous-operations/)

#### Abstract

VPP TLS Plugin: Performance Enhancement With User Space Processing & Pipeline Support
The FD.io Vector Packet Processing (VPP) TLS plugin enhances performance through asynchronous, non-blocking operations. 
By utilizing DPDK user space crypto drivers and the OpenSSL Engine framework, TLS crypto operations are asynchronously submitted to hardware, ensuring that the entire TLS processing occurs in user space. With EVP pipeline support, the DPDK crypto driver allows enqueueing of multiple TLS packets for encryption/decryption, leveraging DPDK burst APIs. Enhanced queue management further boosts efficiency.
Key Features:
Engine Registration: Supports multiple engines with specific algorithms for asynchronous operations.
User Space Driver: Uses DPDK and OpenSSL Engine for hardware-offloaded, user space TLS processing.
Event Handling: Employs an event-driven model for dynamic event management.
Polling Mechanism: Monitors asynchronous operations with dedicated polling functions.
Callback Functions: Handles completion of TLS operations efficiently.
Queue Management: Separates handshake requests from read/write events, reducing contention and improving throughput and latency.
Advantages:
Reduced Contention: Separate queues for different operations enhance smooth processing.
Increased Throughput: Parallel processing of operations boosts the number of TLS operations per second.
Lower Latency: Faster processing of time-sensitive handshake operations.
These improvements make the VPP TLS plugin a robust solution for high-throughput, low-latency network environments.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TTRRV7/feedback/)

---

### Scitags: network traffic tagging for scientific computing

- **Speakers:** Luca Bassi
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 13:10 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6182-scitags-network-traffic-tagging-for-scientific-computing/)

#### Abstract

Scientific research communities move very large volumes of experimental data between large and small international sites, using connectivity provided by National Research and Education Networks (NRENs).
NRENs are therefore particularly interested in understanding how their networks are used by which scientific activities to make informed decisions on how to scale their infrastructures.
This talk introduces Scientific Network Tags (scitags), an initiative promoting identification of the science domains and their high-level activities at the network level.
Scitags provides Network Flow and Packet Marking that can be captured by NRENs to better understand existing network patterns, estimate network usage and track activities.
Network packet marking uses UDP "firefly" packets, whereas flow marking uses the flow label in the IPv6 header.
Scitags is an open source framework developed by the Research Networking Technical Working Group (RNTWG) of the Worldwide LHC Computing Grid (WLCG) community; it is aimed at high-energy physics experiments, but is easily applicable to other scientific communities.
The presentation also demonstrates the usage of flowd, a daemon that has different plugins to retrieve flow identifier and a set of backend to mark the traffic, to add Scitags support to an actual data transfer service (StoRM WebDAV).

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LBFVE9/feedback/)

---

### Securing the Internal Control Plane with Standards & OSS

- **Speakers:** Antonios Chariton
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 13:30 - 13:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4653-securing-the-internal-control-plane-with-standards-oss/)

#### Abstract

There's a lot of work being done to increase routing security on the Internet today using standards such as RPKI and other solutions like IRR, PeeringDB, and so on. It's a difficult problem, and it will take time to solve this. But what about the internal network? Operators and enterprises have networks spanning countries, continents, or the entire world, and at this point they are running into the same issues.
In this talk I am using OSS and open standards to showcase a Free solution anyone can use to protect their IGP with state of the art routing security practices, as well as the pros and cons that come with it.

#### Related Links

- [bird2](https://gitlab.nic.cz/labs/bird)
- [krill](https://github.com/NLnetLabs/krill)
- [routinator](https://github.com/NLnetLabs/routinator)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NVJBT8/feedback/)

---

### Suricata: Insights, Innovations, and Future Directions

- **Speakers:** Victor Julien
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 13:55 - 14:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6717-suricata-insights-innovations-and-future-directions/)

#### Abstract

Since 2009, Suricata has evolved from a groundbreaking intrusion detection and prevention engine into a versatile, community-driven network security platform. In this talk, Suricata's founder and lead developer, Victor Julien, will share the technical journey of Suricata—from its origins as a high-performance IDS/IPS/NSM solution to its pivotal role in addressing today’s complex network security challenges.
Victor will also unveil the current roadmap and explore key innovations shaping the future of Suricata, such as multi-threading, advanced protocol parsing, and deep packet inspection—technologies that have solidified its position at the forefront of open-source security. Throughout, we’ll spotlight the invaluable contributions of the global open-source community, whose collaborative efforts continue to drive the project forward.
Whether you're new to Suricata or a seasoned contributor, join us for a technical deep dive and an engaging conversation about the past, present, and exciting future of this powerful open-source tool.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DWZF8F/feedback/)

---

### Wiresharchaeology: How it started and where we're headed

- **Speakers:** Gerald Combs
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 14:15 - 14:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6726-wiresharchaeology-how-it-started-and-where-we-re-headed/)

#### Abstract

Wireshark started out as a tool that supported a handful of protocols and two operating systems. Over the years we have adapted our code, infrastructure, and sponsorship model to match the needs of our user and developer communities, and Wireshark is now used by millions of people around the world to keep their networks fast, reliable, and secure.
In this talk Gerald Combs, the project's creator and lead developer will cover the history of Wireshark, lessons learned along the way, and discuss possible future directions.

#### Related Links

- [Wireshark web site](https://www.wireshark.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BLPGE9/feedback/)

---

### Cloud-Native Networking, Home Edition: Build and connect your VPCs with the Open Network Fabric

- **Speakers:** Quentin Monnet
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 14:40 - 14:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6286-cloud-native-networking-home-edition-build-and-connect-your-vpcs-with-the-open-network-fabric/)

#### Abstract

In a Cloud-Native world, you eat Kubernetes Services at breakfast, you go through the morning one YAML object at a time, and by the end of the afternoon you've spun clusters by the dozen. Juggling with public cloud resources such as AWS or GKE is a second nature for you. But here's the thing: you realized that your bill would be much smaller over time if you could run your workflows on your own hardware. Maybe you even have requirements for low latency that can't be addressed by external providers. Say you've bought your commodity switches, new servers, perhaps some GPUs. It's great! But now... what? How, exactly, do you turn these into a cloud infrastructure similar to what you'd get from the large providers?
Time to turn to the Open Network Fabric. This is an open-source, vendor-agnostic project, that aims at bringing the user experience from public cloud providers to private environment. It provides tooling and automation around SONiC, an open-source network operating system based on Linux that runs on switches. The Open Network Fabric is built around the concept of Virtual Private Clouds (VPCs) and provides a multi-tenant API to define the user intent on network isolation and connectivity, which is automatically transformed into configuration for switches and software appliances. It also leverages the Kubernetes APIs: all user-facing APIs are Kubernetes Custom Resources (CRDs), so one can use standard Kubernetes tools to manage resources such as VPCs, network attachments, and even switches and servers.
This talk is an introduction to the Open Network Fabric, with a high overview of the different components and on how to use it to set up a VPC. After presenting the current state of the project, we'll also take a look at a few roadmap items for the associated DPDK-based Gateway, currently at an early stage of development.
Bring back the Cloud to your home (or lab): compute on the edge, connect your endpoints and VPCs with the Open Network Fabric. And if you feel like it, join the project!

#### Related Links

- [Open Network Fabric documentation](https://docs.githedgehog.com)
- [Hedgehog (the company behind the project) presents at Networking Field Day #35](https://techfieldday.com/appearance/hedgehog-presents-at-networking-field-day-35/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YN3NGB/feedback/)

---

### Kubenet: Harnessing Kubernetes for Network Automation

- **Speakers:** Wim Henderickx
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 15:00 - 15:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5141-kubenet-harnessing-kubernetes-for-network-automation/)

#### Abstract

Join us for an engaging session on Kubenet, a community-driven initiative designed to explore the untapped potential of Kubernetes as a robust automation and orchestration platform for network systems. While Kubernetes has revolutionized container orchestration, its capabilities extend far beyond, offering powerful tools to automate and manage physical, virtual, and containerized Network Operating Systems (NOS). This talk will highlight how network engineers can leverage Kubernetes to simplify, standardize, and scale network automation.
We’ll discuss the motivations behind Kubenet, its architecture, and its practical applications in diverse networking scenarios such as datacenter networking, WAN, peering, campus networking, and cloud environments. Core topics include:
    •   Abstraction: Simplify and standardize network management with Kubernetes’ abstraction capabilities.
    •   API-First Approach: Leverage Kubernetes’ vendor-agnostic and vendor-specific APIs to create programmable, flexible automation pipelines.
    •   Desired State and Source of Truth (SOT): Use Kubernetes’ declarative model to define and maintain the desired state of network configurations.
    •   Event-Driven Framework: Harness Kubernetes’ event-driven architecture for responsive and real-time network management.
    •   Reconciliation Loop and Drift Detection: Ensure consistent alignment with desired configurations and quickly detect and remediate drift.
    •   Vendor Plugins and Extensions: Integrate a wide range of tools and services through Kubernetes’ extensibility.
    •   GitOps Principles: Adopt collaborative, version-controlled workflows for change and lifecycle management.
This session will also introduce open-source extensions developed by the Kubenet community, designed to tackle real-world networking challenges across Day-0, Day-1, and Day-2 operations.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GCWNGE/feedback/)

---

### Evolving Multi-Network in Kubernetes: From Pod Spec to Dynamic Resource Allocation

- **Speakers:** Miguel Duarte, Doug Smith
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 15:25 - 15:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4510-evolving-multi-network-in-kubernetes-from-pod-spec-to-dynamic-resource-allocation/)

#### Abstract

At last year's FOSDEM, Doug and Miguel presented about upcoming efforts to improve networking APIs in Kubernetes, such as the work done by the SIG-Network Multinetworking Working Group, and efforts to evolve CNI, and... Most of them have been blown out of the water.
How Networking in Kubernetes will work is changing directions rapidly, driven in part by the evolution of dynamic resource allocation (DRA). We're here to draw the map of where the community is going, and to help guide you through the naval mines that might lurk beneath the surface for your implementations and cluster configurations.
Key points we'll cover:
- Recap of the multi-network challenge and last year's proposed solution
- Introduction to Dynamic Resource Allocation (DRA) and its applicability to multi-network scenarios
- Deep dive into KEP-4817, which proposes enriching the Resource Claim Status with standardized network interface data
- Comparison of the DRA approach with previous solutions like Multus CNI
- Practical implications for developers and operators looking to implement multi-network solutions
- Discussion on the future of multi-network in Kubernetes and potential next steps
We'll also share insights on the community collaboration process, highlighting how feedback and consensus-building have shaped the current direction. We'll unpack what went right, what got torpedoed, and what it means for the future for Kubernetes native multi-networking, and how to move the several adjacent communities (CNI, NPWG, device management, kubernetes sig-network) forward.
Join us to learn about the latest developments in Kubernetes networking and participate in shaping the future of multi-network support in cloud-native environments.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VPFHYT/feedback/)

---

### Running an EVPN Endpoint in a Kubernetes Cluster—On My Laptop!

- **Speakers:** Federico Paolinelli
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 15:50 - 16:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5246-running-an-evpn-endpoint-in-a-kubernetes-cluster-on-my-laptop-/)

#### Abstract

In this session, I will share my journey in prototyping and implementing an EVPN termination solution using Kubernetes, all on a single laptop. Leveraging tools like Kind and Containerlab, we’ll start with a basic EVPN example and progressively build toward a more complex spine-leaf topology integrated with a Kubernetes cluster. Finally, I will present a live demo, showcasing the solution in action and proving how easy it is to test and implement complex network topologies with Containerlab and Kind.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UXADW8/feedback/)

---

### LFEnergy SEAPATH - svtrace Tools for Latency Analysis in Virtualized Networking Platforms

- **Speakers:** Paul Le Guen de Kerneizon
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 16:15 - 16:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5521-lfenergy-seapath-svtrace-tools-for-latency-analysis-in-virtualized-networking-platforms/)

#### Abstract

In virtualized networking environments, understanding frame latency is essential to ensure performance and reliability. svtrace and svtrace-ansible are specialized tools designed to compute the latencies of network frames, particularly within virtualized infrastructures. Leveraging eBPF (via bpftrace), these tools offer precise measurements of frame transit times between virtual machines, hypervisors, and physical interfaces, providing critical insights into the behavior of virtualized systems.
This presentation will showcase how svtrace tools are used to analyze latency in real-time, streamlining performance diagnostics for developers working on networked applications.
These tools are part of the SEAPATH project, a virtualization platform developed under LF Energy. 
SEAPATH focuses on creating open-source solutions for high-reliability and real-time automation systems, providing the foundation for next-generation virtualized environments.

#### Related Links

- [svtrace repository (L2 network latency on a single machine, from arrival of packets in host to arrival in VM)](https://github.com/seapath/svtrace)
- [svtrace-ansible repository (L2 network across many machines, using Ansible as orchestrator)](https://github.com/seapath/svtrace-ansible)
- [The LFEnergy SEAPATH project](https://lfenergy.org/projects/seapath/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YKPGHC/feedback/)

---

### Performing link aggregation balance-slb in kernelspace with NetworkManager

- **Speakers:** Fernando Fernandez Mancera
- **Room:** UA2.114 (Baudoux)
- **Day:** Sunday
- **Time:** 16:40 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4936-performing-link-aggregation-balance-slb-in-kernelspace-with-networkmanager/)

#### Abstract

Link aggregation is a widespread mechanism in networks. The linux kernel bond driver currently supports 7 different modes. However, Source Load Balancing (balance-slb) is only supported by OpenvSwitch. SLB bonding allows load balancing without remote switch's knowledge or cooperation. SLB assigns each source MAC+VLAN pair to a link and transmits all packets from that MAC+VLAN through that link. Now this is also available on kernelspace by a combination of nftables rules and kernel bonding configuration, all automated through NetworkManager balance-slb option.
On this talk, we will explore how SLB balancing works and how it was implemented by using nftables and kernel bond driver. In addition, we will explore scenarios where this is useful and some known problems.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-network:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-network:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/V8X8DV/feedback/)

---

## Nix and NixOS (10)

### Welcome to the Nix and NixOS devroom!

- **Speakers:** Paul Meyer, Bryan Honof, Thomas Bereknyei
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 10:30 - 10:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4186-welcome-to-the-nix-and-nixos-devroom-/)

#### Abstract

This lightning-style talk will serve as a welcome and introduction to the Nix and NixOS devroom. It'll go over the rules and expectations of the devroom, as well as introducing you to the devroom managers.

#### Related Links

- [NixOS Homepage](https://nixos.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-nix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-nix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9TCX7H/feedback/)

---

### NixOS @ Doctors Without Borders (MSF) - why we use it and how

- **Speakers:** Ian Sollars, Sohel Sarder & Ramses de Norre, Sohel Sarder
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 10:45 - 11:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5165-nixos-doctors-without-borders-msf-why-we-use-it-and-how/)

#### Abstract

We present a real-world use-case of NixOS to manage an highly distributed fleet of servers & VMs in low-resource settings used for mission critical applications. After a brief overview of who MSF is and what we do, we'll dive into the technical details of how we manage our fleet with NixOS and the unique strengths that NixOS brings to the table.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-nix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-nix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EST8SM/feedback/)

---

### How reproducible is NixOS?

- **Speakers:** Julien Malka
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 11:10 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4430-how-reproducible-is-nixos-/)

#### Abstract

Bitwise reproducibility is recognized as a promising way to increase trust in the distribution phase
of binary artifact and hence increase trust in the software supply chain. But how reproducible is Nixpkgs? We know that the NixOS ISO image is very close to be perfectly reproducible thanks to reproducible.nixos.org, but there doesn't exist any monitoring of Nixpkgs as a whole. In this talk I'll present the findings of a project that evaluated the reproducibility of Nixpkgs as a whole by mass rebuilding packages from revisions between 2017 and 2023 and comparing the results with the NixOS cache.
See for reference: https://luj.fr/blog/is-nixos-truly-reproducible.html

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-nix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-nix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FY8ABL/feedback/)

---

### Six months with Nix & devenv and counting

- **Speakers:** José Miguel Martínez Carrasco
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 11:35 - 11:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5732-six-months-with-nix-devenv-and-counting/)

#### Abstract

On this talk I present my experience introducing Nix, home-manager, darwin-nix and devenv in a project where most team members use a macbook but we spend quite some time on Linux too.
A declarative configuration
- that does not interfere with OSX and company provided tooling
- that can be shared with team members to be used with minimum changes
- that keeps a working environment on every iteration
- that really boosts productivity
adding devenv to the mix 
- so people with no exposure to nix feel comfortable
- so developers have an almost identical setup
- so complexity is hiden using processes and services instead of customised containers and scripts
Unfortunately some pain points too 
- as it was impossible to replicate workflows Linux users were used to
- not all available packages can be installed 
After this six months experience, this combination is highly recommendable for all projects aiming to enjoy the good parts and some to polish edges I have seen.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-nix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-nix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RC9BKJ/feedback/)

---

### Building an LTE router with a $60 (new!) laptop and a single file

- **Speakers:** Colin Dean
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 12:00 - 12:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6437-building-an-lte-router-with-a-60-new-laptop-and-a-single-file/)

#### Abstract

With zero experience with NixOS, I grabbed an unused $60 LTE-enabled laptop bought in a fire sale during the pandemic and an LTE SIM card to build a router for my newly purchased home so I could have the minimal Internet necessary for its security system and home automation without having to record what I did in case the laptop died.
I did this in a few hours with less than 100 lines of Nix. I did not think that it would be this easy. It served my Internet needs for several months without failure.
This talk will cover some hijinks of NixOS, using LTE for home internet somewhere you don't yet live, and the joy of things that Just Work... when they work.

#### Related Links

- [Slide sources](https://github.com/colindean/talks/tree/master/nixos_cellular_router)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-nix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-nix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8ZDSA7/feedback/)

---

### Remote Execution with Buck2 and Nix

- **Speakers:** Claudio Bley
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 12:25 - 12:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5710-remote-execution-with-buck2-and-nix/)

#### Abstract

In this talk, I will present how to integrate the Nix package manager with Buck2, an open-source build system developed by Meta, to achieve highly granular and reproducible builds across different platforms.
By integrating Nix and Buck2, developers can benefit from Nix's robust package management and reproducible build environments, while also taking advantage of Buck2's scalable and efficient build system.
I will dive into the details of using remote execution services that support the Bazel remote execution protocol with Buck2 in conjunction with Nix's remote build capabilities and showcasing that using a sample project.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-nix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-nix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/C98N9H/feedback/)

---

### system-manager: unleashing nix on (almost) any distro

- **Speakers:** Ramses
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 12:50 - 13:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5987-system-manager-unleashing-nix-on-almost-any-distro/)

#### Abstract

Nix offers an alternative to the well-known container-based deployment flow, and can offer several benefits compared to those container-based deployments.
However, it's not immediately obvious how you would use nix to deploy services on machines running Linux distributions other than the nix-native NixOS.
To address this, we developed a tool called system-manager, which allows you to manage certain aspects of the system configuration of a Linux system using nix, while leaving others to be managed using the usual tools of the underlying distribution.

#### Related Links

- [system-manager repository](https://github.com/numtide/system-manager)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-nix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-nix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RRLSRM/feedback/)

---

### Go in the Nix ecosystem: vulnerability scanning and experiments towards a next-gen builder

- **Speakers:** Paul Meyer
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 13:15 - 13:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5654-go-in-the-nix-ecosystem-vulnerability-scanning-and-experiments-towards-a-next-gen-builder/)

#### Abstract

After looking at the current way Go code is packaged in nixpkgs using buildGoModule, disadvantages are pointed out with a focus on security (backed by data from govulncheck-nixpkgs project) and performance. Out-of-tree alternatives are presented with a focus on the new and promising approach of gobuild.nix, which implements a hook-based builder with module-level caching.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-nix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-nix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3AJDPH/feedback/)

---

### My Nix-Powered Homelab

- **Speakers:** Josh Lee
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 13:40 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6330-my-nix-powered-homelab/)

#### Abstract

For me, Nix-the-package manager has replaced homebrew, ASDF, and even docker. But its potential goes far beyond managing development environments. With its declarative, reproducible configurations, Nix is also an excellent choice for managing entire servers.
In this talk, I’ll share how I use NixOS and nixos-generators in order to create both stable and ephemeral VMs on my Proxmox hypervisor hosts, and how I run services like Grafana, Docker, Tailscale, and more.
We’ll explore how to deploy and update Proxmox VMs remotely using Nix, set up a WireGuard router with NixOS, and deploy services directly to NixOS declaratively. I’ll also show how to deploy Docker services to NixOS, using the same object tree and code files as all of your other configurations. 
Whether you’re managing a homelab or building out larger infrastructure, this talk will showcase how Nix can transform your approach to system configuration and service deployment.

#### Related Links

- [NixOS Website](https://nixos.org/)
- [Related Blog Post](https://www.joshuamlee.com/nixos-proxmox-vm-images/)
- [Ansible Homepage](https://www.ansible.com/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-nix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-nix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/Y79VFP/feedback/)

---

### NixOps4: new, sustainable platform for deployment technology

- **Speakers:** Robert Hensing
- **Room:** K.3.601
- **Day:** Saturday
- **Time:** 14:05 - 14:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5366-nixops4-new-sustainable-platform-for-deployment-technology/)

#### Abstract

NixOps used to be the only Nix-native deployment and provisioning tool, but it failed. NixOps4 is a complete redesign of the tool, taking lessons from NixOps, taking inspiration from Terraform, and borrowing its providers. In doing so, it creates a unified deployment platform, architecturally similar to how Nix is a platform for unified builds. It allows you to combine configurations freely with the Nix language and build system, and it makes it easy to "extend" the tool.
In this presentation, we'll have a look at the concepts that make up NixOps4, as well as its integration into the Fediversity project, which aims to enable hosting providers to let their customers deploy applications such as Mastodon, PeerTube and Pixelfed, fully automatically - running NixOps4 "unattended" in production.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-nix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-nix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XPYDLF/feedback/)

---

## Open Hardware and CAD/CAM (19)

### f8 - an 8 bit architecture designed for C and memory efficiency

- **Speakers:** Philipp K. Krause
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 09:00 - 09:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4902-f8-an-8-bit-architecture-designed-for-c-and-memory-efficiency/)

#### Abstract

Even in modern devices, 8-bit processors are found, but the architectures used are often not well-suited to programming in high-level languages, such as C. E.g. MCS-51 (8051, 8052) based microcontrollers in the Realtek WiFi chipsets. The f8 is an architecture based on the experience and lessons learned from maintaining Small Device C Compiler (SDCC) and the many 8-bit architectures it supports. It is designed to find its niche as an 8-bit architecture in places where the power of RISC-V is not needed, and no byte of code or data memory should be wasted.

#### Related Links

- [Current f8 repository (documentation and Verilog code)](https://sourceforge.net/p/sdcc/code/HEAD/tree/branches/f8/f8/)
- [SDCC (compiler that can target the f8) website](https://sdcc.sourceforge.net/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MPGRGG/feedback/)

---

### Free Function API for CadQuery

- **Speakers:** Adam Urbanczyk
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 09:20 - 09:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5286-free-function-api-for-cadquery/)

#### Abstract

CadQuery (CQ) is a scripted CAD Python library built on the OCCT kernel. The upcoming 2.5 CQ release will contain a free function API that is completely stateless and as-such addresses many existing usability constraints. It is more suited for advanced modeling use cases, less imposing on the user and allows to build  custom abstraction layers easily. I will present its design and demonstrate its capabilities with some examples. Moreover, I will give an update other new functionalities, upcoming plans of integrating meshing tools with CQ and show some real life applications.

#### Related Links

- [CadQuery repo](https://github.com/CadQuery/cadquery)
- [Free function docs](https://cadquery.readthedocs.io/en/latest/free-func.html)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QL7N3D/feedback/)

---

### Gruessaugust the functional test harness

- **Speakers:** Mark Meyer
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 09:50 - 10:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4107-gruessaugust-the-functional-test-harness/)

#### Abstract

We'll present the current state of Gruessaugust the open functional test hardness we developed for testing a custom tape plotter/labelling machine at the Welcome Werkstatt community workshop.
This test hardness "mocks" a GRBL CNC Controller, an I2C display, and a keyboard. All of these devices are then connected to the device under test. This allows us to push a change to the application code, rebuild the entire Raspberry Pi operating system image and deploy and test to multiple different hardware versions. All test results, including a video that visualizes keyboard input and display output are then forwarded to the CI system.
Gruessaugust is the German version of the ruler, whose only duty is waving her hand at her people.

#### Related Links

- [Gruessaugust Repo](https://codeberg.org/ofosos/gruessaugust/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KWRVBA/feedback/)

---

### VACASK and Verilog-A Distiller - building a device library for an analog circuit simulator

- **Speakers:** Árpád Bűrmen
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 10:20 - 10:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4681-vacask-and-verilog-a-distiller-building-a-device-library-for-an-analog-circuit-simulator/)

#### Abstract

VACASK is a novel FOSS analog circuit simulator with a clear separation between device models (i.e. equations) and circuit analyses. It is based on the state of the art KLU sparse matrix library and utilizes the OpenVAF Verilog-A compiler for building its device models from Verilog-A sources. A comparison with other FOSS analog circuit simulators is presented and the roadmap for future development is discussed. A major obstacle in development of VACASK (and every other new simulator) is the implementation of legacy device models that boils down to writing tens of thousands of lines of C code. Legacy device models are used in several older PDKs as well as in models of a large number of discrete electronic components. A novel approach to implementing these device models is proposed: a converter from SPICE3 API-based C code into modern Verilog-A code. The performance of the converted models is compared to that of native SPICE3 models. At the present the converted models can be used in VACASK and Ngspice circuit simulators as well as in any other simulator that supports Verilog-A. The limitations of the approach are discussed. Some alternative use cases for the converter are proposed and a roadmap for its future development is presented.

#### Related Links

- [VACASK](https://codeberg.org/arpadbuermen/VACASK)
- [Verilog-A Distiller](https://codeberg.org/arpadbuermen/VADistiller)
- [OpenVAF-reloaded](https://github.com/arpadbuermen/OpenVAF/)
- [VACASK at FSiC 2024](https://wiki.f-si.org/index.php?title=VACASK:_a_Verilog-A_Circuit_Analysis_Kernel)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SGRDW8/feedback/)

---

### PostCAD: OpenCASCADE in the Database

- **Speakers:** Kurt Kremitzki
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 10:40 - 11:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6604-postcad-opencascade-in-the-database/)

#### Abstract

OpenCASCADE is the elephant in the room. Let's enlist an elephant of our own, PostgreSQL!
Learning from the geospatial ecosystem's PostGIS (a database extension that provides geospatial data types and operations) I propose a parallel of our own, PostCAD.
Wrapping OpenCASCADE, it would provide CAD data types and operations and turn a database into a feature-rich CAD application server backed by battle-tested DB software.
As in the geospatial world, this could form the basis for an ecosystem of CAD web apps, mirroring GeoAlchemy, GeoDjango, Leaflet.js, and others.
In this talk, I'll outline what this future PostCAD world could look like, featuring specific use cases for new applications, as well as potential for integrating with FreeCAD and unlocking local-first yet cloud-boosted CAD on the desktop.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8KEZWN/feedback/)

---


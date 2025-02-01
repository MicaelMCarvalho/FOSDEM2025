# FOSDEM 2025 Schedule - Part 6 of 11

*Generated on 2025-02-01*

## Table of Contents

- [Kernel (17)](#kernel-17)
- [Legal and Policy (16)](#legal-and-policy-16)
- [LibreOffice (21)](#libreoffice-21)
- [LLVM (11)](#llvm-11)
- [Low-level AI Engineering and Hacking (27)](#low-level-ai-engineering-and-hacking-27)
- [Matrix.org Foundation and Community (8)](#matrix.org-foundation-and-community-8)
- [Microkernel and Component-Based OS (10)](#microkernel-and-component-based-os-10)

## Kernel (17)

### ngnfs: a distributed file system using block granular consistency

- **Speakers:** Zach Brown
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 10:00 - 10:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5471-ngnfs-a-distributed-file-system-using-block-granular-consistency/)

#### Abstract

ngnfs is a new distributed posix file system for Linux that aims to provide low latency and high concurrency by reducing the machinery between persistent data at rest and the network endpoints operating on it.
ngnfs is the result of the author's experience with classic parallel and clustered file systems in production at scale.  ngnfs is primarily designed to avoid the coarse coherency regimes and heavy server structures of those systems that introduce latency and concurrency bottlenecks.  Instead ngnfs is built around network protocols that  provide block-granular concurrency and distributed atomic transactions.
The talk will highlight the problems that large scale systems encounter, the core components of the design that address these challenges, the state of the implementation and initial performance results, and explore the opportunities for collaboration on a project in its early stages.

#### Related Links

- [Repository of initial userspace support.](https://github.com/versity/ngnfs-progs)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AMWY9T/feedback/)

---

### State persistence over kexec

- **Speakers:** Mike Rapoport, Alexander Graf, James Gowans
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5039-state-persistence-over-kexec/)

#### Abstract

This talk is about Kernel HandOver (KHO) mechanism that allows preserving memory contents across kexec.
We will describe how KHO enables preservation of memory accross kexec, what metadata it uses to pass between old and new kernels and the mechanism that ensures that new kernel can bootstrap itself without stepping over the preserved memory.
The combination of serialization, preservation of arbitrary memory ranges and guaranteed availability of memory for bootstrap of the new kernel makes KHO a solid foundation for solutions that aim to preserve both kernel and userspace memory across kexec.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8SS3A8/feedback/)

---

### Shrinking Memmap

- **Speakers:** Matthew Wilcox
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 11:00 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4860-shrinking-memmap/)

#### Abstract

The kernel takes 1.6% of your RAM for a data structure called memmap. Much of the information in it is redundant and can be expressed more efficiently. The problem is that much of the kernel relies on the current format of memmap. Join Matthew for a high-level overview of the multi-year project to reduce the size of memmap. No prior experience of kernel programming is needed, but understanding C data structures will be an advantage.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NBAMR9/feedback/)

---

### Waste-Free Per-CPU Userspace Memory Allocation

- **Speakers:** Mathieu Desnoyers
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 11:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6245-waste-free-per-cpu-userspace-memory-allocation/)

#### Abstract

Introduce the librseq per-CPU user-space memory allocator. It implements concepts similar to the Linux kernel percpu allocator in userspace, and thus reduces waste of per-CPU data structures hot cache lines by eliminating padding usually required to eliminate false-sharing, and in addition tackles issues that arise from resident memory waste when restricting processes with scheduler affinity or cpusets.
It allows prototyping kernel algorithms within the safe limits of user-space.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/A9HJ9G/feedback/)

---

### Don't let your motivation go, save time with kworkflow

- **Speakers:** Melissa Wen
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 12:00 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5733-don-t-let-your-motivation-go-save-time-with-kworkflow/)

#### Abstract

Another day, another custom kernel deployment on another Linux distribution, on another hardware and on another architecture and you are about to create another script that handles another system configuration... Wait! Stop now! Why not use Kworkflow?
Kworkflow (kw) optimizes the Linux kernel development workflow by significantly reducing the time spent on repetitive tasks and standardizing some practices.
kw development is strongly focused on reliability to offer a comprehensive set of features such as:

Building and deploying custom kernels across remote and local systems running on popular Linux distributions like Arch Linux, Debian, Ubuntu, Fedora, Raspberry Pi OS, and SteamOS.
Seamlessly handling cross-compilation in the same kernel tree, mitigating cross-compilation complexities.
Managing multiple development environments for different setups.
Sorting all your kernel configuration files in a single place.
Facilitating remote kernel debugging and code inspection.
Systematizing Linux kernel guidelines for patch submission.
Support for applying and reviewing patches from mailing lists via lore interface (under development).

This talk will introduce the key features of kw and show how it can be used to improve your kernel development efficiency.
This talk is ideal for Linux kernel developers of all experience levels seeking to streamline their development workflow.
More about kw at: https://kworkflow.org/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WMZHKW/feedback/)

---

### Level up your linux gaming: how sched_ext can save your fps

- **Speakers:** Andrea Righi
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 12:30 - 13:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4618-level-up-your-linux-gaming-how-schedext-can-save-your-fps/)

#### Abstract

Gaming on Linux has significantly improved over recent years, with better support for user-space frameworks (e.g., Wine, Proton, Mesa, Steam...).
While user-space solutions have their place, kernel-level optimizations can also play a crucial role in further enhancing gaming performance. In this talk, we will explore how scheduling policies in the Linux kernel can improve gaming on Linux.
Focusing on the sched_ext [1] framework, we will show how to design scheduling policies that can reduce latency, improve responsiveness and deliver a smoother gaming experience.
[1] https://github.com/sched-ext/scx

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/B9RE9S/feedback/)

---

### TuxTape: A Kernel Livepatching Solution

- **Speakers:** Grayson Guarino, Chris Townsend
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 13:10 - 13:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5689-tuxtape-a-kernel-livepatching-solution/)

#### Abstract

TuxTape is an in-development kernel livepatching ecosystem that aims to aid in the production and distribution of kpatch patches to vendor-independent kernels. This is done by scraping the Linux CNA mailing list, prioritizing CVEs by severity, and determining applicability of the patches to the configured kernel(s). Applicability of patches is determined by profiling kernel builds to record which files are included in the build process and ignoring CVEs that do not affect files included in kernel builds deployed on the managed fleet.
We will present a demo of a proof-of-concept of TuxTape, including the CNA scraper and database builder, the central server for storing CVE metadata and kernel build dispatching, the kernel builder itself, and the interactive dashboard where all of this is managed. We would also like to discuss with the community what a useful livepatch service would look like and how we should move forward with this project to best suit the needs of the community.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EHSL88/feedback/)

---

### Recent TPM Security Enhancements to the Linux Kernel

- **Speakers:** James Bottomley
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 13:40 - 14:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4827-recent-tpm-security-enhancements-to-the-linux-kernel/)

#### Abstract

Recent security updates to Linux, such as the new Systemd Unified Kernel Image[1] rely on the discrete or firmware integrated TPM (Trusted Platform Module) to verify boot and release secrets securely. However, there are many known attacks against the TPM chip itself. We will discuss the newly upstreamed Linux Kernel TPM security patches[2], which not only provide a basis for securely communicating with the TPM but also provide a novel defences against a wide variety of TPM based attacks by using a unique (to Linux) null key scheme. This talk will cover what TPM based attacks are (including interposer attacks), how the Trusted Computing Group expects you to tell you're talking to a real TPM and how you can communicate with it securely and use its policy statements to govern key use and release. We will then move on to how the new Linux Kernel patches extend this and can be leveraged to validate the TPM on every boot and continually monitoring it for any TPM interposer substitutions in real time.
[1] https://github.com/uapi-group/specifications/blob/main/specs/unified_kernel_image.md
[2] https://lore.kernel.org/all/20240429202811.13643-1-James.Bottomley@HansenPartnership.com/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FEZ8WX/feedback/)

---

### Virtualization-assisted Security: A Resilient Security Foundation for the Linux Kernel

- **Speakers:** Sergej Proskurin
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 14:10 - 14:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5255-virtualization-assisted-security-a-resilient-security-foundation-for-the-linux-kernel/)

#### Abstract

The Linux kernel architecture faces inherent limitations in its security design, primarily due to constraints imposed by the underlying hardware. The Linux kernel must not only isolate user-space processes but also protect itself from unauthorized access—a task made increasingly challenging by the presence of vulnerabilities. Since modern security mechanisms rely on the Linux kernel's integrity, their effectiveness collapses as soon as the kernel is compromised. Therefore, the kernel's resilience is crucial to the security of the entire system, raising the fundamental question: how can we maintain robust security despite the presence of kernel vulnerabilities?
In this presentation, we introduce a virtualization-assisted security architecture for the Linux kernel to address these challenges. Our solution provides a lightweight virtualization layer comprising a thin, formally-verifiable virtual machine monitor on top of the open-source NOVA microhypervisor. Acting as a security support layer, this architecture enables the Linux kernel to effectively leverage the system's virtualization extensions to fortify its defenses. In-line with virtualization-based state-of-the-art security mechanisms, our solution enforces Linux kernel code integrity and protects selected data structures from being abused by malicious actors. Beyond these capabilities, it enables advanced security features, such as isolating selected security-critical subsystems within the Linux kernel itself and providing a versatile event monitoring facility targeting the activity of applications and containers in user space. Overall, by bridging the traditional separation between the OS and system virtualization technologies, our open source implementation integrates both to create a more robust and resilient security foundation. We present our implementation as a promising approach to mitigating the risks posed by kernel vulnerabilities while significantly enhancing the security posture of modern systems.

#### Related Links

- [Linux patches for virtualization-assisted security support for the Linux kernel](https://github.com/bedrocksystems/linux-bhv-patches)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DRQRFW/feedback/)

---

### Rust for Linux: an overview

- **Speakers:** Anisse Astier
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 14:40 - 15:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5875-rust-for-linux-an-overview/)

#### Abstract

Rust for Linux is a project to bring the Rust language in the Linux kernel. What is it for? What drivers have been written, and what is currently merged in Linux ? Why are so many people interested in bringing a new language to the kernel?
We'll first do a retrospective of what happened in the past years of the Rust for Linux project, and where it is going.
Then we'll look at specific drivers that have been written in Rust, and look at code examples to understand the advantages Rust brings to the table in the context of kernel development.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BG8KNH/feedback/)

---

### DAMON: Kernel Subsystem for Data Access Monitoring and Access-aware System Operations

- **Speakers:** SJ
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 15:10 - 15:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4396-damon-kernel-subsystem-for-data-access-monitoring-and-access-aware-system-operations/)

#### Abstract

DAMON is a Linux kernel subsystem for efficient data access monitoring and access-aware system operations.  In this session, the speaker will introduce mechanism and design of DAMON with live demonstration of its features using DAMON user-space tool.  The speaker will also introduce known use cases of it from real world products with guidance of the usage for different use cases.  Finally, the speaker will share future development plans for DAMON and how audiences can participate.

#### Related Links

- [Project website](https://damonitor.github.io)
- [Source code in mainline Linux tree](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/mm/damon)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HNJCNB/feedback/)

---

### Redox OS -- a Microkernel-based Unix-like OS

- **Speakers:** Jacob Lorentzon
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 15:40 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5973-redox-os-a-microkernel-based-unix-like-os/)

#### Abstract

Redox is a community-developed Unix-like operating system written in Rust, with the long term goal of being a microkernel-based alternative to its monolithic counterparts. Redox puts strong emphasis on POSIX and source-level compatibility with existing Linux applications, done largely in userspace, and has over time been able to port a growing number of applications.
This presentation will provide an overview of the Redox operating system, its architecture and current status, and will provide a short demo.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KMBZHB/feedback/)

---

### Static analysis of return code propagation

- **Speakers:** Asbjørn Sloth Tønnesen
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 15:50 - 16:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6356-static-analysis-of-return-code-propagation/)

#### Abstract

A journey of using sparse to statically analyze and detect cases where return codes are returned, and overruled within a driver before they are able to reach a generic subsystem API or user-space.
In 2024, while working on some flower patches for the Linux kernel, I stumbled upon a few bugs[1][2][3] in the qede driver.
As an example: A static int helper function could return a number of return codes, but the only caller just used it for a non-zero check, and if so always returns -EINVAL, regardless of the error code returned by the callee.
This class of errors seemed like a good candidate for static analysis. As these bugs had been around and undetected for a long time, I decided to take a stab at it.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ALSVLW/feedback/)

---

### Status and Desiderata for Syscall Tracing and Virtualization Support

- **Speakers:** Renzo Davoli, Davide Berardi
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 16:10 - 16:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6231-status-and-desiderata-for-syscall-tracing-and-virtualization-support/)

#### Abstract

The Linux kernel offers several mechanisms for system call tracing and virtualization, such as ptrace, ptrace with PTRACE_SYSEMU, seccomp with SECCOMP_RET_TRACE, seccomp-unotify, and prctl with PR_SET_SYSCALL_USER_DISPATCH. Each of these methods has unique application domains, strengths, and limitations in terms of complexity and usability, while sharing core capabilities. Although primarily used for building powerful debugging tools (e.g., gdb, strace), these mechanisms can also be leveraged to construct syscall-based virtual machines, achieving varied performance levels and encountering specific challenges.
A distinctive feature of syscall-based virtual machines is their ability to selectively emulate system calls. For example, one might choose to emulate open(2) but not socket(2), thereby providing the guest environment with a tailored "view" of the underlying operating system.
This seminar will explore the current state of syscall tracing and virtualization techniques through practical demonstrations, examine their inherent limitations, and propose potential improvements to enhance usability and performance. Specific focus will be given to the challenges of virtualizing the poll(2) and select(2) syscall families, which are particularly intricate when managing a mixed environment of virtualized and real file descriptors.

#### Related Links

- [VUOS: Syscall Based Virtual Machine](https://github.com/virtualsquare/vuos)
- [libvpoll, virtual poll implementation](https://github.com/rd235/libvpoll-eventfd)
- [Source Code of the examples discussed in the seminar](https://github.com/virtualsquare/syscall_tracing)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JJYDP7/feedback/)

---

### Coccinelle Explorer: Learning Semantic Patching Interactively

- **Speakers:** Michele Martone
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 16:40 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6515-coccinelle-explorer-learning-semantic-patching-interactively/)

#### Abstract

The Compiler Explorer is an online resource which greatly
accelerates compilation and assembly language viewing of C/C++
code for different compilers and architectures.
Now we have a similar tool to learn Coccinelle, the tool for 
large-scale refactorings of the Linux kernel.
The demo will demonstrate how anybody can use the tool while
learning Coccinelle.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HSMLJK/feedback/)

---

## Legal and Policy (16)

### Welcome to the Legal and Policy Issues DevRoom

- **Speakers:** Karen Sandler, Tom Marble, Alexander Sander, Bradley M. Kuhn, Matthias Kirschner, Richard Fontana
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 10:30 - 10:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6602-welcome-to-the-legal-and-policy-issues-devroom/)

#### Abstract

Welcome to the Legal and Policy Issues DevRoom

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FSAAUX/feedback/)

---

### Europe's Way to Mandatory B2B-E-Invoices

- **Speakers:** Jochen Stärk
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 10:35 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4205-europe-s-way-to-mandatory-b2b-e-invoices/)

#### Abstract

After electronic B2G-invoices became mandatory in 2020 (for guideline 2014/55/EU the CEN standard EN16931 was issued) now the EU is planning in their Vat in the Digital Age (ViDA) draft guideline to also request machine readable copies of all Business-to-Business (B2B) cross border invoices. 
Anticipating this change, some countries, like Italy, France and Germany, introduced or are introducing domestic continuous transaction control (CTC) systems requiring short term XML copies of all domestic B2B invoices, replacing paper invoices and PDF invoices without additional XML in the foreseeable future.
This speech will briefly summarize aspects of Italy, cover what is happening in France and focus on the situation in Germany with it's formats Factur-X and XRechnung and dive into open standards (like UBL and UN/CEFACT Cross Industry Invoice=CII as well as Factur-X) as well as open source to view, create, parse, validate and convert electronic invoices.

#### Related Links

- [Mustangproject e-invoicing command line tool](https://www.mustangproject.org/commandline/)
- [Quba E-Invoice viewer](https://quba-viewer.org/)
- [Collection of open source e-invoicing resources](https://zugferd.org/)
- [Samples of EN16931 CII, UBL and FX invoices e.g. for Germany](https://github.com/ZUGFeRD/corpus/tree/master/XML-Rechnung/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JVBLPB/feedback/)

---

### Is There Really an SBOM Mandate?

- **Speakers:** Bradley M. Kuhn
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 11:00 - 11:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6155-is-there-really-an-sbom-mandate-/)

#### Abstract

A consistent mantra of the Software Bill Of Materials (SBOM) ballyhoo is that various government entities around the world have mandated SBOMs in various different places.  From USA POTUS Executive Orders, to EU Directives, to USA NIST whitepapers — it's often been repeated that these various sources mandate SBOMs as a mandatory requirement.
Let's do a deep dive into the source material and find out what these various orders and directives actually say, and figure out what's really mandated.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/V9RTNF/feedback/)

---

### How Does Heinz Have 80% of a Commodity Market?* – Leveraging Trademarks in Free Software

- **Speakers:** Pamela Chestek
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 11:30 - 11:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6544-how-does-heinz-have-80-of-a-commodity-market-leveraging-trademarks-in-free-software/)

#### Abstract

The software industry traditionally used the right to exclude granted by copyright as the means for generating revenue. Free software came along and flipped the script, giving away for free what traditionally was the primary mechanism for extracting payment. But free software has struggled ever since, trying to figure out how to create value that customers are willing to pay for when they can’t use the copyright that way.
More and more, companies are recognizing and leveraging the truly unique asset in free software – the brand. Ketchup is a commodity market, but Heinz has captured 80% of it by convincing U.S. consumers that Heinz ketchup is better than all the rest. Open source software is similar to a commodity market because the original software may be competing with the identical product. Open source software companies are learning how to develop business models around the brand, convincing customers that the customer will be better served by remaining loyal to the branded product instead of their competitors who are simply copying and distributing the software.
But it’s also possible for companies to overextend their trademark rights to subvert the promise given in the copyright license. Frustrated at free-riding or the perception of it, companies are now also trying to extract revenue through questionable trademark infringement theories.
This session will review the current state of trademark thinking in free software as a revenue strategy, both the appropriate and inappropriate ways to manage the customer relationship through the brand.
*Robert Young, How Red Hat Software Stumbled Across a New Economic Model and Helped Improve and Industry, Open Sources, Voices from the Revolution p. 116 (1999).

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8DZD3Z/feedback/)

---

### LGPL enforced in Germany: how we helped a purchaser use the courts to compel compliance

- **Speakers:** Denver Gingerich
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 12:00 - 12:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6169-lgpl-enforced-in-germany-how-we-helped-a-purchaser-use-the-courts-to-compel-compliance/)

#### Abstract

SFC funded and supported Sebastian Steck's lawsuit against wireless router manufacturer AVM.  That lawsuit has recently concluded.  At the end of the lawsuit, complete source code for all LGPL works had been made available, which means everything needed to reinstall changes, for the FRITZ!Box 4020.  This marks the first time to our knowledge in Germany that an individual purchaser has successfully sued a manufacturer and received complete source code as a result.  This talk will describe what the case was about, what the compliance issues were before the lawsuit, and how "the scripts used to control compilation and installation" that AVM provided over the course of the lawsuit brought them into compliance with LGPLv2.1.

#### Related Links

- [AVM's LGPL-compliant source release](https://sfconservancy.org/usethesource/candidate/avm-fritzbox-4020-683-round-3-of-n/)
- [Court documents and other source code candidates](https://sfconservancy.org/copyleft-compliance/avm.html)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YF7LNE/feedback/)

---

### Managing copyrights in free software projects - discussion panel

- **Speakers:** Krzysztof Siewicz
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 12:30 - 12:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5376-managing-copyrights-in-free-software-projects-discussion-panel/)

#### Abstract

For FSF-copyrighted GNU packages, FSF insists on executing copyright assignments and employer disclaimers. These are designed to ensure steady and continuing enforcement of the GPL, as well as to serve other important purposes related to licensing and copyright management. The maintainers of some GNU packages would like to use a simple mechanism called "Developer Certificate of Origin" (DCO). It is hard, and some lawyers think it's even impossible, for a DCO to allow FSF to enforce the GPL. However, we at the FSF have once promised to accept DCOs and to draft a DCO that would best serve the needs of the free software community. We want to fulfill this promise after a broad discussion about issues surrounding copyright assignments: their importance, best approaches, and challenges in managing copyrights in free software projects.
Panelists:
James Bottomley, Andrea Corallo, Ludovic Courtès, Karen Sandler, Craig Topham
Panelists will elaborate on the following questions:
1) How to ensure swift enforcement of the GPL?
2) How to protect free software against third party claims, including employers' copyright or patent claims?
3) How to enable swift relicensing or adding additional permissions, while protecting software against appropriation?
4) How to remove any challenges a contributor might encounter with the process?

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HTADDE/feedback/)

---

### To Mine Or Not To Mine - Training of (Generative) AI Models under the TDM Exception in EU Copyright Laws

- **Speakers:** Lisa Käde
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 13:00 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4794-to-mine-or-not-to-mine-training-of-generative-ai-models-under-the-tdm-exception-in-eu-copyright-laws/)

#### Abstract

For the training of generative AI models, developers usually have to gather large amounts of mostly copyrighted data (texts, images, code, music etc.). Datasets are provided online for download or can be assembled individually via crawling & scraping. 
In both cases, copies and sometimes further adjustments of data are necessary in preparation for AI training - acts relevant to copyright law, usually requiring a license. Since June 2021, the "text and data mining exception", introduced via the DSM directive, is a part of national copyright laws in the member states of the EU, allowing for license-free copies for the purposes of text and data mining (TDM). It is since being discussed whether the TDM exception can be applied to the training of (generative) AI models, and how respective reservations can be made in a "machine-readable format". 
The talk will present the first German court decision (09/2024) on the application of the TDM exception to AI analysis and provide an overview of the discussion regarding the applicability of the TDM exception to AI training in Germany. Participants are also invited to join a constructive discussion regarding the feasibility of a machine-readable reservation and the importance of international / EU-wide (copyright) rules on AI training.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XH9DHD/feedback/)

---

### Panel: When is an AI system free/open?

- **Speakers:** julia ferraioli, Ciarán O'Riordan, Richard Fontana, Zoë Kooyman
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 13:30 - 14:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6639-panel-when-is-an-ai-system-free-open-/)

#### Abstract

This panel will explore what makes a machine learning model, or an “AI system”, Free Software / Open Source. Some topics we may address:
- What, if anything, is the source code of a model? If the source code includes training data, what are the implications for LLMs and other large generative models? Can trained weights themselves be considered source code? 
- What does user freedom (and in particular, freedom to study and modify) mean in the context of AI models?  How, if at all, does it differ from our traditional understanding of software freedom?
- Are there any reasons to tolerate use restrictions in AI model licenses that we would reject for FOSS?
- Proposed normative definitions of free/open AI and related efforts, including the OSI’s OSAID 1.0, FSF’s criteria for free machine learning applications, and the Model Openness Framework
- Should we have different tiers of free-ness/openness when assessing AI models/systems?
- Leaving aside the question of source code, are there other kinds of artifacts that should be released with a model for it to legitimately be considered free/open?

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DJTLHU/feedback/)

---

### Auditing Web Trackers with the EDPB's Open-Source Website Compliance Tool

- **Speakers:** Jerome Gorin, Amandine JAMBERT
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 14:30 - 14:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5120-auditing-web-trackers-with-the-edpb-s-open-source-website-compliance-tool/)

#### Abstract

The European regulations impose strict rules on the collection and use of data via cookies and other trackers on websites. Auditing the practices of these sites is crucial to ensure that the cookies placed, both before and after user consent, comply with current legal obligations. This includes the purpose of the cookies and the transparency of the information provided to users, such as cookie descriptions and an easily accessible refusal option.
Although various website analysis tools exist, their use often requires advanced technical expertise, as they typically operate via command-line interfaces. In this context, the EDPB, through the Support Pool of Experts (SPE), has developed a dedicated audit tool to assess websites' compliance with European regulatory requirements.
The tool is a Free and Open Source Software under the EUPL 1.2 Licence and is available for download on code.europa.eu. The source code is available here. 
Dr. Jérôme Gorin, researcher at UniLaSalle, and Dr. Amandine Jambert, technology expert at EDPB Secretariat,  will present its functionality and its adoption by numerous auditors within data protection authorities across Europe. The presentation will conclude with a discussion on the tool's improvement prospects, aiming to foster knowledge sharing and the detection of the latest online tracking technologies.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BFLLUX/feedback/)

---

### A Free Software App Store for iOS: the App Fair Project's perspective on the DMA

- **Speakers:** Marc Prud'hommeaux
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 15:00 - 15:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5488-a-free-software-app-store-for-ios-the-app-fair-project-s-perspective-on-the-dma/)

#### Abstract

The Digital Markets Act mandates that mobile gatekeepers open their device operating systems to competing app stores. This affects the landscape of app distribution on iOS and Android and has brought about a variety of different compliance efforts, most of which have been found lacking by regulators thus far. The law is important for Free Software, as its obligations grant smaller Free Software projects the rights to demand access to gatekeepers' infrastructure like enabling alternative app store, sideloading and un-installation of software and interoperability with operating systems.
This talk will outline the current state of compliance efforts on the part of Apple and iOS, the primary areas where they are deemed insufficient, and how they effectively block any marketplace from emerging as a viable source of FOSS software distribution for the iPhone and iPad. Financial preconditions, ongoing fees, enforced DRM, centralized notarization app review, and other factors all conspire together to maintain the status quo of monopolistic control over the app marketplace on these devices.
The App Fair Project (appfair.org) is a non-profit charity with the mission of creating an app marketplace for the distribution of digital public goods in the form of free and open-source mobile applications. We have been active in the various workshops and working groups that have examined the DMA compliance efforts on the part of the mobile OS gatekeepers, and have provided technical advice and expertise to groups such as the Free Software Foundation Europe (FSFE) and the NGI TALER project.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7Z7LBE/feedback/)

---

### Breaking tech monopolies in Europe: A fireside chat with the European Commission

- **Speakers:** Lucas Lasota, Alexandre Ruiz Feases, Victor Le Pochat
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 15:30 - 15:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5432-breaking-tech-monopolies-in-europe-a-fireside-chat-with-the-european-commission/)

#### Abstract

The EU Digital Markets Act is a law regulating the economic power of very large technology companies. The law includes several obligations to tackle unfair practices and improve market contestability addressed at companies considered "gatekeepers" of digital markets in the EU. 
The DMA creates new opportunities impacting Free Software, like the obligations to allow alternative app stores, the prohibition of non-removable pre-installed software, the enabling of side-loading of software in devices, and interoperability rules regarding software and hardware.
The European Commission is the main authority responsible for implementing and oversight the DMA. The Commission has been investigating companies like Apple, Google and Meta due to their behaviour and practices.
This fireside chat will provide the audience the opportunity to interact with Commission's officers working directly with the DMA. The session will focus on the legal and technical challenges the Commission faces for DMA compliance, in particular: (a) Enabling alternative app stores in iPhones and iPads; (b) Enhancing interoperability in Apple devices; (c) Breaking lock-ins by leveling the playing field for smaller Free Software projects against gatekeeper commercial practices.
The format consists of:  (1) a short presentation by the Commission's officers on the importance of DMA for Free Software contributors; (2) A longer Q&A session together with the audience moderated by Dr. Lucas Lasota about the technical and legal aspects of the DMA.
This fireside chat will provide valuable insights for the audience on the work of regulators in Europe, and how they implement key legislation for Free Software.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YCX9SH/feedback/)

---

### Let's talk about anti-trust!

- **Speakers:** Karen Sandler, Alanna Rutherford
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 16:00 - 16:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6637-let-s-talk-about-anti-trust-/)

#### Abstract

Many views about antitrust abound in the FOSS communities, but what do the laws actually say? We've invited Alana Rutherford, an accomplished United States antitrust lawyer to answer our questions about how these laws actually work.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UK9FZT/feedback/)

---

### The EU CRA and Copyleft

- **Speakers:** Jimmy Ahlberg
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 16:30 - 16:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5291-the-eu-cra-and-copyleft/)

#### Abstract

With the introduction of the EU Cyber Resilience Act a number of interesting questions are raised. This talk focus on the EU CRA and discuss some of the implication when applied to Free and Open Source Software licensed under Copyleft licenses such as the GPL. 
The EU CRA introduces, under some circumstances, an obligation to contribute upstream if there are vulnerabilities, what will best practices be to manage this obligation in permissively licensed project respective in Copyleft licensed projects, how will this impact customer agreements, R&D collaborations and similar.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3V7LHD/feedback/)

---

### Legislative overlay: anticipating and navigating through regulatory vectors

- **Speakers:** Alexander Sander, fukami, Michael Schuster
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 17:00 - 17:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5325-legislative-overlay-anticipating-and-navigating-through-regulatory-vectors/)

#### Abstract

In recent years, Europe has seen an increase in regulations directly affecting the software industry, and with implications for free and open source software. The regulatory landscape is complex and evolving, which makes a deeper understanding of the intended and unintended consequences on FOSS projects and the ecosystem necessary. 
This session will explore the intricacies of EU legislative processes, using the CRA as a focal point. The panel aims to share and identify key moments of realization ('aha' moments) that enable navigating regulatory challenges more efficiently. 
Participants will hopefully gain practical models and strategies for navigating legislative processes, and actionable methods to effectively engage with policymakers and other stakeholders, or in short: to be better able to talk to the right people at the right moment about the right subject to have most impact.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VDLP3Z/feedback/)

---

### CRA Q&A on Open Source Stewards under the Cyber Resilience Act

- **Speakers:** Alexander Sander, Bradley M. Kuhn, Michael Schuster
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 17:30 - 17:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6638-cra-q-a-on-open-source-stewards-under-the-cyber-resilience-act/)

#### Abstract

Our community has been confused and concerned at the last-minute addition to the Cyber Resilience Act (CRA) that created the class of “Open Source Steward”.  Many projects want to know ASAP if their own project will be such a Steward, or if their fiscal sponsor will be forced to be a Steward.  Most projects operate with small budgets, even those with fiscal sponsors, and as such CRA compliance could financially ruin projects.
At this session, we'll have experts to answer these questions and others, and help you to not panic about what we face in the CRA.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GR9EGH/feedback/)

---

### Organizer's Panel

- **Speakers:** Karen Sandler, Tom Marble, Alexander Sander, Bradley M. Kuhn, Matthias Kirschner, Richard Fontana
- **Room:** H.1301 (Cornil)
- **Day:** Saturday
- **Time:** 18:00 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6607-organizer-s-panel/)

#### Abstract

Legal and Policy Issues Devroom Organizers discuss topics in the DevRoom.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-legal-and-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-legal-and-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MTZZG9/feedback/)

---

## LibreOffice (21)

### Announcement of LibreOffice 25.2

- **Speakers:** Italo Vignoli
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 10:30 - 10:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5735-announcement-of-libreoffice-25-2/)

#### Abstract

LibreOffice 25.2 will be released just after FOSDEM, but it will be pre-announced at FOSDEM to the open source community. During the talk, development numbers will be provided, and the most important new features will be described.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/R9YFUJ/feedback/)

---

### ODF and its Toolkit

- **Speakers:** Svante Schubert
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 10:35 - 10:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6325-odf-and-its-toolkit/)

#### Abstract

Quick intro & update on the ODF standard.
Afterwards, explain the design ideas behind TDF's ODF Toolkit and its usefulness for ODF automation.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TB7D3C/feedback/)

---

### LibreOffice Accessibility on Linux, Windows and macOS

- **Speakers:** Michael Weghorn
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 10:50 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6144-libreoffice-accessibility-on-linux-windows-and-macos/)

#### Abstract

As an application that supports multiple operating systems (including GNU/Linux, Windows, macOS), LibreOffice needs to implement multiple platform-specific accessibility APIs in order to be accessible for everyone. This talk gives an overview of accessibility APIs on the different systems, which of them LibreOffice currently supports, how it does that, and related aspects and challenges.

#### Related Links

- [LibreOffice website](https://www.libreoffice.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3D7HWR/feedback/)

---

### Languages and LibreOffice

- **Speakers:** Jonathan Clark
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 11:00 - 11:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4103-languages-and-libreoffice/)

#### Abstract

A visual retrospective of recent language support improvements in LibreOffice. Examples will be contextualized, used to explore some of the unique challenges of supporting all of the languages of the world, and show how improving support for one language can benefit all.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9SYTVW/feedback/)

---

### Introducing Glow Effect for texts in shapes

- **Speakers:** Balázs Varga
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 11:10 - 11:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5342-introducing-glow-effect-for-texts-in-shapes/)

#### Abstract

In this talk I will introducing the new uniform glow effect for texts in shapes. This glow effect only can be applied for texts in different text object. We already had Blur effect for text objects, but we also need to be able to apply GLOW effects, as can be done on Shapes. This is useful for adding extra highlighting to text.

#### Related Links

- [LibreOffice related projects](https://github.com/libreoffice)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZUJNCN/feedback/)

---

### Improved comments & @mentions

- **Speakers:** Pranam Lashkari
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 11:20 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5216-improved-comments-mentions/)

#### Abstract

Recent improvements in Collabora's online suit based on Libreoffice technology related to comments and the possibility of mentioning other users.
repository: https://github.com/CollaboraOnline/online

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MJL7YY/feedback/)

---

### Testing the QA instructions

- **Speakers:** Gabor Kelemen
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 11:30 - 11:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5754-testing-the-qa-instructions/)

#### Abstract

I will present some first person experiences learned while handholding a relative newcomer to LibreOffice QA, about how easy (or not) is it to pick up speed with bug triaging, bibisecting and more, based on the Wiki instructions.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BD9T87/feedback/)

---

### LibreOffice Technology atomic / threading improvements

- **Speakers:** Caolán McNamara
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 11:40 - 11:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5133-libreoffice-technology-atomic-threading-improvements/)

#### Abstract

With multi-threaded LibreOffice spreadsheet calculations atomic reference counting can become a surprisingly dominant bottleneck. Some profiling data and case studies on implemented improvements in this area.

#### Related Links

- [LibreOffice: Your private, free office suite](https://www.libreoffice.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CD89ZS/feedback/)

---

### LibreOffice's Python API: Working around limitations of the Pythonic approach

- **Speakers:** Sarper Akdemir
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 11:50 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6346-libreoffice-s-python-api-working-around-limitations-of-the-pythonic-approach/)

#### Abstract

LibreOffice's Python API is among the more user-friendly options. It provides extensive functionality in a Pythonic manner right out of the box. However, for aspects of the UNO API that aren't straightforwardly supported, alternative methods may be necessary.
Join me as I demonstrate a few problems on this topic, along with some handy tips and tricks!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ESRZCP/feedback/)

---

### Exploring the deprecated parts of LibreOFfice  API

- **Speakers:** Gabor Kelemen
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 12:00 - 12:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5753-exploring-the-deprecated-parts-of-libreoffice-api/)

#### Abstract

Let's take look at how much of the LibreOffice internal and external API is marked as deprecated and since when.
Maybe also ask ourselves whether we are doing fine or we forgot something important we wanted to do.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CJSYEJ/feedback/)

---

### LOWA, In Need Of a VCL Plug

- **Speakers:** Stephan Bergmann
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 12:10 - 12:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5169-lowa-in-need-of-a-vcl-plug/)

#### Abstract

Putting the pixels of LibreOffice into a browser window.  With or without Qt.  Asking for interaction.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/A7QDTQ/feedback/)

---

### Beautiful remote web dialog widgets built on LOT

- **Speakers:** Szymon Kłos
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 12:20 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6097-beautiful-remote-web-dialog-widgets-built-on-lot/)

#### Abstract

LibreOffice Technology provides great engine for processing the documents with LibreOfficeKit. For more advanced usage in a user-friendly fashion the good UI is needed. JSDialog API provides way to interact with existing dialogs and build bespoke widgets for different platforms in the browser.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BADVRH/feedback/)

---

### Distributed real-time collaboration for Writer - a first prototype

- **Speakers:** Thorsten Behrens
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 12:30 - 12:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6504-distributed-real-time-collaboration-for-writer-a-first-prototype/)

#### Abstract

Come to see a first prototype of a CRDT-based real-time distributed collaboration implementation - for being able to collaboratively comment on a Writer document, from a number of distributed LibreOffice instances (desktop, browser or cloud).

#### Related Links

- [Project homepage](https://libreoffice.org)
- [Prototype patch](https://gerrit.libreoffice.org/c/core/+/175652)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YYEJJ9/feedback/)

---

### Automatic Documents, packed with content and signed

- **Speakers:** Michael Meeks
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 12:45 - 12:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5935-automatic-documents-packed-with-content-and-signed/)

#### Abstract

Many processes are packed with document generation, and forms of various types, from applications to contracts. Come and hear how new APIs built on LibreOffice Technoloy provided by Collabora Online can
make building complex documents easier. From populating fields, to making richer templates, to tweaking chart data, our new Automatic Document REST APIs here enable powerful document interaction - both creation and extraction of data with a simple JSON based API.
Whether you want to extract data from docx files, generate richer templates for subsequent editing, or enable powerful electronic signature functionality - have we got an API for you!?
Come and hear how to use and improve it.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GP8BAE/feedback/)

---

### Optimizing AutoText & settings for multi-tenant collaboration

- **Speakers:** Caolán McNamara
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 12:55 - 13:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5134-optimizing-autotext-settings-for-multi-tenant-collaboration/)

#### Abstract

Overview of a feature implementation in Collabora Online, building on LibreOffice Technology, where autotext and other presets and configuration data can be supplied both at an individual user level and at an organization level, via their wopi server, to a Collabora Online instance serving multiple organization tenants.

#### Related Links

- [Collabora Online: Your own private Office in the Cloud](https://github.com/CollaboraOnline/online)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZHGCBD/feedback/)

---

### New, shiny WebGL presentations in the browser

- **Speakers:** Szymon Kłos
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 13:05 - 13:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6090-new-shiny-webgl-presentations-in-the-browser/)

#### Abstract

LibreOfficeKit has new API to expose slideshow elements: content, animations, transitions and notes. Short story about composing the impressive 3D slideshows in WebGL directly in the browser.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PUVENX/feedback/)

---

### COOL – LibreOffice Technology in the browser

- **Speakers:** Michael Meeks
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 13:15 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5932-cool-libreoffice-technology-in-the-browser/)

#### Abstract

Collabora Online (COOL) delivers collaborative document editing based on LibreOffice Technology to any modern browser. Come and hear about how we've been improving usability, deploy-ability, performance,
feature-set and georgeousness of Collabora Online. See how COOL can be deployed and catch the 
excitement of making code simpler, faster and better for users at pace.
Finally hear how you can get involved with the fun.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JQUBNU/feedback/)

---

### LibreOffice-based document editing in XWiki through COOL

- **Speakers:** Lavinia Vitel
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 13:25 - 13:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5653-libreoffice-based-document-editing-in-xwiki-through-cool/)

#### Abstract

XWiki is a wiki engine, and, as with most wiki engines, it allows uploading attachments to wiki pages. In order to edit these attachments quickly, we recently released an extension allowing to link an XWiki instance with a COOL server, and thus enabling real-time collaboration office files attached to wiki pages.
This presentation will focus on the technical integration of COOL with XWiki, and will discuss use-cases that we identified over the years, as well as the roadmap for this extension. The application code can be found at https://github.com/xwikisas/application-collabora

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8G79H8/feedback/)

---

### Nextcloud Office: On collaborating across FOSS projects

- **Speakers:** Julius Knorr
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 13:40 - 13:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6635-nextcloud-office-on-collaborating-across-foss-projects/)

#### Abstract

How we work together and bring Collabora Online integration in Nextcloud to the next level with file conversion, document transformation and AI.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/D7KTHD/feedback/)

---

### COOL UI / UX command tracking & analysis

- **Speakers:** Attila Szűcs
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 13:55 - 14:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5055-cool-ui-ux-command-tracking-analysis/)

#### Abstract

A presentation about the challenges of tracking and analysis COOL UI / UX commands.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PJCTWZ/feedback/)

---

### LibreOffice on mobile with the Collabora Office app

- **Speakers:** Skyler Grey
- **Room:** H.2213
- **Day:** Saturday
- **Time:** 14:05 - 14:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5093-libreoffice-on-mobile-with-the-collabora-office-app/)

#### Abstract

Collabora Online is an online document editor based on LibreOffice, but there's
also both an Android and an iOS Collabora Office app based on the same
technology - LibreOffice Kit. Have you ever wondered how it works?
In this talk, I'll give a high-level overview of the architecture of the
Collabora Office mobile app. Along the way, I'll discuss how it's similar but
different to the Collabora Online server, and what limitations on the mobile
platform (for example a lack of availability of clipboard web APIs) pushed us
to write in the way that we have.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-libreoffice:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-libreoffice:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WKTWEK/feedback/)

---

## LLVM (11)

### Welcome to the LLVM dev room

- **Speakers:** Kristof Beyls, Peter Smith, Marius Brehler
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 10:30 - 10:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6746-welcome-to-the-llvm-dev-room/)

#### Abstract

A word of welcome by the LLVM Dev room organizers.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-llvm:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-llvm:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XWJHDC/feedback/)

---

### A New Approach to Callee-Saved Registers in LLVM

- **Speakers:** Mikhail Gudim
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 10:35 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6210-a-new-approach-to-callee-saved-registers-in-llvm/)

#### Abstract

Currently LLVM saves and restores callee-saved registers during prologue-epilogue
insertion pass. I would like to present a new approach where we expose callee-saved register
constraints early in the backend pipeline. This creates more opportunities for the optimizers
and gives good performance gains. Interestingly, we achieve per-register shrink-wrapping for
free. However, this makes emission of CFI directives much more complicated.
I am currently in the process of upstreaming this work. The proof-of-concept branch is publicly
available here: https://github.com/llvm/llvm-project/pull/90819 I have only tried this approach
on RISCV, but it could be applied to other targets as well.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-llvm:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-llvm:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GVDEQA/feedback/)

---

### Moving work into the middle end

- **Speakers:** Jon Chesterfield
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 11:05 - 11:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6600-moving-work-into-the-middle-end/)

#### Abstract

The IR passes of LLVM are a happy place. Easy to reason about, easy to test, easy to debug. SSA form is a really great idea.
This talk sketches the (positive!) experience of writing a couple of classically back end tasks in the middle end instead of their proper place. One is a variant on register allocation - assigning variables to offsets in some buffer. The other is the ABI themed challenge of eliminating variadic functions. Maybe time will allow for an example of pulling work out of clang.
More speculatively, what else could be lifted to IR?

#### Related Links

- [LLVM](https://github.com/llvm/llvm-project/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-llvm:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-llvm:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/Z8EFY8/feedback/)

---

### Improving compile-time computation of object size

- **Speakers:** Serge « sans paille » Guelton
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 11:30 - 11:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5201-improving-compile-time-computation-of-object-size/)

#### Abstract

The compiler intrinsic __builtin_object_size and the LLVM intrinsic llvm.objectsize are used to compute the amount of memory allocated given an address. They play an important role in several security-related passes. This talk describes their behavior, where they are used within LLVM and the recent improvements made to their evaluation.
Actually both _FORTIFY_SOURCE, -fsanitize=undefined and -fsanitize=address rely at some point on an efficient implementation of llvm.objectsize and how it is folded by the compiler.
I once wrote a small testbed[0] to compare gcc and clang wrt. the folding of __builtin_object_size and they were mostly on par, until something changed and clang started to stop folding some expressions. Using that story as an Ariadne's thread, we'll dive into the folding of this intrinsic, how it's used by various sanitizer and how it has been improved over the past few months. 
[0] https://github.com/serge-sans-paille/builtin_object_size-test-suite

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-llvm:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-llvm:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BYUVLT/feedback/)

---

### O_o [ Flang + WASM ] o_O

- **Speakers:** Serge « sans paille » Guelton
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 11:50 - 11:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5202-oo-flang-wasm-oo/)

#### Abstract

Fortran => Scientific Computing => Performance
Wasm => In Browser => Portability
Why would someone want to have both?
Can Flang actually do that?

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-llvm:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-llvm:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BFNB7Q/feedback/)

---

### Things are coming together for Flang tooling

- **Speakers:** Tim Heldmann, Peter Arzt
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 12:00 - 12:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6623-things-are-coming-together-for-flang-tooling/)

#### Abstract

At the Scientific Computing Institute at TU Darmstadt, we have experience with developing LLVM-based tools. In the past, however, we usually focused on C/C++ codes via the Clang compiler [1,2]. With the change to flang-new [3] as the default LLVM Fortran frontend, we were interested in developing tooling for Fortran codes. In this talk we want to take you through our journey towards flang‑new based Fortran tooling. After building ~legacy~ established Fortran codes [4,5] with flang-new we wrangled with OpenMPI, employed static analysis tools inside the compile pipeline, and measured performance with the Score‑P [6] profiling library.
We will conclude our talk by presenting first results and describing our first impressions working with the evolving flang-new infrastructure.
This talks is intended for people with an interest in Fortran applications, tooling, or a general curiosity in the possibilities given by the LLVM infrastructure.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-llvm:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-llvm:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZZE987/feedback/)

---

### An introduction to Torch-MLIR

- **Speakers:** Marius Brehler
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 12:25 - 12:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6643-an-introduction-to-torch-mlir/)

#### Abstract

The Torch-MLIR project [1] builds a bridge between the world of machine learning and the LLVM project by providing compiler support from the PyTorch ecosystem to the MLIR ecosystem. This short tutorial covers:

The projects structure and how to build it
The TorchOnnxToTorch conversion
Decomposing complex ONNX
Lowering from Torch to LinAlg and other lower level dialects

Furthermore, it is discussed how you can get involved and what opportunities especially exist for first time contributors to contribute (code) to the project.
[1] https://github.com/llvm/torch-mlir/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-llvm:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-llvm:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MZTPHR/feedback/)

---

### MLIR-based Data Tiling and Packing for Ryzen AI NPU

- **Speakers:** Jorn Tuyls
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 12:50 - 13:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6641-mlir-based-data-tiling-and-packing-for-ryzen-ai-npu/)

#### Abstract

The Ryzen AI NPUs consist of an array of vector processors and programmable interconnect to allow granular control of compute and data movement to achieve high performance and power efficiency. This talk presents a MLIR-based data tiling and packing design for these NPUs that leads to optimized machine instructions. Specifically, it shows how we can derive and optimize how data flows through the array from high-level tiling decisions and how we can efficiently utilize a high degree of data packing by leveraging low-level DMA control and capabilities.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-llvm:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-llvm:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FD78FE/feedback/)

---

### An introduction to building and using LLVM libc

- **Speakers:** Peter Smith
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 13:15 - 13:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5456-an-introduction-to-building-and-using-llvm-libc/)

#### Abstract

LLVM libc has been steadily growing over the past few years. From its origins as an overlay to be used on top of an existing libc, LLVM libc is now complete enough and scalable enough to be used on embedded toolchains too.
This talk will contain:
* LLVM libc's current status.
* Why you might want to use LLVM libc. 
* How to build it for linux and an embedded system.
* How to use a prebuilt example from LLVM Embedded Toolchain for Arm.
* Other uses including the Google Pigweed SDK.
LLVM libc in llvm-project https://github.com/llvm/llvm-project/tree/main/libc

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-llvm:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-llvm:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7HBSAB/feedback/)

---

### Programming is fun; Testing is needed; Infra is …

- **Speakers:** Jan-Patrick Lehr
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 13:45 - 14:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6644-programming-is-fun-testing-is-needed-infra-is-/)

#### Abstract

The LLVM compiler infrastructure uses a range of resources for testing various project components, including Buildbots, Buildkite, and GitHub Actions. However, the diversity of these technologies can be confusing, particularly for new maintainers. I personally found it challenging to understand. The introduction of the new CI/CD admin role and the discussions in the RFC are promising developments that should help clarify these complexities.
AMD ROCm™ is based on the LLVM project, which is why AMD is deeply invested in supporting its development. This includes providing resources to test the AMDGPU code generation backend and various GPU offloading programming models. Consequently, AMD maintains a range of upstream buildbots for this purpose.
In this presentation, I discuss the motivation and objectives behind the AMD ROCm™ compiler buildbots and related initiatives. I share my two-year journey, which began with inheriting a single buildbot, then another, and eventually maintaining multiple machines and bot configurations. I delve into the technical challenges I encountered and the solutions I implemented. I also touch on non-technical issues from my perspective and how they were resolved by both me and the community. The presentation concludes with a forward-looking perspective on potential additions to the upstream test infrastructure to address existing blind spots from our point of view.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-llvm:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-llvm:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FK8C8B/feedback/)

---

### Profile-Guided Optimization (PGO) in LLVM: current challenges from the adopter perspective

- **Speakers:** Alexander Zaitsev
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 14:10 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4109-profile-guided-optimization-pgo-in-llvm-current-challenges-from-the-adopter-perspective/)

#### Abstract

Profile-Guided Optimization (PGO) is a well-known compiler optimization technique that brings runtime statistics about how an application is executed to the Ahead-of-Time (AoT) compilation model. However, this technique is not widely used nowadays.
In this talk, I want to discuss with a wider audience typical issues that I met with PGO implementation in LLVM-based compilers (like Clang and Rustc). During my work on the Awesome PGO project, I gathered a lot of interesting data points and insights about current PGO issues in the ecosystem (mostly with LLVM-based tools since I prefer using LLVM), and discussed many issues with different stakeholders like end-users, maintainers, and application developers. We will talk about:

PGO documentation issues across compilers
Different PGO integration states across LLVM-based compilers
PGO awareness across the industry
Strengths and weaknesses of different PGO modes for different use cases in real-world
Top blockers for PGO adoption
And many other things!

I believe that after the talk more people will be aware of PGO, aware of usual PGO blockers with LLVM, and know more about how to avoid these limitations in practice.
Target audience: LLVM users (especially LLVM-based compiler engineers and LLVM adopters)

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-llvm:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-llvm:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PEX88V/feedback/)

---

## Low-level AI Engineering and Hacking (27)

### The Local AI Rebellion

- **Speakers:** Roman Shaposhnik
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 09:00 - 09:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6159-the-local-ai-rebellion/)

#### Abstract

Our freedom to use, develop, and share software in general has never been more threatened than by the recent efforts to centralize and control AI. This talk will focus on what the "Local LLaMA" movement is doing to democratize AI and preserve software freedom for hackers, by developing open source projects like llamafile and llama.cpp. This talk will cover the technical challenges we've faced, making LLMs run fast on personal computers. It will also cover the organizational challenges we'll encounter facilitating respectful projects that can scale to include the same number of contributors as the Linux Kernel.

#### Related Links

- [llamafile](https://github.com/Mozilla-Ocho/llamafile/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/S8SHUX/feedback/)

---

### Hugging Face ecosystem for Local AI/ ML

- **Speakers:** VB
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 09:05 - 09:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6341-hugging-face-ecosystem-for-local-ai-ml/)

#### Abstract

Hugging Face is an open-source company that creates libraries such as transformers, tokenizers, safetensors, llama.cpp, ratchet, and much more.
In this talk, we'll delve into the Hugging Face stack and how different local AI frameworks leverage it. We'll also discuss the pain points and joys this causes.
The talk's purpose is to start a dialogue about what support we can provide to make Local AI even more feasible.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GFRA8B/feedback/)

---

### Accelerating AI with open source hardware and software

- **Speakers:** William Jones, Jeremy Bennett
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 09:40 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5622-accelerating-ai-with-open-source-hardware-and-software/)

#### Abstract

These days it is easy to design your own AI hardware accelerators using cheap FPGA boards and open source tooling. It's even possible to turn these into ASICs using open source technology.
But how do you get such designs to integrate into your favourite open source AI tooling?
In this talk we'll take you end-to-end through the process of designing custom AI hardware and  integrating it into standard AI workflows, all using open source technology. We will cover:
* Designing your open AI hardware by extending the open RISC-V instruction set
* Creating a software layer to interface with and program it via OneAPI and the SYCL parallel programming language
* Integrating this software layer with existing open AI tooling
This talk draws on our experience with a number of projects at Southampton University and with companies developing next generation AI accelerators.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BKE7VT/feedback/)

---

### ZML: A High-Performance AI Inference Stack Built for Production and Multi-Accelerator Deployment

- **Speakers:** Rene Schallner, Guillaume Wenzek
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 10:00 - 10:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5923-zml-a-high-performance-ai-inference-stack-built-for-production-and-multi-accelerator-deployment/)

#### Abstract

In this talk, we’re introducing ZML, our open-source high-performance AI inference stack built for production on the foundations of the Zig programming language, OpenXLA, MLIR, and Bazel.
We’ll discuss the framework, how to get started, and how we use it to build high-performance inference solutions, with a strong focus on production readiness.
We’ll also highlight some of the “plumbing tools” built into ZML that make production-ready, cross-platform, multi-accelerator deployments seamless.
For example, we’ll demonstrate how providing just a few simple, easy-to-remember command-line options to the build command can produce a Docker image with a Linux binary capable of running on a wide range of runtimes. This includes NVIDIA CUDA, AMD ROCm, Google TPU, AWS Neuron accelerator runtimes, or even a CPU. The process also includes pushing the image to your container registry—all in one command. Identical executable, single image.
We’ll also go into the lengths ZML goes to in downloading and auto-packaging only the absolute essentials of the chosen runtimes at build-time, such as CUDA, ROCm, etc, significantly reducing the size of the built artifact, whether it’s an OCI image or a .tar file.
ZML is also developer-friendly, automatically providing the Zig compiler, language server, and pre-configured setups for VS Code and NeoVim. Its use of Zig, a systems programming language with low-level control and robust abstractions, supports efficient memory management, error handling, and software correctness—key factors for production-grade solutions.
With this talk, we’d like to share our excitement about ZML, its unique approach to simplifying the complexities of delivering production-ready AI systems, and how it enables developers to efficiently transition from development to deployment.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8GFZEP/feedback/)

---

### History and advances of quantization in llama.cpp

- **Speakers:** Tanya Dadasheva, Iwan Kawrakow
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5991-history-and-advances-of-quantization-in-llama-cpp/)

#### Abstract

A lot of progress in adoption of genAI we owe to quantization techniques. There are many of the new techniques that ggml/llama.cpp have used over the time.
It's not always easy to understand how the various formats work, in many cases it requires reading through the PRs that actually introduced the quantization format.
@Ikawrakow (Ivan Kawrakow) is the main person responsible for most of the modern quantization code. Looking through his PRs is generally the best way to learn but really curious you could come to this panel with him and bring your questions!
The panel will cover the experience with different quantization techniques in llama.cpp so far, the possibility of going below 2-bit quantization, QAT and other approaches out there.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VVBTGL/feedback/)

---

### quantizing your GGUF models using iterative refinement of the importance matrix

- **Speakers:** Robert Collins
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 11:00 - 11:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4915-quantizing-your-gguf-models-using-iterative-refinement-of-the-importance-matrix/)

#### Abstract

Presenting Llama-gguf-optimize, the result of work and research in creating high-quality quantizations for multilingual models, specifically of the salamandra series. With a focus on preserving language diversity, the project leverages llama.cpp’s importance matrix approach to minimize quantization loss across distinct language domains. This presentation will outline the scripts in the toolkit in terms of a systematic approach for quantizing your models using iterative refinement of the importance matrix (I-matrix) and evaluating quantization quality through KL-divergence metrics.

#### Related Links

- [llama-gguf-optimize homepage](https://github.com/robbiemu/llama-gguf-optimize)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BHCJLB/feedback/)

---

### Apache Arrow: The Great Library Unifier

- **Speakers:** Matthew Topol
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 11:20 - 11:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4801-apache-arrow-the-great-library-unifier/)

#### Abstract

There are multiple low-level libraries used for AI development with GPUs such as PyTorch, libcudf, and TensorFlow. Each has pros and cons with different available algorithms and functions, so how do you pick which one to use? Instead of having to pay the cost for copying data back and forth between GPU and CPU, data can be passed around between these various libraries while leaving it on the GPU and sharing pointers to device data!
This talk will cover how to leverage the Apache Arrow data format and its C Device Interface, in conjunction with DLPack to connect these various libraries together for building low-level AI pipelines. We'll go over examples of handing off data between libraries without forcing extraneous copies from GPU to CPU and back, utilizing HuggingFace's Arrow formatted caches for training, and efficient conversion between Arrow and DLPack interfaces to unify multiple libraries for customized processing.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/Y33HWK/feedback/)

---

### Building Your (Local) LLM Second Brain

- **Speakers:** Olivia Buzek
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 11:50 - 11:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6542-building-your-local-llm-second-brain/)

#### Abstract

LLMs are hotter than ever, but most LLM-based solutions available to us require you to use models trained on data with unknown provenance, send your most important data off to corporate-controlled servers, and use prodigious amounts of energy every time you write an email.
What if you could design a “second brain” assistant with OSS technologies, that lives on your own laptop?
We’ll walk through the OSS landscape, discussing the nuts and bolts of combining Ollama, LlamaIndex, OpenWebUI, Autogen and Granite models to build a fully local LLM assistant. We’ll also discuss some of the particular complexities involved when your solution involves a local quantized model versus one that’s cloud-hosted.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/79U8NK/feedback/)

---

### How Llamagator helps to implement LLM-as-a-Judge concept on your local machine

- **Speakers:** Sergy Sergyenko
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 11:55 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5584-how-llamagator-helps-to-implement-llm-as-a-judge-concept-on-your-local-machine/)

#### Abstract

In this talk, I explore how the landscape of large language model (LLM) accessibility has shifted dramatically. 
It is now possible to run these powerful models locally, right on your laptop, eliminating the need for cloud-based solutions like OpenAI.  Previously, the sheer size of LLMs, requiring massive GPUs and RAM, made local deployment impossible for most developers. This reliance on cloud services limited experimentation, customization, and affordability.
My presentation focuses on Llama.cpp, an inference engine enabling efficient execution of LLMs, including Meta's Llama, Qwen, and Mistral models, on CPUs. 
I detail the process of acquiring, building, and quantizing models for local use, showcasing how Ruby bindings and a built-in HTTP server simplify interaction.  I also introduce two open-source tools I've created: Llamagator and Rspec-Llama. 
Llamagator is a Rails application, streamlines the management, testing, and comparison of various LLMs, both local and cloud-based. With it, you can create prompts, define assertions, and evaluate model performance and easily implement pattern of LLM-as-a-judge.
Rspec-Llama extends Rspec with a specialized DSL for interacting with and validating responses from LLMs, making it easier than ever to integrate these models into testing workflows. These tools, combined with the ability to run LLMs locally, empower developers to explore AI's potential without relying on external providers.

#### Related Links

- [LLamagator](https://github.com/aifoundry-org/llamagator)
- [Rspc-Llama](https://github.com/aifoundry-org/rspec-llama)
- [Slides from the talk I conducted before](https://docs.google.com/presentation/d/1w2I_gnTijOSul0SiIUmJ5GNHwcdfX4OAMEHQIiGt3K4/edit#slide=id.g2d49c4c4d82_1_31)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7MHC8J/feedback/)

---

### Data Prep Kit: Open Source Data Engineering for LLMs

- **Speakers:** Joe Olson
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 12:00 - 12:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6761-data-prep-kit-open-source-data-engineering-for-llms/)

#### Abstract

Introducing Data Prep Kit (DPK) - an open source data engineering framework for LLMs. DPK was developed internally by IBM to assist with the development of its open source Granite family of LLMs and released in 2024. DPK is built on Kubeflow pipelines, running on scalable compute ranging from a developer's laptop to massive clusters. In addition Kubeflow pipelines allows the community to collaborate on common LLM data engineering workflows problems, such as determining licensing state of the data and determining the state of its GDPR compliance.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DSJKQC/feedback/)

---

### The Model Openness Framework (MOF)

- **Speakers:** Arnaud Le Hors
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 12:05 - 12:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5058-the-model-openness-framework-mof-/)

#### Abstract

The Model Openness Framework (MOF) defines a ranked classification system that rates machine learning models based on their completeness and openness, following principles of open science, open source, open data, and open access. The MOF aims to prevent misrepresentation of models claiming to be open, to guide researchers and developers in providing all model components under permissive licenses, and to help individuals and organizations differentiate models that are truly open from those that are not.
This session will give attendees an overview of the MOF and practical information on how they can use it along with the Model Openness Tool (MOT) to find out which models are really open and evaluate how their own models line up with the MOF.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TLYHAF/feedback/)

---

### Building AI Applications on Kubernetes: Leveraging Instructlab and the Bee Agent Framework

- **Speakers:** Martin Hickey, Paul Schweigert
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 12:10 - 12:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5348-building-ai-applications-on-kubernetes-leveraging-instructlab-and-the-bee-agent-framework/)

#### Abstract

Join us for an enlightening talk on building AI agents on Kubernetes! Unlike LLMs which are limited by the data they were trained on, agents use external tools to obtain up-to-date information, optimize workflow and create subtasks autonomously to achieve complex goals. Our speakers, seasoned experts in AI and Kubernetes, will share insights into the benefits of using Kubernetes for deploying AI agents and provide best practices for designing and implementing them using open source tools. We'll do a deep dive on the Bee Agent Framework, which makes it easy to build scalable agent-based workflows with your model of choice. We will show how to use Instructlab to add specialized knowledge to an existing model without the need for fully fork and fine-tune. Don't miss out on this opportunity to level up your AI skills and learn how to create intelligent agents that can interact with users and perform various tasks. See you there!

#### Related Links

- [InstructLab Open Source Community](https://instructlab.ai/)
- [Bee Agent Open Source Framework](https://i-am-bee.github.io/bee-agent-framework/)
- [Kubernetes](https://kubernetes.io/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WQPYGT/feedback/)

---

### GPUStack: Building a Simple and Scalable Management Experience for Diverse AI Models

- **Speakers:** Lawrence Li, Frank Mai
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 12:20 - 12:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5487-gpustack-building-a-simple-and-scalable-management-experience-for-diverse-ai-models/)

#### Abstract

Outstanding tools like llama.cpp, Ollama, and LM Studio have made life significantly easier for developers. Running large language models (LLMs) on laptops has become remarkably convenient. However, inference engines and their wrappers don’t address the following challenges:
  1.  Scaling your solution as your team grows.
  2.  Supporting models beyond LLMs, such as using diffusion models for role-playing applications, TTS models for NotebookLM equivalents, rerankers and embeddings for retrieval-augmented generation (RAG), and more.
Today, both models and inference engines are highly diverse and rapidly evolving, while GPU resources remain fragmented and heterogeneous. In this talk, we will share our experience building GPUStack — a platform designed to help developers abstract away these complexities and focus solely on building APIs for AI applications.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FRVVRL/feedback/)

---

### Self-hosted LLMs at a scale with Paddler

- **Speakers:** Mateusz Charytoniuk
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 12:40 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4590-self-hosted-llms-at-a-scale-with-paddler/)

#### Abstract

Paddler is an open-source llama.cpp load balancer designed to address unique challenges that Large Language Models pose. 
Typical balancing algorithms like round-robin or least-connections are not the most efficient approaches. 
To introduce predictability into your infrastructure, Paddler reaches for alternative solutions that account for unpredictable response times while being able to scale services up and down at any moment.
This talk will demonstrate Paddler's general design concepts (the "why") and some primary use cases (the "how").

#### Related Links

- [GitHub Repository](https://github.com/distantmagic/paddler)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LLQS3Z/feedback/)

---

### RamaLama: Making working with AI Models Boring

- **Speakers:** Eric Curtin
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 13:00 - 13:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4486-ramalama-making-working-with-ai-models-boring/)

#### Abstract

Managing and deploying AI models can often require extensive system configuration and complex software dependencies. RamaLama, a new open-source tool, aims to make working with AI models straightforward by leveraging container technology, making the process "boring"—predictable, reliable, and easy to manage. RamaLama integrates with container engines like Podman and Docker to deploy AI models within containers, eliminating the need for manual configuration and ensuring optimal setup for both CPU and GPU systems.
This talk will introduce RamaLama’s key features, including support for multiple AI model registries (Ollama, Hugging Face, and OCI), simplified commands for running models as chatbots or REST API services, and compatibility with alternative AI runtimes like llama.cpp and vllm. We’ll explore RamaLama’s unique capabilities, such as generating Podman quadlet files for edge deployments and Kubernetes YAML for scalable deployment, demonstrating how it allows developers to seamlessly transition from local experimentation to production. Join us to learn how RamaLama enables frictionless, containerized AI model deployment for developers and system administrators alike.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MXTH7P/feedback/)

---

### Building AI Applications from your desktop with Podman AI Lab

- **Speakers:** Cedric Clyburn, Stevan Le Meur
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 13:20 - 13:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4813-building-ai-applications-from-your-desktop-with-podman-ai-lab/)

#### Abstract

Generative AI is revolutionizing how we build modern applications, but for developers, it can be daunting, particularly with evaluating models, building with Gen AI, and the path to production. But, it doesn’t have to be worrisome! Join us in this session to be ahead of the curve when it comes to AI-enabled cloud-native application development. 
Using container technology and open source models from Hugging Face, we’ll show how to practically integrate Gen AI in an existing application from your local development environment and ultimately deploy it onto Kubernetes. Why work with local and open-source models? From reducing cloud computing costs, keeping control of your sensitive data, and alleviating vendor-locking, it’s an increasingly popular way for developers to prototype AI applications quickly. We’ll demonstrate a sample of the whole AI journey, starting from assessing models, building applications with LLMs, and deploying/serving AI applications.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GYCMRX/feedback/)

---

### From Supercomputer to Raspberry Pi: Building Open Source Polish Language Models

- **Speakers:** Bielik Team, Maciej, Pawel Cyrta, Adrian
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 13:40 - 13:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6660-from-supercomputer-to-raspberry-pi-building-open-source-polish-language-models/)

#### Abstract

The creation of Polish language models presents a unique set of challenges and opportunities in the Polish AI landscape. Through collaboration between SpeakLeash Foundation and Academic Computer Centre Cyfronet AGH, we've established Bielik - a family of open-source language models designed to democratize access to AI. 
Our journey began with training larger models of 7B and 11B parameters, providing us with valuable experience and knowledge about training models in the Polish language. This experience has led us to our latest effort: developing a compact 1.5B parameter model that brings advanced language capabilities to edge devices like Raspberry Pi.
During this presentation, we'll explore the real-world challenges of training Polish language models, sharing technical insights from our transition from 11B to 1.5B parameters. We'll discuss our work with large Polish datasets, examining the intricacies of the training process for our compact model.
Our presentation will provide insights into the process of model development, from creating high-quality Polish language datasets to enhancing cooperation between an open-source foundation and academic institution. We'll also discuss the balance between model size and performance, highlighting how we make advanced language models accessible for practical use.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YMC3PV/feedback/)

---

### Tricks Learned from Training Large Open-Source Models

- **Speakers:** Marcus Edel
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 13:55 - 14:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6322-tricks-learned-from-training-large-open-source-models/)

#### Abstract

Tricks learned from training large open-source models on the example of WhisperSpeech, an open-source text-to-speech model.
WhisperSpeech is a new open-source text-to-speech model created by Collabora. It is based on recent research from the biggest AI labs (Google, Meta, Microsoft, OpenAI). It delivers high-quality speech that it learned from tens of thousands of hours of human speech recordings.
To deliver state-of-the-art quality, we scaled our models and training pipelines from hundreds to tens of thousands of hours of speech, and we share the lessons learned along the way. Nearly every component of your initial training process had to be replaced or tweaked heavily.
Challenges we'll briefly cover:
- Gone in 16 minutes: the importance of small-scale experiments.
- Full throttle: is 100% GPU utilization enough?
- Do you need a fancy framework? From single- to multi-GPU training.
- Are SSDs fast enough? WebDataset brings a 10x improvement.
- Does bigger always mean better? How to effortlessly scale AI models.
- Clouds, enthusiasts, or clusters? How to hunt down GPUs.
- Defending moats. How is a gaming 4090 different from an H100?

#### Related Links

- [Project Repository](https://github.com/collabora/WhisperSpeech/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YTARZM/feedback/)

---

### Synthetic Data: The Secret Ingredient in Better Language Models

- **Speakers:** Carol Chen, Cedric Clyburn
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 14:10 - 14:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4816-synthetic-data-the-secret-ingredient-in-better-language-models/)

#### Abstract

What’s powering the next generation of AI breakthroughs without relying on massive amounts of human-labeled data? Synthetic data generation has emerged as a transformative approach in enhancing Large Language Models (LLMs). This session demystifies synthetic data, exploring how it’s created, the innovative methodologies behind it, and its transformative impact on AI. Learn how synthetic data bridges knowledge gaps, accelerates training at scale, and enhances performance across tasks like natural language understanding and complex reasoning. Whether you're intrigued by the technical mechanics or its real-world applications, this talk will equip you with actionable insights to practice synthetic data generation and understand how synthetic data is rapidly changing the world of language models.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ELB3UP/feedback/)

---

### LLM Tool use in vLLM

- **Speakers:** Max de Bayser
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 14:25 - 14:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6214-llm-tool-use-in-vllm/)

#### Abstract

Tool use or function calling is one of the key features required to realize the promises of agentic applications. While it is still a novelty with a lot of experimentation and variation among model providers, protocols such as the OpenAI function calling extensions of the chat completions API have become a standard for a specific case of tool calling. In this talk we're going to explain how function calling works all the way from the API endpoint down to the actual model prompt. We're going to explore the different kinds of interaction flows that are possible with this protocol and what the current limitations are.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WURCKG/feedback/)

---

### Scoping out the Tenstorrent Wormhole

- **Speakers:** Peter Cawley
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 14:40 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5118-scoping-out-the-tenstorrent-wormhole/)

#### Abstract

The Tenstorrent Wormhole n300s PCIe accelerator board is available for purchase, featuring 672 RISC-V cores driving 466 TFLOP/s of FP8 matmul. There is an open source software stack, including kernel driver, user-mode driver and SDK. It'll be a challenge compressing it down to just 20 minutes, but I'll give a description of what the hardware can (and cannot) do, and try to convey how it differs from a conventional GPU. Expect to hear about network-on-chip, ethernet, RISC-V ISA extensions, memory-mapped I/O, and more.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZYE8VJ/feedback/)

---

### Building a new GGML backend: How, Challenges and Opportunities with Novel Accelerators

- **Speakers:** Martin Chang
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 15:00 - 15:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5122-building-a-new-ggml-backend-how-challenges-and-opportunities-with-novel-accelerators/)

#### Abstract

llama.cpp/GGML is a popular piece of software to run (mostly) large language models. It has support for common consumer and enterprise hardware like NVIDIA, AMD and Intel GPUs. But what if you want to onboarding new accelerators? Say a new architecture that promises to reduce power by a few fold. This talk aims to share the experience and knowledge learned building a (work in progress) GGML backend for Tenstorrent's Grayskull and Wormhole AI processor. And what's like to work with a brand new software stack.
Source code: https://github.com/marty1885/llama.cpp/tree/metalium-support/
Documentation: https://github.com/marty1885/llama.cpp/blob/metalium-support/docs/backend/Metalium.md

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VSX9UP/feedback/)

---

### Porting GGML to the NUX Kernel Development Framework.

- **Speakers:** Gianluca Guida
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 15:20 - 15:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5975-porting-ggml-to-the-nux-kernel-development-framework-/)

#### Abstract

NUX is an open source set of tools and libraries aimed at building custom kernels and user space environments for quick prototyping.
This talk will describe the effort of porting GGML to compile under NUX, both in kernel and user space. And how this can be useful for prototyping ML-centric custom OS kernels, running on modern hardware.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ECXXEM/feedback/)

---

### Expanding GGML Hardware Support using the Vulkan API

- **Speakers:** Ruben Ortlam
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 15:40 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6772-expanding-ggml-hardware-support-using-the-vulkan-api/)

#### Abstract

Most machine learning applications are accelerated using vendor-specific APIs like CUDA and ROCm. While alternatives like OpenCL and SYCL exist, they are not as well-supported. What if we could harness the broad driver support that is being put into gaming and use Vulkan compute shaders instead? In this talk, I will present advantages and disadvantages of this approach and the difficulties I had to overcome to create a Vulkan API backend for llama.cpp.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VEMA7A/feedback/)

---

### The bare metal perspective on AMD's GPU ASICs

- **Speakers:** Jon Chesterfield
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 16:00 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6241-the-bare-metal-perspective-on-amd-s-gpu-asics/)

#### Abstract

The compute machine running below the programmable shader abstraction of GPU programming models no longer looks much like it did in the 90s. It gained an integer branch unit for cheap control flow. "Shaders" can now spawn other shaders or write to the network. There can be x64 cores running in the same address space, cooperating through atomic instructions. 
Said abstraction is built on open source software. The ISA is documented. The driver is in your linux kernel already. Upstream LLVM knows how to emit machine code for the chip. If you want to mangle the existing stack out of all recognition the raw material is all on github to start from. If you disregard the official vendor supplied software stack entirely the machine still computes exactly what you told it to.
This talk will sketch what the hardware looks like as an embedded target and how you might go about bending it to your will. The limits of shader programming are not the limits of our world.

#### Related Links

- [LLVM](https://github.com/llvm/llvm-project/)
- [ROCm](https://github.com/ROCm/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CAAAKM/feedback/)

---

### wllama: bringing llama.cpp to the web

- **Speakers:** Xuan-Son Nguyen
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 16:20 - 16:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5154-wllama-bringing-llama-cpp-to-the-web/)

#### Abstract

As one of the main contributor of the llama.cpp project, I’ve explored ways to bring its capabilities to the web through WebAssembly, creating a frontend solution for on-device inference without the need for servers or external APIs. This talk shares my journey in implementing wllama, a lightweight TypeScript/JavaScript library designed to push llama.cpp’s limits in a web context. I’ll discuss my motivations, the implementation details, the challenges faced, and the future roadmap, offering insights into the technical and creative decisions behind the project.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZWGAP8/feedback/)

---

### Milliwatt sized Machine Learning on microcontrollers with emlearn

- **Speakers:** Jon Nordby
- **Room:** UB2.252A (Lameere)
- **Day:** Sunday
- **Time:** 16:40 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4524-milliwatt-sized-machine-learning-on-microcontrollers-with-emlearn/)

#### Abstract

It the recent year, generative AI models have come to dominate the discourse around artificial intelligence and machine learning. Both Large Language Models and other generative models for image/video/sound use huge deep learning models, running on expensive and energy intensive GPUs. However there are several other application areas of machine learning, operating under other contraints. One of these is the area of "TinyML", where machine learning is used to analyze sensor data on microcontroller-grade systems. A typical TinyML system is under 1 watt, under 1 MB of RAM and FLASH and under 10 USD bill-of-materials.
emlearn is an open-source project started in 2018, which provides machine learning inference implementations for microcontrollers. It is written in portable C99 code, and supports models trained with scikit-learn and Tensorflow/Keras. Since 2023 the emlearn project also provides bindings for MicroPython, a Python for microcontrollers.
In this talk we will talk about machine learning on microcontrollers; the applications, developments in the field over the last years, and current trends - both on software and hardware side. This niche of machine learning is extremely concerned with computational efficiency, and we believe that these perspectives may be useful also to developers working in different areas.

#### Related Links

- [emlearn project](https://github.com/emlearn/emlearn/)
- [emlearn-micropython](https://github.com/emlearn/emlearn-micropython)
- [Slides and notes](https://github.com/jonnor/embeddedml/tree/master/presentations/FOSDEM2025)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-ai:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-ai:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FE8WNW/feedback/)

---

## Matrix.org Foundation and Community (8)

### Matrix State of the Union

- **Speakers:** Greg Sutcliffe, Matthew Hodgson, Amandine Le Pape
- **Room:** K.4.201
- **Day:** Sunday
- **Time:** 13:00 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6236-matrix-state-of-the-union/)

#### Abstract

A quick update on all the latest progress on core Matrix development from the project founders.  Likely areas of focus include:
 * State Resolution improvements
 * Matrix 2.0 roll-out (including on matrix.org!)
 * Invisible Encryption and TOFU updates
 * Updates on Matrix uptake, especially in the public sector
 * Thoughts on mainstream Matrix, given the continued zeitgeist shift towards decentralisation
 * Possibilities for Matrix 3.0!

#### Related Links

- [The Matrix Specification](https://github.com/matrix-org/matrix-spec)
- [Matrix server implementations](https://matrix.org/ecosystem/servers/)
- [Matrix client implementations](https://matrix.org/ecosystem/clients/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-matrix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-matrix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SCVP7K/feedback/)

---

### Getting the Rust SDK running on webassembly

- **Speakers:** Timo Kandra
- **Room:** K.4.201
- **Day:** Sunday
- **Time:** 13:30 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5031-getting-the-rust-sdk-running-on-webassembly/)

#### Abstract

The Rust programming language is often hailed as a perfect companion to WebAssembly (Wasm), leading many to wonder: why aren’t matrix clients like Element Web fully leveraging the Rust SDK? Why does the JavaScript SDK remain the optimal choice for building Matrix-based webapps?
In this talk, we’ll explore the practical realities of running Rust SDKs in the web environment. While Rust offers powerful features and performance benefits and the great code quality of the Matrix Rust SDK, limitations like WebAssembly’s inability to directly access system-level APIs (such as retrieving timestamps) pose significant hurdles.
We’ll dive into the current state of Rust’s compatibility with WebAssembly for Matrix applications, highlighting what does work—most notably the crypto crate—and detailing the remaining steps to bring the full Rust SDK, up to the UI crate, into the browser. Additionally, we’ll discuss the challenges of creating JavaScript bindings for Rust code, including the current limitations of tools like uni-ffi and the manual effort required for bridging these worlds.
Join us for the latest updates, insights, and perhaps even a sneak peek of a Rust SDK-powered webapp prototype. Whether you're a Rust enthusiast, a Matrix developer, or simply curious about WebAssembly’s potential, you might find it interesting what is possible as of today.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-matrix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-matrix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KSG8AZ/feedback/)

---

### Demystifying Federation in Matrix

- **Speakers:** Kegan Dougal
- **Room:** K.4.201
- **Day:** Sunday
- **Time:** 14:00 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5016-demystifying-federation-in-matrix/)

#### Abstract

Step into the TARDIS as we go on a deep-dive to explain how federation in Matrix works. We'll cover
the protocol, its robustness qualities and how it relates to CRDTs, all whilst operating safely in
Byzantine environments far larger than consensus-based blockchains. To aid in our journey,
interactive visualisations backed by real homeservers are used to explain core concepts via
TARDIS and other tooling.

#### Related Links

- [Time Agnostic Room DAG Inspection Service](https://github.com/matrix-org/tardis)
- [matrix.org](https://matrix.org/)
- [Complement: Server testing suite](https://github.com/matrix-org/complement)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-matrix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-matrix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BJSYHQ/feedback/)

---

### State of Synapse: where we're at, Matrix 2.0, and the future

- **Speakers:** Erik Johnston
- **Room:** K.4.201
- **Day:** Sunday
- **Time:** 14:30 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5773-state-of-synapse-where-we-re-at-matrix-2-0-and-the-future/)

#### Abstract

A dive into the state of Synapse, including what we've been up to, what Synapse even is and who it's for, and the challenges we're facing. We'll also talk about the recent efforts to support Matrix 2.0 and pushing the Matrix protocol further, how we're using Rust to fix performance bottlenecks, and where we're going in the future.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-matrix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-matrix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KJSTAE/feedback/)

---

### Building the World's First Server-to-Server Matrix Federation Bridge/Peer

- **Speakers:** Gabriel Engel
- **Room:** K.4.201
- **Day:** Sunday
- **Time:** 15:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5596-building-the-world-s-first-server-to-server-matrix-federation-bridge-peer/)

#### Abstract

This talk details our journey in implementing the Matrix server-to-server protocol for 100% Federation compatibility with Rocket.Chat. We've developed the world's first production-ready "server-to-server" bridge/peer, pioneering a new standard for open source servers interoperability.
Gabriel will kick off by explaining the architecture and high-level functionality of the native Matrix protocol server within Rocket.Chat’s mature microservices-based backend.
He'll then discuss the technical challenges we encountered—including programming language incompatibilities, crypto library issues, scaling architecture discrepancies, data schema hierarchy conflicts, and foundational differences in access control models/flows — and share how we addressed each of them in details.
This session is perfect for those directly working with Matrix server code or managing Matrix bridges. Gabriel’s presentation will provide a practical look at the obstacles and solutions involved in creating a federated communication system using the open-source Matrix protocol.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-matrix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-matrix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8CAWM7/feedback/)

---

### How Ubuntu Entered the Matrix

- **Speakers:** Schiano Grégory, Merlijn Sebrechts, Nils Büchner
- **Room:** K.4.201
- **Day:** Sunday
- **Time:** 15:30 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6061-how-ubuntu-entered-the-matrix/)

#### Abstract

Ubuntu has recently adopted Matrix for instant messaging. This talk explains how we went through the process of moving from many different messaging platforms to Matrix, and how we ensure our users have the best experience on Matrix.
Are you interested in adopting Matrix for your community? Or are you a user curious about Matrix? This talk explains some best-practices and possible pitfalls of Matrix, and how to make the best of this federation.
It covers a lot of different aspects from governance and moderation to server operations.

How we combat spam on Matrix using Mjolnir and the "Community Moderation Effort" (CME) banlists.
How we decide on community policies with the Matrix Council.
Our unique approach to moderation where we coach people to be better members of our community.
How we automatically manage the homeserver using Juju.
Our extensive documentation to guide users towards a better experience.

The talk will end in a Q&A session where people can talk directly to the Ubuntu Matrix Operators to ask them about their experience and discuss possible future improvements.

#### Related Links

- [Juju operator to manage a synapse server](https://github.com/canonical/synapse-operator)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-matrix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-matrix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FVG8HR/feedback/)

---

### Robrix: a pure Rust multi-platform Matrix Client and more

- **Speakers:** Kevin Boos
- **Room:** K.4.201
- **Day:** Sunday
- **Time:** 16:00 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5841-robrix-a-pure-rust-multi-platform-matrix-client-and-more/)

#### Abstract

Robrix is a new up-and-coming Matrix client for power users, written from scratch in Rust to demonstrate and drive the featureset of Project Robius, a multi-platform app dev framework. Thanks to the efforts of the Robius software stack, and in particular the Makepad UI toolkit. Robrix runs seamlessly across Android, iOS, macOS, Linux, and Windows (with web and OpenHarmony to come), all without a single line of platform-specific code.
This talk will cover the general architecture and features of Robrix, our experience developing apps in Rust and the challenges encountered therein, and how Robrix's needs have driven the development of ecosystem components. We'll demonstrate the high performance and efficiency of Robrix and its underlying software stack, along with some of its more "unique" features, such as a dockable tabbed UI view of multiple rooms akin to your favorite IDE (which works identically on smartphones, tablets, and desktops). 
Finally, we'll lay out our future vision for Robrix as an open-source "hub" app, bringing together many aspects of the fediverse beyond Matrix chat: decentralized social networks, decentralized identity providers like OpenWallet, and the integration of secure AI features via local LLMs that maintain data privacy & sovereignty.

#### Related Links

- [Recent presentation about Robrix in October 2024](https://www.youtube.com/watch?v=DO5C7aITVyU)
- [Presentation slide deck about Robrix](https://github.com/project-robius/files/blob/main/GOSIM%20China%202024/Robrix%20Talk%20GOSIM%20China%20October%2017%2C%202024.pdf)
- [Robrix repository homepage on Github](https://github.com/project-robius/robrix)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-matrix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-matrix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8YJDTA/feedback/)

---

### MatrixRTC: Building Real-Time Applications on Matrix

- **Speakers:** Timo Kandra, Robin Townsend, Will Hunt
- **Room:** K.4.201
- **Day:** Sunday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5034-matrixrtc-building-real-time-applications-on-matrix/)

#### Abstract

MatrixRTC is poised to become the foundation for real-time applications built on the Matrix protocol, unlocking new possibilities for secure, extensible communication. This session will dive into the latest developments in MatrixRTC, focusing on the final pieces of its proposed specification and showcasing how it enables a broad range of real-time applications.
We’ll start with a technical introduction, covering critical concepts like to-device key sharing and RTC room state. From there, the session will transition into practical guidance, demonstrating how developers can build their own real-time solutions using MatrixRTC, LiveKit, and the Matrix SDK.
This talk will provide you with the insights and tools to use the potential of MatrixRTC for your own projects. Join us to explore the future of real-time applications on Matrix!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-matrix:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-matrix:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KQ7BGT/feedback/)

---

## Microkernel and Component-Based OS (10)

### Welcome to the Microkernel and Component-Based OS Devroom

- **Speakers:** Udo Steinberg, Alexander van der Grinten
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 15:00 - 15:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6190-welcome-to-the-microkernel-and-component-based-os-devroom/)

#### Abstract

This short talk will serve as a welcome and introduction to the Microkernel and Component-Based OS devroom. We will quickly go over the rules of the devroom, as well as introducing you to the devroom managers and answering general questions.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-microkernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-microkernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QUFZPJ/feedback/)

---

### HelenOS: 20 years of past history, 20 years of future vision

- **Speakers:** Martin Decky
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 15:05 - 15:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5234-helenos-20-years-of-past-history-20-years-of-future-vision/)

#### Abstract

The basic foundations of the HelenOS project as we know it today have been laid in late 2004 and early 2005. This 20th anniversary is an opportunity not only for the usual status update talk about the recent developments and near future plans, but also a great opportunity to look at the bigger picture.
While the first 5 years of HelenOS were exploratory and the next 10 years were defined by dynamic expansion on all fronts by more than 80 individual contributors, the last 5 years could be fairly described as maintenance with much less activity.
HelenOS is alive and well, but there are no longer any low-hanging fruits in terms of major subsystems or frameworks missing. There is obviously still a sheer amount of individual hardware devices, file systems, standard APIs and polished features that could be supported or implemented, but that is clearly a less rewarding endeavor for potential contributors than working on the major building blocks like before.
Are there generic lessons to be learned from the story of HelenOS? Is every community-driven non-mainstream OS destined to end up in this "serene valley"? How do we plan to get out of it? The goal of this talk is to discuss these questions.

#### Related Links

- [HelenOS project website](https://www.helenos.org/)
- [HelenOS sources](https://github.com/HelenOS/helenos/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-microkernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-microkernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JF7PZZ/feedback/)

---


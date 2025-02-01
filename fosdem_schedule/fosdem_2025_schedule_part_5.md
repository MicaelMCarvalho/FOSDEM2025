# FOSDEM 2025 Schedule - Part 5 of 11

*Generated on 2025-02-01*

## Table of Contents

- [GCC (GNU Toolchain) (11)](#gcc-gnu-toolchain-11)
- [Geospatial (9)](#geospatial-9)
- [Go (16)](#go-16)
- [Government Collaboration (11)](#government-collaboration-11)
- [HPC, Big Data & Data Science (20)](#hpc,-big-data-&-data-science-20)
- [Identity and Access Management (17)](#identity-and-access-management-17)
- [Image-Based Linux and Boot Integrity (8)](#image-based-linux-and-boot-integrity-8)
- [Inclusive Web (8)](#inclusive-web-8)
- [JavaScript (7)](#javascript-7)
- [Kernel (17)](#kernel-17)

## GCC (GNU Toolchain) (11)

### Debug fission - Separating debug symbols from executables

- **Speakers:** Johan Herland
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 18:25 - 18:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5089-debug-fission-separating-debug-symbols-from-executables/)

#### Abstract

An introduction and exploration of how to separate debug information from C/C++ build artifacts in order to save space and time when building large codebases. Is it possible to have fast builds without stripping away debug symbols altogether? How would you integrate this into a larger build system?
After a quick introduction to debug symbols, we dive into various compiler and linker options to make an executable smaller without stripping away its debug capabilities. We compare multiple approaches for splitting debug symbols from executables, and demonstrate their pros and cons.
After looking at the details, we take a step back and show how to integrate these techniques into larger build systems like CMake and Bazel, where the effect of split debug symbols is much more noticeable.

#### Related Links

- [Related blog post](https://www.tweag.io/blog/2023-11-23-debug-fission/)
- [GCC Wiki on Debug Fission](https://gcc.gnu.org/wiki/DebugFission)
- [Slides](https://docs.google.com/presentation/d/155z7Mc3807TjE_-u7PDfpvA5MMRHNrbXJvqpngzTrx4/edit?usp=sharing)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-gcc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-gcc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/REGNJJ/feedback/)

---

### Cross-platform JIT compilers with GNU Lightning

- **Speakers:** Paul Cercueil
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 18:45 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6070-cross-platform-jit-compilers-with-gnu-lightning/)

#### Abstract

Writing a Just-In-Time (JIT) compiler is a complex task. For that reason, libraries like libgccjit were developed to ease the process; but most often than not, JIT compilers are written from scratch, and only target one or two architectures.
In this talk I am going to present GNU Lightning, a cross-platform library that can be used to generate machine code at run-time. I will present its strengths and weaknesses, how to use it, and why I decided to use it in my JIT compiler project.

#### Related Links

- [GNU Lightning website](https://www.gnu.org/software/lightning/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-gcc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-gcc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9JFH3N/feedback/)

---

## Geospatial (9)

### MapTCHA, the open source CAPTCHA that improves OpenStreetMap

- **Speakers:** Anna Zanchetta
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 10:30 - 10:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5879-maptcha-the-open-source-captcha-that-improves-openstreetmap/)

#### Abstract

Bots and spam are challenges for online platforms. Traditional CAPTCHAs help block bots, but often involve improving proprietary maps and software, while exposing user information to third-party CAPTCHA providers. OpenStreetMap (OSM) has many objects remaining to be mapped, but the quality of AI-generated objects is not high enough for direct inclusion. We introduce “MapTCHA”, a CAPTCHA that leverages the uncertainty of interpreting imagery with computer vision, and provides human verification for AI predictions: users are asked to identify images containing correctly interpreted objects, e.g. building outlines.
We separate known positive cases, where both the AI prediction and OSM contain an object, from unknown cases, where objects are only in the prediction. We also generate known negatives from areas where objects are neither in OSM nor in the prediction. We show a mix of these images without telling the user which are which. Humans are validated by confirming the known positives and negatives, and we determine the truth of the unknown images by aggregating users’ responses through voting. When the voting indicates high confidence that an object exists, we suggest the location for OSM mapping.
Our prototype identifies buildings using aerial imagery with high enough resolution to visualise individual buildings and medium-sized objects. Image recognition is provided by fAIr, an open-source AI-assisted mapping system developed by the Humanitarian OpenStreetMap Team (HOT). It allows the training and fine-tuning of pre-trained machine learning models to segment building footprints.
Future plans include expanding to more objects and types of imagery; refining AI models; integrating MapTCHA into various login systems; and enhancing the user interface.
In this session we will talk about how we are building this solution, how it might enhance mapping efforts in OSM that will support projects on the ground, and some of the challenges of working with AI derived data.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-geospatial:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-geospatial:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EG8WZ9/feedback/)

---

### Discovering indoor environments and positioning systems

- **Speakers:** Maxim Van de Wynckel
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 11:00 - 11:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4526-discovering-indoor-environments-and-positioning-systems/)

#### Abstract

Have you ever gotten lost in a building and wished they had some sort of navigation system or at least a floor plan? I have, unfortunately, and it was only later that I realised that not only they had a floor plan online - but they had a navigation app for that building. The reality is that a user who is not familiar with a building will not find such an app until it's too late. Indoor environments sometimes have public floorplans available via some service. Similarly, more and more indoor positioning systems are being deployed in buildings to provide navigation services or asset tracking. However, as a person visiting a building, you are often not aware that these services exist or where to find them. Even if some global registry exists to discover this data, it is often proprietary, discouraging developers from interfacing with such systems. I want to bring a shift into the landscape of indoor positioning systems and services and solve this! In this presentation, I will talk about discovering indoor environments and positioning systems through proximity-based discovery methods and linked data. How nice would it be, that instead of downloading the FOSDEM app, you simply use Google Maps or any open-source navigation application to find the location of this talk?

#### Related Links

- [SemBeacon website](https://sembeacon.org)
- [SemBeacon GitHub](https://github.com/SemBeacon)
- [OpenHPS website](https://openhps.org)
- [Slides](https://sembeacon.org/slides/fosdem2025/?presenter)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-geospatial:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-geospatial:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/B3JHKY/feedback/)

---

### 15-minute city in 15 minutes

- **Speakers:** Ilya Zverev
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 11:30 - 11:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4627-15-minute-city-in-15-minutes/)

#### Abstract

By now everybody should know what a 15-minute city concept is. What amenities are accessible with a 15 minute walk? What parts of a city do not do well in this regard? Much has been talked about, but how would you get this information about your own city? Uhm... Find some maps online? They are outdated and use buckets that are a bit too big for local usage. Calculate those yourself? With what? There has been nothing on Github.
Until now. Here I will demonstrate how 15-minute maps are done, which open source tools help with calculations, and what further opportunities do this new tool provide.

#### Related Links

- [GitHub](https://github.com/Zverik/15minute/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-geospatial:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-geospatial:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DJB8MZ/feedback/)

---

### Panoramax: the full FLOSS alternative to share ground level imagery

- **Speakers:** Christian Quest
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 11:50 - 12:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4448-panoramax-the-full-floss-alternative-to-share-ground-level-imagery/)

#### Abstract

Panoramax is a FLOSS project initiated 2 years ago in France by OpenStreetMap France and the national geographic institute (IGN).
Its goal is to provide a decentralized way to share and publish street level imagery.
This session will present the current status of the project, the software stack and the standards on which we built Panoramax like STAC and EXIF.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-geospatial:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-geospatial:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WWCLB8/feedback/)

---

### Unlocking Open-Source Capabilities in the Copernicus Data Space Ecosystem

- **Speakers:** Pratichhya Sharma
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 12:20 - 12:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5112-unlocking-open-source-capabilities-in-the-copernicus-data-space-ecosystem/)

#### Abstract

The satellites of the Sentinel family are Europe's eye in space – managed by the European Space Agency (ESA). They observe the earth continuously and collect enormous amounts of data that provide valuable insights into environmental, climatic, and geospatial changes. These data are used for various applications, including Land Use and Land Cover (LULC) mapping, environmental monitoring, disaster response, climate change analysis, and agricultural monitoring.
The Copernicus Data Space Ecosystem makes these data freely available to users, along with tools for processing and analysis. It encourages researchers, developers, and organizations to use these products for various applications, from scientific studies to practical environmental monitoring solutions. These products include but are not limited to, Sentinel data, Digital Elevation Models (DEMs), mosaics, and service products like biophysical parameters such as FAPAR (Fraction of Absorbed Photosynthetically Active Radiation). In addition to these products, the ecosystem also provides a range of tools, including cloud-computing environments and APIs, to simplify and enhance the usability of Earth Observation data.
In this session, we will explore how, in addition to freely available data, the Copernicus Data Space Ecosystem provides several open-source capabilities to simplify and enhance EO data usability. These include a cloud-computing environment like JupyterLab, a user-friendly Copernicus Browser for easy data exploration, and APIs like STAC and openEO for streamlined data access and integration. By offering these resources openly, the Copernicus Data Space Ecosystem supports a growing community of users, helping them turn satellite data into actionable knowledge to address global challenges.

#### Related Links

- [Documentation of available services](https://documentation.dataspace.copernicus.eu/#/)
- [Sample examples](https://github.com/eu-cdse/notebook-samples)
- [Forum (Support for EO discussion)](https://forum.dataspace.copernicus.eu/)
- [Reuseable EO algorithms with a set of enough free credits for scientific research each month](https://marketplace-portal.dataspace.copernicus.eu/catalogue)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-geospatial:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-geospatial:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FS8RA3/feedback/)

---

### Terra Draw: Drawing on all the web maps!

- **Speakers:** James Milner
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 12:50 - 13:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4713-terra-draw-drawing-on-all-the-web-maps-/)

#### Abstract

Dealing with web mapping can be complicated, and when tasked with the requirement of drawing on one, things can quickly become a challenging, especially when dealing with complex requirements. Enter Terra Draw: an open source JavaScript library designed to simplify and standardise drawing functionality across popular web mapping libraries such as Leaflet, OpenLayers, Google Maps, MapboxGL JS, and MapLibreGL JS.
Terra Draw offers a versatile set of built-in drawing modes, enabling seamless creation of geometries. The library supports simpler geometry types like points lines and polygons, but also more complex modes like rectangles, circles and sectors. There is also advanced functionalities like snapping, rotation, and scaling, which often require significant effort to implement from scratch. These functionalities are designed to "just work" across the different mapping ecosystems.
The library’s modular design promotes extensibility, allowing developers to create custom drawing modes and adapters for new mapping libraries that may come along. Thanks to its decoupled architecture, any mode can work with any adapter, creating a multiplier effect. This flexibility also ensures that swapping out one mapping library should be much simpler, as the drawing logic is abstracted away from the mapping library.
In this talk, we’ll explore the origins of Terra Draw, demonstrate how to get started, and provide a glimpse of what's possible with it. Whether you're a seasoned developer or just starting with web maps, you'll walk away with practical insights on how Terra Draw can be used in your project.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-geospatial:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-geospatial:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SBHVFW/feedback/)

---

### Connecting the Geospatial Dots with Raku

- **Speakers:** Brian Duggan
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 13:20 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6141-connecting-the-geospatial-dots-with-raku/)

#### Abstract

Geospatial programming often requires stitching together a variety of formats, interfaces, APIs, libraries, tools and languages.   How can we fluidly download data from OpenStreetMap using the Overpass Query Language, run performant queries with GEOS, calculate projections with PROJ, store and manipulate GeoJSON or WKT-formatted data with duckdb's spatial extention, and then visualize things with a javascript library like Leaflet or Deck.gl?
This talk explores Raku's expressive and powerful style as we mesh together all of these things, creating new modules along the way, and leapfrogging ahead of other implementations with some of Raku's unique features such as NativeCall for native libraries, Grammars for parsing, multiple modes of interacting with command line tooling, and plentiful concurrency models.   Also let's see how we can reign in large language models so that we can apply them judiciously to our data and our code.
Links:
raku-geos, Geo::Basic, WebService::Overpass, Geo::Geometry, Duckie, WebService::Nominatum

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-geospatial:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-geospatial:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/T7CQ3Z/feedback/)

---

### OpenLayers, the reference web-mapping library

- **Speakers:** Olivia Guyot
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 13:35 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6058-openlayers-the-reference-web-mapping-library/)

#### Abstract

Interactive maps on the web have evolved a lot in the past years. OpenLayers is no exception: it has been around for more than a decade and has become a reference with its extensive feature set and excellent performance. As a landmark open-source project, it has received thousands of contributions over time while managing a very high level of quality.
In this talk we will look at the state of the library today, what it now allows and why, now more than ever, it is an essential part of every geospatial web application. From high-performance rendering of large datasets to on-the-fly satellite image processing, its list of features is so large that you will most likely discover things along the way. New formats, ever-improving WebGL rendering, a powerful new expression-based styling API, and more!
Whether you're a long-time user or just discovering OpenLayers, this session promises fresh insights and practical takeaways for leveraging its full potential.
Find the OpenLayers website here: https://openlayers.org/
And the GitHub repository here: https://github.com/openlayers/openlayers

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-geospatial:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-geospatial:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MYXCDD/feedback/)

---

### How to Save a Life

- **Speakers:** Skylar MacDonald
- **Room:** AW1.120
- **Day:** Saturday
- **Time:** 14:05 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4914-how-to-save-a-life/)

#### Abstract

You, Eleanor Shellstrop, are dead. You are in cardiac arrest. Your heart has stopped beating, you have stopped breathing, and medically speaking you have died. Not a great start to your day! But worry not: someone has called emergency services. This is the story of that call — and how open geospatial information just might help save your life.
This talk, presented by the CAD & Technical Lead at the London Ambulance Service, will discuss how we use open data to locate patients, how your phone sends live geospatial information to our control room, and the other open (and some not-open) data that our emergency medical service uses to save lives across London every day.
Expect high-level conversations about medical emergencies, but this talk is suitable for all ages.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-geospatial:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-geospatial:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/APPHRX/feedback/)

---

## Go (16)

### The state of Go

- **Speakers:** Maartje Eyskens
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5353-the-state-of-go/)

#### Abstract

What is new since Go 1.23. In this talk we'll bring you up to date with all upcoming changes to the Go language and the community!
Go 1.24 will be released in February 2024, we will be taking a look to all upcoming features as well as give an update on important changes in Go 1.23. This includes traditionally updates about the language, tooling, libraries, ports and most importantly the Go Community.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TEC7XG/feedback/)

---

### The Inner Workings of Go Generics

- **Speakers:** Anton Sankov
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 11:00 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5329-the-inner-workings-of-go-generics/)

#### Abstract

Generics have long been a hot topic in the Go community, with years of debate, research, and anticipation surrounding their introduction. In this talk, we'll trace the journey of generics in Go—from the early days of design discussions to their eventual implementation in Go 1.18. We'll cover the challenges that led to Go's unique approach to generics, the technical design decisions involved, and how they were implemented to balance simplicity with powerful functionality. Attendees will gain a deeper understanding of the compiler magic that makes Go generics possible and explore practical examples of how generics enhance type safety and flexibility without sacrificing Go's performance and readability principles. This talk is ideal for anyone curious about how generics work under the hood and what they mean for the future of Go.

#### Related Links

- [Slides](https://asankov.dev/go-generics)
- [Repo with notes](https://github.com/asankov/go-generics)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/73T89Y/feedback/)

---

### Swiss Maps in Go

- **Speakers:** Bryan Boreham
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 11:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6049-swiss-maps-in-go/)

#### Abstract

Did you know that the 'map' type has a whole new implementation as of Go 1.24?
Known as "Swiss Maps", they run as much as 60% faster and 25% smaller.
Originally created in 2016 as a C++ library, Swiss Map uses ingenious bit-manipulation techniques to get more throughput from your CPU.
We'll cover:

How does it work?
How do benchmarks look for the new maps?
New SIMD (single-instruction, multiple-data) support in the compiler.
Performance results from real-world applications.
Gotchas and caveats.

#### Related Links

- [Proposal to use Swiss Maps in the Go project](https://github.com/golang/go/issues/54766)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JDNNCG/feedback/)

---

### Privilege Separation In Go

- **Speakers:** Alvar Penning
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 12:00 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5302-privilege-separation-in-go/)

#### Abstract

Most computer programs run with far more privileges than necessary. Many techniques have been developed to drop privileges and split applications into multiple components, each of which can run with the least amount of privileges necessary to do its job. This can greatly reduce the impact of security bugs, as the affected component will hopefully no longer have the rights to spawn other processes or even access files. Relatively small architectural changes can result in huge security gains.
Most privilege separated daemons out there are written in C. However, it is also possible to do this in Go, as this talk will show with almost copy-pasteable examples targeting POSIX-like operating systems.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PPVTSZ/feedback/)

---

### Go-ing Easy on Memory: Writing GC-Friendly code

- **Speakers:** Sümer Cip
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 12:30 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5343-go-ing-easy-on-memory-writing-gc-friendly-code/)

#### Abstract

Motivation
Computer Science curriculums often focus on theoretical lessons, such as how garbage collection (GC) works under the hood or the trade-offs between different GC designs. However, there is much less emphasis on how to write GC-aware code in languages like Go. This is surprising since most of these practices are language-agnostic.
This is a significant gap, especially given GC's impact on application performance. Profiling data from real-world applications consistently shows that a considerable amount of time is spent on memory allocation and GC-related activities.
This talk will be a practical session on writing memory-efficient code, supported by an understanding of Go's garbage collection and memory allocation internals.
The talk
Introduction
I will begin by discussing the motivation behind this talk and explaining why this topic is crucial, backed by empirical profiling data from real-world applications.
Essentials
Next, I’ll provide a high-level overview (a 10,000-foot view) of stack, heap, and GC concepts. This segment will be brief but necessary to establish a foundational understanding. 
Main


Walk through real code examples and demonstrate techniques for writing memory-efficient Go code, such as avoiding pointers, preventing overallocation of slices, minimizing the overuse of interfaces and generics and many more, clarify misconceptions about sync.Pool and leverage it effectively.


Short  Overview of Go's standard tooling for observing memory usage and GC behavior: memory profiler, benchmarking tools, escape analysis, GC configuration, execution tracer. Shed more light on less known/used tools like execution tracer. 


Finish
Finish the talk by emphasizing that writing allocation-friendly code is crucial for maintaining application performance and should not be overlooked and a wrap-up.

#### Related Links

- [Slides](https://docs.google.com/presentation/d/1qP9RuO0BOGC6spwwdeX9lFdZW_jv6XI0ZIhjFh3dVLU/edit#slide=id.g30eb54ac2b6_0_43)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AGDEVL/feedback/)

---

### Build better Go release binaries

- **Speakers:** Dimitri John Ledkov
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 13:00 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4406-build-better-go-release-binaries/)

#### Abstract

go build . is a very common way to build and release binaries for go projects. But there are many settings one can pass to go to build better release binaries. This talk will give overview of compile time optimizations, give guidance on re-releasing, apply CGO hardening as recommended by OpenSSF, upgrading dependencies, ensuring binaries can be scanned for vulnerabilities, ensure codebase is compatible with popular go forks for FIPS compliance, and are easier to reproduce.
Relevant projects:
- https://pkg.go.dev/cmd/go#hdr-Compile_packages_and_dependencies
- https://best.openssf.org/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++.html
- https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck
- https://github.com/chainguard-dev/gobump
- https://github.com/chainguard-dev/melange/blob/main/pkg/build/pipelines/go/build.yaml
- https://github.com/wolfi-dev/os

#### Related Links

- [Build better go release binaries (Google Drive Slides)](https://docs.google.com/presentation/d/1Aj65XLc246sLFhAbODS3wk6OXz-LKrMqswDvVVIc5io/edit?usp=sharing)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9PRDZH/feedback/)

---

### A database for your program state

- **Speakers:** Dylan Reimerink
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 13:30 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4643-a-database-for-your-program-state/)

#### Abstract

Pretty much every application has state, the bigger your application the more state you have. Things can get challenging when you are asking much of your state. You might need to maintain multiple indexes into your state, react to changes to the state, keep multiple pieces of state in sync and make sure that all of it is thread-safe for multiple readers and writers. Doing this for one piece of state is a challenge, but doing it for a few dozen is painful.
Presenting, StateDB (cilium/statedb) a non-persistant in-memory database of your application state. It was created to tackle state management challenges experienced by Cilium. It leverages Go features such as generics, iterators, channels and Go’s garbage in combination with immutable data structures to make complex state management easy.
StateDB provides Multi Version Concurrency Control (MVCC) through snapshots, indexing(multiple indexes per table, unique and non-unique indexes, composite keys), write transactions across multiple tables and the ability to watch for changes on a whole table or a subset of data. To name a few.
Let's explore StateDB together and take a little peek under the hood.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MVRDBM/feedback/)

---

### High performance gRPC

- **Speakers:** Aurelien Deroide
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 14:00 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4231-high-performance-grpc/)

#### Abstract

gRPC is a popular RPC framework and go has a quite performant gRPC implementation. However, the performance can still be significantly increased by changing the default setup and by using the library in a way that reduces memory allocations. 
This talk will also show how to use the excellent go tooling to profile and benchmark some code.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DPZJED/feedback/)

---

### Katzenpost: developing privacy software in Go

- **Speakers:** Eva Infeld
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 14:30 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5475-katzenpost-developing-privacy-software-in-go/)

#### Abstract

Katzenpost is a robust privacy software project. It includes a mix network implementation with a powerful, realistic threat model,  hybrid post-quantum cryptography libraries, messaging protocols and metadata-private networking - all implemented in Go and under an AGPLv3 license. 
The purpose of this talk is to go over all of these elements and explain how they may be implemented in other software projects, rather than explain the high level design of the mix-net in detail. The Katzenpost code can be found at [the project's GitHub](https://github.com/katzenpost).

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/T3ENQU/feedback/)

---

### Developing a modern shell and programming language with Go

- **Speakers:** Qi Xiao
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 15:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4944-developing-a-modern-shell-and-programming-language-with-go/)

#### Abstract

I will talk about implementing Elvish (https://elv.sh), a modern shell with Go. I will cover the following topics:

An introduction to Elvish, including how to integrate it with Go-based tools for real-world scripting use cases
How Go makes it easy to implement Elvish, such as pipeline semantics, standard library
Testing strategy of Elvish as a case study of testing complex Go projects - Elvish has a test coverage of 92% and increasing, uses both unit tests, end-to-end tests and fuzzing

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FD37PF/feedback/)

---

### An Intro to eBPF with Go: The Foundation of Modern Kubernetes Networking

- **Speakers:** Donia Chaiehloudj
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 15:30 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5124-an-intro-to-ebpf-with-go-the-foundation-of-modern-kubernetes-networking/)

#### Abstract

eBPF is revolutionizing how we secure, observe, and scale Kubernetes networking, but its complexity can be daunting. This session demystifies eBPF by exploring how Go makes it accessible, focusing on its integration with Kubernetes through the open-source project Cilium. Attendees will learn the basics of eBPF, how Go simplifies working with it, and practical use cases that demonstrate Cilium’s ability to enforce secure, scalable network policies. This talk is perfect for Kubernetes practitioners curious about eBPF and Go but unsure where to begin.

#### Related Links

- [cilium/eBPF repository](https://github.com/cilium/ebpf/tree/main/examples)
- [eBPF for Gophers repository](https://github.com/doniacld/ebpf-4-gophers/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YVLWKJ/feedback/)

---

### WebAssembly for Gophers: from Wasm to Asm and back!

- **Speakers:** Edoardo Vacchi
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 16:00 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4966-webassembly-for-gophers-from-wasm-to-asm-and-back-/)

#### Abstract

Have you ever heard about WebAssembly?
WebAssembly is a compilation target meant for efficient compilation, portability, and safe execution. A WebAssembly runtime is a language VM that is small and easy to embed.
All cool gophers know they can compile their Go software into Wasm using the Go compiler and TinyGo. But did you know that you can also embed Wasm binaries in your applications? Did you know that you can use Wasm to dynamically load code at runtime without giving up memory safety and performance?
In this talk, we will first show how WebAssembly might be relevant to your use cases, such as providing extension points to your end users or importing foreign libraries.
We will then dive deep into the implementation of one such language VM specifically designed for embedding in Go, and show how a WebAssembly function is compiled into efficient native code and then invoked without sacrificing the portability, safety, and integrity of your Go code base.
Join this session for a journey from Wasm to Asm from the eye of a gopher!

#### Related Links

- [wazero](https://wazero.io)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SZ7KQ9/feedback/)

---

### Playing games without a computer: Hardware fun with TinyGo

- **Speakers:** Daniel Esteban
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5048-playing-games-without-a-computer-hardware-fun-with-tinygo/)

#### Abstract

What if gaming didn’t require a powerful computer or even a traditional console? In this talk, we’ll explore how with TinyGo you can create interactive games and experiences directly on microcontrollers and embedded hardware. From LED matrix games to unconventional input methods and minimalist sound effects, we’ll demonstrate how to harness the simplicity of TinyGo for innovative hardware projects.
Whether you're a seasoned Go developer curious about embedded systems or a hardware tinkerer looking for new ways to code your ideas, join us for a fun, hands-on dive into the possibilities of TinyGo-powered gaming, no computer required!

#### Related Links

- [TinyGo - The Go compiler for small places](https://tinygo.org/)
- [TinyGo Keeb - custome keyboard](https://gopherbadge.com/tinygo_keeb/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BDKBTU/feedback/)

---

### Implementing parallelism: how we added threading and multicore support in TinyGo

- **Speakers:** Ayke van Laethem
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 17:00 - 17:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5736-implementing-parallelism-how-we-added-threading-and-multicore-support-in-tinygo/)

#### Abstract

Parallelism is hard. So until recently, TinyGo (the alternative Go compiler for small systems) simply did not implement it. Instead, we used a simple single threaded scheduler that provides concurrency, but not parallelism. This made all programs act like GOMAXPROCS=1, which caused some practical issues.
Over the past few months we added support for running multiple goroutines in parallel on Linux, MacOS, and on the dual-core RP2040 chip. This required changes in many parts of TinyGo that previously assumed single threaded operation.
This talk will cover a variety of topics that may be interesting to anybody who wants to learn about low level primitives:

Which parts of Go are affected by parallelism.
Futexes: the building block of concurrency primitives on modern operating systems.
How some synchronisation primitives like channels and sync.Mutex are implemented in TinyGo.
How parallelism is implemented in TinyGo on Linux, MacOS, and the RP2040 chip.

#### Related Links

- [TinyGo website](https://tinygo.org/)
- [TinyGo GitHub repository](https://github.com/tinygo-org/tinygo/)
- [Slides](https://aykevl.nl/talks/2025-02-01-fosdem/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XADGZY/feedback/)

---

### Return Of Go Without Wires

- **Speakers:** Ron Evans
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 17:30 - 18:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5907-return-of-go-without-wires/)

#### Abstract

In the latest installment of the Go Without Wires saga, I will demonstrate several new capabilities in wireless communication using a variety of frequencies of the electromagnetic spectrum, all using our favorite programming language. There will be moving objects.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PWTREY/feedback/)

---

### Go Lightning Talks

- **Speakers:** Maartje Eyskens
- **Room:** UD2.120 (Chavanne)
- **Day:** Saturday
- **Time:** 18:00 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4609-go-lightning-talks/)

#### Abstract

Come speak! As every edition the last hour of the Go Devroom will be open for 5 minute lightning talks. The CfP for this will open shortly before the event and close 90 minutes before the session starts.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-go:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-go:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UWMLJJ/feedback/)

---

## Government Collaboration (11)

### Government Collaboration - Intro

- **Speakers:** Felix Kronlage-Dammers, Thorsten Schwesig, Lea Beiermann, Camille CAZIN
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 13:10 - 13:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6707-government-collaboration-intro/)

#### Abstract

Government Collaboration - Intro
by the hosts

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-government-collaboration:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-government-collaboration:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7KNBAK/feedback/)

---

### How is Development and Collaboration Done in Public Sector Open Source Software Projects? Insights from Six Mature Case Studies

- **Speakers:** Johan Linåker
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 13:15 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5379-how-is-development-and-collaboration-done-in-public-sector-open-source-software-projects-insights-from-six-mature-case-studies/)

#### Abstract

Collaboration on public sector Open Source Software (OSS) projects is steadily increasing along with demands for sovereign and interoperable technology stacks. Still, the practice has yet to catch up compared to industry and the broader OSS ecosystem, whose ways of working need to be tailored to manage the many challenges and restraints falling on the public sector. Examples we've come across include the dependency on sourcing of technical expertise, rigorous public procurement frameworks, risk-aversive and self-centric culture, and limited forums for collaboration. 
To help accelerate the public sector's use and development of OSS, we therefore investigated six successful cases of public sector OSS projects from different countries and levels of government. In this talk, we will provide insights on how development is commonly concentrated and performed with the use of national and local service providers. We will talk about different funding models, either involving one or a few central actors, or a wider set through different setups of crowd-funding. We will further elaborate on sustainability challenges related to the various ways of working, and potential approaches to addressing these proactively. 
Attendees will walk away with concrete and live examples to reference, as well as insights on how their organizations can start to engage and collaborate on new and existing public sector OSS projects. The presentation will further help to provide framing and input to other presentations within the devroom and hallway talks, stimulating knowledge sharing and growing a community of practice.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-government-collaboration:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-government-collaboration:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DU9ASU/feedback/)

---

### OSOR Handbook on Open Source Software in Public Administration

- **Speakers:** Axel Thévenet
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 13:30 - 13:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5693-osor-handbook-on-open-source-software-in-public-administration/)

#### Abstract

The European Commission's Open Source Observatory (OSOR) will showcase its latest initiative, the OSOR Handbook—a practical guide designed to support public administrations in adopting and effectively using open source software. Following the publication of the handbook's initial version in early 2024, a community consultation was launched to gather insights and feedback from the OSOR network. This process informed a revised edition of the handbook, highlighting the diverse needs of public administrations across Europe. These knowledge-sharing efforts are essential to foster collaboration among governments, as they help provide the necessary competences for government to collaborate.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-government-collaboration:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-government-collaboration:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/V93KCB/feedback/)

---

### Nubo: the French government sovereign cloud

- **Speakers:** Thierry Carrez, Louis Vigneras, Giuseppina URSO
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 13:45 - 14:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6234-nubo-the-french-government-sovereign-cloud/)

#### Abstract

As geopolitical tensions increase, the need for digital sovereignty pushes governments and organizations to adopt open source solutions to provide computing infrastructure.
Nubo is the inter-ministerial cloud of the French State, built by the Public Finance General Directorate (DGFiP) and powered by free and open source software, including OpenStack. In this presentation, Louis Vigneras and Thierry Carrez will explain why open infrastructure software is needed today more than ever, and retrace the journey of DGFiP into adopting those technologies.

#### Related Links

- [OpenStack official website](https://www.openstack.org/)
- [Description of the Nubo project](https://www.numerique.gouv.fr/services/cloud/cloud-interne/)
- [OpenInfra Foundation official website](https://openinfra.dev/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-government-collaboration:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-government-collaboration:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9NSFQJ/feedback/)

---

### openDesk on openCode: Developing a Secure Office Suite and SDLC

- **Speakers:** Leonhard Kugler, Alexander Smolianitski
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 14:15 - 14:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5572-opendesk-on-opencode-developing-a-secure-office-suite-and-sdlc/)

#### Abstract

openCode is Germany’s nationwide platform through which federal, state and local government authorities can search for and use open source software, provide their own code or contribute to existing projects. openCode aims to create an infrastructure that promotes the use of sustainable open source solutions for the public sector. A crucial aspect of achieving this goal is implementing a secure software development life cycle (SDLC). openCode offers an ideal environment for developing secure and reliable applications. One such application is openDesk, an all-in-one solution for collaborative office work in the public sector that integrates trusted open-source tools. openDesk’s source code is published on openCode and serves as an example to demonstrate how openCode supports its secure development.

#### Related Links

- [openCode Plattform](https://opencode.de/en)
- [openDesk](https://opendesk.eu/en/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-government-collaboration:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-government-collaboration:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8CMYZR/feedback/)

---

### Round Table Government Collaboration - 4 Topics and 7 Expert Speakers

- **Speakers:** Ludovic Dubost, Michael Meeks, Amandine Le Pape, Tilman Kranz, René Fischer, Frank Karlitschek
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 14:45 - 15:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6709-round-table-government-collaboration-4-topics-and-7-expert-speakers/)

#### Abstract

Bringing Together 4 Topics and 7 Expert Speakers

5 Top reasons why Governments should work together with Open Source Vendors and 5 ways on how to do it !
Ludovic Dubost, Michael Meeks, Frank Karlitschek
Solving the political problem of data sovereignty when working cross-organisation via open standards
Amandine Le Pape
A Sovereign Open Source Work Environment with LCM and openDesk
Tilman Kranz, Stefan Bogner
10 Cooks, 1 Kitchen: How We Made Different Software (Companies) Work Together
René Fischer

These four insightful proposals will converge in a collaborative roundtable discussion.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-government-collaboration:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-government-collaboration:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8F9PQX/feedback/)

---

### Note-Worthy Collaboration: Co-developing a Note-Taking Application

- **Speakers:** Virgile Deville, Alexander Smolianitski, Yousef El-Dardiry
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 15:20 - 15:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6403-note-worthy-collaboration-co-developing-a-note-taking-application/)

#### Abstract

In a 100-Day-Challenge, French and German product teams joined forces to co-develop a note-taking application for integration into their respective public sector office & collaboration suites, openDesk and La Suite Numérique. We show how this feature was developed, highlighting the challenges and successes of our joint endeavor. We'll explore the design and technical decisions behind the application and how it enables collaboration across different national workspaces. By sharing our experiences and lessons learned, we aim to showcase the potential of joint European initiatives in shaping sovereign digital workspaces that transcend borders.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-government-collaboration:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-government-collaboration:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZSSNSF/feedback/)

---

### GovStack Cloud BB: Sovereign Clouds for all countries

- **Speakers:** Kurt Garloff, Nico Lueck
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 15:50 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6506-govstack-cloud-bb-sovereign-clouds-for-all-countries/)

#### Abstract

The govstack project[1] creates building block (BBs) that help countries of the world to deliver digital services to their citizens in a sovereign way. By consequence, all building blocks are using open standards and are supposed to be implemented by open source software (OSS).
One of the latest additions is a cloud BB [2] which defines the requirements and characteristics of sovereign cloud infrastructure, which has been defined in close collaboration with the Sovereign Cloud Stack project[3] which also delivers an implementation[4] that conforms to the requirements.
The authors will give an overview over the specifications and will talk about some of the activities that are ongoing to disseminate the knowledge about building and operating sovereign infrastructure and how we hope to support countries across the world in owning their infrastructure without the dependencies that come with proprietary platforms.
[1] https://govstack.global/
[2] https://govstack.gitbook.io/bb-cloud-infrastructure
[3] https://scs.community/
[4] https://www.govstack.global/software/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-government-collaboration:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-government-collaboration:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MQJPNF/feedback/)

---

### Building open digital infrastructures for public health

- **Speakers:** Bianca Kastl
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 16:05 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6381-building-open-digital-infrastructures-for-public-health/)

#### Abstract

This talk gives an introduction into the efforts in building open digital infrastructures for public health in Germany within the project GA-Lotse since 2021. We will talk about the challenges in development, maintenance and scaling open digital infrastructures into the highly distributed world of health departments in Germany.
How can you build state of the art zero trust networks – in a not so digitally advanced area like the public administration? How can you integrate privacy by design and security by design? How can you rebuild specialist government application as cloud native applications? How can leverage service mesh and data mesh concepts for many public health departments at once? And most important: how can you do this in Open Source?
GA-Lotse is a software project with the aim to assist the Hessian public health departments in their daily business with a modern and unifying software. The project started development in late 2023, but was planned to be open source since the start in late 2021.
It is available in OpenCoDE (code repository and documentation is mostly in english).

#### Related Links

- [Source code](https://gitlab.opencode.de/ga-lotse/ga-lotse-code)
- [Documentation](https://gitlab.opencode.de/ga-lotse/ga-lotse-documentation)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-government-collaboration:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-government-collaboration:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YLQHZF/feedback/)

---

### FLOSS as a public policy: The case of Decidim

- **Speakers:** Nil Homedes, Andrés Pereira de Lucena
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 16:35 - 16:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5579-floss-as-a-public-policy-the-case-of-decidim/)

#### Abstract

Launched by the Barcelona City Council in 2016, the Decidim Barcelona project was initially created to coordinate the Municipal Action Plan, a participatory initiative aimed at strategically planning the city's projects for the next four years. In its early stages, Decidim was managed directly by the City Council, but over time, it became clear that an independent entity was needed to ensure the project's sustainability and facilitate its adoption and reuse by other governments.
To address this, the Decidim Association was established on February 16, 2019, during an extraordinary assembly. It was created as the governance body for the Decidim community, with the City Council transferring the management and maintenance of the source code to the Association through a formal agreement.
This public-common collaboration is an example of how to design the governance of digital commons. It is a unique example in the world of how to implement free software as a public policy with a community governance model.
In this session, we will explore how the Decidim Association collaborates with governments worldwide, focusing on three key aspects:

Technological Governance: Defining the roadmap and identifying needs.
Reuse and Adaptation of the Framework: Tailoring Decidim for diverse governmental contexts.
Challenges and Lessons Learned: Insights from working with governments globally.

This talk is ideal for those interested in learning how public organizations can develop FLOSS solutions and the best practices for implementing them with a community governance model.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-government-collaboration:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-government-collaboration:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NSB9VZ/feedback/)

---

### Government Collaboration - Outro

- **Speakers:** Felix Kronlage-Dammers, Thorsten Schwesig, Lea Beiermann, Camille CAZIN
- **Room:** AW1.126
- **Day:** Sunday
- **Time:** 16:45 - 16:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6708-government-collaboration-outro/)

#### Abstract

Government Collaboration - Outro
by the hosts

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-government-collaboration:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-government-collaboration:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/N3RCFP/feedback/)

---

## HPC, Big Data & Data Science (20)

### Optimizing Resource Utilization for Interactive GPU Workloads with Transparent Container Checkpointing

- **Speakers:** Adrian Reber, Radostin Stoyanov, Viktória Spišaková
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 09:00 - 09:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4042-optimizing-resource-utilization-for-interactive-gpu-workloads-with-transparent-container-checkpointing/)

#### Abstract

Interactive GPU workloads, such as Jupyter notebooks and generative AI inference are becoming increasingly popular in scientific research and data analysis.
However, efficiently allocating expensive GPU resources in multi-tenant environments like Kubernetes clusters is challenging due to the unpredictable usage patterns of these workloads. Container checkpointing was recently introduced as a beta feature in Kubernetes and has been extended to support GPU-accelerated applications. In this talk, we present a novel approach to optimizing resource utilization for interactive GPU workloads using container checkpointing. This approach enables dynamic reallocation of GPU resources based on real-time workload demands, without the need for modifying existing applications. We demonstrate the effectiveness of our approach through experimental evaluations with a variety of interactive GPU workloads and present preliminary results that highlight its potential.

#### Related Links

- [CUDA plugin for CRIU](https://github.com/checkpoint-restore/criu/tree/criu-dev/plugins/cuda)
- [AMD GPU plugin for CRIU](https://github.com/checkpoint-restore/criu/tree/criu-dev/plugins/amdgpu)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/L3XCLU/feedback/)

---

### Efficient Histogramming for High-Performance Computing in C++ with YODA

- **Speakers:** Christian Gutschow
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 09:30 - 09:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4809-efficient-histogramming-for-high-performance-computing-in-c-with-yoda/)

#### Abstract

Histogramming is a fundamental operation in scientific data analysis, but as datasets grow and computational demands increase, traditional approaches can become bottlenecks, especially in high-performance computing (HPC) environments. YODA (Yet more Objects for Data Analysis) addresses this challenge by providing a lightweight, C++-based histogramming library optimised for HPC use cases. In this talk, we’ll delve into YODA’s design principles and its approach to memory efficiency and parallel processing. We’ll discuss how YODA’s architecture supports large-scale histogramming workflows in data-intensive fields, with particular focus on LHC data analysis applications. Through examples, we’ll demonstrate YODA’s ability to handle high-throughput demands, leveraging modern C++ features to ensure compatibility with HPC and GPU architectures. This session will be of interest to developers and researchers working in high-performance data analysis who seek efficient, open-source solutions for handling complex datasets in resource-intensive environments.

#### Related Links

- [YODA gitlab repo](https://gitlab.com/hepcedar/yoda)
- [YODA website](https://yoda.hepforge.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PXUXQB/feedback/)

---

### Explainable forecasting from big weather data: rapid and sustainable solutions

- **Speakers:** David Salvador-Jasin
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 10:00 - 10:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5629-explainable-forecasting-from-big-weather-data-rapid-and-sustainable-solutions/)

#### Abstract

We present DynaModERA, an open-source Python package to perform Dynamic Mode Decomposition (DMD) at scale on the publicly available ERA5 dataset, the fifth generation ECMWF atmospheric reanalysis of the global climate covering the period from January 1940 to present. DMD is a popular technique for data-driven modeling of a variety of dynamical systems due to its simplicity and interpretability. In contrast to state-of-the-art deep learning models for data-driven weather prediction, such as those developed by NVIDIA, Huawei and Google DeepMind, DMD is a computationally inexpensive algorithm that provides a best-fit, linear characterization of a non-linear dynamical system, and generates explainable and interpretable results in the form of spatial modes with temporal evolution. These modes often have physical meaning that align with the underlying physics of the problem.
A common limitation of DMD is its inability to handle large datasets. DynaModERA addresses this challenge by enabling DMD on big weather data through the generation of low-rank approximations of ERA5 and the construction of smaller DMD models for different temporal subsamples. These models are then combined into a unified framework, allowing for stable predictions across all time scales. DynaModERA also provides a comprehensive pipeline for the entire process, including downloading appropriate ERA5 slices from the cloud, data versioning and tracking using Data Version Control (https://dvc.org/) , producing low-rank approximations at scale, and generating DMD models and predictions. By applying DMD to extensive portions of the ERA5 dataset, DynaModERA not only establishes a benchmark for comparing more advanced data-driven weather prediction models but also provides valuable physical insights through DMD modes, which can be used as input features for deep learning models.

#### Related Links

- [GitHub repository for the Python package](https://github.com/ClimeTrend/DynaModERA)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BBN8Y7/feedback/)

---

### Exa-Tracer: Tracing HPC Supercomputers with LTTng

- **Speakers:** Mathieu Desnoyers, Olivier Dion
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 10:30 - 10:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6269-exa-tracer-tracing-hpc-supercomputers-with-lttng/)

#### Abstract

Over the past two years, the developers from EfficiOS have been working with the Argonne National Laboratory (THAPI), Lawrence Livermore National Laboratory, and AMD to adapt the LTTng tracer to meet the requirements from the HPC field.
The LTTng tracer provides flexible, low-overhead tracing of large multi-core systems. It has historically focused on the stringent requirements from the telecom and embedded industries, and is currently being adapted through the (Exa-Tracer) project to target HPC GPU-based supercomputers: instrumentation of MPI and ROCm APIs, scaling the tracer to analyze large clusters.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZJ7TQM/feedback/)

---

### The High Performance Software Foundation (HPSF)

- **Speakers:** Gregory Becker
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 10:55 - 11:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6656-the-high-performance-software-foundation-hpsf-/)

#### Abstract

The High Performance Software Foundation (HPSF) is building a sustainable, open-source future for HPC software. HPSF supports performance-portable projects across diverse hardware, enabling developers to seamlessly build, deploy, and optimize applications – from supercomputers to cloud platforms and personal machines. HPSF is tackling key challenges in HPC, such as:

Continuous Integration (CI) with GPU and next-gen architecture access.
Cloud-ready packaging and containerization for easier deployment.
Lowering barriers to adopting high-performance software stacks.

This talk will discuss how HPSF is helping projects to build their communities, through neutral governance, collaboration, CI services, training, and events. We'll talk about what it means to join HPSF and how open source projects and organizations can get involved with this growing community.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DKZUNZ/feedback/)

---

### Environment Modules: why this old idea is still useful today and what's next

- **Speakers:** Marc Joos, Xavier Delaruelle
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 11:05 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4639-environment-modules-why-this-old-idea-is-still-useful-today-and-what-s-next/)

#### Abstract

Since more than 3 decades, Environment Modules helps HPC sites to provide access to their scientific software catalog. Such tool relies on updating the environment of a shell session, being able to undo what it changed.
This talk will first present what is the module command and what it is useful for. We will then quickly go through the history of this tool, describe the different implementations in use nowadays (Modules and Lmod), and give an insight of the most prominent features added in the recent years.
Based on the current context with multiple solutions available to build and install scientific software, we will see why Environment Modules is still useful today. Last part of the presentation will be about the future directions to integrate new ideas and improve the user experience.

#### Related Links

- [Source code](https://github.com/envmodules/modules)
- [Documentation](https://modules.readthedocs.io/)
- [Website](https://envmodules.github.io/modules/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GS93FY/feedback/)

---

### Programming models with the ROCm™ compiler

- **Speakers:** Jan-Patrick Lehr
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 11:35 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5143-programming-models-with-the-rocm-compiler/)

#### Abstract

This presentation showcases the different programming models that users of the AMD ROCm™ compiler can employ to offload computation to AMD GPUs. The talk highlights the interoperability of the programming models (HIP, OpenMP®, OpenCL™) with the supported languages (C, C++, Fortran), given the common compiler infrastructure. The talk summarizes the different compilers that AMD provides to address the confusion and point users to the correct compiler for their application. Since programming environments are not complete without libraries, the talk also showcases available libraries, such as rocBLAS. The talk provides a high-level overview together with examples on how to use the different approaches.
First, it covers some fundamentals of GPU programming and the execution model of HIP. It then shows how to construct an easy HIP kernel from scratch. This is followed by a look at the HIPIFY tool to port codes from CUDA to HIP. Second, the talk covers OpenMP® as GPU programming model in both C++ and Fortran. It highlights the difference between HIP and OpenMP® when it comes to control and convenience. Third, the C++ stdpar capability of ROCm™ is presented to highlight that the user can write pure C++ programs while still benefiting from GPU offload via compiler magic. Lastly, an example is given on how libraries can be used to offload the most relevant computation to the GPU without the need to write GPU kernel code at all.
All components mentioned in the talk are open-source, with most of the actual compiler work being done in the upstream llvm-project.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CHYCPD/feedback/)

---

### Adding built-in support for basic performance test analytics to ReFrame

- **Speakers:** Felix Abecassis, Vasileios Karakasis
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 12:00 - 12:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4755-adding-built-in-support-for-basic-performance-test-analytics-to-reframe/)

#### Abstract

ReFrame is the tool of choice of many data centers and vendors alike when it comes to HPC cluster validation, ranging from small university clusters to large national supercomputers. Despite its highly capable test programming API and its feature-rich runtime, it has always delegated the post-processing of the test results to the user, requiring homegrown site-specific solutions for post-processing. In this talk we will present our recent contribution to ReFrame that enables support for basic analysis of past performance results. All the information about the test cases that have run in a session is stored in a backend database and a new set of CLI options are added for querying, analyzing and comparing past results. We will also discuss how we make use of this feature in our highly dynamic data center environment.

#### Related Links

- [Tutorial on inspecting past results with ReFrame](https://reframe-hpc.readthedocs.io/en/latest/tutorial.html#inspecting-past-results)
- [Full documentation on the new feature](https://reframe-hpc.readthedocs.io/en/latest/manpage.html#querying-past-results)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BG8HSX/feedback/)

---

### Making Data Fun Again: Extending EESSI to improve Research Data Management

- **Speakers:** Thomas Röblitz
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 12:30 - 12:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6225-making-data-fun-again-extending-eessi-to-improve-research-data-management/)

#### Abstract

While digitalisation leads to ever growing data collections, exploiting the full potential of these data collections remains a challenge. Relevant data is difficult to find and it's not easy to use either. At the same time making data available such that others can find and (re)use them is cumbersome. For more than a decade various approaches - technical, organisational, cultural - are followed to help improve the situation, yet at best one witnesses isolated solutions and for many research data management remains a hassle. 
Solving challenges of Research Data Management (RDM) requires coordinated efforts of many parties involved. What happens often is that research projects start by writing down a Data Management Plan (DMP), then do their research and at the end struggle making their data publicly available as required by publishers and research funders.
This talk proposes extensions to EESSI - the European Environment for Scientific Software Installations (pronounced as "easy", https://eessi.io) - to help improve research data management. EESSI provides a large software stack of hundreds of software installations that are streamed on-demand to client systems. It combines several FOSS tools including CernVM-FS (https://cernvm.cern.ch/fs/), Gentoo Prefix (https://wiki.gentoo.org/wiki/Project:Prefix), EasyBuild (https://easybuild.io) and Lmod (https://lmod.readthedocs.io/) to build a service that can be used by anyone on any Linux machine anywhere in the world. A user just needs to install and configure a small client on his/her system and is ready to do science - analysing or generating data - within a few minutes.
A key building block of EESSI is its compatibility layer which provides system-level tools and libraries for basic functions such as file management, process creation, and so on. The compatibility layer uses Gentoo that is installed under a prefix. For each of the CPU families supported by EESSI - x86_64 and aarch64 (and soon riscv64) - EESSI just needs a single common installation of Gentoo. Because Gentoo is built from sources, extending a few functions in that layer is particularly easy and everyone who uses EESSI would be enabled to use these extensions.
Extending core functions of EESSI's compatibility layer facilitates the logging of data accesses (which process accesses what data and when) and simplifies access to remote data (data that is not already present where the data processing should happen).
Logging information about data accesses facilitates the creation of data flow graphs which can be used for optimisation, reproducibility, and in particular to automate the description of how results such as diagrams, tables, other data products were obtained. Detailed descriptions may help others to understand how the data was processed, to apply the processing to new data or to modify the processing to their needs.
Today, more and more data sets are published and associated with a persistent identifier. Instead of downloading data sets in a separate step and then processing them, the EESSI compatibility layer can be extended such that data sets can be accessed directly via persistent identifiers. While it may seem like a small improvement, this would enrich the logging information. Without any further steps by a researcher the used data sources would be identifiable and they could be cited automatically. Reproducing results would be improved and last but not least those who published the data would be acknowledged more easily.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/88CRPE/feedback/)

---

### EuroHPC FP: a Federated Platform for HPC Infrastructure in Europe, Built with Open Source Software

- **Speakers:** Henrik Nortamo
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 13:00 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6718-eurohpc-fp-a-federated-platform-for-hpc-infrastructure-in-europe-built-with-open-source-software/)

#### Abstract

Currently a scientist being granted compute resource from the EuroHPC JU can expect to create fully separate accounts and projects through completely different processes for each supercomputer they need to access. Various machines also provide differing levels of features for novice users or users whose field of science has been historically less "low-level HPC" oriented. All this combined creates extra work and a higher barrier to entry to the users in need of compute resources.
We present the EuroHPC federation platform which once completed will provide users with a single federated identity across all EuroHPC JU Supercomputers; uniform access both via the command line and web browser; and advanced features like interactive graphical usage, multi-machine workflows and a common software stack across all machines.
The platform place a great emphasis on modularity and open-source technologies, with most of the core functionality being based on open-source components. Key components include:     

Waldur: Allocating, managing, and monitoring of the resources integrated with the platform (https://waldur.com)
LEXIS: Automatized workflows across Cloud and HPC systems (https://docs.lexis.tech/)
Open OnDemand: Graphical web interface providing interactive applications and file management across the federated resources (https://openondemand.org)
European Environment for Scientific Software Installations (EESSI): Shared stack of optimized scientific software installations (https://www.eessi.io)
Authentication and Authorization Infrastructure (AAI) leveraging MyAccessID: SSH Certificate Authorities for access (https://wiki.geant.org/display/MyAccessID)

The talk presents the architecture for the federation platform and how it leverages open-source to achieve the lofty goals.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CDDVNJ/feedback/)

---

### Running Kubernetes Workloads on HPC with HPK

- **Speakers:** Antony Chazapis
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 13:30 - 13:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5722-running-kubernetes-workloads-on-hpc-with-hpk/)

#### Abstract

Cloud and HPC increasingly converge in hardware platform capabilities and specifications, nevertheless still largely differ in the software stack and how it manages available resources. The HPC world typically favors Slurm for job scheduling, whereas Cloud deployments rely on Kubernetes to orchestrate container instances across nodes. Running hybrid workloads is possible by using bridging mechanisms that submit jobs from one environment to the other. However, such solutions require costly data movements, while operating within the constraints set by each setup’s network and access policies. In this work, we explore a design that enables running unmodified Kubernetes workloads directly on HPC. With High-Performance Kubernetes (HPK), users deploy their own private Kubernetes “mini Clouds”, which internally convert container lifecycle management commands to use the system-level Slurm installation for scheduling and Singularity/Apptainer as the container runtime. We consider this approach to be practical for deployment in HPC centers, as it requires minimal pre-configuration and retains existing resource management and accounting policies. HPK provides users with an effective way to utilize resources by a combination of well-known tools, APIs, and more interactive and user-friendly interfaces as is common practice in the Cloud domain, as well as seamlessly combine Cloud-native tools with HPC jobs in converged, containerized workflows.

#### Related Links

- [High-Performance Kubernetes](https://github.com/CARV-ICS-FORTH/HPK)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XSTATP/feedback/)

---

### OpenCL, CUDA, and HIP as compilation targets for functional array programs

- **Speakers:** Troels Henriksen
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 14:00 - 14:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4504-opencl-cuda-and-hip-as-compilation-targets-for-functional-array-programs/)

#### Abstract

OpenCL, CUDA, and HIP are possibly the most popular APIs for low-level
GPU programming, and most GPUs support more than one. A lot of
superstitition abounds about their relative performance compared to
each other, but little data is available, largely because it is very
tedious to implement otherwise-equivalent programs using these APIs,
in order to compare their performance.
In this presentation I will present my experiences using OpenCL, CUDA,
and HIP as compilation targets for Futhark, a functional array
language. I look at the performance of OpenCL versus CUDA, and OpenCL
versus HIP, on the code generated by the Futhark compiler on a
collection of 48 application benchmarks on two different GPUs -
probably the largest such comparison done, at least in terms of
benchmarks. Despite the generated code in most cases being equivalent,
I observe significant performance differences on the same hardware. I
can identify the root causes of most of these differences, many of
which are due to relatively superficial details such as inconsistent
defaults regarding compiler optimisation and numerical accuracy,
although a few remain mysterious. The obtained information is useful
to anyone who seeks to generate low-level GPU code from higher level
specifications or libraries.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DQQFR9/feedback/)

---

### Harnessing Reduced Precision for Accurate and Efficient Scientific Computing in HPC

- **Speakers:** Nima Sahraneshinsamani
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 14:10 - 14:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6081-harnessing-reduced-precision-for-accurate-and-efficient-scientific-computing-in-hpc/)

#### Abstract

As high-performance computing (HPC) scales to tackle increasingly complex problems, balancing computational efficiency and precision has become a challenge. Reduced-precision floating-point formats, such as FP16 and FP32, offer significant speedups but require careful strategies to maintain numerical stability. This talk explores how mixed-precision approaches can enhance the performance of dense linear algebra operations and solve linear systems efficiently. Highlighting techniques implemented on modern GPU architectures, we discuss their applicability to scientific computing workloads, including LU factorization and beyond. The discussion also addresses challenges in optimizing sequential portions of computation, which often leave GPU resources underutilized, and presents strategies for improving both parallel and sequential execution.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WZ9CEF/feedback/)

---

### Easier API Interoperability: writing a bindings Generator to C/C++ with Coccinelle

- **Speakers:** Michele Martone, Ivan Pribec
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 14:20 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6509-easier-api-interoperability-writing-a-bindings-generator-to-c-c-with-coccinelle/)

#### Abstract

Software developers using high-level programming languages often find they need to call procedures from specialized libraries only offering a C or C++ API.
While most languages expose mechanisms for calling C functions, writing the bindings for potentially hundreds of procedures remains menial work: tedious and error-prone.
Is there a better way?
In this talk we take you on a journey of writing library bindings for BLIS, a large C library for linear algebra operations.
Using Coccinelle, a powerful code matching and transformation system, we present how a handful of semantic patches (augmented by little Python scripts) can cover the full BLIS library making it available to modern Fortran.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WFS37A/feedback/)

---

### A Pantheon of The Gods: Open Source Multiphysics Software for Analysis of Fusion Power Plant Systems

- **Speakers:** Aleksander Dubas
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 14:35 - 14:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5802-a-pantheon-of-the-gods-open-source-multiphysics-software-for-analysis-of-fusion-power-plant-systems/)

#### Abstract

Developing commercially viable fusion energy is a challenging multiphysics problem: strong magnetic fields, fluid dynamics, high heat loads and plasma physics all combine and interact to create complex systems that require a holistic approach to engineer properly. Through high performance computing, we have a cost effective pathway to future power solutions through a digital engineering approach. 
Therefore we need to develop connected multiphysics tools that can scale up to and beyond the exascale to truly be able to perform in silico analysis of prototype fusion power plant designs.
This work presents a collection of open source multiphysics tools covering electromagnetics, neutronics, computational fluid dynamics, heat transfer and isotope transport. These tools can be coupled through 
the MOOSE framework allowing the concurrent solution of all the physics of interest in a system. And thus can be used for the analysis of power plant systems at scale and enable the acceleration of making fusion power a reality.
Fusion is not a problem that can be solved by a single group and so we leverage the benefits of open source in our digital engineering approach to enable global collaboration in addressing the challenge of climate change and future renewable energy sources.

#### Related Links

- [Proteus Digital Twin Repo](https://github.com/aurora-multiphysics/proteus)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BAYNTY/feedback/)

---

### Effect of kernel optimizations on HPC workloads performance

- **Speakers:** Alex Domingo
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 14:45 - 14:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6520-effect-of-kernel-optimizations-on-hpc-workloads-performance/)

#### Abstract

HPC clusters are characterized by powerful hardware and fine-tuned software environments to extract as much performance as possible from the system. Surprisingly, many HPC systems typically use the default kernel provided by its Linux distribution of choice, which is a generic binary built to maximize stability and compatibility and lacks the fine-tuning for performance characteristic of such systems.
We explored the impact of different optimization techniques that can be carried out on the Linux kernel without changing its code. We tested compiler optimizations with GCC and LLVM, using CPU instruction sets specific to the target hardware, profile guided optimizations (PGO) or link time optimizations (LTO). The result is that such optimizations on kernel space have limited effects and depend on the type of workload, rendering them difficult to apply on HPC systems with a diverse ecosystem.
The main goal is to generate (more) optimized kernel images with the same exact functionality of the distribution kernel used in your system. We specifically target kernels of RPM-based Linux distributions and show how to generate drop-in replacements with the aforementioned optimizations.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TACPBM/feedback/)

---

### Multithreading in Python using OpenMP?

- **Speakers:** Dorian Ouakli
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 15:00 - 15:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4034-multithreading-in-python-using-openmp-/)

#### Abstract

Python 3.13 now allows for true multithreading in Python thanks to the removal of the GIL.
What if we wrote an open-source library that implements OpenMP for Python?
Time to improve the performance of your apps by adding a couple lines of code!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9D9WAS/feedback/)

---

### What’s the (floating) Point of all these data types? A (not so) brief overview of the history and usage of datatypes within the wide world of computation

- **Speakers:** Felix LeClair
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 15:30 - 15:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6537-what-s-the-floating-point-of-all-these-data-types-a-not-so-brief-overview-of-the-history-and-usage-of-datatypes-within-the-wide-world-of-computation/)

#### Abstract

This presentation delves into the fascinating and sometimes aggravating world of numerical data types, exploring the evolution, strengths, and weaknesses of decimal, fixed point, floating point, and shared exponent formats over the past 70 years.
Moving through various Eras, from the early computing era, where arithmetic operations were often emulated using cumbersome decimal arithmetic, to the widespread adoption of floating-point representations in modern computing. Starting with decimal data types, we will examine their suitability for financial and commercial applications where precision and exactness are paramount. Next, we will discuss fixed-point data types and their application in real-time systems and embedded devices where computational resources are limited. A significant portion of the presentation will be dedicated to floating-point data types, including the IEEE 754 standard and its evolution. We will investigate the trade-offs between range, precision, and performance, as well as the challenges of accurately representing real numbers in a finite digital format. 
Recent developments in floating-point formats, such as the IEEE 754-2019 standard, Google's Brain Float 16, NVIDIA's 19 bit TensorFloat 32, and the 18 flavors of 8 bit floating point, will also be covered. Additionally, we will explore the concept of shared exponent data types, including block float and posits which have gained popularity in recent years. We will analyze the potential benefits and drawbacks of these formats, including their impact on numerical computations and their suitability for specific applications. Throughout the presentation, we will draw on real-world examples, benchmarks, and use cases to illustrate the practical implications of choosing the right data type for a particular task. 
By the end of this talk, it is the hope of the speaker that attendees will gain a deeper understanding of the history, trade-offs, and best practices for working with non integer data types, enabling them to make informed decisions in their own projects and applications.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UFLLVA/feedback/)

---

### Mapping Applications to the Hardware Portably and Transparently

- **Speakers:** Edgar Leon
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 16:00 - 16:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4383-mapping-applications-to-the-hardware-portably-and-transparently/)

#### Abstract

When we consider the grand challenges addressed by distributed systems, we likely imagine large-scale machines and parallel code. Yet, these two pillars of computing – hardware and software – are not enough to ensure high efficiency and reproducible performance. When unaware of the topology of the underlying hardware, even well-designed applications and software libraries can fail to achieve their scientific goals. Affinity – how software maps to and leverages local hardware resources – forms a third pillar critical to computing systems. 
Multiple factors motivate an understanding of affinity for HPC and Data Science users. On the software side, applications are increasingly memory-bandwidth limited making locality more important. On the hardware side, today’s computer architectures offer increasingly complex memory and compute topologies, making proper affinity policies crucial to effective software-hardware assignments.
In this talk, I will present mpibind, a memory-driven library to map parallel hybrid applications to the underlying architecture transparently from the point of view of applications. This library provides a simple interface for computational scientists and results in a full mapping of MPI tasks, threads, and GPU kernels to hardware processing units and memory domains. Furthermore, scientists do not have to deal with intricate details of the hardware topology and thus increasing their productivity. Finally, mpibind is portable across computer architectures bridging the gap between performance and ease-of-use on parallel clusters.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CZW3ZD/feedback/)

---

### Job-specific performance monitoring on HPC clusters: Challenges and Solutions

- **Speakers:** Christian Iwainsky
- **Room:** UB5.132
- **Day:** Sunday
- **Time:** 16:30 - 16:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5831-job-specific-performance-monitoring-on-hpc-clusters-challenges-and-solutions/)

#### Abstract

Traditional monitoring in high-performance computing (HPC) clusters primarily supports administrators in maintaining and managing their systems. However, especially performance data is also a valuable resource for users aiming to optimize their applications and support personnel to identify jobs that abuse the HPC system or identify users and projects that need help.
To address the needs of all roles in an HPC environment, administrators, support personnel, project managers, and users, we developed Cluster Cockpit, an open-source monitoring framework that is easy to deploy and maintain that offers a powerful web-interface with specific views for the different HPC roles.
ClusterCockpit can cover multiple HPC clusters from small to large scale. By providing an intuitive user interface, ClusterCockpit simplifies performance analysis and enhances usability for diverse stakeholders. While analyzing job profiles can provide critical insights, manual analysis often requires significant time and expertise. To streamline this process, we developed Patho-Jobs, an automated tool that leverages data from ClusterCockpit to detect underperforming jobs or those requiring intervention. In this presentation, we will introduce the core concepts of ClusterCockpit and Patho-Jobs, along with insights gained from their deployment at German National High-Performance Computing (NHR) sites.
ClusterCockpit: https://clustercockpit.org/
Patho-Jobs: https://git-ce.rwth-aachen.de/pathojobs/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hpc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hpc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XZEDZ7/feedback/)

---

## Identity and Access Management (17)

### Welcome to Identity and Access Management devroom!

- **Speakers:** Alexander Bokovoy, Iker Pedrosa
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 09:00 - 09:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4065-welcome-to-identity-and-access-management-devroom-/)

#### Abstract

Welcome to the devroom, rules and initial setup.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZREYGA/feedback/)

---

### Heimdall: An Identity-Aware Proxy for Secure Access Control

- **Speakers:** Dimitrij Drus
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 09:05 - 09:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4883-heimdall-an-identity-aware-proxy-for-secure-access-control/)

#### Abstract

Modern distributed systems demand scalable, robust authentication and authorization. While different protocols and services exist to address these needs, seamlessly integrating them remains a challenge. Heimdall, an open-source identity-aware proxy, simplifies this process by abstracting authentication and authorization methods, enabling developers to focus on business logic without worrying about protocol-specific complexities. This session features a live demo showcasing heimdall’s flexibility in integrating diverse protocols and authorization systems, demonstrating enhanced security, scalability, and reduced developer effort without any loss of control over access decisions.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RXY9AK/feedback/)

---

### Partly Cloudy IPA - joining cloud VMs to FreeIPA

- **Speakers:** André Boscatto
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 09:35 - 10:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5054-partly-cloudy-ipa-joining-cloud-vms-to-freeipa/)

#### Abstract

Cloud workloads need to comply with your organisation's security policies. Joining them to an identity management domain can help with that, and automatically joining them is even better. Learn how the Podengo project enables automatic and secure enrollment of VMs into a FreeIPA domain. 
FreeIPA is an open source identity management solution providing authentication, access control, and other security features for Linux machines, to help organisations meet their security and compliance objectives. These objectives persist when running workloads on public clouds. But the typical workflow of using SSH keys to access the machine may struggle to meet them.
Enter Podengo. The Podengo service registers your FreeIPA deployment (which could be on-premises), authenticates cloud VMs, and facilitates an automatic and secure domain enrollment. This presentation will explain how the protocol works, what is required to use it, and how we use the Podengo service to provide the Domain Join feature in Red Hat Hybrid Cloud Console (and how you could use it in other settings).
After covering the fundamentals and current use cases, we will discuss some of the feature gaps (and how to close them), and how we could add support for more identity management solutions.
This presentation could be particularly useful for system and cloud administrators, infosec people, and the cryptography-curious.
PS: There will be recorded demos available due to time constraints!
References:
https://www.freeipa.org/
https://github.com/podengo-project

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/S377FD/feedback/)

---

### Deep Dive into OIDC flows

- **Speakers:** Milan Jakobi
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 10:05 - 10:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5209-deep-dive-into-oidc-flows/)

#### Abstract

Modern web applications strongly rely on Authentication/Authorization infrastructures. To address these needs, the OSS community has strongly endorsed open protocols such as OpenIdConnect and OAuth2, on top of JSON and REST. In turn, these protocols have been implemented in software products such as Keycloak, WSO2 or Lemonldap.
OpenIdConnect and OAuth2 are authorization protocols, closely aligned with authentication, as provided by Identity Providers.  They have been designed within various standardization bodies such as the OpenId foundation or the Internet Engineering Task Force. Understanding these standards is demanding, but needed in order to implement feature-rich solutions, to understand the various options offered to implementers.
This talk will therefore discuss in details OIDC and OAuth : the various flows that exist in order to obtain access tokens for standard clients, and some advanced features enabled by these protocols.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GXSR3R/feedback/)

---

### Nubus: An Enterprise Open Source IAM Stack in Kubernetes

- **Speakers:** Daniel Tröder
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 10:35 - 11:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5510-nubus-an-enterprise-open-source-iam-stack-in-kubernetes/)

#### Abstract

Nubus is an open-source Identity and Access Management (IAM) stack built on well-known enterprise open-source software components, including Keycloak and OpenLDAP. This combination creates an easy-to-deploy identity management solution that focuses on developing integrated software landscapes.
It is the IAM component of openDesk and, e.g., the central directory service of the digital sovereign workplace of the German federal state Schleswig-Holstein.
Nubus is available as part of a Debian-based Linux distribution or as a Helm package for Kubernetes.
Nubus provides APIs for provisioning users, groups, and other resources into the IAM and an event system for provisioning these objects to third-party applications.
This talk will discuss how Nubus can assist you in integrating both closed-source and open-source applications and IAM solutions.
Product Page | Documentation | Download | Source

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/Z7EE9A/feedback/)

---

### ACME Certificates with FreeIPA: Simplify SSL/TLS Management

- **Speakers:** José Ángel de Bustos Pérez, Josep
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 11:05 - 11:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5667-acme-certificates-with-freeipa-simplify-ssl-tls-management/)

#### Abstract

SSL/TLS certificate management doesn’t have to be a headache. With FreeIPA’s integrated ACME protocol support, you can automate certificate issuance and renewal, simplifying your security workflows while maintaining enterprise-grade reliability.
In this session, we’ll explore how FreeIPA ACME capabilities can streamline certificate management across diverse environments. From Kubernetes to traditional systems, FreeIPA’s ACME integration empowers organizations to enhance security, reduce manual effort, and ensure uptime. As a practical example, we’ll demonstrate how Kubernetes’ cert-manager Operator can leverage FreeIPA’s ACME capabilities to manage certificates for containerized applications. This is just one of many possible integrations enabled by FreeIPA’s robust feature set.
The ACME protocol allows automated interactions between certificate authorities and your servers so you can automate the deployment of your public key infrastructure at a low cost, with relatively little effort. ACME protocol combined with the new features incorporated in the last release of mod_md make it so easy to have a completely automated environment to manage the renewal of the certificates of your webservers. Using the ACME feature of FreeIPA integrated with mod_md you can manage multiple security sites in a  completely automated and scalable way without any external dependencies so you will never need to be concerned about common topics such as: when to perform the operation, possible disruptions, long times waiting for the CA to sign your certificates or any kind of problems you experienced in the past. Mod_md also includes several fine tuning mechanisms about when to perform the operations to make the server aware of any issue in your certs.  We will also review them and this combined with appropriate monitoring reduces the renewal operation to the minimum.
Whether you manage Kubernetes, hybrid infrastructure, or standalone systems, FreeIPA offers a flexible and scalable approach to SSL/TLS management. Join us to uncover how FreeIPA’s ACME support can transform your certificate lifecycle management, improving security posture with minimal complexity no matter your applications are running on top of Kubernetes or on Apache. Don’t miss the opportunity to master certificate automation with FreeIPA!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TFPKD7/feedback/)

---

### systemd's User Database API

- **Speakers:** Lennart Poettering
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 11:35 - 12:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5071-systemd-s-user-database-api/)

#### Abstract

Since a longer time systemd suite contains a "userdb" component that allows local services to provide rich, extensible user records, that are consumed by various other systemd components. In this talk i'd like to explain what this is, and why identity management systems with a focus on local logins on Linux/systemd systems should consider implementing the necessary simple IPC interfaces and provide their user records in systemd's format.
This talk will cover various topics that are documented here:
https://systemd.io/USER_RECORD
https://systemd.io/GROUP_RECORD
https://systemd.io/USER_GROUP_API/
https://www.freedesktop.org/software/systemd/man/latest/systemd-userdbd.service.html

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BA3BM8/feedback/)

---

### Federated Identities Anyone? We've got lots of them ...

- **Speakers:** Stephan Schwichtenberg
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 12:05 - 12:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6019-federated-identities-anyone-we-ve-got-lots-of-them-/)

#### Abstract

In the recent past federated identity setups have grown in importance, as they avoid the additional storage and maintenance of accounts. But can you imagine an internet that exists solely of federated identities talking to each other? The neuropil cybersecurity mesh is exactly this: a federated identity space, where every participant uses different sets of digital identities to protect it's privacy and to increase the security of the users. Based on ZeroTrust with MixIns from Self-Sovereign Identities, Named Data Networks and Attribute Access Control, we would like to present our design choices and usage of digital identities, starting with famous Alice and Bob and continuing to involve Eliza and Marvin. As the title implies: there will be lots of digital identities ...

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MM7VWV/feedback/)

---

### SSSD and IdPs

- **Speakers:** Sumit Bose
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 12:35 - 13:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4756-sssd-and-idps/)

#### Abstract

Identity Providers (IdP) based on OAuth 2.0/OIDC and other REST APIs like e.g.
Keycloak or Entry ID play a dominant role in the identity management of
web-based applications. But organizations which are using IdPs for their internal
applications still have to use other services, typically LDAP based, to manage
access and authentication to LINUX/POSIX user workstations.
To help to avoid running two services for identity management SSSD started to
use IdPs to lookup users and authenticate them against the IdPs. In contrast to
LDAP there are no standards and conventions with respect to POSIX users and
groups in the IdP world.
This talk will focus on how SSSD is getting user and group information from
IdPs, how information required by POSIX, e.g. the numeric user and group IDs,
is created and what kind of limitations there are. Additionally it will be
explained why the OAuth 2.0 Device Authorization Flow  was chosen for
authentication and demonstrated.

#### Related Links

- [SSSD - System Security Services Daemon - sssd.io](https://sssd.io/)
- [SSSD on github](https://github.com/SSSD/sssd)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9HF3U7/feedback/)

---

### Fine-grained access control in LXD with OpenFGA

- **Speakers:** Mark Laing
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 13:05 - 13:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6194-fine-grained-access-control-in-lxd-with-openfga/)

#### Abstract

LXD is increasingly deployed on premises as a private cloud solution. To manage access over the HTTPS API, LXD has developed a novel approach using relationship-based access control (ReBAC) and OpenFGA. This approach facilitates fine-grained permission management and enforcement in air-gapped deployments where it is not feasible to deploy a separate OpenFGA server.
This talk will outline LXD's implementation and discuss its benefits and drawbacks.
Implementation details can be found in the specification and in the LXD Github repository

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YLDXSY/feedback/)

---

### localkdc - A general local authentication hub

- **Speakers:** Alexander Bokovoy, Andreas Schneider
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 13:35 - 14:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5618-localkdc-a-general-local-authentication-hub/)

#### Abstract

For several decades we used simple username/password authentication to access services, being them at home, somewhere in the internet or in an enterprise environment. We started to get Single-Sign-On (SSO) support, first via Kerberos and later via web authentication mechanism.
A local Kerberos Key Distribution Center (KDC) is not a new invention. It is a useful tool in combination with the Kerberos IAKerb extension but also allows to map SSO from a web authentication to local authentication or in a network environment isolated from the rest of the enterprise environment.
This talk aims to show a prototype of a common set of requirements and approaches to represent a secure POSIX identity management integration with OAuth 2.0-based identity providers. We also show how use of NTLM in SMB protocol will be replaced by a localkdc in combination with IAKerb.

#### Related Links

- [localkdc repository (prototype)](https://gitlab.com/cryptomilk/localkdc)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RCPWSA/feedback/)

---

### OpenBao at GitLab - Building Native Secrets for GitLab CI/CD Pipelines

- **Speakers:** Alex Scheel
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 14:05 - 14:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5145-openbao-at-gitlab-building-native-secrets-for-gitlab-ci-cd-pipelines/)

#### Abstract

OpenBao is the open source continuation of HashiCorp Vault under the Linux Foundation. OpenBao is a secrets and identity broker, allowing secure storage and auditing of applications’ credential usage. This talk shares how GitLab has architected its native integration of OpenBao for CI/CD Pipelines to provide a native experience for managing pipelines' secrets. In addition, it explores improving scalability, advanced multitenancy improvements, and other exciting major changes within the OpenBao ecosystem.

#### Related Links

- [OpenBao Website](https://openbao.org)
- [OpenBao - GitHub](https://github.com/openbao)
- [GitLab Secrets Manager - Design Doc](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/secret_manager/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RKFLSB/feedback/)

---

### FreeIPA-to-FreeIPA Migration: Current Capabilities and Use Cases

- **Speakers:** Francisco Triviño García
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 14:35 - 15:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5175-freeipa-to-freeipa-migration-current-capabilities-and-use-cases/)

#### Abstract

The migration of FreeIPA servers is a critical process for organizations seeking to modernize, consolidate, or restructure their identity management systems. This talk introduces a new tool, ipa-migrate, designed to facilitate robust IPA-to-IPA migrations while addressing the complexities of LDAP schema, configuration, and database migration. The tool supports both online (network-based) and offline (LDIF-based) approaches, allowing flexibility for various deployment sizes and environments.
Key features include configurable migration modes: production for retaining critical IDs and staging for regenerating attributes, and options to mix and match online and offline methods for optimized performance. Advanced capabilities such as dry-run simulations, selective content migration, and non-IPA data handling further enhance the tool’s adaptability.
This talk also targets real-world scenarios, such as migrating from production to staging environments or between staging and new production setups, detailing challenges like Kerberos key management, certificate handling, and ID range conflicts. By offering a streamlined, user-centric interface with detailed logging and error recovery mechanisms, ipa-migrate ensures efficient, reliable migrations that minimize downtime and data integrity risks. This work aims to provide administrators with a practical guide to IPA server migration.
https://freeipa.readthedocs.io/en/latest/designs/ipa_to_ipa_migration.html

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/M978SU/feedback/)

---

### Enhancing PAM Communication: A JSON-Based Approach for Modern Authentication

- **Speakers:** Iker Pedrosa
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 15:05 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4678-enhancing-pam-communication-a-json-based-approach-for-modern-authentication/)

#### Abstract

This presentation explores the novel extension of the PAM conversation through JSON messages, enabling richer communication between PAM applications and SSSD. This extension was driven by the need to support passwordless authentication mechanisms, such as displaying QR codes for external identity verification, within graphical environments like GDM (GNOME Display Manager).
The talk delves into the technical details of this JSON-based interface between SSSD and GDM, providing insights into its design and implementation. Furthermore, a simple PAM rust client will be presented as a practical example, serving as a reference for developers seeking to integrate this protocol into their own PAM applications. This opens up a wide range of possibilities for enhanced authentication flows, including:

Contextual Information: Sharing user-specific data or authentication challenges.
Adaptive Authentication: Dynamically adjusting authentication steps.
Multi-Factor Authentication: Orchestrating complex authentication sequences.

The presentation will conclude with live demonstrations showcasing the capabilities of this extended PAM conversation and its potential for innovation in authentication systems.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XZAATS/feedback/)

---

### Comprehensive Federated Authentication for AI/HPC Infrastructure

- **Speakers:** Jonathan Calmels
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 15:30 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4771-comprehensive-federated-authentication-for-ai-hpc-infrastructure/)

#### Abstract

With the advent of accelerated computing comes the need to provide comprehensive end-to-end authentication across all the resources that comprise a typical AI/HPC cluster.
However, for many organizations, this involves reconciling typical corporate identity infrastructure, such as Microsoft Active Directory, with Linux-based systems.
Additionally, these clusters pose unique challenges, including preserving proof of identity during batch scheduling, within CI/CD pipelines, on parallel filesystems and/or across several network fabrics.
In this presentation, we will demonstrate how to achieve the best of both worlds, using the Eos supercomputer (#10 on Top500) as a reference. We will showcase how we solved these issues leveraging the federated authentication and identity management from FreeIPA, alongside the capabilities of our project, Sybil.
We will detail how we were able to provide strong security guarantees for various types of services (e.g. SSH, Lustre, NFS, CI/CD, Slurm, SHARP, MNVLink) coupled with modern best practices (SSO, 2FA, etc), while accommodating both on-premises and cloud-based authentication.

#### Related Links

- [Tools for Kerberos protocol transition and ticket impersonation](https://github.com/NVIDIA/sybil)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WGSD7C/feedback/)

---

### Delegating the chores of authenticating users to Keycloak

- **Speakers:** Alexander Schwartz
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 16:00 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5673-delegating-the-chores-of-authenticating-users-to-keycloak/)

#### Abstract

Authenticating users can start simple with a username and a password for each user. But you will also need to handle forgotten passwords and user registration. You might also want to validate email addresses, add second factors, have users update their profile information as needed, or even offer password-less authentication.
A single-sign-on system like Keycloak can handle all that for you and will redirect users after they are authenticated to your applications using the industry standards like OpenID Connect and SAML.
Join this talk to see how you can delegate all the tasks around authentication to Keycloak. We will start simple and enable more and more features in our demo to show the functionality and flexibility of Keycloak. We will also look at features of the latest release and the road map ahead.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XJQQLY/feedback/)

---

### Building Cross-Domain Trust Between FreeIPA Deployments

- **Speakers:** Alexander Bokovoy, Francisco Triviño García
- **Room:** UA2.118 (Henriot)
- **Day:** Sunday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5178-building-cross-domain-trust-between-freeipa-deployments/)

#### Abstract

FreeIPA and SSSD teams are  working on making independent FreeIPA deployments to interoperate. This talk outlines the progress made toward achieving IPA-IPA trust, a feature that mirrors existing integration with Active Directory (AD) but adapts to modern, self-sufficient deployments that may not rely on traditional AD infrastructure.
IPA-IPA trust leverages Kerberos cross-realm authentication to establish secure relationships between distinct FreeIPA domains and allows seamless access to resources across trusted environments. Building on existing support for AD trusts, the approach reuses proven mechanisms in FreeIPA and SSSD to resolve identities, enforce access policies, and manage trusted domain configurations. This includes adapting Kerberos authorization data extensions to securely exchange identity details and group membership information, which FreeIPA already utilizes for AD trusts.
Key developments include enhancing SSSD to support multiple subdomain types, enabling it to handle IPA-specific identity structures, and introducing new mechanisms to facilitate identity information retrieval across trusted IPA domains. Initial experiments demonstrate the viability of this approach, with prototypes and Fedora-based builds available for testing. 
This talk highlights the technical challenges, solutions, and progress achieved so far, offering insights into the collaborative efforts that aim to extend FreeIPA’s trust capabilities.

#### Related Links

- [FreeIPA project](https://freeipa.org/)
- [SSSD project](https://sssd.io/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-iam:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-iam:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DTRW7C/feedback/)

---

## Image-Based Linux and Boot Integrity (8)

### systemd & TPM in 2025

- **Speakers:** Lennart Poettering
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 09:00 - 09:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5073-systemd-tpm-in-2025/)

#### Abstract

An update on systemd's TPM2 support. What's new and where we are going to bring Boot Integrity to generic Linux

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-image-based-linux:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-image-based-linux:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UGZ9YP/feedback/)

---

### ParticleOS: Can we make Lennart Poettering run an image based distribution?!

- **Speakers:** Daan De Meyer
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 09:30 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4057-particleos-can-we-make-lennart-poettering-run-an-image-based-distribution-/)

#### Abstract

Lennart Poettering likes to evangelize image based distributions, their security properties and all the good stuff systemd supports these days to make secure image based distributions possible (https://0pointer.net/blog/fitting-everything-together.html, https://0pointer.net/blog/brave-new-trusted-boot-world.html, https://www.youtube.com/watch?v=vT2uw25o0uM, ...). 
However!!! Does Lennart actually run an image based system himself?!! The answer is no! He runs a mostly stock Fedora system (luckily without grub). So how do we get Lennart onto an image based system? That's where ParticleOS comes in, an image based distribution built completely on top of systemd tooling that intends to implement all of the ideas presented and implemented by Lennart across the years.
Unlike other image based distributions, ParticleOS focuses on letting users assemble, configure and sign their own image based distribution instead of providing a prebuilt and presigned one that is hard to customize. Users build ParticleOS themselves and sign it with their own keys. As ParticleOS is built with mkosi, any distribution supported by mkosi can be used as the base distribution and users can customize the image to their liking (adding packages, running arbitrary commands, switching to a different filesystem, ...).
This talk will first expose Lennart, then introduce ParticleOS, compare it to other image based distributions and hopefully convince the listeners that ParticleOS is a good fit for power users looking for a customizable, self-signed image based distribution based on top of all the ideas evangelized by Lennart over the years.
ParticleOS: https://github.com/systemd/particleos
mkosi: https://mkosi.systemd.io/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-image-based-linux:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-image-based-linux:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/779BFT/feedback/)

---

### FDE is almost there, how do we tackle the last hurdles?

- **Speakers:** Richard Brown
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 10:00 - 10:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5893-fde-is-almost-there-how-do-we-tackle-the-last-hurdles-/)

#### Abstract

This session will be part case-study, part open-floor discussion, and part cry for help.
Aeon Desktop, as part of its efforts to be a user-friendly, tinker-free, Linux desktop that "just works" has implemented Full Disk Encryption, deployed as an image.
When installed on capable hardware, TPM measurements provide strong boot integrity checking.
This session will give a brief overview of how Aeon has implemented this, lessons learned, and challenges still to be tackled.
This will lead to some discussions points, including
- how best to handle hardware that is incapable of strong boot checks?
- how to improve the story surrounding recovery keys and the storing of them?
- how to improve the input and use of recovery keys?
- how to best reduce/minimise false invalidations of boot integrity checks? (ie. Which TPM Registers make most sense for Desktop vs Server usecases)
Finally, the talk will encourage attendees to help implement any discussed solutions, in ways that can be easily consumed by not only Aeon but other similar projects.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-image-based-linux:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-image-based-linux:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UKHRQE/feedback/)

---

### "Signed, Sealed, and Delivered", with UKIs and composefs

- **Speakers:** Timothée Ravier, Allison Karlitskaya
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5191--signed-sealed-and-delivered-with-ukis-and-composefs/)

#### Abstract

Using composefs and fs-verity, we can link a UKI to a complete read only filesystem tree, guarenteeing that every byte of every file is verified on load. This is done, similar to Git, using only hashes.  This means that the signature on the UKI effectively signs the whole tree.
With composefs, file content is split from the metadata which enables de-duplication at the file level. We can thus host any number of OS images on a single filesystem and there is no need to reserve space on the system in advance for each image. This frees us from fixed size disk image formats such as dm-verity which is used in a lot of image based systems.
We illustrate this architecture by building an OS image using an OCI container via the familiar Containerfile syntax, then pushing it to a container registry and finally deploying it on a system.

#### Related Links

- [Upstream repository](https://github.com/containers/composefs-rs)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-image-based-linux:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-image-based-linux:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CZFWAG/feedback/)

---

### Lessons learned from deploying boot security features on embedded systems

- **Speakers:** Valentin Geffroy, Johann Gautier
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 11:00 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5244-lessons-learned-from-deploying-boot-security-features-on-embedded-systems/)

#### Abstract

Verifying the integrity of the entire boot process is today mandatory for embedded systems. Secure Boot is typically a feature that ensures the integrity of loaded binaries (such as vendor firmware, bootloaders, initramfs and the Linux kernel) to unauthorized modifications of essential boot components. If the bootloader or the Linux kernel does not match with what's expected, the boot process will be halted. After securizing as possible the boot process, there are other methods to enforce the rootfs like using dm-crypt for encryption, dm-verity for integrity...
This presentation will explore these security features in the context of an embedded operating system called redpesk OS. How can they enhance system security? Can they be applied to specific embedded systems? These are some of the key topics we will cover, with general security features then we'll explain some difficulties we had by deploying boot security features in a restricted environment (old Linux kernel version, CPU & memory usage).

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-image-based-linux:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-image-based-linux:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JQA9LU/feedback/)

---

### Generating immutable, A/B updatable, securely booting Debian images

- **Speakers:** Jan Kiszka
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 11:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4695-generating-immutable-a-b-updatable-securely-booting-debian-images/)

#### Abstract

Debian provides a lot of the pieces you need to create a securely booting Linux system that is able to encrypt all its sensitive data while storing the key in a device-bound trust anchor like a TPM. It even permits to use immutable rootfs images that can be updated in A/B fashion atomically. But all these pieces are neither plugged together by its official installer nor would that help when you need offline-built and signed images.
The Civil Infrastructure Platform project (https://www.cip-project.org) aims at closing this gap, specifically for Debian use cases in the embedded industrial field, although results are not limited to that. This talk introduces the integration layer isar-cip-core (https://gitlab.com/cip-project/cip-core/isar-cip-core) that the project created, presents its current key features and next plans. It looks back on how some custom packages that used to be generated ad-hoc became regular Debian packages. Furthermore, it explains how (most) generated images were made bit-identically reproducible.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-image-based-linux:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-image-based-linux:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YPHFD7/feedback/)

---

### Bootable Containers and Image Mode: Transforming Linux OS Management with Bootc

- **Speakers:** Eric Curtin, Pierre-Yves Chibon
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 12:00 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4513-bootable-containers-and-image-mode-transforming-linux-os-management-with-bootc/)

#### Abstract

As containers continue to reshape how applications are deployed and managed, bootable containers have emerged as the next frontier—extending cloud-native concepts down to the operating system itself. In this talk, we’ll introduce Bootc and explore how it powers image-based OS deployment, boot integrity, and manageability. By leveraging Bootc, the operating system becomes as portable and manageable as a containerized app, bridging traditional OS management with modern DevOps practices.
We’ll cover "Image Mode" for Red Hat Enterprise Linux and Fedora, an approach that allows developers, operations teams, and solution providers to manage the entire OS as a container image. Image Mode incorporates the bootc CLI, the main command-line tool for managing updates and other tasks on end devices, along with the bootc-image-builder, which can generate a variety of image types. These include disk images (such as ISOs) suitable for disconnected installations, and virtual disk image formats like QEMU Copy-On-Write (QCOW2), Amazon Machine Images (AMI), and Virtual Machine Images (VMI). This method not only reduces complexity across environments but also enables a unified DevOps approach, integrating seamlessly with container-native tools and CI/CD pipelines. Attendees will learn how image-based deployments address security needs with containerized scanning, validation, and signing tools, and hear about opportunities for standardization within the container ecosystem to ensure boot and operational integrity at scale.

#### Related Links

- [booc project](https://containers.github.io/bootc/)
- [Getting started with bootable containers - Fedora](https://docs.fedoraproject.org/en-US/bootc/getting-started/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-image-based-linux:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-image-based-linux:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8EQTU7/feedback/)

---

### Case Study: Measured Boot and Remote Attestation in Confidential Containers

- **Speakers:** Magnus Kulke
- **Room:** UB4.136
- **Day:** Sunday
- **Time:** 12:30 - 12:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4559-case-study-measured-boot-and-remote-attestation-in-confidential-containers/)

#### Abstract

In this talk we want to present how the Confidential Containers project is using Measured Boot, vTPMs and Rego policies to provide ephemeral, integrity-protected sandboxes for containers in a Trusted Execution Environment. We'll describe the lifecycle of a such a confidential cloud-native workflow, specifically the remote attestation workflows and the components that are involved. Our experience with the tools that we love (UKIs, mkosi!) and the tools that we can't go around (libtss) will be covered, along with lessons learned and remaining challenges.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-image-based-linux:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-image-based-linux:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PC7JL7/feedback/)

---

## Inclusive Web (8)

### Top Accessibility Errors Found in Open Source Through Automated Testing

- **Speakers:** Raashi Saxena
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 09:00 - 09:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6075-top-accessibility-errors-found-in-open-source-through-automated-testing/)

#### Abstract

Professional accessibility evaluations offer a thorough and meticulous analysis of all WCAG 2.2 criteria applicable to your tool, encompassing assessments with assistive technology and disabled users. These audits not only assist teams in adhering to accessibility standards and regulations but also contribute to heightened user engagement and enhanced SEO.
In this talk, we present the top accessibility errors found in open source tools used in the internet freedom community through manual and automated testing on web and mobile applications. We will share currently examples and case studies of our ongoing accessibility solutions with the open source tools offered to the internet freedom community that actively works towards countering surveillance and censorship in repressed environments. We'll be covering open source tools simulating the user experience of a person with disability (screen reader user) and other assistive technologies. Ultimately, products developed through the accessibility guiding principles will possess unparalleled quality, providing everyone, including people with disabilities, the opportunity to utilize them.
This session is open to all developers, testers, UX designers, product teams, managers and other FOSS contributors as we share insights derived from our firsthand experiences delivering technological services to teams, companies, and organizations committed to significantly improving their digital accessibility standards.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-inclusive-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-inclusive-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HRVXN9/feedback/)

---

### Solving the world’s (localization) problems

- **Speakers:** Eemeli Aro, Ujjwal Sharma
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 09:30 - 09:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5561-solving-the-world-s-localization-problems/)

#### Abstract

Efficiently localizing user interfaces is an age-old problem that has haunted programmers since the early days of software development. Many tools and techniques have been employed over the years for this with differing levels of success by organizations across the world.
A few years ago, stakeholders came together in the Unicode Consortium from various areas of work bringing along tools and knowledge in order to build a definitive system that could be a standard solution for these problems. The first part of this design has taken shape as “MessageFormat 2”.
What is MessageFormat 2 like? How does it approach the vast problem space and how exactly could it be adopted across various user interfaces? What further tools and standards are already being developed on top of it? Join us in this session to answer these questions and find out what the future of localization will look like.

#### Related Links

- [Unicode MessageFormat Working Group](https://github.com/unicode-org/message-format-wg)
- [MF2 JavaScript implementation and Intl.MessageFormat polyfill](https://github.com/messageformat/messageformat/tree/main/mf2/messageformat)
- [moz.l10n: A new library of Python tools for working with localization files](https://github.com/mozilla/moz-l10n)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-inclusive-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-inclusive-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TBLGTT/feedback/)

---

### Alternative Text for Images: How Bad Are Our Alt-Text Anyway?

- **Speakers:** Mike Gifford
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 10:00 - 10:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4709-alternative-text-for-images-how-bad-are-our-alt-text-anyway-/)

#### Abstract

Alt text really are one of the low-hanging fruit of an inclusive web. Images need to be described. It is the very first success criteria in WCAG - SC 1.1.1: Non-text Content (Level A). It is so simple, yet it isn't. Despite all the guidance, including presentations like this one, folks get it wrong, over and over again. A lot can be done through using approaches like those recommended in the Authoring Tool Accessibility Guidelines (ATAG) 2.0. Clearly, authors need support. 
This presentation will cover a bit of this theory, but also highlight a simple Python script that I wrote to crawl a website so that we can more easily examine the alternative text that is provided. I'll quickly walk through the script, and then look at some of the more entertaining alt-text which is sitting on public government websites. 
It is worth noting that there is no automated tool that presently does much more than check that there is alt-text on an image. This clearly isn't sufficient to determining if the meaning of the image is represented in that alt text.

#### Related Links

- [AltText Scan Tool](https://github.com/CivicActions/site-evaluation-tools/blob/main/alt-text-scan.py.md)
- [Alt Text Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-inclusive-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-inclusive-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FJHKZE/feedback/)

---

### Secure and Inclusive: WebAuthn for (Multi-Factor) Authentication

- **Speakers:** Storm Heg
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 10:30 - 10:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5777-secure-and-inclusive-webauthn-for-multi-factor-authentication/)

#### Abstract

Many websites and services require users to authenticate themselves. Passwords are the well-known way to do this, but they don't provide great security anymore on their own. That's why many websites and services are moving to require Multi-Factor Authentication (MFA), using phone apps and SMS messages and email links.
These methods aren't always very user friendly, especially to people with disabilities. 
WebAuthn is a new standard that allows websites to use your user's device to authenticate them - more commonly known as Passkeys. It's more secure than passwords, and more user friendly than most MFA.
Let's discuss how WebAuthn works and how you can integrate it into your website or service.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-inclusive-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-inclusive-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/D9YXSC/feedback/)

---

### How do we work out the environmental savings from accessibility?

- **Speakers:** Chris Adams
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 11:00 - 11:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5292-how-do-we-work-out-the-environmental-savings-from-accessibility-/)

#### Abstract

We know that using devices for longer can reduce the amount e-waste the world generates, but how much can it help?
In this talk, we'll take a look how we can quantify the environmental savings from supporting a wider range of devices with the digital services we design and operate.
We'll look at the approach used by peer reviewed papers on induced hardware upgrades, and see how they track obscelence through user data, to see which techniques we can apply to our own work.
In addition, we'll also look at a few high profile examples of companies ending support for older devices, or requiring beefier minimum spec hardware to help understand the environmental impact of these decisions.
Finally, we'll conclude with a tour of the policy changes and dataset releases in different parts of the world, that show signs of a way forward out of this mess. These will be useful to people looking to refer to new laws being passed and new data to when making the argument for both accessibility and sustainability in the workplace.

#### Related Links

- [The Green Web Foundation's own calculations working for understanding the CO2 footprint of our digital services](https://github.com/thegreenwebfoundation/Technology-Carbon-Standard)
- [The presenter's earlier talk at FOSDEM presenting G.O.L.D. - the sustainabilty version of P.O.U.R., used in accessibility](https://archive.fosdem.org/2021/schedule/event/webperf_building_a_greener_web/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-inclusive-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-inclusive-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZBMYDF/feedback/)

---

### Growing inclusive communities: Djangonaut Space program

- **Speakers:** Raffaella Suardini
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 11:30 - 11:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5237-growing-inclusive-communities-djangonaut-space-program/)

#### Abstract

Abstract: Increase regular and sustainable contributions, create a sustainable space for new contributors to join are the goals of the Djangonaut Space mentorship program.  In this talk, I will show how the program achieved its goals and provide strategies for building similar initiatives.
Description: The Djangonaut Space program, designed for the Django framework, is proof that an inclusive community can make a huge difference.
This talk will show how and why a mentorship program could be a win example to follow. 
Outline:
1. The importance of inclusivity in open source
The challenges for new contributors
Why mentorship
2. Djangonaut Space explained
Create a space and invite them to join
The structure
Not code only: events and not non-code contributions
3. Some result
How the program had an impact on the Django community

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-inclusive-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-inclusive-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/39CYV9/feedback/)

---

### Multilingual Speech Technologies That Understand You

- **Speakers:** Jessica Rose
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 12:00 - 12:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5948-multilingual-speech-technologies-that-understand-you/)

#### Abstract

As more and more users connect to the web for the first time, they’re often met with an online environment that fails to support them in the languages they use day to day. Limited language options on the web and in connected technologies doesn’t just leave individual users unsupported, but also contributes to pressures that endanger minority languages. To help combat these pressures in speech technologies, Common Voice has collected a multilingual, crowdsourced speech dataset to encourage developers and researchers to build for their communities in the languages they use daily. Together we’ll explore how speech technologies lower barriers to access for web users, how dataset access issues often restrict linguistic diversity and look at what a future of meaningfully inclusive speech technologies could mean for the speakers of +7000 languages around the world.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-inclusive-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-inclusive-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7PXMJ9/feedback/)

---

### ATAG accessibility audits: worth your while

- **Speakers:** Thibaud Colas
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 12:30 - 12:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5806-atag-accessibility-audits-worth-your-while/)

#### Abstract

Have you heard about ATAG? The Authoring Tool Accessibility Guidelines are very relevant for content creation tools, and yet few people are aware of its existence and how to approach it. We’ll have a look at a real-world example, sharing practical tips and examples on the theme of getting up to speed with ATAG.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-inclusive-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-inclusive-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XJ7TYN/feedback/)

---

## JavaScript (7)

### Push-Based Hypermedia with Datastar

- **Speakers:** Patrick Marchand
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 09:00 - 09:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6316-push-based-hypermedia-with-datastar/)

#### Abstract

Datastar is a lightweight, extensible JavaScript framework for building push-based web applications. This talk will demonstrate how Datastar simplifies UI development compared to full-stack frameworks like React, Vue.js, or Svelte, while embracing a hypermedia-driven approach.
Patrick will demonstrate how you can instantly add reactivity and real-time updates to a frontend using Datastar and set up a backend using NodeJS for streaming server-sent events (SSE). Attendees will learn how to use Datastar to develop fast, reactive and highly efficient web applications.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-javascript:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-javascript:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZQAR9K/feedback/)

---

### How to lose weight? - Optimising memory usage in JavaScript and beyond

- **Speakers:** Aapo Alasuutari
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 09:30 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4391-how-to-lose-weight-optimising-memory-usage-in-javascript-and-beyond/)

#### Abstract

In this talk we'll take a look at strategies, tips, and tricks for optimising memory usage in not only JavaScript but software in general. The core ideas come from databases and data-oriented design principles, storing data efficiently and taking advantage of context knowledge on the data you work with. Reasoning about the memory usage of a JavaScript program also requires looking into the internal workings of JavaScript engines, which we'll cast a critical eye on. We then try to apply the strategies on a JavaScript engine, using the speaker's Nova engine as the end result example.
https://trynova.dev/

#### Related Links

- [Presentation slides Google Docs](https://docs.google.com/presentation/d/10UltQVVPwZ7FfDbNuYc3lW99bMzZZS6HBa2bmM-xrjk/edit?usp=drivesdk)
- [Presentation code examples repository](https://github.com/aapoalas/losing-weight)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-javascript:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-javascript:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HLJ3JQ/feedback/)

---

### JSR: from private ownership to open governance

- **Speakers:** Leo Kettmeir, Luca Casonato
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 10:00 - 10:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6519-jsr-from-private-ownership-to-open-governance/)

#### Abstract

JSR is a new JavaScript registry, which was started by the Deno company. However, from the beginning, the idea was to not have this to remain the case, and instead move it to be under open governance.
The reasons and processes for such things are multifold and complex, but despite this are beneficial and important to move forward the ever-evolving JavaScript ecosystem.

#### Related Links

- [Repository](https://github.com/jsr-io/jsr)
- [Website](https://jsr.io/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-javascript:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-javascript:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GQRXXS/feedback/)

---

### Nobody asks "How is JavaScript?"

- **Speakers:** Ujjwal Sharma
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4276-nobody-asks-how-is-javascript-/)

#### Abstract

From frontend developers to data scientists; from hobbyists to researchers, the JavaScript programming language offers something to everyone. Still, while everybody asks "what is JavaScript?" nobody asks "how is JavaScript?".
It might therefore be interesting to dig a bit deeper into this complex and versatile programming language: Where is it going? How has it evolved over the years? How does language design and evolution happen in the first place? What are the rules put in place to ensure that it evolves in the right direction and continue to serve its ever-evolving set of users and other stakeholders?
Join me in this overview of the TC39 standards committee, its processes and initiatives as we learn just how much work goes into reshaping the most popular programming language for the future.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-javascript:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-javascript:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SHP3PW/feedback/)

---

### Privacy-first architecture: alternatives to GDPR popup and local-first

- **Speakers:** Andrey Sitnik
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 11:00 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4233-privacy-first-architecture-alternatives-to-gdpr-popup-and-local-first/)

#### Abstract

Why and how modern developers could increase the privacy of modern Web.
The popularity of clouds, the rise of huge monopolies across the internet, and the growth of shady data brokers recently have made the world a much more dangerous place for ordinary people—here is how we fix it.
In this talk, Andrey Sitnik, the creator of PostCSS and the privacy-first open-source RSS reader, will explain how we can stop this dangerous trend and make the web a private place again.
— Beginners will find simple steps, which can be applied to any website
— Advanced developers will get practical insights into new local-first architecture
— Privacy experts could find useful unique privacy tricks from a global world perspective and beyond just U.S. privacy risks

#### Related Links

- [Slides](https://slides.com/ai/privacy/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-javascript:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-javascript:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QSLMU9/feedback/)

---

### Demystifying Temporal: A Deep Dive into JavaScript New Temporal API

- **Speakers:** Aditi
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 11:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4397-demystifying-temporal-a-deep-dive-into-javascript-new-temporal-api/)

#### Abstract

This talk covers fundamental principles that drive Temporal's functionality, including essential concepts like immutable objects, extended range and precision, and improved time zone support. It also provides details about all different data types you can find in the API, when and how to use them,
and essentially sets the stage for seamless integration of Temporal into your codebase.

#### Related Links

- [Temporal proposal github repository](https://github.com/tc39/proposal-temporal)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-javascript:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-javascript:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/33ATEQ/feedback/)

---

### 25 years of JavaScript

- **Speakers:** Steven Goodwin
- **Room:** UB5.230
- **Day:** Sunday
- **Time:** 12:00 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4227-25-years-of-javascript/)

#### Abstract

I have being coding with JavaScript for 25 years. In that time I've seen everything - from when debugging meant calls to alert() and web animations meant Flash, to canvas graphics and real-time MIDI. So, why not see what was considered cutting edge in a world before Facebook and bitcoin!
From 3D graphics without WebGL, to particle systems, Grand Theft Auto in LEGO, YouTube APIs, WebRTC, speech recognition, VR, WebAudio, Alexa, WebSockets, and myriad frameworks, there are a million things now possible with JavaScript that was unimaginable back in 1999. Come and enjoy the history lesson (if you're young) or the nostalgia (if you're old...er) to be reminded just how great JavaScript can be!

#### Related Links

- [MIDI lib](https://github.com/MarquisdeGeek/midilib)
- [Flight Spy - mashing up OSM and Flight Radar to determine what's on your flightpath](https://github.com/MarquisdeGeek/FlightSpy)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-javascript:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-javascript:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NYYUXC/feedback/)

---

## Kernel (17)

### Linux Kernel Mainline Real-Time History, Support and Experience Based on Robotic and Automotive Projects

- **Speakers:** Pavel Pisa
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 09:00 - 09:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5411-linux-kernel-mainline-real-time-history-support-and-experience-based-on-robotic-and-automotive-projects/)

#### Abstract

In September 2024, the last modification required to enable PREEMP_RT for the x86, AArch64 and RISC-V architectures was submitted to the main development tree by Thomas Gleixner (Linutronix). Even the previous real-time-related enhancements brought so many valuable fixes and features for kernel deployment outside the RT area that Linus Torvalds recognized the community around RT deployment of GNU/Linux as valuable and worthy of gradually incorporating its work over the years.  The first meeting of the community interested in using GNU/Linux in RT applications took place in Vienna exactly 25 years ago (Real Time Linux Workshop). Another round anniversary is 20 years since kernel list debate following by possible solutions for real-time Linux deployment debate at the Real Time Linux Workshop conference at Lanzhou University in China. The first minor modifications (runtime locking correctness validator) were included in the main development tree by that time as well as mutex priority inheritance, the fundamental requirement for each RTOS. To date, about 10,000 changes have been submitted to the main kernel tree directly by the RT development team and 5,000 changes in the related drivers and subsystems added by their maintainers in response to patch requests and other needs.
In this talk, I will present the development history, highlight and gaps learned, testing for automotive communication etc. because I have followed the development from the beginning to allow our applications and projects realization.

#### Related Links

- [Real Time Linux collaborative project Wiki by Linux Foudation](https://wiki.linuxfoundation.org/realtime/start)
- [Open Source Automation Development Lab (OSADL) QA Farm on Real-time for Linux kernel latency testing](https://www.osadl.org/OSADL-QA-Farm-Real-time.linux-real-time.0.html)
- [Czech Technical University in Prague CAN/CAN FD projects for automotive, industry, RTOSes (Linux, RTEMS, NuttX), IP cores, latency testing etc.](https://canbus.pages.fel.cvut.cz/)
- [CTU FEE Open Technologies Research Education and Exchange Services wiki (the mostly procesor systems, control, PMSM, Linux and other RTOSes for education and practice)](https://gitlab.fel.cvut.cz/otrees/org/-/wikis/home)
- [It is really time to celebrate!, Thomas Gleixner and Heinz Egger publication about PREEMPT_RT development (PDF)](https://www.linutronix.de/PDF/Art_24_09_RT_Festschrift.pdf)
- [Mastodon announce/confirmation of  PREEMP_RT enable for x86, AArch64 and RISC-V mainlining at RT event](https://social.kernel.org/notice/AmBb9tDqmw7QG6B7Bo)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CD8RPX/feedback/)

---

### Macros Gone Wild: The Usage of the C Preprocessor in the Linux Kernel

- **Speakers:** Diomidis Spinellis
- **Room:** UD2.208 (Decroly)
- **Day:** Sunday
- **Time:** 09:30 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4717-macros-gone-wild-the-usage-of-the-c-preprocessor-in-the-linux-kernel/)

#### Abstract

The Linux kernel is a foundational element of the modern IT infrastructure, powering billions of devices from smartphones and routers to desktops and supercomputers. Consequently, the quality of its code affects IT's reliability, resilience, performance, and evolution. Through this presentation I aim to improve our understanding of the Linux kernel's code quality regarding its usage of the C preprocessor: a dated, ubiquitous, and often insidious part of the compilation process. I show the characteristics of the C preprocessor's usage, the introduced technical debt, the usage's evolution, and the feasibility of reducing the incurred technical debt, mainly through refactoring and by utilizing facilities of the Rust programming language.
As a tool for the analysis I extended the CScout refactoring browser to collect tens of metrics before and after the C preprocessor's execution. I then applied CScout on three versions of Linux spanning two decades, running the oldest kernel analysis on the QEMU emulator  and the newest on the ARIS supercomputer, processing in total more than 45 million lines of code.
I found that the C preprocessor is extensively used, often doubling key code elements seen by the C compiler-proper. The preprocessor's use is associated with several types of technical debt including namespace pollution; scoping, namespace, and control-flow confusion; composite identifiers; hybrid call paths; deep and cyclic include hierarchies; expansion explosions; and structural quality metrics deterioration. Although the density of some preprocessor usages is steady or decreasing over time, some worrisome usages are showing significant increases.
To explore how this situation can be addressed, I present a taxonomy of non-trivial C preprocessor use cases, which indicates that there two broad categories of changes that can be made. First, most object-like macros can be easily refactored into C const objects or enum values, while about half of the function-like macros could be rewritten as C functions. Although this change is wide in scope the corresponding gains in code maintainability will be small. Second, the remaining non-trivial C preprocessor function-like macros could be refactored; many through specific facilities of Rust that I describe for corresponding macro use cases. In this case however the amount of required engineering effort is large.

#### Related Links

- [CScout - The C refactoring browser used to analyze the Linux kernel](https://github.com/dspinellis/cscout)
- [Three Linux kernels broken down at the level of individual identifier tokens provided as SQLite databases](https://doi.org/10.5281/zenodo.13756472)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-kernel:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-kernel:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LZDHSK/feedback/)

---


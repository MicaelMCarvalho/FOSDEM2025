# FOSDEM 2025 Schedule - Part 10 of 11

*Generated on 2025-02-01*

## Table of Contents

- [Robotics and Simulation (14)](#robotics-and-simulation-14)
- [Rust (12)](#rust-12)
- [Security (17)](#security-17)
- [Social Web (12)](#social-web-12)
- [Software Bill of Materials (SBOM) (19)](#software-bill-of-materials-sbom-19)
- [Software Defined Storage (14)](#software-defined-storage-14)
- [Swift (13)](#swift-13)
- [Testing and Continuous Delivery (19)](#testing-and-continuous-delivery-19)

## Robotics and Simulation (14)

### Eclipse Zenoh: Understanding the Protocol and its Potential in Robotic

- **Speakers:** Julien Enoch
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 15:10 - 15:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5446-eclipse-zenoh-understanding-the-protocol-and-its-potential-in-robotic/)

#### Abstract

Eclipse Zenoh has established itself as the new kid on the block in communication protocols. In just a few years it has been identified as the best protocol in robotics and the next big thing in distributed computing such as Vehicles-to-everything (V2X) and communications.
This talk will introduce the innovations brought by Zenoh, explain its unique features and explain what it does differently from other protocols. Additionally, it will explain why it has been chosen as an alternative middleware for ROS 2 and how it unlocks a series of use cases that were extremely hard to implement before. Finally the talk will give an overview of what's coming next with Zenoh for robotic and beyond.

#### Related Links

- [Eclipse Zenoh repository](https://github.com/eclipse-zenoh/zenoh)
- [Zenoh plugin for ROS 2](https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds)
- [RMW Zenoh for ROS 2](https://github.com/ros2/rmw_zenoh)
- [Zenoh web site](https://zenoh.io)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BZJHMS/feedback/)

---

### BTstudio, a web tool for programming robots with Behavior Trees

- **Speakers:** JoseMaria Cañas Plaza, Javier Izquierdo Hernández
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 15:40 - 16:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5820-btstudio-a-web-tool-for-programming-robots-with-behavior-trees/)

#### Abstract

BTstudio is an open-source tool crafted for the development of robotic applications. Its primary objective is to facilitate the quick deployment of behavior tree-based robotic applications within ROS 2. In BTstudio, a robotics app is defined as a graphical tree coupled with actions scripted in Python, which the tool then translates into a ROS 2 package. This process circumvents the unnecessary complexities often associated with ROS-specific configurations, offering developers a more streamlined approach.
Check it out its repo (https://github.com/JdeRobot/bt-studio) and some recent demo videos (https://www.youtube.com/watch?v=otDZ_CdceP0) (https://www.youtube.com/watch?v=3t_r88cMECU)

#### Related Links

- [GitHub repository](https://github.com/JdeRobot/bt-studio)
- [Demo video 1](https://www.youtube.com/watch?v=otDZ_CdceP0)
- [Demo video 2](https://www.youtube.com/watch?v=3t_r88cMECU)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PWQQQT/feedback/)

---

### ArduPilot : Trusted, Versatile and FOSS autopilot for all and everything

- **Speakers:** PIERRE KANCIR
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 16:10 - 16:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5476-ardupilot-trusted-versatile-and-foss-autopilot-for-all-and-everything/)

#### Abstract

ArduPilot is a trusted, versatile, and open source autopilot system supporting many vehicle types: multi-copters, traditional helicopters, fixed wing aircraft, boats, submarines, rovers and more. The source code is developed by a large community of professionals and enthusiasts.
ArduPilot enables the creation and use of trusted, autonomous, unmanned vehicle systems for the peaceful benefit of all. ArduPilot provides a comprehensive suite of tools suitable for almost any vehicle and application. As an open source project, it is constantly evolving based on rapid feedback from a large community of users. The Development Team works with the community and commercial partners to add functionality to ArduPilot that benefits everyone. Although ArduPilot does not manufacture any hardware, ArduPilot firmware works on a wide variety of different hardware to control unmanned vehicles of all types. Coupled with ground control software, unmanned vehicles running ArduPilot can have advanced functionality including real-time communication with operators. ArduPilot has a huge online community dedicated to helping users with questions, problems, and solutions.
https://ardupilot.org/
This talk is an introduction to ArduPilot project. It will emphasis what can be done from a software point of view, what hardware (we are far from Arduino) and robotic vectors can be used  (we aren't not restricted to UFO), and what are the testing and simulation capabilities (aka stop crashing your robots). It will also showcase relationship to some other major projects like ROS2 and Gazebo or AI (added for better SEO). 
This won't be a tutorial or live demo session but a true introduction of the project.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WQXXWK/feedback/)

---

### Whales use Lighthouses too: Open source positioning for open source robots

- **Speakers:** Michel Hidalgo, Lucas Chiesa
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 16:40 - 16:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6448-whales-use-lighthouses-too-open-source-positioning-for-open-source-robots/)

#### Abstract

This talk is a chronicle of our journey integrating Andino an open source ROS 2 differential drive robot, with the Bitcraze™ Lighthouse Positioning System and the Beluga library for Monte Carlo Localization. By exposing raw Lighthouse measurements through ROS 2 and leveraging Beluga’s algorithms, Andino achieves precise and affordable localization. This project highlights the practical benefits of collaboration within the open-source robotics community and emphasizes the importance of fostering synergy between open hardware and software projects to drive innovation.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HDQWCY/feedback/)

---

### Build, Launch, and Soar with Dronecode: The infrastructure ecosystem for the development of autonomous aerial robotics.

- **Speakers:** Ramon Roche
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 16:45 - 16:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6353-build-launch-and-soar-with-dronecode-the-infrastructure-ecosystem-for-the-development-of-autonomous-aerial-robotics-/)

#### Abstract

This talk will offer a roadmap into the ins and outs of the top projects in aerial robotics, including a detailed overview of the PX4 Autopilot and Pixhawk. Our projects helped propel the industry from its DIY roots into a mature and professional industry, supporting thousands of developers and companies. I will offer attendees a complete guide on how to maximize the benefits of the open-source codebases and the community surrounding the projects. 
The Dronecode Foundation hosts an ecosystem of open source projects, developers, and contributing organizations. Dronecode is an umbrella foundation (part of The Linux Foundation) hosting open-source projects that offer solutions to robotics developers looking to build Aerial solutions. 
With the PX4-Autopilot at its center, our projects are part of a comprehensive toolbox with everything developers need to create anything from a simple waypoint-following vehicle to delivering packages in urban environments for Walmart. 
I will provide everything you need to know about the projects, plus offer a never-before-seen look into the inner workings of the maintainer team building the infrastructure supporting them and showing you how you too can help them as an individual contributor.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WS9Q9Y/feedback/)

---

### Integration and unit testing in ROS 2

- **Speakers:** Arne Baeyens
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 16:50 - 16:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6310-integration-and-unit-testing-in-ros-2/)

#### Abstract

As modern robotics systems grow more complex, it’s crucial to have an effective testing strategy in place to ensure robust and reliable performance as well as an efficient development workflow. In this talk, we'll show how to set up unit and integration testing in ROS 2, covering tools such as launch_testing, unittest, gtest and pytest, as well as integration testing basics (including test isolation) and test output visualization.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KJRPNU/feedback/)

---

### ROS in transition: a new organizational path under the Open Source Robotics Alliance

- **Speakers:** Jose Luis Rivero
- **Room:** UB2.147
- **Day:** Sunday
- **Time:** 16:55 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6212-ros-in-transition-a-new-organizational-path-under-the-open-source-robotics-alliance/)

#### Abstract

At FOSDEM 2013, Open Robotics provided an overview of the Robot Operating System (ROS), which was originally developed in 2007. In FOSDEM 2020, the community was introduced to ROS 2, a major rewrite of the framework. Now, five years later, Open Robotics no longer exists as a company, and the largest open-source robotics community is navigating the transition to a new, sustainable model. It’s an exciting time.
This talk will provide a quick overview of the years of ROS under the umbrella of Open Robotics Inc (and the Open Source Robotics Foundation).It will explore the transition following the dissolution of Open Robotics Inc., and introduce the new operational and governance model that has been established through the formation of the Open Source Robotics Alliance with a focus on how the different models impact the technical work done by the core team.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-robotics:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-robotics:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QV9UZL/feedback/)

---

## Rust (12)

### Augurs: a time series toolkit for Rust

- **Speakers:** Ben Sully
- **Room:** UB2.252A (Lameere)
- **Day:** Saturday
- **Time:** 10:30 - 11:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4668-augurs-a-time-series-toolkit-for-rust/)

#### Abstract

augurs is a new library for time series analysis (think forecasting, outlier detection, clustering, and more) written in Rust, with bindings available for Javascript and Python. It includes functionality borrowed from both Python and R libraries, plus some more novel ideas. Come and learn about what it can do, as well as:

choices made when porting algorithms from different languages
techniques used for profiling and optimizing ML code in Rust
tradeoffs when creating Javascript/WebAssembly bindings
what kind of performance and usability gains to expect

#### Related Links

- [Demo](https://demo.augu.rs)
- [Docs](https://docs.augu.rs)
- [GitHub](https://github.com/grafana/augurs)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rust:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rust:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8YATE7/feedback/)

---

### Building a watt-meter esp-rs and a rocket backend

- **Speakers:** Santiago Saavedra
- **Room:** UB2.252A (Lameere)
- **Day:** Saturday
- **Time:** 11:15 - 11:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5470-building-a-watt-meter-esp-rs-and-a-rocket-backend/)

#### Abstract

I wanted to have a watt-meter that I could plug into my electrical supply to ensure I didn't trip the max rating at my granparents' when charging an EV. I could have bought a "smart-balancing charger" to handle this for me, but I wanted to keep costs low and learn embedded Rust.
On this talk I'll go over how to manage side-projects, keep objectives reasonable and the technical details and how easy it is to build an API backend using Rocket, handling serialization and parallelism, as well as using Rust on the embedded device, including flashing, demonstrated how this is all integrated into cargo as a build tool.
Wattmeter code: https://github.com/ssaavedra/esp32-amp-sensor
Backend: https://github.com/ssaavedra/amp-sensor-backend

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rust:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rust:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ERWZVL/feedback/)

---

### Huge graph analysis on your own server with WebGraph in Rust

- **Speakers:** Sebastiano Vigna
- **Room:** UB2.252A (Lameere)
- **Day:** Saturday
- **Time:** 11:40 - 12:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4773-huge-graph-analysis-on-your-own-server-with-webgraph-in-rust/)

#### Abstract

Huge graphs, from billions to trillions of nodes and arcs, are more and more common in modern data-intensive applications. Graph compression techniques allow loading and manipulating such graphs into main memory of either high-end workstations or commercial-grade servers, depending on graph size. In this talk, we report about webgraph-rs, a recent clean-slate Rust re-implementation of WebGraph, a state-of-the-art graph compression framework, formerly implemented in Java. webgraph-rs comes as a series of interconnected Rust crates of general interest, including high-performance bit streams, zero-copy (de)serialization, constant-time measurement of heap size for large data structures, and high-performance implementation of succinct data structures . Using webgraph-rs one can load graphs such as the Software Heritage Merkle DAG (about 0.6 trillion edges ) in less than 200 GiB of RAM and visit it in a few hours with a single core.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rust:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rust:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9JLWVN/feedback/)

---

### Bringing terminal aesthetics to the Web with Rust (and vice versa)

- **Speakers:** Orhun Parmaksız
- **Room:** UB2.252A (Lameere)
- **Day:** Saturday
- **Time:** 12:25 - 13:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5496-bringing-terminal-aesthetics-to-the-web-with-rust-and-vice-versa-/)

#### Abstract

Everyone loves the terminal! It's simple, efficient, and fast — almost everything the web is not.
What if I told you it is possible to build terminal-like web applications with Rust and vice versa?
Join me in this talk, where we explore the future of the terminal and the web and how the Ratatui ecosystem is bringing these two worlds together. We will take a look at example Rust projects that achieved this, their implementation, and the challenges that we are facing.
Get ready to be visually impressed!

#### Related Links

- [GitHub (@orhun)](https://github.com/orhun)
- [YouTube (@orhundev)](https://www.youtube.com/@orhundev)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rust:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rust:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SANWW3/feedback/)

---

### Abusing reborrowing for fun, profit, and a safepoint garbage collector

- **Speakers:** Aapo Alasuutari
- **Room:** UB2.252A (Lameere)
- **Day:** Saturday
- **Time:** 13:10 - 13:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4394-abusing-reborrowing-for-fun-profit-and-a-safepoint-garbage-collector/)

#### Abstract

Rust's references adhere to a strict "one exclusive XOR many shared" model, which gives the language much of its greatest safety guarantees. Reborrowing is a feature that seems on surface to break this rule: An exclusive reference can be turned into shared references and those shared references can be used together with the exclusive reference as long as these are all used as if they were shared references. Only once the exclusive reference is used as exclusive, all the derived or "reborrowed" shared references are invalidated. The XOR rule is upheld, but in a way that breaks a literal reading of the rule.
Usually reborrowing is used temporarily but what if we make it our modus operandi? This talk explores using and slightly abusing reborrowing and comes out the other side with an awkward but functional safepoint garbage collector built upon reborrowing a ZST marker and a whole load of typed indexes. The garbage collector is part of the Nova JavaScript engine.
https://trynova.dev/

#### Related Links

- [Presentation slides Google Docs](https://docs.google.com/presentation/d/1jC5JZLdvuYmknKnJ9yTW1QisaDchahHUkOsGRep1vqU/edit?usp=drivesdk)
- [Presentation code samples repository](https://github.com/aapoalas/losing-weight)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rust:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rust:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WE39B8/feedback/)

---

### Type tips and tricks

- **Speakers:** Nikolai Vazquez
- **Room:** UB2.252A (Lameere)
- **Day:** Saturday
- **Time:** 13:55 - 14:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6412-type-tips-and-tricks/)

#### Abstract

Rust's type system can feel complicated and overwhelming. However, crates like Bevy and Divan take advantage of the advanced features to deliver simpler developer experiences. This talk will demonstrate how to create these easy-to-use APIs by covering advanced techniques like polymorphism, type states, and conditional typing.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rust:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rust:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VENK3H/feedback/)

---

### How I optimized zbus by 95%

- **Speakers:** Zeeshan Ali Khan
- **Room:** UB2.252A (Lameere)
- **Day:** Saturday
- **Time:** 14:40 - 15:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4104-how-i-optimized-zbus-by-95-/)

#### Abstract

This is a story of how I used a few readily-available Open Source tools to achieve huge optimizations in zbus, a pure Rust D-Bus library. This was long journey but gains were worth the efforts. I will go through each single bottleneck found, how it was found and why it was a bottleneck and how it was optimized away.
While attending this talk will by no means make you an expert in optimizations, it is my hope that by you will be able to relate to some of bottlenecks or solutions I will present ("hey", I also do that in my code!") and learn from my experience. Maybe afterwards, you can suggest an even better solution? Moreover, if you don't already have any experience with profiling and optimizations, this talk should be a good introduction for that.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rust:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rust:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JL9UTJ/feedback/)

---

### Programming ROS 2 with Rust

- **Speakers:** Júlia Marsal Perendreu
- **Room:** UB2.252A (Lameere)
- **Day:** Saturday
- **Time:** 15:25 - 15:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6548-programming-ros-2-with-rust/)

#### Abstract

Discover how the Rust programming language and the ROS 2 framework are transforming robotics development in this talk. Everything can be found in this repository: https://github.com/roboticswithjulia/ros2_rust_workshop. Participants will dive into the fundamentals of the ROS2 Rust package: https://github.com/ros2-rust/ros2_rust.
The session will highlight Rust's performance and safety benefits, its integration with ROS 2 for robotic systems, and practical implementation techniques. Through guided exercises, attendees will learn how to program and control a quadruped robot using Rust within the ROS 2 framework, gaining insights into the challenges of robotic systems and how this powerful combination addresses them effectively.
This talk is ideal for developers looking to enhance their robotics expertise using a modern programming language and a robust middleware. Whether you're new to Rust, ROS 2, or seeking to deepen your robotics knowledge, this session offers a unique opportunity to build robust and efficient systems for the robots of tomorrow.

#### Related Links

- [Programming ROS2 with Rust](https://docs.google.com/presentation/d/e/2PACX-1vQgFzPR4k4aCXXpMM0_NIh9Gmk6wpBSeMUWV2GFvW4RBP6vLjdyryvoxO4NAUO_d_XoO0ByuxX4boEM/pub?start=true&loop=false&delayms=3000)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rust:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rust:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8SMKUW/feedback/)

---

### Lessons from rewriting systems software in Rust

- **Speakers:** Ruben Nijveld
- **Room:** UB2.252A (Lameere)
- **Day:** Saturday
- **Time:** 15:50 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5088-lessons-from-rewriting-systems-software-in-rust/)

#### Abstract

Rewrite it in Rust has been a theme (and meme) for almost as long as Rust exists. But what actually makes a rewrite work? At first glance you would think that just making a memory safe implementation of a protocol, library or program should be enough. But in practice there are many factors that make an implementation work.
Our work on, among others, ntpd-rs, zlib-rs and sudo-rs gave us some insight into that. Both from outside the Rust community: How to identify projects that could benefit from a rewrite? What do you need to do to get your Rust project accepted in a wider community? How do you get your project known? How do I get my project distributed? But also from inside the Rust community: Which crates do can I use as dependencies? What if my preferred crate name is already in use? Should I publish on crates.io? Do I offer a Rust interface for my crate?

#### Related Links

- [Trifecta Tech Foundation](https://trifectatech.org/)
- [Sudo-rs dependencies: when less is better](https://tweedegolf.nl/en/blog/119/sudo-rs-depencencies-when-less-is-better)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rust:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rust:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PCUWBL/feedback/)

---

### Writing safe PostgreSQL extensions in Rust: a practical guide

- **Speakers:** Damien Clochard
- **Room:** UB2.252A (Lameere)
- **Day:** Saturday
- **Time:** 16:35 - 17:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4317-writing-safe-postgresql-extensions-in-rust-a-practical-guide/)

#### Abstract

PostgreSQL's extensibility is legendary, and a revolution is brewing: Rust is emerging as the new gold standard for writing robust, performant database extensions, with the promise to make them safer, faster, and more maintainable than ever before.
In this hands-on session, we'll discover the PGRX framework through 4 practical examples showcasing:

Memory safety guarantees
A fully managed development environment
Access to Rust's vast ecosystem of libraries
Seamless PostgreSQL integration

Based on my experience rewriting the PostgreSQL Anonymizer extension from C to Rust, I'll share the lessons learned along the way.
Whether you're a seasoned C developer, a rustacean,  or a new to PostgreSQL extension writing, this talk will equip you with the knowledge to leverage Rust's powerful features in your next database projects.

#### Related Links

- [PostgreSQL Anonymizer Extension](https://gitlab.com/dalibo/postgresql_anonymizer)
- [Practical Rust extension examples](https://gitlab.com/daamien/pgrx-tuto)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rust:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rust:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ELFYCF/feedback/)

---

### Rust-ifying the Linux kernel scheduler (in user space)

- **Speakers:** Andrea Righi
- **Room:** UB2.252A (Lameere)
- **Day:** Saturday
- **Time:** 17:20 - 18:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4620-rust-ifying-the-linux-kernel-scheduler-in-user-space-/)

#### Abstract

In the realm of operating systems, the heart of performance lies in the CPU scheduler: a critical component responsible for managing the execution of tasks on a system.
Exploring and customizing CPU scheduling policies has long been the realm of few highly specialized kernel developers, leaving most developers and researchers without the tools to tailor system performance to their unique needs.
What if we could unlock this potential and make it accessible to a wider audience, from game developers, cloud service providers to AI researchers and performance engineers?
With sched-ext [1], eBPF and Rust, this vision can become a reality, enabling the development of multiple dynamic specialized schedulers, tailored to specific system workloads and architectural topologies, that can be loaded and managed as regular user-space programs [2].
[1] https://sched-ext.com/
[2] https://github.com/sched-ext/scx/tree/main/rust/scx_rustland_core

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rust:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rust:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/L7JJLU/feedback/)

---

### Adventures in oxidizing Arch Linux Package Management

- **Speakers:** David Runge
- **Room:** UB2.252A (Lameere)
- **Day:** Saturday
- **Time:** 18:05 - 18:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6259-adventures-in-oxidizing-arch-linux-package-management/)

#### Abstract

In 2023 a small set of developers set out to work on a Rust-based framework for Arch Linux Package Management (ALPM) - see talks from FrOSCon 2023 and All Systems Go! 2023.
After months spent on securing funding for the work ahead, in late 2024 the project has picked up work again in an extended capacity.
In this talk we will explore the technical challenges this project seeks to overcome and provide an overview of the work ahead.
This will cover topics such as the writing of specifications for custom file types, dedicated metadata file parsers and writers, the design of libraries for package handling, the more generic verification of digital signatures for distribution artifacts and the integration with existing and upcoming package building and package management infrastructure.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-rust:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-rust:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PDWKV7/feedback/)

---

## Security (17)

### Syd: An Introduction to Secure Application Sandboxing for Linux

- **Speakers:** Ali Polatel
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4176-syd-an-introduction-to-secure-application-sandboxing-for-linux/)

#### Abstract

In this talk, I will introduce Syd, a GPL-3 licensed, rock-solid application kernel designed for sandboxing applications on Linux systems (version 5.19 and above). Over the past 16 years, Syd has evolved from a tool used within Exherbo Linux to detect package build mishaps into a robust security boundary for applications. The recent rewrite in Rust leverages modern Linux APIs such as seccomp-unotify(2), openat2(2), and pidfd_getfd(2) to eliminate time-of-check to time-of-use (TOCTTOU) vulnerabilities, which is essential for building a secure sandbox.
Syd aims to provide a simple interface over complex Linux sandboxing mechanisms -- including Landlock LSM, namespaces, ptrace(2), and seccomp-BPF/Notify -- which are often considered brittle and difficult to use. This approach is somewhat similar to OpenBSD's pledge(2) system call, offering a practical way to restrict application behavior. Unlike other sandboxing tools like Falco, Bubblewrap, Firejail, gVisor, and minijail, Syd operates without requiring extra privileges, SETUID binaries, or privileged kernel context. It adheres to the UNIX philosophy of doing one thing well with the least privilege necessary.
The presentation will cover Syd's key features:

Path Sandboxing: Controls filesystem access through various operations including read, write (with append-only paths and path masking), stat (aka path hiding), tmpfile creation, attribute changes, truncation, node creation, file creation, and deletion.
Execution Control: Implements exec sandboxing with SegvGuard, force sandboxing for verified execution, and Trusted Path Execution to enforce strict execution policies.
Network Sandboxing: Restricts network access, supporting UNIX, IPv4, IPv6, Netlink, and KCAPI sockets, along with application firewalls and IP blocklists.
Advanced Features: Includes lock sandboxing using Landlock LSM, proxy sandboxing with network namespace isolation (defaulting to TOR), memory and PID sandboxing as simpler alternatives to control groups, SafeSetID for secure UID/GID transitions, and Ghost mode for enhanced process isolation.

I will also discuss how Syd addresses common security challenges such as TOCTOU issues and side-channel attacks, aligning with a threat model similar to that of seccomp. Attendees will gain insights into the design and implementation of Syd, its practical applications in enhancing system security, and how it can be integrated into various environments -- including as a login shell -- to provide robust application isolation.

#### Related Links

- [Syd homepage](https://sydbox.exherbolinux.org)
- [Syd source](https://gitlab.exherbo.org/sydbox/sydbox)
- [Syd CTF](https://ctftime.org/event/2178)
- [Article: State of Sandboxing on Linux](https://git.sr.ht/~alip/syd/tree/main/item/doc/toctou-or-gtfo.md)
- [PDF](https://gitlab.exherbo.org/sydbox/sydbox/-/blob/main/doc/talks/2025-Syd-FOSDEM/Syd-FOSDEM.pdf?ref_type=heads)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YEC9VE/feedback/)

---

### Tightening every bolt

- **Speakers:** Daniel Stenberg
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 11:00 - 11:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4204-tightening-every-bolt/)

#### Abstract

Things to do in order to sleep well while having your C code in twenty billion installations. A talk about what the curl project does to minimize security risks: Security, Safety, Reproducibility, Vulnerability handling and the processes and tooling around it.
As BDFL of the curl project, Daniel talks about what this project does to avoid it causing the world to burn. From code style, reviews and tests to signings, reproducibility, running a bug-bounty and becoming a CNA to filter bogus CVEs. curl aims to be top of the class in (Open Source) software security. Here's your chance to point finger and tell us what we should do better.

#### Related Links

- [The curl project](https://curl.se/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/A7RD7H/feedback/)

---

### Kintsugi: A Decentralized E2EE Key Recovery Protocol

- **Speakers:** Emilie Ma
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 11:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5266-kintsugi-a-decentralized-e2ee-key-recovery-protocol/)

#### Abstract

Key recovery is the process of regaining access to end-to-end encrypted data after the user has lost their device, but still has their password. Existing E2EE key recovery methods, such as those deployed by Signal and WhatsApp, centralize trust by relying on servers administered by a single provider.
In this talk, we share our recent work on Kintsugi, a decentralized recovery protocol that distributes trust over multiple recovery nodes, which could be servers run by independent parties, or end users in a peer-to-peer setting. This talk will cover how we developed Kintsugi and its unique security properties, as well as compare it to prior E2EE key recovery work.
See the demo implementation here.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YTX97U/feedback/)

---

### Nothing to see here - practical advice to avoid tunnel vision and similar decloaking techniques against VPNs

- **Speakers:** Till Maas
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 12:00 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5833-nothing-to-see-here-practical-advice-to-avoid-tunnel-vision-and-similar-decloaking-techniques-against-vpns/)

#### Abstract

In May 2023, the a decloaking method called tunnelvision raised awareness about security implications about supporting the DHCP option 121. This talk with show practical mitigation methods against this technique and also similar issues that deserve similar attention. This will be from the perspective of the team developing NetworkManager that makes mitigation against this easily available.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TDXRU8/feedback/)

---

### The SELinux problem that cast a months long shadow

- **Speakers:** Matyas Horky
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 12:30 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4332-the-selinux-problem-that-cast-a-months-long-shadow/)

#### Abstract

In February 2024, Red Hat released an update to insights-core, a package providing host data for Red Hat Insights. It slipped through our testing and caused all SELinux-enabled systems to crash the service, stopping the hosts from reporting. Even though the patch was released two days later, we couldn’t fix the hosts ourselves, and had to figure out which customers are affected and how to even contact them. It was a big lesson to both engineering and management. We’d like to share this story with the public.

#### Related Links

- [Product page for Red Hat Insights](https://www.redhat.com/en/technologies/management/insights)
- [Main repository of insights-client](https://github.com/RedHatInsights/insights-client/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AJKYVM/feedback/)

---

### A Practical Introduction to using sq, Sequoia PGP's CLI

- **Speakers:** Neal H. Walfield
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 13:00 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6297-a-practical-introduction-to-using-sq-sequoia-pgp-s-cli/)

#### Abstract

sq is Sequoia PGP's primary command line tool.  After seven years of
development, we've just released version 1.0.
In this talk, I'll present sq.  I'll start by discussing sq's design
philosophy.  In particular, I'll explain how sq aims to firstly be a
tool for end users, and not developers writing scripts, and what that
means for users of the tool.  I'll then present how sq is different
from other tools in the ecosystem.  In this regard, one of the most
important differences is that sq explicitly does not support curated
keyrings; users have to authenticate all of the certificates that they
use.  At first blush, this may sound like a usability nightmare, but
I'll show how sq supports users by managing evidence, which simplifies
these decisions.  Finally, I'll demonstrate several workflows.  These
include how to verify files, how to create and manage a certificate,
how to find a certificate and use it, and how to create and manage a
CA for your organization.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7VH3QM/feedback/)

---

### Using DPoP to use access tokens securely in your Single Page Applications

- **Speakers:** Alexander Schwartz, Takashi Norimatsu
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 13:30 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5370-using-dpop-to-use-access-tokens-securely-in-your-single-page-applications/)

#### Abstract

OAuth 2.0 uses access tokens to grant access to secured resources. When using Single Page Applications, they are passed from browsers to the servers as bearer tokens using HTTP headers.
While they are secured in transit using TLS, those tokens could be stolen from a browser, replayed, or mis-used by a malicious or vulnerable server. OAuth 2.0 Demonstrating Proof-of-Possession (DPoP) takes this one step further by equipping the client like your Single Page Application with a key pair so that it can show a proof when passing the access token, so no-one else can use the access token. DPoP is part of the FAPI 2.0 Security Profile by the OpenID Foundation. It promotes best practices on how to protect APIs exposing high-value and sensitive (personal and other) data, for example, in finance, e-health and e-government applications.
This talk will explain the concepts and demos how this can be implemented using Keycloak and other open source components. We will also describe the current challenges, limitations and alternatives of the approach.

#### Related Links

- [Demo Code](https://github.com/ahus1/dpop-demo)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RXRFSK/feedback/)

---

### Breaking Barriers: The Art of (Free) Gamified Security Training

- **Speakers:** Joseph Katsioloudes
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 14:00 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4719-breaking-barriers-the-art-of-free-gamified-security-training/)

#### Abstract

In a world where security training often feels like a mundane chore, discover the refreshing impact of gamification and turn learning into an enjoyable experience. Embark on an insightful journey as we unveil the success story of gh.io/secure-code-game, an open-source game hosted on GitHub Skills, that attracted over 5,000 developers within its first year.
This session will provide you with an exclusive behind-the-scenes perspective, offering valuable insights and practical strategies to revolutionize various aspects of security training for your benefit. We’ll explore a case study from a tech startup that observed, among the developers who played the game, an increased sense of ownership for code security, improved communication with security teams, and a strong willingness to embrace further security training.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BLBSG9/feedback/)

---

### TKey, an open source/open hardware security token for SSH et c

- **Speakers:** Michael Cardell Widerkrantz
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 14:30 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6613-tkey-an-open-source-open-hardware-security-token-for-ssh-et-c/)

#### Abstract

The Tillitis TKey is a radical new open source and open hardware
FPGA-based general computer in the form factor of a USB security
token.  Due to the mandatory measurement of apps it generates secret
material on demand, with no persistance, based on the integrity of the
app and provides a secure environment to do sensitive computing like,
for instance, cryptographic signing, authentication, and similar uses.
In the talk I will present how the TKey works, especially with the killer app SSH, how it came about, and touch on how you develop apps for it, the tools available, and welcome
you to join the open source projects behind it. With a small,
dedicated team you can get a lot of things done, even with hardware
designs using FPGAs and your own design of PCBs.

#### Related Links

- [Tillitis repos](https://github.com/tillitis/)
- [Tillitis](https://tillitis.se/)
- [TKey Developer Handbook](https://dev.tillitis.se/)
- [TKey SSH Agent](https://github.com/tillitis/tkey-ssh-agent/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9HMKQ9/feedback/)

---

### Hardware backed SSH keys: ssh-tpm-agent

- **Speakers:** Morten Linderud
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 15:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5544-hardware-backed-ssh-keys-ssh-tpm-agent/)

#### Abstract

SSH keys are an important part of system administration as they give access to remote systems. While openssh supports the PKCS11 interface, and yubikeys through the sk key types, they introduce challenges such as acquiring additional hardware, or introducing external code into sensitive processes. TPM are widely available hardware devices that allows key creating, signing and encryption operations on a separate hardware, however they do not have native supported by the openssh, and similar projects.
ssh-tpm-agent implements support for TPM wrapped SSH keys through the ssh agent interface. This allows a clear process separation for the keys, while ensuring no new support is required in the openssh project. The agent has support for RSA and ECDSA keys, while also having additional features like host keys, proxy support for additional agents, wrapping of existing keys and import of remotely created keys.
In this talk we will take a look at how the agent works, how the TPM is capable of preventing key extraction, and the other features available in the agent.

#### Related Links

- [linderud.dev: Store ssh keys inside the TPM: ssh-tpm-agent](https://linderud.dev/blog/store-ssh-keys-inside-the-tpm-ssh-tpm-agent/)
- [Github: ssh-tpm-agent](https://github.com/Foxboron/ssh-tpm-agent)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/R7VE7D/feedback/)

---

### Sigsum: Detecting rogue signatures through transparency

- **Speakers:** Niels Möller
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 15:30 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5661-sigsum-detecting-rogue-signatures-through-transparency/)

#### Abstract

When you install a properly signed software update, maybe the update
you got is different from what everyone else get. Maybe the attacker
was able to sign a malicious update due to key compromise, or coercion
of the legitimate key holder. How would you, or anyone else, notice?
One way to enable detection (but not prevention) of this kind of
attack is transparency. When installing updates, verify the signature
as usual. In addition, require that the signature is visible in a
public append-only transparency log, where entries can be added but
never removed.
Sigsum is a minimalistic transparency log that can accept signed
checksum submissions for a wide variety of applications and entities
that are neither known, nor trusted, by the log operator. The log
itself does not become a trusted third party for applications,
instead, applications depend on m-of-n trusted witnesses attesting
that the log behaves correctly. One of the many use-cases of Sigsum
logging is transparency for signed software packages and updates.
This talk explains the "detection, not prevention" benefits one can
get from Sigsum, and describes the different roles that make up the
Sigsum system.

#### Related Links

- [Project website](https://www.sigsum.org)
- [Repositories for source code and project documentation](https://git.glasklar.is/sigsum/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RJUHFN/feedback/)

---

### An overview on detecting Login Anomalies with BuffaLogs

- **Speakers:** Federico Foschini, Lorena Goldoni
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 16:00 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5623-an-overview-on-detecting-login-anomalies-with-buffalogs/)

#### Abstract

The infosec industry has seen a big growth in recent years, with a plethora of mostly closed-source solutions such as Endpoint Detection and Response (EDR), Security Information and Event Management (SIEM), and Security Orchestration, Automation, and Response (SOAR) marketed as indispensable tools for defending organizations. These solutions often emphasize protection against sophisticated adversaries, zero-day exploits, and malicious insiders. However, our real-world experience reveals that the majority of initial compromises occur through simpler approaches, such as stolen credentials and phishing attacks.
In this talk, we introduce Buffalogs, an open-source solution designed to detect and alert on anomalous login behaviors. Adhering to the Unix philosophy of "do one thing and do it well," Buffalogs offers a way to analyze common application logs (ssh, Apache, Microsoft Entra ID, etc) and detect credential misuse. Attendees will gain insights into the challenges of login anomaly detection, the development of Buffalogs and the differences between our solution and other commercial alternatives.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3GEQYC/feedback/)

---

### Managing Vulnerabilities in Open-Source Dependencies

- **Speakers:** Eva Sarafianou
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5588-managing-vulnerabilities-in-open-source-dependencies/)

#### Abstract

In today’s software development landscape, products are often an intricate blend of in-house code and open-source third-party dependencies. While many organizations have robust procedures to secure their own codebase, the strategies to safeguard against vulnerabilities in open-source components are not as well-developed.
In this session, we will navigate the complexities of implementing an effective process to manage vulnerabilities within open-source dependencies. Our discussion will cover key considerations for evaluating software composition analysis tools and detail the steps necessary for a successful tool rollout. We will delve into effective strategies for triaging findings and shifting from a reactive to a proactive security posture.
You will leave the session equipped with a foundational but adaptable process, ready to enhance the security of your products that depend on open-source dependencies.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JWZXVM/feedback/)

---

### What if Log4Shell were to happen today?

- **Speakers:** Piotr P. Karwasz
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 17:00 - 17:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6281-what-if-log4shell-were-to-happen-today-/)

#### Abstract

The Log4j project gained worldwide attention, when the Log4Shell bug shook the foundations of many software companies and government agencies, affecting millions of applications worldwide.
While the possibility of a security vulnerability can never be excluded, we will look at the steps taken by the Log4j project to minimize the security exposure of its users and drastically improve reaction times to any future vulnerability.

#### Related Links

- [Apache Log4j website](https://logging.apache.org/log4j/2.x/index.html)
- [Apache Log4j main repository](https://github.com/apache/logging-log4j2/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/G9FYGJ/feedback/)

---

### How Threat Actors Are Weaponizing Your Favorite Open-Source Package Registry

- **Speakers:** Ian Kretz, Sebastián Obregoso
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 17:30 - 18:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5662-how-threat-actors-are-weaponizing-your-favorite-open-source-package-registry/)

#### Abstract

What was the last npm package you installed?  Did anything unexpected happen?  Are you sure?
The scale and pace of modern software development are made possible by the ready availability of open-source packages via major registries like npm and PyPI.  These registries are always within reach of developers thanks to command-line package managers like npm and pip, enabling rapid testing and deployment of third-party code as part of normal workflows.  However, these benefits come at the cost of particular security concerns: threat actors routinely target software developers via open-source package registries, either by publishing backdoored packages or by taking over and corrupting legitimate software. In many such supply-chain attacks, merely installing the malicious package is enough to hand control of one’s system over to the adversary.
In this talk, we lay out the strategies that threat actors use when targeting software developers via open-source package registries.  We do so by examining case-studies in open-source malware delivery via npm and PyPI, some involving nation-state actors, that we at Datadog Security Research have collected while continuously monitoring these ecosystems with GuardDog, an open-source scanner for identifying malicious packages by analyzing code patterns and package metadata.  We then propose recommendations for developers, as well as for the package registries themselves, to counter these strategies that could lead to a greater overall level of software supply-chain security in the open-source community.

#### Related Links

- [GuardDog GitHub repository: CLI tool that allows to identify malicious PyPI and npm packages or Go modules](https://github.com/DataDog/guarddog)
- [Malicious Software Packages Dataset GitHub repository: open-source dataset with more than 2.8k malicious software packages](https://github.com/datadog/malicious-software-packages-dataset)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SBGRW9/feedback/)

---

### Hunting for GitHub Actions bugs with zizmor

- **Speakers:** William Woodruff
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 18:00 - 18:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6543-hunting-for-github-actions-bugs-with-zizmor/)

#### Abstract

Much of the world's open source lives on GitHub, and uses GitHub Actions to provide tasks ranging from routine testing to critical build and release processes. As such, the security of GitHub Actions (and the workflows and actions that users develop and consume) is paramount to the security of the world's software.
But how secure is GitHub Actions, really? This talk will introduce GitHub Actions' internal building blocks and (mostly implicit) security model, and provide real world examples of security failures and surprising avenues of exploitation that recur in widely used actions and workflows. These examples will be motivated via zizmor, a Rust-based static analysis tool for GitHub Actions that can catch many of the most common (and severe) footguns that occur when writing workflows.
Attendees will leave knowing more about GitHub Actions security and best practices for writing secure workflows, as well as how to use zizmor both locally and in CI to detect potential security issues. No prior familiarity with GitHub Actions is necessary.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/L9MCYZ/feedback/)

---

### Enhancing artifact security with GitHub Artifact Attestations

- **Speakers:** Fredrik Skogman
- **Room:** UB4.132
- **Day:** Saturday
- **Time:** 18:30 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5344-enhancing-artifact-security-with-github-artifact-attestations/)

#### Abstract

In the evolving landscape of software development, ensuring the
integrity of build artifacts like container images is crucial.
GitHub Artifact Attestations is an artifact signing solution and PKI
built on open source software like TUF and Sigstore. In this talk,
I'll discuss and demonstrate how to use Artifact Attestations to
generate signed SLSA attestations, and verifying their origin and
authenticity.
By the end of this session, you'll have a good understanding of how
open source tools like Sigstore, in-toto, SLSA and TUF can
collectively strengthen the security of the software supply chain.

#### Related Links

- [Sigstore](https://github.com/sigstore)
- [The Update Framework](https://github.com/theupdateframework)
- [The SLSA Framework](https://github.com/slsa-framework/)
- [GitHub CLI](https://github.com/cli/cli)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-security:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-security:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SVQPN8/feedback/)

---

## Social Web (12)

### Federated Blogging with WriteFreely

- **Speakers:** Matt Baer
- **Room:** UA2.118 (Henriot)
- **Day:** Saturday
- **Time:** 15:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6017-federated-blogging-with-writefreely/)

#### Abstract

While much of the fediverse has historically focused on microblogging, we've built an open source, federated blogging platform called WriteFreely that enables publishing long-form content to the social web.
In this talk, I'll show how WriteFreely works, and discuss how we integrated ActivityPub into our existing software (written in Go) to give writers a new way to socialize on the open web. I'll share lessons learned from this process, and discuss some ideas for supporting new content forms (like long-form Articles) into the wider fediverse.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-social-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-social-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/W3QMB7/feedback/)

---

### Friendica - under the radar since 2010

- **Speakers:** Tobias Diekershoff, Michael Vogel
- **Room:** UA2.118 (Henriot)
- **Day:** Saturday
- **Time:** 15:30 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5289-friendica-under-the-radar-since-2010/)

#### Abstract

Friendica has been part of the Fediverse since 2010, building bridges between Laconica and Diaspora*, making it one of the oldest active projects of the Fediverse - yet Friendica has flown under the radar most of the time. 
In this talk we will give a short introduction to Friendica, its unique features and how it differs from other systems.
The Friendica project homepage can be found at friendi.ca, the source code for the core is maintained on github and for the addons on git.friendi.ca.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-social-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-social-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/D3SCCZ/feedback/)

---

### Funkwhale presentation : to audio federation

- **Speakers:** petitminion
- **Room:** UA2.118 (Henriot)
- **Day:** Saturday
- **Time:** 16:00 - 16:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6622-funkwhale-presentation-to-audio-federation/)

#### Abstract

A presentation of the Funkwhale project with a focus on interoperability. We want to highlight the role of  the activityPub protocol but also show the interest of musicbrainz, rss, wikipedia to build a web of knowledge.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-social-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-social-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YUKY8J/feedback/)

---

### Elk: A Nimble Client for Mastodon

- **Speakers:** Ayo Ayco
- **Room:** UA2.118 (Henriot)
- **Day:** Saturday
- **Time:** 16:10 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5049-elk-a-nimble-client-for-mastodon/)

#### Abstract

Elk is a nimble Mastodon client with great attention to user experience, boasting features such as being an installable Progressive Web App (PWA), support for code blocks with syntax highlighting, chronological threading, and markdown formatting.
Started by core maintainers behind popular developer tooling in the Vue/Vite/Nuxt ecosystem in 2022, it attracted hundreds of contributors and resulted to the creation of new libraries now widely used in other projects.
In this talk, I will give a brief history of Elk development from the perspective of a contributor who has never written a Vue component (before Elk), a walkthrough of key strengths of the technology under the hood, and a look forward to the future of the project.
Links

Elk Git Repo
Elk mastodon account
My contribution highlights
My Github
Some screenshots

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-social-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-social-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MZ8NZ9/feedback/)

---

### Build your own timeline algorithm

- **Speakers:** Davide Eynard
- **Room:** UA2.118 (Henriot)
- **Day:** Saturday
- **Time:** 16:20 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5601-build-your-own-timeline-algorithm/)

#### Abstract

Timeline algorithms should be useful for people, not for companies. Their quality should not be evaluated in terms of how much more time people spend on a platform, but rather in terms of how well they serve their users’ purposes. Objectives might differ, from delving deeper into a topic to connecting with like-minded communities, solving a problem or just passing time until the bus arrives. How these objectives are reached might differ too, e.g. while respecting instances’ bandwidth, one’s own as well as others’ privacy, algorithm trustworthiness and software licenses.
This talk introduces an approach to personal, local timeline algorithms that people can either run out-of-the-box or customize. The approach relies on a stack which makes use of Mastodon.py to get recent timeline data, llamafile to calculate post embeddings locally, and marimo to provide a UI that runs in one’s own browser. Using this stack, we will show how to perform search, clustering, and recommendation of posts from the fediverse without any of them leaving your computer.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-social-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-social-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SZMXU3/feedback/)

---

### Non-Microblogging Software Design on the Fediverse

- **Speakers:** Casey Kolderup
- **Room:** UA2.118 (Henriot)
- **Day:** Saturday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6375-non-microblogging-software-design-on-the-fediverse/)

#### Abstract

Postmarks is a piece of Fediverse software meant to provide a social bookmarking platform along the lines of De.licio.us and its successors. Despite the published ActivityPub spec having in mind a variety of verbs and nouns, and the ability to create "extensions", most software that I found while looking around in the early days of Postmarks looked to be recreating "timeline-based social media", where the primary activity took place on the platform itself and involved reading content from other users and generating more content of the same expectations. This is not to say there are none, but how much they expect to integrate with platforms like Mastodon varies.
When thinking about what that meant for Postmarks, deciding how interoperability should work presents some interesting questions. There are opportunities in interoperability: even if you're not the kind of person to whom the activity of bookmarking and curating links is interesting, you may know someone who does whose work you want to follow, which you can then do from Mastodon. On the flipside, you may be a researcher who spends time collecting information and values the viewpoints of others but doesn't want to take part in a product designed like a traditional social media site. There are also drawbacks: as an individual maintainer with a handful of contributors to my platform, integrating with existing platforms that are already large enough to have abusers, scrapers, and other bad actors opens me up to those problems much sooner than it would if I were creating my own siloed ecosystem. Less urgently, there are new software design questions raised by the functionality of the platforms interacting. How do I make Postmarks content appear on platforms like Mastodon? As I build out the ability to find bookmarkable content from the Fediverse within Postmarks, how do I do that in a way that keeps in mind the ideals of Postmarks rather than the spaces it's connecting to? What choices have been made that add extra requirements on top of the ActivityPub spec in order to make interoperability smooth and consistent? In designing a piece of ActivityPub software designed to have one small "instance" that hosts the activity of one "actor", I also found myself stumbling across design decisions made in the creation of large platforms like Mastodon and Pixelfed that left me with questions about the ethics of designing software that can interact with those places. How do I prevent my software from becoming a tool for bad actors targeting those places?
By looking at the design problems introduced within the early development of Postmarks and an analysis of other ActivityPub platforms that have either dealt with, are still working on, or have not faced these questions, we can create space for discussing what a future looks like where a broad variety of ActivityPub software is out on the internet speaking the same protocol but choosing when and how they interact in a way that cultivates communication and works to minimize harm.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-social-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-social-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VRYHHN/feedback/)

---

### Fediscovery: Improving Search and Discovery on the Fediverse

- **Speakers:** David Roetzel
- **Room:** UA2.118 (Henriot)
- **Day:** Saturday
- **Time:** 17:00 - 17:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4531-fediscovery-improving-search-and-discovery-on-the-fediverse/)

#### Abstract

Today, each application (and server/instance) that participates in the
Fediverse is largely independent when it comes to discovery. User
search, discovery of content, trends and recommendations are not easily
possible across the network. This is especially problematic for small
servers.
"Fediscovery" is a project led by Mastodon gGmbH and funded by NGI
Search that explores a way to improve this situation with a set of
external services that any fediverse software can use.
The project is meant to produce both specifications that everyone can
implement and a reference server implementation.
This talk will give an overview of the project and its goals. And it
will give an update about the current state of both the specification
efforts and the reference implementation.

#### Related Links

- [Fediscovery project website](https://www.fediscovery.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-social-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-social-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZJMCNK/feedback/)

---

### Today's fediverse: a good start, but there's more to do

- **Speakers:** Christine Lemmer-Webber, Jessica Tallon
- **Room:** UA2.118 (Henriot)
- **Day:** Saturday
- **Time:** 17:30 - 17:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5128-today-s-fediverse-a-good-start-but-there-s-more-to-do/)

#### Abstract

ActivityPub remains, to this day, the most successful decentralized social networking platform to date: dozens of interoperable implementations, thousands of servers, millions of users, all speaking over the same protocol in what's today called the "fediverse" (federated social web).  The modern-day fediverse is an impressive achievement, but it also leaves many issues to be addressed.  Servers can go down, content can disappear and users can lose access to their identity.  Authorization mechanisms are under-specified and rich interactions are fairly limited.  This talk, by the two primary editors of the ActivityPub specification, explores where we think the fediverse should go and how we're building a future for "secure collaboration" technology at the Spritely Institute.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-social-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-social-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YRCLMC/feedback/)

---

### Manyfold: Federating 3d models

- **Speakers:** James Smith
- **Room:** UA2.118 (Henriot)
- **Day:** Saturday
- **Time:** 17:40 - 17:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4181-manyfold-federating-3d-models/)

#### Abstract

Manyfold (https://manyfold.app) is a self-hosted tool for storing, organising and sharing 3d print models. This session will talk about how we've approached adding ActivityPub federation to the system using the "Federails" Rails Engine (https://gitlab.com/experimentslabs/federails), and our approach to using custom extensions to share information across instances and different AP software systems.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-social-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-social-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MLJKHB/feedback/)

---

### Show and Tell: Federation at Forgejo

- **Speakers:** meissa
- **Room:** UA2.118 (Henriot)
- **Day:** Saturday
- **Time:** 17:50 - 18:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5610-show-and-tell-federation-at-forgejo/)

#### Abstract

What is a problem on Twitter et al will become the same mess on GitHub od Gitlab - just a matter of time.
For this reason Forgejo is working on federation for git platforms. Some months ago we released the first user visible feature the federated star and we will continue our path.
We will talk about our motivation, point out the general roadmap and show implementation details.
Other fedi devs and discussions are very welcome.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-social-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-social-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NZM7WZ/feedback/)

---

### Mobilizon: Decentralizing Event Management for a Privacy-Respecting Social Web

- **Speakers:** Stéphane, Alexandra
- **Room:** UA2.118 (Henriot)
- **Day:** Saturday
- **Time:** 18:00 - 18:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4381-mobilizon-decentralizing-event-management-for-a-privacy-respecting-social-web/)

#### Abstract

Mobilizon is a decentralized, privacy-focused platform for event management and group organization. In this talk, we will explore how Mobilizon empowers users to create and manage events without sacrificing their privacy or control over their data. We will discuss the importance of decentralization, provide a technical overview of the platform, and share insights into its growing community and future roadmap.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-social-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-social-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JNHMSM/feedback/)

---

### Networked Journalism: Bringing long-form publishing to the Fediverse

- **Speakers:** John O'Nolan
- **Room:** UA2.118 (Henriot)
- **Day:** Saturday
- **Time:** 18:30 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4673-networked-journalism-bringing-long-form-publishing-to-the-fediverse/)

#### Abstract

In an era dominated by centralized platforms and algorithm-driven content, the open web's foundational principles of diversity and user autonomy have been overshadowed. John O'Nolan, founder and CEO of Ghost.org, will explore how Ghost is integrating ActivityPub to reconnect with the open web's ethos. This session will delve into the motivations behind adopting ActivityPub, the technical journey of embedding it into Ghost, and the anticipated impact on publishers and readers. Attendees will gain insights into the challenges and triumphs of this integration and understand Ghost sees the evolution of independent media and networked publishing.
Key Takeaways:

Understanding the significance of ActivityPub in journalism and publishing
Insights into Ghost's strategic and technical approach in integrating ActivityPub.
The anticipated benefits for publishers and readers within the Fediverse.
A vision for the future of open, interconnected web platforms.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-social-web:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-social-web:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7MG77F/feedback/)

---

## Software Bill of Materials (SBOM) (19)

### Welcome to the SBOM devroom

- **Speakers:** Alexios Zavras (zvr), Adolfo García Veytia, Kate Stewart
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 09:00 - 09:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6689-welcome-to-the-sbom-devroom/)

#### Abstract

Introduction to the topics and the structure of the devroom.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KLMTKU/feedback/)

---

### SBOMs and cryptographic algorithms: status and next steps

- **Speakers:** Agustin Benito Bethencourt, Matias Daloia
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 09:10 - 09:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5870-sboms-and-cryptographic-algorithms-status-and-next-steps/)

#### Abstract

During 2024 two relevant steps have been taken that will enable the inclusion of cryptographic algorithms in SBOM in the near future. On one side, SCANOSS has published as open data (CC0) the cryptographic algorithms detected across the internet, included in the product knowledge, together with a very simple mechanism to detect them in any software composition. In addition, SPDX has taken the decision to create a cryptographic algorithms list following the work done on the SPDX License List.   
The talk will provide an overview of why including crypto algorithms in SBOMs is relevant in a variety of use cases for different industries. It will describe the work done by SCANOSS during 2024 in this field, including how the open data set published with crypto algorithms information is evolving, now the SPDX Crypto Algorithms List is defined as upstream, as well as recent improvements in the detection mechanisms. Measures to promote contributions to it will be announced during the talk.  
The speaker will then ask the audience about how to improve the data set, so it becomes useful to an increasing number of use cases, so more organizations and upstream projects include cryptographic algorithms in SBOMs. The talk will end by providing the opportunity to the audience to point to other developments that should be considered in this field, and how and where we can create the corresponding forum to coordinate further actions during 2025.
Crypto_algorithms_open_dataset: https://github.com/scanoss/crypto_algorithms_open_dataset

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/URTV3K/feedback/)

---

### Intro to the SPDXFunctional Safety Model

- **Speakers:** Nicole Pappler
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 09:30 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6266-intro-to-the-spdxfunctional-safety-model/)

#### Abstract

While SPDX provides with its relationships already a good starting base to model the internal dependencies, setting all actions and work products that are part of a functional safety release of a project sparked some discussions in the Functional Safety community. This talk lines out the main discussion points with the different viewpoints discussed in the SPDX FuSa group, along with matching prototype models.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QFRFN3/feedback/)

---

### A retrospective on Google’s SBOM implementation

- **Speakers:** Brandon Lum, Marco Deicas
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 10:00 - 10:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6074-a-retrospective-on-google-s-sbom-implementation/)

#### Abstract

This talk takes a look back on how we designed our Google-wide SBOM solution, exploring the technical challenges and trade-offs Google encountered while implementing SBOMs at scale, and how those decisions have aged almost 2 years out! We delve into the intricacies of generating and managing 100Ms SBOMs (~4M SBOMs/wk), ranging from design decisions in SBOM generation, trade-offs between build and analysis SBOMs, to hurdles with finding SBOMs and associating them with products.. We will talk about how we are using SBOMs outside EO14028 compliance, and the challenges around SBOM data quality, accuracy and completeness we face (software identifiers, analysis mishaps, etc.).

#### Related Links

- [SPDX Spec](https://github.com/spdx/spdx-spec)
- [Anchore Syft SBOM Generator](https://github.com/anchore/syft)
- [SCALIBr SBOM generator](https://github.com/google/osv-scalibr)
- [Graph for Understanding Artifact Composition (GUAC)](https://github.com/guacsec/guac)
- [PURL Spec](https://github.com/package-url/purl-spec/)
- [SPDX Golang Tools](https://github.com/spdx/tools-golang)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SWR3SE/feedback/)

---

### SBOM journey for an Open Source Project - Apache NuttX RTOS

- **Speakers:** Alin Jerpelea
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4528-sbom-journey-for-an-open-source-project-apache-nuttx-rtos/)

#### Abstract

This talk will take you through the journey of SBOM implementation on the Apache NuttX RTOS from the legal background, to the current status, providing the steps that we followed and the lessons learned.
We will share the experience acquired over the past 2 years, starting from License compliance, SPDX implementation, and the current SBOM status.
You can find more information about Apache NuttX RTOS on project's website https://nuttx.apache.org/.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8TEJDQ/feedback/)

---

### Lessons learned from integrating SBOM in a supply chain

- **Speakers:** Sébastien DOUHERET
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 11:00 - 11:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5784-lessons-learned-from-integrating-sbom-in-a-supply-chain/)

#### Abstract

In the context of a Linux software factory dedicated to building embedded software, we will discuss the choices and challenges we encountered in integrating SBOM file generation into a software supply chain involving many packages.
The talk will begin with a brief overview of the various formats (SPDX, CycloneDX, ...), tools and ecosystems surrounding SBOM, highlighting the essential knowledge required to integrate these features into a supply chain.
Then, this presentation will address the challenges we faced in retrieving accurate and reliable information to generate various BOMs: 
How do we ensure the data is correct and up-to-date?
What are the common pitfalls in data collection?
Which format best suits your needs, and what are the trade-offs between different solutions?
Finally, we will explore the importance of having SBOMs and the necessity of tracing and signing each element in the supply chain to ensure integrity (focusing here on SLSA).
More information about redpesk factory and redpesk OS:
- redpesk documentation - Technical documentation of redpesk factory and redpesk OS
- redpesk community edition - A free to use version of redpesk SaaS factory
- redpesk OS - Security Framework and components sources on github

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NDNL3D/feedback/)

---

### A Novel Ontology for Enhanced SBOM Data Modeling with TOSCA

- **Speakers:** Alexios Zavras (zvr)
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 11:20 - 11:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5280-a-novel-ontology-for-enhanced-sbom-data-modeling-with-tosca/)

#### Abstract

As everyone involved with SBOMs knows, the accurate and efficient recording of data about software components is crucial for security, compliance, and operational efficiency. This presentation introduces a novel data modeling approach that leverages an ontology in RDF terms, similar to the approach used by SPDX. This new model distinguishes between abstract software components and specific software packages, providing a more granular and efficient way to manage software metadata.
Traditionally, SBOMs have focused on recording information about software packages, such as "OpenSSL v3.0.1 distributed by Ubuntu" or "OpenSSL v3.1.1 distributed by Debian." However, this approach can lead to redundancy and inefficiencies, particularly when dealing with licensing information and other metadata that is common across multiple versions and distributions of the same software. Our novel ontology introduces the concept of a "component" as an abstract reference to a piece of software, distinct from a "package," which represents a specific version of the software distributed by a particular supplier.
By implementing this distinction, our ontology allows for the creation of relationships between different parts of the software ecosystem. For example, both "OpenSSL v3.0.1 distributed by Ubuntu" and "OpenSSL v3.1.1 distributed by Debian" can be linked to the abstract component "OpenSSL." This relationship-based approach not only enhances the clarity and organization of SBOM data but also leads to significant storage savings. Common information, such as the licensing terms of a component, can be stored once and referenced across multiple packages, eliminating redundancy.
The practical application of this ontology can be demonstrated by a new tool called TOSCA (The Open Source Component Aggregator) that we have developed. TOSCA demonstrates the power and efficiency of this data model by aggregating and managing millions of data points about open-source components. While the presentation will primarily focus on the ontology and its benefits, TOSCA will be mentioned as a proof of concept that highlights the real-world applicability and advantages of this approach.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TXV8MZ/feedback/)

---

### Discover Dependency License Information Using SBOMs and ClearlyDefined

- **Speakers:** Jeff Mendoza
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 11:40 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5839-discover-dependency-license-information-using-sboms-and-clearlydefined/)

#### Abstract

SBOM specifications provide comprehensive capabilities for expressing license and legal information. However, SBOM generators often leave information missing or incomplete. Compounding this, package authors sometimes fail to clearly describe the license of their package or omit license information for included and vendored files.
ClearlyDefined is a community-curated repository of discovered license information for software packages. Its data is generated by deep scanning tools, such as ScanCode, which uncover legal information that may not be explicitly declared.
This session explores new SBOM tooling, built using Protobom, that queries licenses, produces NOTICE files, augments and outputs new SBOMs, all using high-fidelity legal information from ClearlyDefined.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KXEEKY/feedback/)

---

### Persistent Copyright & Licensing Information in Client-side JS, CSS &sim. (proposal)

- **Speakers:** Matija Šuklje
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 12:00 - 12:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5313-persistent-copyright-licensing-information-in-client-side-js-css-sim-proposal-/)

#### Abstract

License information in source code is best stored in each file of the source code as a comment, if at all possible. That way the license metadata travels with the file even if it was copied from its original package/repository into a different one.
Client-side JavaScript, CSS and similar languages that make up a large chunk of the web are often concatenated, minified and even uglified in an attempt to make the website faster to load. In this process, most often, the comments get culled the first to reduce the number of characters that serve no function to the program code itself.
The problem therefore is that typically when JavaScript, CSS (or similar client-side code) is being built, it tends to lose not just comments that describe the code’s functionality, but also comments that carry licensing and copyright information. And since licenses (FOSS or not) typically require the text of the license and copyright notices to be kept with the code, such removal can be problematic.
A few months ago I proposed a way to preserve SPDX tags even in minified code. This proposal relies solely on commonly used tooling and existing wide-spread standards/specs (SPDX and REUSE), but applies the SPDX-Snippet-* tags in an inventive way to achieve this.
In this talk I will briefly present that proposal, followed by the feedback I received up until FOSDEM, and – most importantly – a hopefully lively discussion to come up with a much better proposal.
The ultimate goal is to finally figure out how to make the client-side web JS/CSS easy to reuse and ship in a license-compliant way. Ideally with relying on commonly used tools and specs, unchanged.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GAADGY/feedback/)

---

### The Breadth and Depth of SBOMs

- **Speakers:** Michael Lieberman
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 12:20 - 12:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6164-the-breadth-and-depth-of-sboms/)

#### Abstract

One SBOM is good, more SBOMs are better. Tracking a single piece of software's SBOMs across versions and time can reveal a lot of interesting information and through analysis can be used to understand how your risks change over time. Be able to answer questions like When did you fix that vulnerability? What is the progress of moving off of BSL licensed software?
Similarly by keeping multiple SBOMs for different software, e.g. as part of a large environment or organization you can understand shared risks. Does a vulnerability impact one piece of software or multiple? Are you using the same logging library across your Go applications or are you using multiple different ones?
We will look at how a lot of open source tools from the simple like jq to the more complicated like DuckDB and GUAC can be used to track and analyze SBOMs over time and across environments to answer the questions you have about your software.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WQPZPC/feedback/)

---

### Struggles with making SBOMs for C apps

- **Speakers:** Chris Swan
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 12:40 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4846-struggles-with-making-sboms-for-c-apps/)

#### Abstract

Making SBOMs for modern languages is easy - point a tool at the lock file, crank the handle, almost done (apart from all that pesky NTIA stuff). But C presents challenges as there's no widely used package manager to serve up log files, and many tools over promise and under delivery. This talk will run through various attempts to create SBOMs for a C project, and why the tools proved inadequate. It will also take a brief look at projects like Yocto where getting SBOMs for C stuff is working.

#### Related Links

- [sbomify guest post "The C conundrum - generating SBOMs when there's no lockfile"](https://sbomify.com/2024/11/18/c-conundrum/)
- [NoPorts repo where SBOMs are generated for Dart and Python, but not yet C](https://github.com/atsign-foundation/noports)
- [Yocto project - Creating a Software Bill of Materials](https://docs.yoctoproject.org/dev/dev-manual/sbom.html)
- [Trivy - the scanner that's used in sbomify to generate SBOMs from lock files](https://trivy.dev/v0.17.2/)
- [Syft - A CLI tool and Go library for generating a Software Bill of Materials (SBOM) from container images and filesystems](https://github.com/anchore/syft)
- [Conan, software package manager for C and C++ developers](https://conan.io/)
- [sbomify GitHub Action](https://github.com/sbomify/github-action/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZY7CU7/feedback/)

---

### TEA - Let the SBOM ride down the software supply chain!

- **Speakers:** Olle E. Johansson
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 13:00 - 13:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5858-tea-let-the-sbom-ride-down-the-software-supply-chain-/)

#### Abstract

The SBOM file is a carrier of software transparency data. It is meant to be shared across the borders of a software supply chain, together with other artefacts like VEX files, SCITT statements, IN-TOTO attestations and much more. The OWASP Transparency Exchange API is going to be a standard for this exchange with a focus on discovery and retrieval of these objects and as a second step, a way to reach and query actual data within objects. In this talk, you will get an overview of the TEA platform, a status update of how far the project has come towards writing enough specifications and starting to test implementations.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/R3MAUZ/feedback/)

---

### BASIL an open source tool that supports requirements traceability with design SBOM

- **Speakers:** Luigi Pellecchia
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 13:30 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4798-basil-an-open-source-tool-that-supports-requirements-traceability-with-design-sbom/)

#### Abstract

BASIL is an open source software quality management tool that has been developed to simplify the definition and maintenance of traceability matrix in Safety Critical applications. Even if BASIL provides several features as the management of quality related work items and a test execution framework, usually in critical applications we have to deal with complex toolchains.
Due to that it is mandatory to have a way to share data between tools in a consistent way.
Join us in a session where we will see how BASIL is supporting SPDX to share quality related work items as a SBOM.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WMGM78/feedback/)

---

### Where in the OSS Supply Chain do SBOM attributes come from?

- **Speakers:** Salve J. Nilsen
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 14:00 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6483-where-in-the-oss-supply-chain-do-sbom-attributes-come-from-/)

#### Abstract

2025 may become "the year of SBOM" in the EU. Businesses and other institutions are taking the first steps to explore the new demands of the Cyber Resilience act and the NIS2 directive – and soon they'll start asking some important questions:

What are the sources of the required metadata?
How do we ensure they are authoritative, up-to-date and correct?
What can we do to help these sources help us?

Sadly, the answer isn't that simple – legislative demands for SBOM attributes are coming from many places, and the software ecosystems need to take all these demands into account. Is this a train-wreck in the making?
In this talk, Salve J. Nilsen will share some of his findings on this matter – The attributes, the volunteers and the regulations. After this talk we'll have an idea of what this landscape looks like, and how to improve it!

#### Related Links

- [CPAN Security Group](https://security.metacpan.org/)
- [Roles and metadata in open source supply chains (Github)](https://github.com/CPAN-Security/security.metacpan.org/blob/master/docs/supplychain-sbom.md)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DHCKDX/feedback/)

---

### Implementing a triage process supporting all flavours of VEX

- **Speakers:** Anthony Harrison
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 14:30 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5270-implementing-a-triage-process-supporting-all-flavours-of-vex/)

#### Abstract

As part of the Google Summer of Code 2024, Cve-Bin-tool (see https://github.com/intel/cve-bin-tool) upgraded it's triage process to support the various flavours of VEX
The triage process allows users of the tool to customise the reports they get by adding extra data on the vulnerabilities found, particularly any mitigations. This is often used for discarding false positives, or cases where the reported vulnerability is not exploitable based on a risk assessment of the context where the software is used..
Although Cve-Bin-Tool has supported a basic triage process for several years, the GSOC project was able to introduce support for the 4 flavours of VEX documents (CSAF, CycloneDX, OpenVEX and SPDX) by use of the lib4vex library which allows for the parsing and generation of VEX documents in the different formats.
This talk will describe the journey and some of the challenges which were encountered in producing the VEX support.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FYJZ7V/feedback/)

---

### Airflow Beach Cleaning - Securing Supply Chain

- **Speakers:** Jarek Potiuk, Munawar Hafiz, Michael Winser
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 15:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4594-airflow-beach-cleaning-securing-supply-chain/)

#### Abstract

For years, we've been focusing on producing the SBOMS, but how about using them. Let's talk about one of the first real, high-scale applications usage of SBOMS in the Open Source Space. Airflow Beach Cleaning - Securing Supply Chain    Airflow’s power comes from its vast ecosystem, but securing this intricate web requires a united front. This talk unveils a groundbreaking collaborative effort between the Python Software Foundation (PSF), the Apache Software Foundation (ASF), the Airflow Project Management Committee (PMC), and Alpha-Omega Fund - aimed at securing not only Airflow, but the whole ecosystem. We’ll explore this new project dedicated to improving security across the Airflow landscape.

#### Related Links

- [Apache Airflow](https://github.com/apache/airflow)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7KDQXW/feedback/)

---

### Connecting SBOMs with OSS Project Health to Better Understand Dependencies

- **Speakers:** Georg Link
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 15:30 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5715-connecting-sboms-with-oss-project-health-to-better-understand-dependencies/)

#### Abstract

While it is encouraging to see organizations continue integrating OSS into their technologies, it’s critical to fully understand the impact of this accelerated adoption on their software supply chains and to ensure that the health of the community behind open source projects is not being overlooked. 
This talk explores how going beyond traditional SBOM analysis with the open source project health metrics from the CHAOSS GrimoireLab tool offers a deeper, more comprehensive understanding of dependency risks. It provides valuable insights into the sustainability, risks, and long-term viability of the open source projects that organizations rely on. 
This approach enables organizations to:

Assess the long-term viability of their open source dependencies
Make informed decisions about library selection and integration
Proactively mitigate risks associated with unhealthy or unsustainable communities

Join us to discuss the importance of OSS project health in SBOMS and to learn actionable strategies to understand your dependencies better, manage them with data, and reduce the risk associated with your open source projects.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TVV8F9/feedback/)

---

### Towards Quality SBOMs: the OpenChain Telco SBOM Guide

- **Speakers:** Marc-Etienne Vargenau
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 16:00 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4792-towards-quality-sboms-the-openchain-telco-sbom-guide/)

#### Abstract

OpenChain is the international standard for open source license compliance programs ; it has been created by a joined effort of the community. The OpenChain project has several work groups. The Telco work group was formed to create a recommendation for an SBOM format to be exchanged between telecommunication companies, their suppliers and customers.
The result is the "OpenChain Telco SBOM Guide" that describes what a quality SBOM should contain and how and when it should be distributed. It includes industry standard requirements like "NTIA SBOM Minimum elements" and PURL. Although developed by telcos, it is generic and can be used by other industries.
Translations of the guide are available in French, Japanese and Chinese to facilitate its adoption worldwide.
The OpenChain Telco SBOM Guide is used by Nokia as a basis for its SBOM format. Nokia provided an open source tool to validate SBOMs against the guide. The talk will discuss lessons learned from implementing the Guide at Nokia.
The OpenChain Telco SBOM Guide is available at https://github.com/OpenChain-Project/Telco-WG/blob/main/OpenChain-Telco-SBOM-Guide_EN.md
The validator is available at https://pypi.org/project/openchain-telco-sbom-validator/ 
The source code is available at https://github.com/OpenChain-Project/Telco-WG/tree/main/tools/openchain_telco_sbom_validator under Apache-2.0 license.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/X3LPL8/feedback/)

---

### Open Discussion

- **Speakers:** Alexios Zavras (zvr), Adolfo García Veytia, Kate Stewart
- **Room:** H.2213
- **Day:** Sunday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6690-open-discussion/)

#### Abstract

An open-for-all session to ask any questions and discuss any topic about SBOMs.
If you have topis for discussion before the start of the session, please reach out to the moderators during the day.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-sbom:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-sbom:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SMM9AQ/feedback/)

---

## Software Defined Storage (14)

### Declarative Object Storage at Scale: Integrating Rook, Ceph, and OpenStack

- **Speakers:** Sirisha Guduru, Joachim Kraftmayer, Artem Torubarov
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4862-declarative-object-storage-at-scale-integrating-rook-ceph-and-openstack/)

#### Abstract

This talk outlines our journey in building a reproducible Ceph object storage setup that can be deployed across multiple regions with a single click, using an Configuration-as-Code approach with Rook. Our primary goal was to replace OpenStack Swift with Ceph RGW to achieve strictly consistent object storage while maintaining backward compatibility with existing OpenStack components such as Keystone and Barbican.
The good news? Many of these capabilities already existed in Ceph, albeit in varying states of readiness. However, not all of them were natively configurable in a declarative manner using Rook. This presentation will dive into the challenges we encountered while integrating Ceph, OpenStack, and Rook. We'll explore the gaps we identified, the features we developed or refined, and the current state of the ecosystem for those considering a similar path today.
Attendees will gain practical insights into building resilient object storage solutions and learn how to navigate the complexities of integrating Ceph into modern cloud-native and OpenStack environments.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FUJ3AC/feedback/)

---

### Intelligent Tiering for RGW

- **Speakers:** Shreyansh Sancheti, Jiffin Tony Thottan
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 11:05 - 11:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4090-intelligent-tiering-for-rgw/)

#### Abstract

Ceph can currently provide Tiering(Storage Classes) using different pools in the Ceph on-prem cluster and can also do cloud transitions(AWS, s3 compatible endpoints). The movement of data through different storage classes can be achieved using S3 lifecycle rules based on the age of the files. Intelligent tiering for RGW (Rados Gateway) is a feature in Ceph storage that automatically moves data between storage tiers based on policies. This feature optimises storage costs and performance by moving frequently accessed data to faster storage tiers and less frequently accessed data to lower-cost, higher-capacity tiers. The intelligent tiering policy is customizable, allowing users to define criteria for data migration, such as access frequency, time, and size. This feature is particularly useful for large-scale object storage deployments, where optimizing storage costs and performance is crucial. The first step is to extend the existing cloud transition to include features like read-through, restore API(like glacier in s3 protocol)

#### Related Links

- [Ceph repository](https://github.com/ceph/ceph)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HHUZ7B/feedback/)

---

### Making NooBaa Resilient by Eliminating Single Points of Failure

- **Speakers:** Shriya Mulay, Vaishnavi Deshpande
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 11:40 - 12:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5881-making-noobaa-resilient-by-eliminating-single-points-of-failure/)

#### Abstract

NooBaa is a software-defined storage platform that enables seamless management of object storage across diverse environments. In NooBaa, the database plays a vital role, it stores information related to the object buckets, object indexing, configuration data etc,  — but what happens if that database fails or becomes slow? It can bring your entire storage system to a halt, impacting availability and performance.
In this session, we'll discuss the current noobaa architecture, the challenges of NooBaa’s database dependency , along with some real-world examples of outages caused by this. We’ll explore how to safeguard your storage environment and ensure consistent access to your object buckets, even during database failures using different database handling strategies.
links:  https://github.com/noobaa

#### Related Links

- [noobaa project link](https://github.com/noobaa)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/W38EXM/feedback/)

---

### Understanding Ceph: A Journey from Metrics to Tracing

- **Speakers:** Marcel Lauhoff
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 12:15 - 12:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6460-understanding-ceph-a-journey-from-metrics-to-tracing/)

#### Abstract

While metrics provide valuable insights into system behavior, they often lack the detail to really understand the system. In this talk, we will explore how tracing techniques can complement metrics to provide a more detailed view of Ceph operations, enabling deeper analysis and troubleshooting.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/77DXYP/feedback/)

---

### Scaling Ceph-SMB connections

- **Speakers:** Sachin Prabhu
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 12:50 - 13:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5603-scaling-ceph-smb-connections/)

#### Abstract

The SMB service in Ceph uses a Samba container to export the Cephfs volume using the vfs_ceph_new plugin. We hit a problem when scaling the number of client connection which results in resource exhaustion on the server host. This was determined to be caused by Samba's forking model and the way data is cached by libcephfs. This presentation delves deeper into the cause of this problem and the proposed solution - the multiplexing proxy.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SNQNYG/feedback/)

---

### SMB3.11 Unix Extensions current status

- **Speakers:** Volker Lendecke
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 13:25 - 13:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5679-smb3-11-unix-extensions-current-status/)

#### Abstract

There have been a lot of talks in the past years about how to present Linux/Posix semantics over the SMB3.11 protocol to provide an alternative to the NFS protocol for installations that already have existing SMB infrastructure and who could benefit from better semantics when sharing files to Linux and other Posix-based file server clients.
In the past few months there has been a great deal of progress in Samba towards the goal of better supporting Linux clients. Notable changes are improvements to present special files like sockets and FIFO files to clients. There has been improvements to better support operations like chmod and chown in the Linux client and the Samba server.
The biggest change on the Samba side has been an overhaul of handling native symlinks. Samba 4.22 will present symlinks for Posix clients in the same way Windows presents symlinks it finds on its local NTFS file system.
This talk will present the current status of the ongoing work to improve Linux file system semantics presented over the SMB protocol.

#### Related Links

- [Samba project website](https://www.samba.org/)
- [SMB3 Unix Extensions protocol specification](https://gitlab.com/samba-team/smb3-posix-spec)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/S9EBLH/feedback/)

---

### Security in Ceph and Rook, recent improvements

- **Speakers:** Federico Lucifredi, Sage  McTaggart
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 14:05 - 14:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5929-security-in-ceph-and-rook-recent-improvements/)

#### Abstract

We explore the security model exposed by Rook with Ceph, the leading software-defined storage platform of the Open Source world. We discuss major updates within the past year to our threat model, dashboard, call home, and encryption, including work on TCMs, NVMe and exploration of open source post quantum encryption algorithms, within a major project. We discuss the challenges and benefits of promoting open source, and how to ensure we adhere to Executive Order 14028, and the challenges and rewards of dependency tracking and updating.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8XBTUB/feedback/)

---

### Optimizing Longhorn for high performance hardware

- **Speakers:** Konstantinos Kampdais
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 14:40 - 15:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5709-optimizing-longhorn-for-high-performance-hardware/)

#### Abstract

Longhorn is an open-source, Cloud-native volume manager, which implements its own distributed block storage system. It is a complete and independent software defined storage solution, handling internally all aspects related to capacity management, performance, fault-tolerance, as well as interfacing with both Kubernetes and the end user. Longhorn is an actively-developed and mature software, however our installations have revealed that it currently lacks the ability to take advantage of the hardware performance available in local servers that feature high-speed solid state disks and high-bandwidth network connectivity. This presentation investigates a series of performance optimizations that have been engineered in the Longhorn's core that collectively allow the system to achieve an order of magnitude better IOPS and bandwidth.

#### Related Links

- [Longhorn Engine optimizations](https://github.com/CARV-ICS-FORTH/longhorn-engine/tree/ublk-dev)
- [DBS storage](https://github.com/Kampadais/dbs)
- [Ublk framework](https://github.com/Kampadais/ubdsrv)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3VZJE8/feedback/)

---

### From Particle Collisions to Physics Results: EOS Open Storage at CERN

- **Speakers:** Abhishek Lekshmanan, Guilherme Amadio
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 15:20 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5789-from-particle-collisions-to-physics-results-eos-open-storage-at-cern/)

#### Abstract

In this talk, we'll explore the lifecycle of data at CERN, 
the European Organization for Nuclear Physics, starting 
at particle collisions ultimately leading to physics research.
The bulk of the data from the physics programme at CERN is 
stored in an open source storage system developed at CERN, 
EOS - EOS Open Storage.
We'll delve into technical & architectural details on EOS 
and cover how it solves the problem of large scale storage
for scientific data and analysis use cases. EOS supports 
FUSE, HTTP & GRPC as access protocols. EOS is used also 
outside of physics use cases, for eg. powering CERNBOX, 
a cloud storage for CERN users, at JRC, for analytics etc
and may power your next large scale storage needs!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VHXWYJ/feedback/)

---

### CERN CTA Service: writing LHC data to tape with opensource software on commodity hardware

- **Speakers:** Julien Leduc
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 15:55 - 16:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5737-cern-cta-service-writing-lhc-data-to-tape-with-opensource-software-on-commodity-hardware/)

#### Abstract

CERN (European Organization for Nuclear Research) is one of the world's largest and most respected centres for scientific research. It is home to the world's largest particle accelerator (Large Hadron Collider, LHC) and is the birthplace of the Web.
CERN's Storage and Data Management Group is responsible for enabling data storage and access for the CERN laboratory, in particular the long-term archival, preservation and distribution of LHC data to a worldwide scientific community (WLCG).
The CERN Tape Archive (CTA) Service manages more than 900 PBs of data distributes over about 50,000 high-capacity tapes in 6 tape libraries. The service ingests this exponentially growing amount of data at LHC data acquisition rates though its EOS based flash buffer and feeds up to 180 tape drives that write date on mounted tapes at over 90% write efficiency.
This high efficiency archival service runs on open-source software and is deployed on-premise on commodity hardware.
In this talk I would like to give you a high level view of the global CERN tape service performances and dive in the details of its real life deployment: from the flash buffer design principles to the tape servers connected to multiple tape drives via a dedicated network topology.
All of the presented software are open source and available for use and are deployed in other laboratories around the world.

#### Related Links

- [CERN Tape Archive open source software](https://cta.web.cern.ch/)
- [EOS open source software](https://eos.web.cern.ch/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FSYWHY/feedback/)

---

### Advancing Large Scale Scientific Collaborations with Rucio

- **Speakers:** Hugo Gonzalez Labrador, Martin Barisits
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6558-advancing-large-scale-scientific-collaborations-with-rucio/)

#### Abstract

Managing the data deluge (exabytes) generated by worldwide large-scale scientific collaborations is a challenge. 
The Rucio Data Management platform is an open-source framework written in Python engineered to orchestrate the storage, distribution, and management of massive data volumes across a globally distributed and heterogeneous storage infrastructure.
Rucio meets the requirements of high-energy physics, astrophysics, genomics, and beyond, pioneering new ways to facilitate research at the exabyte-scale and is used by major scientific experiments:
the ATLAS and CMS experiments at CERN, Square Kilometer Array Observatory, Cherenkov Telescope Array, KM3NET and Belle II to name a few.
This presentation introduces the Rucio project and the technology behind it.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DPQER8/feedback/)

---

### CephFS: from synthetic benchmarks to real-world user workloads

- **Speakers:** Mattia Belluco
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 17:10 - 17:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6570-cephfs-from-synthetic-benchmarks-to-real-world-user-workloads/)

#### Abstract

Since CephFS was declared stable, it has become a viable option for workloads ranging from High Performance Computing to Kubernetes. In this talk we discuss the configuration tuning we applied to transition from a freshly deployed filesystem to one suitable for a production usecase that mixes decent performance, reliability and capacity.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MFCXXY/feedback/)

---

### Case Insensitive Trees in CephFS

- **Speakers:** Patrick Donnelly, Günther Deschner
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 17:45 - 18:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6598-case-insensitive-trees-in-cephfs/)

#### Abstract

Like most POSIX file systems, CephFS has always been a case-sensitive file
system. However, it has become a priority to improve integration with gateways
like Samba which present a case-insensitive view of some tree in the file
system. In order to present that view, Samba requires expensive checks for file
name lookups to locate a directory entry with the computed case-insensitive
folding. It is also necessary to politely handle interoperating with other 
clients that are using normal case-sensitive names. To address this gap, CephFS
now provides a mechanism for enforcing case-insensitive operations on a
directory tree for all clients by simply setting a Ceph extended attribute.
This talk will walk through the challenges for Samba's gateway on CephFS, the
changes to the CephFS metadata server and clients, the interfaces used by other
well-known file systems, and the expectations users may have going forward.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/88SWW8/feedback/)

---

### Operating OpenStack Swift in real life

- **Speakers:** Seongsoo Cho
- **Room:** K.3.401
- **Day:** Saturday
- **Time:** 18:20 - 18:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6167-operating-openstack-swift-in-real-life/)

#### Abstract

OpenStack Swift is the object storage component of OpenStack, unique in its ability to be deployed independently for object storage services.
In this session, I will share valuable insights and experiences gained from operating OpenStack Swift as a public cloud service over the past eight years. Compared to other projects like Ceph, OpenStack Swift has fewer documented use cases. This presentation aims to provide practical knowledge for those looking to build and manage object storage solutions using Swift.
The discussion will cover:
    •   Key components of OpenStack Swift
    •   Architecture design for public cloud services
    •   Operational scenarios for scaling nodes and handling failures
    •   Monitoring strategies for effective operating
Project Repo : https://github.com/openstack/swift

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-storage:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-storage:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WMAHPM/feedback/)

---

## Swift (13)

### Welcome to the Swift ecosystem!

- **Speakers:** Paris Pittman
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 15:00 - 15:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6421-welcome-to-the-swift-ecosystem-/)

#### Abstract

Swift isn’t just for Apple platforms; there is something for all in this great open source general purpose programming language. 
In this community welcome message, Paris Pittman, a member of the Swift Core Team, will provide an ecosystem overview. We’ll touch on milestones that we’ve achieved together and some of the up and coming work on our plates. And the best part - you can join us in the journey! Paris will detail out how you can plug in, no matter your platform of choice.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XMD3P3/feedback/)

---

### Why Swift is the Next Big Thing for IoT

- **Speakers:** Lilly Seay
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 15:10 - 15:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6148-why-swift-is-the-next-big-thing-for-iot/)

#### Abstract

Internet of Things (IoT) connects everyday devices, from sensors to smart home gadgets, with apps that control and monitor them. Building these systems requires programming languages that can work seamlessly across both embedded devices and applications. Swift has been great with C and C++ interoperability, but the introduction of Embedded Swift has brought this to a new level.
With Swift, we can now program embedded systems with low-power sensors and small memory footprints, while also taking advantage of Swift’s simplicity and safety to create interfaces that integrate seamlessly with high-level UI code.
This talk explores why Swift is the next big thing for IoT, demonstrating how it bridges the gap between embedded systems and user-interfacing Swift apps. You’ll learn why Swift’s expressive syntax, interoperability, and cross-platform capabilities simplify development for IoT.

#### Related Links

- [Open source link for Swift](https://www.swift.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/S9WM7J/feedback/)

---

### Blink them to death using Embedded Swift

- **Speakers:** Eric Bariaux
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 15:25 - 15:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4163-blink-them-to-death-using-embedded-swift/)

#### Abstract

Using the recently announced Embedded Swift Swift.org - Get Started with Embedded Swift on ARM and RISC-V Microcontrollers we'll program an nRF52840 micro-controller.
We’ll start by introducing the world of embedded devices and their specific characteristics. The talk will explain what Embedded Swift is and how it allows us to program these devices using the Swift language. We’ll also cover some of the current limitations of using Swift in this context, particularly when compared to developing on Apple platforms.
Starting from the "blinky" example published by Apple—a simple program that makes an LED blink, widely considered the “Hello World” of embedded programming, we'll progressively modify the code, making it more closely resemble idiomatic Swift code, so that any Swift developer can feel at home.
In the final part of the presentation, we'll explore more advanced projects implemented using Embedded Swift, talk about the other domains where these concepts can be applied and the future of this budding initiative.
Although having a foundational understanding of Swift helps, attendees without prior experience with Swift should still be able to follow along quite easily. No prior embedded systems experience is required.

#### Related Links

- [The Swift Programming Language](https://github.com/swiftlang/swift)
- [Example code of using Embedded Swift on nRF52](https://github.com/nelcea/EmbeddedSwift-nRF52-Examples)
- [Slides from my previous talks on Embedded Swift](https://github.com/ebariaux/slides)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TT7SXD/feedback/)

---

### Building a Ferrofluidic Music Visualizer with Embedded Swift

- **Speakers:** Rauhul Varma
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 15:40 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5284-building-a-ferrofluidic-music-visualizer-with-embedded-swift/)

#### Abstract

Discover the possibilities of Embedded Swift in action with a unique open-source project: a ferrofluidic music visualizer and Bluetooth speaker. This lightning talk will introduce Embedded Swift, explain how it integrates seamlessly with C code, and address common challenges faced when building firmware for embedded systems.
The talk will feature a high-level walkthrough of the firmware, including an overview of the DSP logic for generating I2S output to control the device’s electromagnets. The project—fully open-source and hosted in the swift-embedded-examplesGitHub repository—showcases the use of the Raspberry Pi Pico W SDK alongside Swift to create a functional, innovative product.
To wrap up, the firmware will be deployed live, culminating in a demo where the device visualizes music with ferrofluid. Perfect for developers curious about leveraging Swift for embedded systems, this session offers a fast-paced glimpse into the creative potential of Embedded Swift.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JDGFPK/feedback/)

---

### age-plugin-se: Building a lean cross-platform cryptography tool

- **Speakers:** Remko Tronçon
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 15:55 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4159-age-plugin-se-building-a-lean-cross-platform-cryptography-tool/)

#### Abstract

age-plugin-se allows you to protect arbitrary files with your Apple Secure Enclave.
This plugin for age (a simple, modern and secure file encryption tool) is written entirely in Swift, and works on macOS, Linux, and Windows. 
In this talk, I will show age-plugin-se in action, and touch on the steps taken to make it robust, simple, and distributable on multiple platforms (including Alpine Linux), all while keeping the dependencies (including tools) to a minimum.

#### Related Links

- [age](http://age-encryption.org)
- [Swift Crypto](https://github.com/apple/swift-crypto)
- [nvim-coverage](https://github.com/andythigpen/nvim-coverage)
- [Alpine Linux](https://alpinelinux.org)
- [age-plugin-se](https://github.com/remko/age-plugin-se)
- [passage: Password store using age](https://github.com/FiloSottile/passage)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/Q3J37F/feedback/)

---

### Why Swift is the best language for building modern applications on the backend

- **Speakers:** Tim Condon
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 16:05 - 16:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5408-why-swift-is-the-best-language-for-building-modern-applications-on-the-backend/)

#### Abstract

Swift is a relatively new language in the server world but provides a significant number of benefits that makes it ideal for building applications for servers. In this session you’ll see how Swift's tenets of Safety, Performance, Ease of Use using modern features along with a goal of making it an ideal language for anywhere in the stack make it the perfect language for backend development.
We’ll take a short tour of the language and see how easy it is to write clear, maintainable safe code that scales for large asynchronous applications. We'll discuss the language features that eliminate entire classes of common programming errors and see the capabilities that enable Swift to run on embedded devices, Lambda functions, WASM environments, and Docker containers. Finally we’ll discuss Swift’s interoperability with other languages such as C, C++ and Java that make it easy to migrate codebases to Swift.

#### Related Links

- [Swift GitHub Project](https://github.com/swiftlang/swift)
- [Vapor GitHub Project](https://github.com/vapor/vapor)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CMS3KH/feedback/)

---

### Live coding a streaming ChatGPT proxy with Swift OpenAPI—from scratch!

- **Speakers:** Si Beaumont, Honza Dvorsky
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 16:30 - 16:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5230-live-coding-a-streaming-chatgpt-proxy-with-swift-openapi-from-scratch-/)

#### Abstract

Join us as we build a ChatGPT client, from scratch, using Swift OpenAPI Generator. We’ll take advantage of Swift OpenAPI’s pluggable HTTP transports to reuse the same generated client to make upstream calls from a Linux server, providing end-to-end streaming, backed by async sequences, without buffering upstream responses.
In this session you’ll learn how to:

Generate a type-safe ChatGPT macOS client and use URLSession OpenAPI transport.
Stream LLM responses using Server Sent Events (SSE).
Bootstrap a Linux proxy server using the Vapor OpenAPI transport.
Use the same generated ChatGPT client within the proxy by switching to the AsyncHTTPClient transport.
Efficiently transform responses from SSE to JSON Lines, maintaining end-to-end streaming.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YZDUVV/feedback/)

---

### How to put Swift in a box: Building container images with swift-container-plugin

- **Speakers:** Euan Harris
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 16:55 - 17:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5116-how-to-put-swift-in-a-box-building-container-images-with-swift-container-plugin/)

#### Abstract

Did you know that you can write a cloud-native service in Swift and publish it in a container image, ready to run on any standard container-based cloud infrastructure, all using just the Swift compiler and its build system?    
In this talk we'll see how Swift's strong multi-platform support and highly extensible package manager can take care of the whole process for you, allowing you to build your application, package it and upload it in one efficient step:

Swift SDKs extend your native Swift compiler, giving it the ability to cross-compile and produce Linux executables directly on macOS.
swift-container-plugin extends Swift Package Manager, giving it the ability to construct a container image and publish it to a container registry.

We'll see these tools in action and peek behind the scenes to learn how they actually work.   Along the way we'll answer questions such as:

How can we build Linux binaries on macOS?
Can we build our own custom Swift SDKs?
What actually goes on when we build, push and pull container images?
How can we build a container image from scratch, just using Swift?

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7VLRQN/feedback/)

---

### Building Truly Native Cross-Platform Desktop Apps (With a Focus on GNOME)

- **Speakers:** David Häner
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 17:20 - 17:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4562-building-truly-native-cross-platform-desktop-apps-with-a-focus-on-gnome-/)

#### Abstract

Get to know the Aparoksha project. Write your app once and deliver a truly native look and feel across the major desktop platforms, all with a declarative framework!
The most mature part of this project is the Adwaita for Swift package, allowing the creation of native GNOME apps.
In this presentation, I'll introduce the core principles of Aparoksha, showcase its current capabilities, and share my vision for its future.

#### Related Links

- [Aparoksha Website](https://aparoksha.dev/)
- [Code](https://git.aparoksha.dev/aparoksha)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SY9FZS/feedback/)

---

### Your First AWS Lambda Function

- **Speakers:** Mikaela Caron
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 17:35 - 17:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4592-your-first-aws-lambda-function/)

#### Abstract

LIVE! Writing and deploying your first AWS Lambda function using Swift. We'll write a simple lambda function and deploy it within 20 minutes using the VSCode extension for AWS Lambda.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZHJK7R/feedback/)

---

### „Which is which, and who is who?” - Building a new Swift unqualified name lookup library during GSoC 2024

- **Speakers:** Jakub Florek
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 18:00 - 18:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4760--which-is-which-and-who-is-who-building-a-new-swift-unqualified-name-lookup-library-during-gsoc-2024/)

#### Abstract

This talk gives an overview of the new Swift unqualified name lookup swift-syntax library: SwiftLexicalLookup and the process required to integrate it within the compiler.
It dives into the intricacies of Swift’s name handling, highlights the complex lexical scope hierarchy with many, sometimes unexpected, interesting cases, and provides an overview of the challenging process of testing the new implementation and integrating it within the compiler.
Lastly, the talk provides some practical insights on how to start contributing to Swift from the perspective of a new contributor.

#### Related Links

- [Initial forum post discussing SwiftLexicalLookup](https://forums.swift.org/t/gsoc-2024-swiftlexicallookup-a-new-lexical-name-lookup-library/75889)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NVC93X/feedback/)

---

### Distributed Tracing in Server-Side Swift

- **Speakers:** Moritz Lang
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 18:15 - 18:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5218-distributed-tracing-in-server-side-swift/)

#### Abstract

This talk will provide an overview of observability in server-side Swift, with a focus on Distributed Tracing. I’ll start off by talking about some of the design decisions that went into building the swift-distributed-tracing library, which I co-created as part of Google Summer of Code in 2020. The talk will not only compare it to other Swift observability libraries (swift-log, swift-metrics), but also highlight some of the differences between Distributed Tracing in Swift compared to other ecosystems. My personal highlight is the fact that we eliminated the need for support libraries such as “OTel instrumentation for this specific web framework” by implementing swift-distributed-tracing to be used by libraries directly.
During the next part, I’ll cover what it means to build a tracer implementation for swift-distributed-tracing with plenty of examples from my OpenTelemetry client swift-otel. I’ll finish the talk with an end-to-end example of a server-side Swift application using the Hummingbird web framework, fully instrumented using Logging, Metrics, and Distributed Tracing, including context propagation and log correlation. This example exports logs, metrics, and spans via the OpenTelemetry Protocol (OTLP) to both a standalone OTel Collector instance and other observability backends that support OTLP natively.
Links:
- GitHub: apple/swift-distributed-tracing
- GitHub: slashmo/swift-otel
- OpenTelemetry Website

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VNYBTL/feedback/)

---

### Building reliable and scalable apps with Distributed Actors

- **Speakers:** Jaleel Akbashev
- **Room:** K.4.401
- **Day:** Saturday
- **Time:** 18:40 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4800-building-reliable-and-scalable-apps-with-distributed-actors/)

#### Abstract

Swift Distributed Actors offers an exciting way for building reliable and scalable apps in Swift. In this talk, we’ll start with a quick introduction to Distributed Actors itself, and Cluster System—peer-to-peer cluster actor system implementation. I’ll share my journey of implementing a simple event-sourcing and Virtual Actors plugin for this system, demonstrating how these patterns simplify state management and enhance fault tolerance. We’ll explore a small example and will see how it scales and manages different failures.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-swift:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-swift:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7PFV8B/feedback/)

---

## Testing and Continuous Delivery (19)

### Enhancing Testing Strategies for Critical Systems: Statistical Path Coverage

- **Speakers:** Imanol Allende
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 10:30 - 10:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5081-enhancing-testing-strategies-for-critical-systems-statistical-path-coverage/)

#### Abstract

Modern embedded and autonomous systems are pushing the boundaries of software complexity, especially in critical applications. Traditional testing methods often struggle to meet the demands of these systems, particularly when operating on resource-sharing architectures running complex operating systems like Linux. To address this challenge, we introduce Statistical Path Coverage (SPC), a novel statistical approach designed to enhance test effectiveness by statistically focusing on the execution paths exercised by target applications.
This presentation will discuss how SPC can quantify execution path coverage, estimate the risk of untested paths, and support assurance. We will also introduce DB4SIL, a tool leveraging FTrace to collect and analyze execution traces, enabling actionable insights into the kernel’s behavior during testing campaigns. Through examples, we will demonstrate how SPC and DB4SIL can guide developers in prioritizing testing efforts, improving test coverage, enabling continuous monitoring, and reducing risk in complex, software-driven systems.

#### Related Links

- [DB4SIL2 tool](https://gitlab.opentech.at/public_ot/db4sil2.git)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RBDMSG/feedback/)

---

### The Trustable Software Framework: A new way to measure risk in continuous delivery of  critical software

- **Speakers:** Paul Sherwood
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 11:00 - 11:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6204-the-trustable-software-framework-a-new-way-to-measure-risk-in-continuous-delivery-of-critical-software/)

#### Abstract

Many of the international standards for software in critical systems (e.g. IEC 61508, ISO 26262) are published under restrictive licences, at high prices. They broadly discourage the use of FOSS, by imposition of processes that do not align with modern open source best practices such as continuous delivery and automated testing. As a result some industries such as automotive, medical and aerospace, are locked in to proprietary software.
This talk will introduce the Trustable Software Framework (TSF), a new free and open source project which establishes an evidence-based method for measuring the actual risks involved in continuous delivery of software in critical systems.
TSF is applicable over the entire software supply chain, including CICD tools and infrastructure, build dependencies, operating systems, target applications and test environments, and is intended to measure risk on projects delivering critical systems which demand reliability, availability, security and safety.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DYZYTC/feedback/)

---

### KernelCI - upgrading Linux development and integration workflows

- **Speakers:** Paweł Wieczorek
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 11:30 - 11:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6487-kernelci-upgrading-linux-development-and-integration-workflows/)

#### Abstract

KernelCI has come a long way. It started as a simple tool that was only building and boot testing ARM devices, but its story didn't end there. KernelCI evolved to actively participate in the workflow of Linux developers and maintainers and is committed to provide a CI system that alleviates their workload.
In this talk Paweł will present how various CI workflow challenges were approached and resolved. He will show how KernelCI integrates with existing tools and highlight recently introduced improvements. Join Paweł to see how it enhances Linux kernel development process and discuss the next chapter of the KernelCI story!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8YEKAV/feedback/)

---

### Concurrency Testing using Custom Linux Schedulers

- **Speakers:** Johannes Bechberger, Jake Hillion
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 12:00 - 12:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4489-concurrency-testing-using-custom-linux-schedulers/)

#### Abstract

Consider you want to have a concurrency bug that requires threads to run in a specific order. Wouldn't it be great if you could stop and start threads at random? Prevent them from being scheduled onto the CPU? And the best part: Without the application being able to prevent this, like it could do with POSIX STOP and START signals?
In come the scheduler extensions for the Linux Kernel. Introduced in version 6.12, they allow you to quickly write your own schedulers with eBPF, and can be the base for simple libraries that enable you to start and stop threads directly in the Linux kernel. This opens the possibility of creating complex scheduler scenarios at a whim.
In this talk, we'll show you a prototypical sched_ext-based library for concurrency testing.

#### Related Links

- [sched-ext tutorial](https://github.com/sched-ext/scx/wiki)
- [hello-ebpf repository](https://github.com/parttimenerd/hello-ebpf)
- [sched-ext repository](https://github.com/sched-ext/scx)
- [prototypical scheduler](https://github.com/parttimenerd/concurrency-fuzz-scheduler)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SSRQLH/feedback/)

---

### Continuously Update Everything two years later

- **Speakers:** Olivier Vernin
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 12:30 - 12:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6076-continuously-update-everything-two-years-later/)

#### Abstract

In a continuously changing IT world, not being able to adapt is the difference between yesterday's and tomorrow’s projects. Everybody wants the benefits of changes, but nobody wants to endorse its associated risk. From dev to ops, I’ll share why we created Updatecli, an open-source declarative dependency manager. How automation helps us to anticipate, and fix early, our day-to-day challenges, and where the traps lie.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CLAMDX/feedback/)

---

### Automating Low-Level Firmware Validation with Robot Framework

- **Speakers:** Maciej Pijanowski
- **Room:** UD6.215
- **Day:** Saturday
- **Time:** 12:45 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5996-automating-low-level-firmware-validation-with-robot-framework/)

#### Abstract

Validating low-level firmware presents unique technical challenges, from
automating hardware control operations to testing interactive UEFI firmware
menus. In this presentation, we delve into how the Dasharo Open Source Firmware
Validation (OSFV) project uses Robot Framework, an open-source automation tool,
to address these complexities.
Drawing from years of firmware development experience across diverse hardware
platforms ranging from network appliances to workstations we will showcase how
OSFV tackles:
- automating hardware interactions such as GPIO toggling, UART communication,
  power control, video output capture, USB devices simluation, and more, on a
  wide variety of hardware platforms,
- testing dynamic and interactive firmware interfaces, including menu
  navigation and switching configuration options,
- managing the variability of real-world hardware environments to ensure
  repeatable and reliable test execution.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-testing:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-testing:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KW8YHL/feedback/)

---


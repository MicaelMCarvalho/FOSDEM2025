# FOSDEM 2025 Schedule - Part 4 of 11

*Generated on 2025-02-01*

## Table of Contents

- [Embedded, Mobile and Automotive (19)](#embedded,-mobile-and-automotive-19)
- [Energy: Accelerating the Transition through Open Source (24)](#energy:-accelerating-the-transition-through-open-source-24)
- [FOSDEM Junior (18)](#fosdem-junior-18)
- [FOSS on Mobile Devices (11)](#foss-on-mobile-devices-11)
- [Free Java (17)](#free-java-17)
- [Funding the FOSS Ecosystem (12)](#funding-the-foss-ecosystem-12)
- [GCC (GNU Toolchain) (11)](#gcc-gnu-toolchain-11)

## Embedded, Mobile and Automotive (19)

### Reverse engineering CAN communication and building ECUs using Elixir and the BEAM

- **Speakers:** Thibault Poncelet
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 15:30 - 15:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4973-reverse-engineering-can-communication-and-building-ecus-using-elixir-and-the-beam/)

#### Abstract

When tinkering with cars or other vehicles, being confronted with CAN communication or a similar bus is unavoidable. Throughout the past year, Thibault has been using CAN communication to build an Open Vehicle Control System and using it on a real car. In this talk, Thibault will explain how to get started with CAN reverse engineering, how he made different car parts from different brands talk together, and why Elixir and the Erlang Virtual Machine (the BEAM) is a good candidate for them to quickly prototype ECUs with cheap parts.

#### Related Links

- [Can library source](https://github.com/open-vehicle-control-system/cantastic)
- [Open Vehicle Control System source](https://github.com/open-vehicle-control-system/ovcs)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FW7M87/feedback/)

---

### Samsung Camera to Mastodon Bridge

- **Speakers:** Georg Lukas
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 16:00 - 16:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5026-samsung-camera-to-mastodon-bridge/)

#### Abstract

Between 2009 and 2015, Samsung released over 30 WiFi-equipped compact and mirrorless camera models that could email photos or upload them to social media. In 2021, they shut down the required API services, crippling the WiFi functionality.
To revive the WiFi feature, the firmware of multiple camera models was reverse-engineered to understand the protocol and to “circumvent” the WiFi hotspot detection implemented by Samsung.
Based on the gained knowledge, a FOSS implementation of the API was created using the Python Flask framework, allowing to post to Mastodon right from the camera. The project supports ~75% of the camera models, looking for hardware donations and better-skilled reverse engineers to close the gap.
It was exemplarily deployed on an inexpensive LTE modem running Debian, allowing on-the-go use of the camera WiFi.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VDWTXY/feedback/)

---

### Introduction to pmbootstrap

- **Speakers:** Anjan Momi
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 16:10 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6187-introduction-to-pmbootstrap/)

#### Abstract

PostmarketOS is a distribution based on Alpine Linux that boots on everything from Amazon Alexas to Android phones (over 500 devices). To help users install and develop this distribution, we use pmbootstrap - a swiss army knife for embedded and mobile development. In this talk, I will go over how we use pmbootstrap to develop postmarketOS and how you can use pmbootstrap for general embedded linux development.
https://gitlab.postmarketos.org/postmarketOS/pmbootstrap
https://postmarketos.org/

#### Related Links

- [Notes and Links](https://momi.ca/posts/2025-01-28-fosdem.html)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RTHUYY/feedback/)

---

### Interacting with Tesla vehicles locally over BLE using ESPHome

- **Speakers:** Yasir Ekinci
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 16:20 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4664-interacting-with-tesla-vehicles-locally-over-ble-using-esphome/)

#### Abstract

In early 2024, Tesla introduced strict API rate limits, reducing the number of commands to just 50 per day. This disrupted my smart charging automations, which were sending thousands of commands on a daily basis for tasks like solar charging and load balancing. To overcome this, I re-implemented Tesla's vehicle protocol in C++ for the ESP32 microcontroller, enabling local control of my Tesla by acting as a BLE (Bluetooth Low Energy) vehicle key.
In this talk, I'll give an overview of Tesla's vehicle protocol, dive into BLE communication using an ESP32, and show practical ESPHome implementations for common vehicle controls. The result is a cheap, open-source solution operating entirely locally with sub-second response times - no internet or API tokens required.

#### Related Links

- [C++ library repo](https://github.com/yoziru/tesla-ble)
- [ESPHome project repo](https://github.com/yoziru/esphome-tesla-ble)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FNQTQL/feedback/)

---

### MicroPython - Python for microcontrollers and Embedded Linux

- **Speakers:** Jon Nordby
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 16:30 - 16:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4525-micropython-python-for-microcontrollers-and-embedded-linux/)

#### Abstract

MicroPython is a tiny implementation of Python, designed for very constrained environments such as microcontrollers and embedded devices. It can run on devices with as little as 64 kB of RAM and 256 kB of FLASH. Over the last 10 years, MicroPython has become a productive development environment and mature platform for firmware development. It has been used in many applications - and has been deployed on everything from smartwatches to medical devices and satellites.
There are many features of MicroPython that make it an attractive way of developing firmware,
such as: the built-in file systems, first-class package management, built-in communication over WiFi/Ethernet/BLE/USB/etc, interactive programming via REPL, automated testing on PC and device. We will introduce these features briefly, and then discuss our favorite feature: the support for C modules,
and how it enables building sensor systems that are both computationally efficient and fast to develop.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7HCXGS/feedback/)

---

### Zephyr RTOS Roasting Party

- **Speakers:** Benjamin Cabé
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 17:00 - 17:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5760-zephyr-rtos-roasting-party/)

#### Abstract

You've heard it from colleagues, you've seen it on Reddit... Zephyr RTOS can be difficult to navigate.
Join this session for a "Zephyr Roasting Party" where we'll openly look at and discuss the most complained-about aspects of Zephyr, and try to honestly answer common questions and criticisms such as:

"Zephyr is bloated and really has poor real-time performance compared to other RTOSes"
"I already have a HAL from my silicon vendor, why would I need even more HW abstractions?"
"Devicetree is so complex! How do I even understand what's going on with all these 'macrobatics'?"
"There's lots of drivers available upstream, sure, but how do I know how mature they are?"
"What is this west thing, and why are you asking me to learn Python?"
"Why is my board/driver not supported?"

The goal of the talk is NOT to rhetorically question some of the "bad" parts of Zephyr, only to immediately tell you why Zephyr is in fact the best thing since sliced bread. Instead, we will honestly discuss these pain points to help you understand better some of the design decisions behind Zephyr, and why they might (or might not!) actually be worth the steep learning curve. This will also prove to be an interesting exercise that will help you understand when you might not need or want an RTOS in the first place.
Through practical demos and examples, we’ll show how tools like Devicetree, Kconfig, or West can actually make embedded development more efficient, and we'll try to make those "scary" parts of Zephyr more approachable, and give a sense of the roadmap for all the other areas of Zephyr that still need work and love.

#### Related Links

- [Zephyr Project - GitHub](https://github.com/zephyrproject-rtos/zephyr)
- [Zephyr Project - Documentation](https://docs.zephyrproject.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/U3WMN9/feedback/)

---

### Developing BLE Host Applications with Zephyr

- **Speakers:** Florian Limberger
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 17:30 - 17:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6262-developing-ble-host-applications-with-zephyr/)

#### Abstract

Bluetooth Low Energy, commonly abbreviated as BLE, is a well-known wireless communication technology aimed at low-power applications.
It divides devices into two categories: low-cost, potentially high volume, battery constrained peripheral devices such as head phones or heart rate monitors,
and comparatively more powerful and less constrained central devices, such as smartphones and notebooks.
The Zephyr Project has supported developing BLE peripheral applications for a long time.
But it may not be well known that it also supports BLE host applications, or central devices as the standard calls them.
In his talk, Florian will take a look at how we can develop BLE host applications using Zephyr.
After a (very) short introduction to the BLE protocol stack, he will delve into Zephyr's Bluetooth API and more importantly talk about the pitfalls
he encountered while getting his feet wet with Zephyr.
On the practical side, this talk will look into how BLE applications remain portabile between boards by different vendors,
and how the many BLE-enabled emulators and simulators provided by Zephyr can be used for quicker development and testing.
In this talk you will learn about:

the basics of the BLE protocols
the Zephyr Bluetooth API and its pitfalls
how portable Zephyr applications using BLE are
how you can utilize the Zephyr emulators and simulators for BLE development

#### Related Links

- [The Zephyr Project Homepage](https://zephyrproject.org/)
- [Zephyr Repository](https://github.com/zephyrproject-rtos/zephyr)
- [Bluetooth 6.0 Specification](https://www.bluetooth.com/specifications/specs/core-specification-6-0/)
- [Zephyr Bluetooth Documentation](https://docs.zephyrproject.org/latest/connectivity/bluetooth/index.html)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UAXKG3/feedback/)

---

### The USB-MIDI 2.0 device class in Zephyr

- **Speakers:** iTitou
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 18:00 - 18:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4561-the-usb-midi-2-0-device-class-in-zephyr/)

#### Abstract

A few years ago, a musician friend of mine reached out, hoping to build a custom controller for a live act performance. Together, we decided on a USB-MIDI device, which soon became a hands-on learning journey into Zephyr, USB development, and the MIDI protocol.
MIDI (Musical Instrument Digital Interface) has been the leading standard for connecting digital instruments and controllers since the 1980s. Although USB includes MIDIStreaming (a subclass of the Audio device class), Zephyr had no support for it. So, I decided to build one.
In this talk, I’ll walk you through my adventures implementing (and eventually upstreaming) this new device class. We’ll start by revisiting the original MIDI 1 protocol from the eighties, the original USB-MIDI1.0 from the 2000s and the updated USB-MIDI2.0 specification from 2020. After a brief refresher on USB devices, I’ll introduce the USB MIDIStreaming interface and the various supported topologies. Finally, we’ll see how to bring it all together using Zephyr USB device_next, and how it is used from your application's code. In the end, we should be able to make any kind of MIDI speaking device using our favorite kite-stamped RTOS.
Alongside this technical content, I may relate my experience as an occasional hobbyist contributor since Zephyr 1.14, and how I navigated spec updates (Device tree changes, USB-MIDI 1.0 to 2.0, Zephyr USB device next).

#### Related Links

- [USB-MIDI pull request in Zephyr](https://github.com/zephyrproject-rtos/zephyr/pull/81197)
- [Zephyr Project website](https://zephyrproject.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HT8UJX/feedback/)

---

### Using embedded Rust to build an unattended, battery-powered device

- **Speakers:** Xabier Crespo Álvarez
- **Room:** H.1302 (Depage)
- **Day:** Saturday
- **Time:** 18:30 - 18:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6300-using-embedded-rust-to-build-an-unattended-battery-powered-device/)

#### Abstract

In late 2023, the Libre Space Foundation asked my company to develop an Open Source photometer—a device designed to help astronomers measure and understand sky quality. The goal was to create a community-friendly tool accessible to enthusiasts and professionals alike, with an ambitious vision of building a global, crowdsourced network of photometers. While the network is a story for another time, this talk focuses on the journey of designing and deploying the device itself.
After writing down the requirements, we realized that the architecture—comprising I2C sensors, a microcontroller, and WiFi connectivity—was relatively straightforward. This simplicity gave us the opportunity to explore new technologies. In particular, could we use Rust to build a robust, unattended, battery-powered device?
Fast forward to today: we have manufactured several hundred units and are collaborating with the Instituto de Astrofísica de Canarias, a leading research institute, to rigorously test the devices under challenging conditions. In this session, we’ll share the lessons learned during development, the hurdles we overcame, and how Rust has since become an integral part of our workflow.

#### Related Links

- [Firmware repository](https://gitlab.com/scrobotics/optical-makerspace/dark-sky-meter-fw)
- [Hardware repository](https://gitlab.com/scrobotics/optical-makerspace/dark-sky-meter-hw)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-embedded:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-embedded:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NKA9EH/feedback/)

---

## Energy: Accelerating the Transition through Open Source (24)

### DIYing the "smartness" into an EV charger for profit and open source

- **Speakers:** Santiago Saavedra
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 09:00 - 09:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5468-diying-the-smartness-into-an-ev-charger-for-profit-and-open-source/)

#### Abstract

EVSE standards engineers envisioned AC charging to be the lowest barrier of adoption possible. And I think they succeeded! However, some charging boxes are still (unreasonably?) expensive or have very few features, and it's hard/expensive to find open source/flashable ones yet. How can we bridge the gap?
My use case features a low-energy house with 2.2kW energy availability, and I wanted to ensure the car plus appliances did not go over the limit. Using an off-the-shelf smart charger was unreasonable due to cost, installation requirements and expected savings.
Instead, I built my own watt-meter using ESP32 and Rust, a backend to track the energy expenditure, and an out-of-band mechanism to talk to the car.
I'll explore the trade-offs to the different options you have to talk to the EV (ISO 15118, IEC 61851-1 and vendor API if available), and present the repos that made the current iteration possible.
I'll also talk about alternatives (having a Matter-enabled Watt-meter) and future work that could be welcome,including the current reliance on a non-vendor-neutral API.
Wattmeter code: https://github.com/ssaavedra/esp32-amp-sensor
Backend: https://github.com/ssaavedra/amp-sensor-backend

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VSDBSA/feedback/)

---

### Tux-EVSE, an open-source EV charger

- **Speakers:** Hugo Mercier
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 09:30 - 09:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5399-tux-evse-an-open-source-ev-charger/)

#### Abstract

We introduce Tux-EVSE, an open-source suite of embedded software components for building a complete Electric Vehicle (EV) charging system using readily available hardware on Linux.
Tux-EVSE is designed with a strongfocus on security and ease of integration, utilizing a lightweight microservice framework (AFB) that isolates components for flexible development and testing.
This modular structure allows developers to efficiently test and refine each component on a local machine before deploying to the final embedded hardware.
The framework also embeds a security layer so that fine-grained permissions can be requested and granted to the application and / or services.
Written primarily in Rust, Tux-EVSE supports modern EV charging protocols, including ISO 15118-2x, DIN SPEC 70121, SLAC, and OCPP.
We will detail the different components of the charger: which kind of hardware components it can use, how the charging logic is implemented and how the modular architecture could allow one to adapt the charger to ones needs.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MU3UNP/feedback/)

---

### CitrineOS - one year of progress of a Charge Station Management System

- **Speakers:** Christian Weissmann
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 09:50 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5019-citrineos-one-year-of-progress-of-a-charge-station-management-system/)

#### Abstract

A little over a year ago, CitrineOS was launched to address a critical need in the EV charging landscape: a reliable, open-source Charge Station Management System (CSMS) built on the OCPP 2.0.1 protocol. Last year, I had given a talk here about CitrineOS as a fresh project. Since then, CitrineOS has made significant strides, achieving key milestones while navigating the challenges of scaling an open-source project in the rapidly evolving EV industry.
In this talk, I'll provide a comprehensive update on CitrineOS, highlighting key milestones such as the project’s first major release, compliance with Core and Advanced Security certification profiles. I also want to share how the project has evolved, what challenges we faced and the lessons we have learned. Then we will take a look at it's future and what is planned next.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZHEZFK/feedback/)

---

### Unleashing Bidirectional Charging: Protocols, Challenges, and Strategies with EVerest

- **Speakers:** Andreas
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 10:05 - 10:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5704-unleashing-bidirectional-charging-protocols-challenges-and-strategies-with-everest/)

#### Abstract

Bidirectional charging is transforming electric vehicles into active participants in the energy system, enabling energy flows between vehicles, charging infrastructure, and the grid. This talk will examine the entire impact chain of bidirectional charging, from the vehicle to the grid, and focus on how protocols such as EEBUS, OCPP, and ISO 15118-20 facilitate communication and energy management within this process.
We will explore the key challenges and gaps in this ecosystem and discuss strategies for addressing them. EVerest, an open-source EV charging stack, will be highlighted as a solution for integrating these protocols to enable efficient and interoperable charging solutions. Join us to discover how open standards and innovative strategies are driving the future of bidirectional charging and energy management.

#### Related Links

- [EVerest](https://github.com/EVerest)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QCGBD3/feedback/)

---

### Re-purposing EV battery packs as home energy storage using open-source

- **Speakers:** Christopher Obbard
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 10:25 - 10:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6043-re-purposing-ev-battery-packs-as-home-energy-storage-using-open-source/)

#### Abstract

EV Battery packs are generally recycled (or stored in a breakers yard) instead of repurposed, even though they have a lot of life left in them. Thankfully, there is a thriving open-source project by DalaTheGreat called Battery-Emulator which aims to allow enthusiasts to connect these used EV battery packs to off-the-shelf solar inverters, enabling cost-effective home battery storage systems to be created all while keeping users safe from the high-voltage energy contained inside the packs.
As of now, the project supports 23 different EV battery protocols from various manufacturers and 14 different inverter protocols. You can connect your choice of battery to your choice of inverter!
In this talk I will introduce the Battery-Emulator project and share the story of how I reverse engineered a 90kWh battery pack from a Jaguar i-Pace, using open-source tools such as SavvyCAN and the Canable USB-CAN adaptor to implement support for the battery in the project for everyone to enjoy !

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZVWS3L/feedback/)

---

### Flow Battery Research Collective: Building an Open-Source Battery for Stationary Storage

- **Speakers:** Kirk Smith, Josh Hauser, Daniel Fernandez Pinto
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 10:55 - 11:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6003-flow-battery-research-collective-building-an-open-source-battery-for-stationary-storage/)

#### Abstract

Batteries are a bottleneck in the energy transition. They can be expensive, require strict operating conditions, and may pose safety risks. Batteries degrade with time and use. Some chemistries rely on problematic minerals in their supply chains and others are hard to recycle at the end of their useful lives.
Yet, batteries can unlock clean mobility, stabilize electrical networks powered by intermittent renewables, provide backup emergency power, enable off-grid systems, and many other benefits. Many closed-source enterprises are competing to provide solutions in this space, but the commercial path to scale is difficult, with many startups running out of funding before their product hits the market. When they’re in business, there is little transparency or external validation of their development process, and if they go out of business, the wider community learns little from their failures.
We will present our efforts as part of the Flow Battery Research Collective (FBRC) to develop an open-source battery technology for stationary applications. FBRC is developing a battery designed for stationary energy storage use at the residential scale, that aims to be cheaper, safer, longer lasting, more sustainable, and more recyclable than current technologies. We’ll give a quick overview of existing battery technologies and cover the fundamentals of the technology we are working with—flow batteries—and why we picked this technology. 
We’ll cover our progress so far, our roadmap, and how we plan to integrate with the many open-source power electronics and battery/energy management systems that exist on the other side of our development gap. Network-connected batteries need secure software/firmware to operate safely; we will go over some ways in which a (flow) battery could be abused if a bad actor were able to control the system remotely. Finally, we will present our personal observations on launching an open-source, mechanical/chemical hardware project and how it aligns with/diverges from conventional open-source software communities.

#### Related Links

- [Development Kit Repository](https://codeberg.org/FBRC/RFB-dev-kit)
- [Project Website](https://fbrc.dev/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GUVKML/feedback/)

---

### Kubernetes Emissions Insights: Turning Cloud-Native Green (Without Recycling Pods)

- **Speakers:** Flavia Paganelli, Jasper Geurtsen
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 11:20 - 11:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6557-kubernetes-emissions-insights-turning-cloud-native-green-without-recycling-pods-/)

#### Abstract

What’s the carbon footprint of your Kubernetes workloads? In this session, we’ll introduce the Kubernetes Emissions Insights Tool, an open source project we’re building to estimate the environmental impact of workloads running on Kubernetes clusters—without resorting to recycling pods.
Built with open source technologies like Kepler for energy consumption monitoring, Electricity Maps for real-time carbon intensity data, and Boavizta for embodied emissions, this tool delivers a clear view of what your infrastructure is costing the planet.
We’ll also share insights from our work on Green Reviews, a CNCF project under the Environmental Sustainability TAG, which aims to estimate and track the emissions of CNCF projects. Together, these initiatives demonstrate how open source tools can empower developers to make informed, greener choices.
Whether you’re managing sprawling Kubernetes clusters or just curious about sustainability, this talk will show how open source innovation is turning the cloud a little greener—and maybe even make it fun along the way.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NSLMRL/feedback/)

---

### Measure what you manage: Transparent Energy consumption of cloud infrastructure

- **Speakers:** Josefine Kipke
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 11:40 - 11:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5646-measure-what-you-manage-transparent-energy-consumption-of-cloud-infrastructure/)

#### Abstract

Cloud infrastructure emits up to 4 % of the  world's carbon emissions. With the trend of shifting more and more workloads to cloud infrastructure being able to manage this through the lens of not only economical but also ecological reasoning is a must. 
Creating accurate energy models for cloud infrastructure is a complex but essential step toward achieving sustainable digital systems. In the Eco:Digit project, we embarked on a journey to measure and understand energy consumption in virtualized cloud environments, uncovering the challenges of correlating software workloads with physical resource usage.
This talk shares the process of developing energy profiles for cloud infrastructure, focusing on the use of open-source conform SCS clouds to create an energy model. We will discuss the technical and methodological hurdles we faced—such as accessing host-level metrics in virtualized environments, calibrating virtual consumption against physical measurements facing heterogeneous hardware, and dealing with limited transparency in hyperscaler clouds.
Key lessons shared include how to design a test environment that reliably maps energy consumption across physical and virtual layers, the importance of integrating diverse monitoring tools, and the role of collaborative partnerships with cloud providers like PlusServer and ScaleUp. Finally, we'll present the current state of our energy profiling system, showcasing its capabilities for generating detailed energy consumption reports and enabling actionable sustainability insights.
This talk will provide the audience with technical takeaways and practical knowledge for anyone interested in energy monitoring, open-source cloud infrastructure, or advancing sustainability in the digital domain.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ECVN8H/feedback/)

---

### Software Licensing For A Circular Economy -- How FOSS Reduces The Energy Consumption And Carbon Footprint Of ICT

- **Speakers:** Joseph P. De Veaugh-Geiss
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 11:55 - 12:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5431-software-licensing-for-a-circular-economy-how-foss-reduces-the-energy-consumption-and-carbon-footprint-of-ict/)

#### Abstract

The International Energy Agency estimates that the Information & Communications Technology (ICT) sector consumes about 10% of worldwide energy, half of which comes from device production alone. Overall, ICT accounts for 2-3% of global CO2 emissions, which is on a par with the aviation industry; if nothing changes, by 2050 this will rise to over 30%. When looking at emissions over the lifespan of devices, the vast majority of CO2 (85+%) comes from production, not usage.
Moving to a circular economy can reduce the disproportionate energy consumption and CO2 emissions associated with hardware manufacturing. Hardware and software are inextricably linked, and a Free Software license disrupts the produce-use-dispose linear model of hardware and enable the shift to a reduce-reuse-recycle circular model. In this talk I provide an overview of the environmental harm driven by both hardware and software and how FOSS is well-positioned to address the issues. I will link the inherent values that come with a Free & Open Source Software license to sustainable software design. Finally, I will present the various ways that Free Software can prevent the unnecessary production of new devices, whether by adapting the software to hardware one already owns, or recycling existing software to support the newest hardware being produced.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NT3BQH/feedback/)

---

### PowerLetrics: Democratizing Energy Metrics for Linux

- **Speakers:** Didi Hoffmann
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 12:10 - 12:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4685-powerletrics-democratizing-energy-metrics-for-linux/)

#### Abstract

The environmental impact of software and hardware systems has become a pressing concern. While mainstream operating systems like macOS and Windows provide proprietary tools to analyze energy usage, Linux—the cornerstone of open-source computing—lacks comparable capabilities. To address this gap, we present PowerLetrics, an open-source framework enabling detailed, per-process energy footprint analysis on Linux systems.
Key Contributions:


Secure and Granular Power Metrics: By leveraging the /proc file system, PowerLetrics delivers real-time power consumption data on a per process/ container level without requiring elevated permissions, ensuring both usability and security. 


Inspired by macOS's powermetrics: Our solution adapts the power estimation principles of macOS's powermetrics utility to Linux, offering an analogous capability tailored to open systems.


Customizable Energy Models: Through the Linux Energy Estimation Engine (L3E), PowerLetrics empowers users to tweak or design bespoke energy models, fostering a flexible and adaptable ecosystem.


Open-Source Accessibility: Available under an open-source license (AGPL), PowerLetrics is a community-driven initiative designed for scalability across diverse hardware platforms, from servers to mobile devices. By providing clear, actionable data on energy consumption, we empower the tech community to make informed decisions that favor environmental sustainability, aligning technological advancement with ecological responsibility.


With its modular architecture and minimal performance overhead, PowerLetrics integrates seamlessly into existing Linux environments, supporting both developers and system administrators in optimizing energy efficiency.
The project is accessible via GitHub (https://github.com/green-kernel), and we invite the open-source community to collaborate on enhancing its capabilities. Future directions include automated benchmarking tools for hardware-specific models and support for proprietary hardware components like GPUs.

#### Related Links

- [Green Kernel](https://github.com/green-kernel)
- [PowerLetrics](https://github.com/green-kernel/powerletrics)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/V938ZU/feedback/)

---

### Overcoming the chicken-and-egg problem: From the battlelines of the S2 energy flexibility protocol adoption

- **Speakers:** Nicolas Höning, Vlad
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 12:25 - 12:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6109-overcoming-the-chicken-and-egg-problem-from-the-battlelines-of-the-s2-energy-flexibility-protocol-adoption/)

#### Abstract

Open communication protocols and open source software go hand in hand and fuel each other. But there is a potential chicken-and-egg problem: Should the OEMs support it first, or are they waiting for widespread support of the protocol in EMS implementations (who are hesitant if the OEMs don't support it)?
The only forward is to start showing real solutions and implementations with front-runners from both sides. Then, these smaller showcases can become an avalanche and lift the sector up in an open way. Both steps are difficult and need partnerships.
Energy flexibility optimization behind the meter is already deployed in practice. However, networking protocols and definitions of flexibility are used which are not standardized and not openly available. This makes building new solutions with new flexible energy assets (like EVs, batteries, heat pumps and also solar inverters) a chore and drives up costs. Each new energy asset (or new brand) has to be integrated with their specific protocols and patterns. New protocols attempt to standardize these concepts, such as the S2 protocol. It targets an international audience for both existing and new/future energy assets. See https://s2standard.org/ 
S2 is approved as European standard, but the next batteline is to showcase that implementations can work and that both sides, OEMs and EMS, are willing to get to work. Open source implementations will provide building blocks and serve as reference.
This presentation will show the efforts and experiences of two different consortia, from different implementation projects, with adopting the protocol and creating tools to spur adoption by other innovators and OEMs. Of course, we will also briefly outline the protocol itself, and address differences and shared features in other existing protocols in this space, like EEBus and OpenADR.
We hope this talk can spur more interest and collaboration in this space and towards a lift for open efforts in the industry. 
Join our presentation if you want to learn more about protocol standardization efforts within the energy transition and S2 specifically!

#### Related Links

- [The S2 standard](https://s2standard.org/)
- [First standard impĺementations of S2 (in Python)](https://github.com/flexiblepower)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QXJTL9/feedback/)

---

### Engaging households to avoid congestion works: mixing gamification, automation and trading

- **Speakers:** Pierre Kil
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 12:50 - 13:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5024-engaging-households-to-avoid-congestion-works-mixing-gamification-automation-and-trading/)

#### Abstract

Last year we presented our first residential pilot, together with DSO Alliander in Amsterdam where we prevent local net congestion by incentivising residents in the same district to shift power consumption outside forecasted time windows of net congestion. In this presentation we are sharing the results: residents actually participate and change their behaviour.
In the initial step we took a gamification approach where everybody can participate, regardless of their personal situation. Now, with active involvement of Alliander we are extending the approach towards automation logic for charging, thermostats and home batteries. We will share the forecasting and optimisation methods we are using for combining automation with the original gamification.
The next challenge is to enable users to participate in additional markets at the same time without creating conflicts: local congestion, dynamic tariffs, energy sharing and even seasonal storage. With that in mind we started additional projects with the City of The Hague and DSO Stedin, as well as with the City of Arnhem and DSO Alliander. We are combining household participation in reducing net congestion with optimising shared assets such as district batteries and public charging. Jointly we started a collaboration with GOPACS (the Dutch congestion management portal) to enable the energy community of residents to trade, a first of it's kind. We will demonstrate the cases for Amsterdam, Arnhem, and The Hague.

#### Related Links

- [OpenRemote GitHub](https://github.com/openremote)
- [OpenRemote Documentation](https://docs.openremote.io/docs/introduction/)
- [OpenRemote Forum](https://forum.openremote.io/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UL7HSY/feedback/)

---

### SunPeek - Open-Source Software for Performance Assesment and Monitoring of Large Solar Thermal Plants

- **Speakers:** Marnoch Hamilton-Jones, Philip Ohnewein
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 13:10 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6500-sunpeek-open-source-software-for-performance-assesment-and-monitoring-of-large-solar-thermal-plants/)

#### Abstract

Heating and cooling account for around 50% of Europe’s final energy consumption, making renewable heating and cooling technologies a significant lever to reduce carbon emissions. One well established renewable heat technology is solar thermal. Solar thermal systems use solar radiation to heat a working fluid directly, providing a low-cost heat source with a significantly better specific yield per unit of collector area than PV. Solar thermal collectors have been used to supplement domestic hot water heating for decades, but more recently the market for large solar thermal arrays to supply bulk heat to district heating systems or industrial customers has begun to grow significantly. At present long-term monitoring of these systems is carried out using a variety of proprietary tools developed by industry stakeholders – with limited agreement on methodology and little transparency on the algorithms being employed – or not at all. To address this, the international standard ISO 24194 was published in 2022, providing an open standard for the assessment of the performance of solar thermal arrays in operation. The SunPeek project is the first open-source implementation of this standard and aims to become the reference implementation by providing an open, trusted, user friendly application with well documented design decisions in cases where the standard is ambiguous. SunPeek is designed with highly automated workflows in mind and includes robust data preprocessing and error checking. It also includes several extensions of the ISO methodology to allow valid assessments to be made under a wider range of operating conditions, and funding has been secured to add fault detection, localization and remediation decision support functionality.  
Several use cases are cases envisioned including: 
Long term automated regular performance assessment. 
performance guarantee verification (a use case which clearly demonstrates the value of being open source, due to verifiability of the codebase) 
Research applications 
Integration into existing fully featured plant monitoring solutions.  
Different interfaces and packaging formats are provided to support these.  
The core functionality is written in python, and made available as a package on PyPi (https://pypi.org/project/sunpeek/). 
A set of docker images and a compose configuration allow deployment as a web application with Vue.js based user interface and FastAPI based REST API. 
The project is hosted on GitLab (https://gitlab.com/sunpeek), documentation is at https://docs.sunpeek.org and a demo is available at https://demo.sunpeek.org. 
This work has been supported by the Austrian Research Promotion Agency (project HarvestIT, project number FFG 887648, and IEA SHC Task 68, FO999890460) and the European Commission (project IndHeap, proposal number 101136140).

#### Related Links

- [SunPeek Core Project on GitLab](https://gitlab.com/sunpeek/sunpeek)
- [SunPeek Documentation Site](https://docs.sunpeek.org/)
- [SunPeek Demo](https://demo.sunpeek.org)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ELFBZK/feedback/)

---

### Energy Access Explorer  : The Digital Public Good to deliver Climate-compatible Energy Transitions for Everyone

- **Speakers:** Akansha Saklani
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 13:30 - 13:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6547-energy-access-explorer-the-digital-public-good-to-deliver-climate-compatible-energy-transitions-for-everyone/)

#### Abstract

Energy services are highly interconnected with socio-economic development and human well-being. Yet, life without reliable energy is a reality for more than 675 million people globally, while more than 2 billion people use polluting fuels to cook their meals. Addressing the critical challenge of extending energy access to the unserved and underserved communities, more than six decades after full electrification in Europe and the United States, is imperative. Unfortunately, the current trajectory falls short. The latest SDG 7 Tracking Report highlights that the world is off course in achieving Sustainable Development Goal (SDG) 7 by 2030, with 85% of those without electricity residing in Sub-Saharan Africa. The repercussions of this shortfall are significant, with adverse impacts on societies and economies: inadequate healthcare persists, educational institutions struggle to provide quality education, and agricultural and industrial sectors face competitiveness challenges in regions where reliable energy remains elusive. Despite efforts such as grid extension, community-run mini-grids, and individual household solutions, progress has been insufficient because these solutions haven't been delivered at scale, in a coordinated way. We urgently require access to data, analytical tools and innovative strategies to deliver affordable, reliable, and clean energy to those who lack access to it. While existing solutions have primarily focused on supply-side and technology-centric approaches, there's a crucial need to prioritize demand-side perspectives to truly meet the needs of users, whether households or institutions.
What is the Energy Access Explorer (EAE)? 
To help address this challenge, WRI, in collaboration with partners has developed the Energy Access Explorer (https://www.energyaccessexplorer.org/; https://github.com/energyaccessexplorer) (EAE), a data-driven, integrated and inclusive approach to achieving universal access to energy for equitable, socio-economic development. EAE is the first, open-source, online and interactive geospatial platform that enables energy planners, clean energy entrepreneurs, donors, and development institutions to identify high-priority areas for energy access interventions. EAE functions also as a dynamic information system, reducing software engineering and data transaction costs for both data providers and users and facilitating data management and governance.  
Use cases 
With over 25,000 users, 48% of which are women, EAE users can customize the analysis and identify areas of interest based on their perspective. More specifically, the use of this platform enables the following:
Energy Planning Agencies improve the ways integrated and inclusive planning is carried out using a data-informed approach. They will explore the potential for grid extension, off grid systems, clean cooking technologies and renewables for expanding energy access where needed the most. Clean Energy Enterprises, especially the ones with limited or no market intelligence / GIS capacity in house, identify new market opportunities. They will access demographic, socio-economic data, consumer ability to pay for energy services combined with information on energy resource availability and power infrastructure to locate priority areas for expanding their businesses.  Service Delivery Institutions in the health, education, productive use of energy, agriculture sectors get a better understanding of energy needs associated to development services. Clean Cooking agencies identify areas where the uptake of clean cooking technologies should be prioritized based on location specific data on demand, supply and environment. Donors and Development Finance Institutions identify areas where their grants and investment will have the most impact.  
Outcomes to Date
To date, EAE has contributed to: the Powering Healthcare Roadmap of the Government of Zambia and the Powering Healthcare initiative of the Health Ministry in Uganda, the development of local, integrated and inclusive County Energy Plans in Kenya, to support the 0.5 billion USD Africa Mini Grid and the Energizing Agriculture Program in Nigeria, to inform the results based financing scheme for off grid electrification in Ethiopia and to establish cross sectoral EAE working groups enabling an integrated and inclusive approach to planning.

#### Related Links

- [Energy Access Explorer](https://github.com/energyaccessexplorer)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/V8NQC8/feedback/)

---

### What would a green energy system look like? Assessing the costs and benefits of different scenarios with Antares

- **Speakers:** Peter Mitri, Florian OMNES
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 13:50 - 14:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5457-what-would-a-green-energy-system-look-like-assessing-the-costs-and-benefits-of-different-scenarios-with-antares/)

#### Abstract

With its Green Deal, Europe aims to become the first climate-neutral continent.
To achieve this neutrality, a large number of industries need to be transformed, especially in the energy sector.
However, the introduction of more renewable energies is notoriously difficult: these energies are highly intermittent and unpredictable, and maintaining a balance between supply and demand will be a major challenge.
Policy makers can no longer make decisions without first assessing their impact on the increasingly fragile physical system.
The open source Antares software suite can help simulate different scenarios of the energy system to assess the costs and benefits of a given investment strategy.
Antares is widely used by RTE (French TSO) to perform studies on a French & European scale to help decision makers, as well as by other European TSOs to perform their own studies.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3MUVVP/feedback/)

---

### Costumer & Energy Management for Distributed Renewable Energies in the global south

- **Speakers:** Vivien Barnier
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 14:10 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5577-costumer-energy-management-for-distributed-renewable-energies-in-the-global-south/)

#### Abstract

Decentralized Electric Utilities (DEUs) and Solar-Home-System distributors (SHS-D) are increasingly emerging to reach and serve deep rural unelectrified communities in the global south (mainly in Africa and Asia). These DEUs & SHS-D are required to handle a vast and complex range of technical (e.g., energy, power, etc. ) and financial data points from their operations daily. Particularly, domestic small and midsize entrepreneurs find themselves hands-tied in their quest to digitize and optimize their operations, allowing them to scale and reach more unserved rural communities. The integrations with different energy asset communications and the integrations with payment providers (e.g., mobile money, which is widely used) come with significant efforts for these small-size companies. Therefore, we see an enormous value (in supporting bottom-up, locally driven rural electrification) in the provision and maintenance of the Open Source MicroPowerManager, where all those integrations and interopearbilities need to be set up only on time and benefit a variety of domestic companies and initiatives. Also, the operational and business models of the different DEUs and SHS-D are generally slightly different. The core processes are the same, and the Open Source MicroPowerManage software provides all the required basic functionalities to ease these processes. 
In the presentation, we will dive into the current technology setup of the Project, both organizationally and technically. We want to shed light on the MicroPowerManager, its current functionalities, feature pipeline, particular technical and community-building challenges, and other possible use opportunities. We hope to have fruitful exchanges and interesting feedback from the community; maybe one or the other wants to support our journey.

#### Related Links

- [GitHub repository of the MicroPowerManager](https://github.com/EnAccess/micropowermanager)
- [EnAccess Homepage](https://enaccess.org/)
- [Project Page for the MicroPowerManager in the EnAccess OS Library](https://enaccess.org/micropowermanager/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HEHKJF/feedback/)

---

### Bringing Machine Learning Renewable Energy Forecasting Models to the Open Source Community - data engineering and other challenges implementing large ML models

- **Speakers:** Peter Dudfield
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 14:35 - 14:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5606-bringing-machine-learning-renewable-energy-forecasting-models-to-the-open-source-community-data-engineering-and-other-challenges-implementing-large-ml-models/)

#### Abstract

Solar energy is predicted to be the largest form of power generation globally by 2040 and having accurate forecasts is critical to balancing the grid. Unlike fossil fuels, renewable energy resources are unpredictable in terms of power generation from one hour to the next. In order to balance the grid, operators need a close estimate of when and how much solar and wind power will be generated on a given day. 
Open Climate Fix (an open source AI company) developed and deployed PVNet, a large ML model which forecasts solar generation for the next 36 hours. The forecasts are used by the UK electricity grid operator for real-time decision making and for reserve planning. These forecasts can save 200,000 tonnes of CO₂ and £20 million per year. 
But how do we make sure the model is usable by the Open Source community? We will explore the challenges of accessing 100s of TB of Numerical Weather Prediction (NWP) datasets, and the challenges of data engineering these large NWP datasets. We will also talk about the challenge of working with these large ML models and what we are doing to enable the Open Source community to benefit. 
Open Climate Fix is an open-source not for profit company using machine learning (ML) to respond to the need for accurate renewable energy forecasts. Connecting energy industry practitioners with ML researchers doing cutting-edge energy modelling is our aim, and one way we seek to do this is by making much of our code open-source.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UKGV37/feedback/)

---

### Electricity market simulations with the open agent-based model AMIRIS

- **Speakers:** Christoph Schimeczek
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 14:55 - 15:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5406-electricity-market-simulations-with-the-open-agent-based-model-amiris/)

#### Abstract

We present the Agent-based Market model for the Investigation of Renewable and Integrated energy Systems AMIRIS which can be used, e.g., to
* assess future electricity market dynamics (e.g. prices),
* investigate dispatch strategies for new demand actors such as electrolyzers, and
* evaluate electricity market designs and policies.
AMIRIS was created in 2008 and released as open source in 2021. It has been actively developed ever since. AMIRIS represents all major actors in the electricity system, models their assets and decision strategies, and enables its users to observe emerging market dynamics. To this end, AMIRIS includes agents for market places, trading, power plant operation, storage operation, demand-side flexibility, and policy instruments. Back-testing demonstrates the high quality of AMIRIS results.
We aim to provide a powerful open tool that is usable by scientist and market stakeholders alike. In order to leverage the power of the open source community, we constantly lower the barriers for new people onboarding the project by continuously improving our documentation, creating easy installation and execution routines, and providing extensive open data sets and training material. To enable smooth integration of AMIRIS in other workflows, we follow the FAIR4RS principles and provide a full metadata description of AMIRIS model parameters, linking to the Open Energy Ontology wherever possible.
This talk will give a brief introduction to the AMIRIS model and its toolchain, demonstrate its installation and execution, provide examples of AMIRIS applications, and show the roadmap for future developments.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8BEUCY/feedback/)

---

### Assessing and Mitigating the Risk of Carrington-Type Events with PowerModelsGMD.jl

- **Speakers:** Arthur K Barnes
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 15:10 - 15:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4714-assessing-and-mitigating-the-risk-of-carrington-type-events-with-powermodelsgmd-jl/)

#### Abstract

Geomagnetic disturbances resulting from space weather activity have the potential to disrupt or damage the bulk electric power system, but the severity is a hotly debated topic. Compared to other large scale contingency events on electric power systems, the impact of Geomagnetic Disturbances is  a rare event. This means that little in the way of empirical data is available to quantify impacts or to guide policymakers or utilities in hardening systems against such events. We present PowerModelsGMD.jl, an open-source  Julia toolbox within the PowerModels.jl ecosystem for analysis and optimal mitigation of such events. This talk will discuss the state of open-source software in this problem space, the software architecture of PowerModelsGMD.jl, how it can be applied to produce actionable results, and summarize remaining research gaps.

#### Related Links

- [Repo](https://github.com/lanl-ansi/PowerModelsGMD.jl)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HPEVXJ/feedback/)

---

### Ensuring Reliable Energy Access: Optimizing Mini-Grid Dispatch with Joint Chance Constraints

- **Speakers:** Alessandro Onori
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 15:30 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5637-ensuring-reliable-energy-access-optimizing-mini-grid-dispatch-with-joint-chance-constraints/)

#### Abstract

Off-grid rural electrification faces significant challenges, including unreliable grid connections, high variability in renewable energy generation, and limited financial resources. In many regions, such as Sub-Saharan Africa, weakly-connected mini-grids present a promising solution; however, their operation is often constrained, if not undermined, by uncertainties in energy demand, renewable production, and frequent grid outages. Addressing these challenges requires advanced optimization techniques to ensure reliable, cost-effective energy access.
The Autarky model, developed in Julia, offers an innovative approach to optimizing the economic dispatch of renewable-powered, weakly-connected mini-grids under uncertainty. By integrating Joint Chance Constraints (JCC), the model ensures robust operation during outages and renewable variability while maintaining reliability at a predefined probability level. It addresses four key uncertainties: solar power forecasting errors, load demand forecasting errors, and the timing and duration of main grid outages. The model strategically schedules diesel generators and battery reserves to maximize operational efficiency and guarantee energy supply even during grid disruptions.
Autarky is benchmarked against three alternative approaches — Individual Chance Constraints (ICC), an Expected-Value Model (EVM), and a Regular deterministic model — to evaluate the trade-offs between reliability and cost. The framework is validated through a real-world case study of a mini-grid in Lake Victoria, Tanzania. Results demonstrate that the JCC model achieves a 90% probability of successful islanding with 3-hour daily grid outages, significantly enhancing reliability compared to ICC (58%) and EVM (20%), while leading to a 25% reduction in profit.
Key contributions of this work include:
•   A stochastic optimization framework tailored for weakly-connected mini-grids, integrating multivariate Gaussian distributions through spherical-radial decomposition.
•   A comparative analysis of dispatch strategies, quantifying the trade-offs between cost and reliability across different models.
•   A practical case study using real-world data from Tanzania, validating the model's effectiveness in addressing uncertainties and improving energy access.
By fostering open-source collaboration, Autarky aspires to accelerate the global deployment of resilient mini-grids, thereby contributing to universal clean energy access and the realization of the United Nations’ Sustainable Development Goal 7 (SDG-7). 
The model is openly accessible on GitHub. 
Link: https://github.com/Autarky-Power/Minigrid-JCC/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EU3Y9L/feedback/)

---

### Empowering the Energy Transition through Fast and Flexible Network Simulation

- **Speakers:** Jaap Schouten, Thijs Baaijen
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 15:55 - 16:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4662-empowering-the-energy-transition-through-fast-and-flexible-network-simulation/)

#### Abstract

Join us for a insightful presentation on the open source "Power Grid Model DS" project, an innovative extension designed to harness the power-grid-model core for advanced data science applications. This session will delve into the project's new modeling and simulation interface, which facilitates efficient grid calculations and utilizes graph algorithms for detailed network analysis. Discover the extended numpy model that enriches development ease and the practical simulation tools for network mutations, underscored by robust debugging capabilities like intuitive network visualization. This discussion is essential for those interested in cutting-edge solutions for smarter, sustainable energy systems.
Building on the foundational strengths of the open-source "Power Grid Model," this library is pivotal in addressing the challenges within the electricity grid, such as the integration of renewable energy sources and smart technologies. Through its C++ core and Python API, it offers advanced features like state estimation, power flow, and short-circuit calculations, crucial for both current applications and academic research. This presentation will highlight how the new open source "Power Grid Model DS" project extends these capabilities, enhancing both immediate operational needs and long-term strategic planning in energy networks, fostering the smart energy transition.

#### Related Links

- [Power Grid Model website at LF Energy](https://lfenergy.org/projects/power-grid-model/)
- [Power Grid Model organisation at Github](https://github.com/PowerGridModel)
- [Power Grid Model DS Github](https://github.com/PowerGridModel/power-grid-model-ds)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/Q7ESNC/feedback/)

---

### OwnTech Update: A demo-talk of our V1 software suit and hardware advancements

- **Speakers:** Luiz Villa
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 16:20 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6078-owntech-update-a-demo-talk-of-our-v1-software-suit-and-hardware-advancements/)

#### Abstract

OwnTech is a company and a foundation dedicated to democratizing access via open-source to a key enabler of the energy transition: Power Electronics.
Discrete and ubiquitous, power electronics allows the creation of hardware and software that drive electric cars, charge batteries and connect solar panels to the grid. It is an amalgamy of electronics hardware, real-time embedded software and control algorithms. It is complex, hard and central to decarbonizing society.  
Yet, despite its key role in the transition, power electronics is still an obscure discipline only properly understood by a handful few. It has not yet gone through the type of open-source fast-prototyping revolution brought about by Arduino or Raspberry Pi in the industrial informatics and computer fields.
We at OwnTech are dedicated to do just that: revolutionize the way power electronics is taught, understood and used in the field.
Last year we introduced ourselves to the FOSDEM community, this year we bring the updates and showcase our consolidated open-software and open-hardware advancements.
In this talk we will briefly describe the origin of our project, our technology and provide a working demo of our V1 embedded software. We will also show you our hardware, the types of functions it can provide and how it can become a game-changer in the power electronics fast prototyping community.
See you at the FOSDEM Energy DevRoom!

#### Related Links

- [OwnTech Foundation GitHub Repository](https://github.com/owntech-foundation)
- [OwnTech Documentation Center](https://docs.owntech.org)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XKP8WP/feedback/)

---

### CityCatalyst: Open Source Helps Cities Start Their Climate Journey

- **Speakers:** Evan Prodromou, Milan Gruner
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 16:35 - 16:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6099-citycatalyst-open-source-helps-cities-start-their-climate-journey/)

#### Abstract

CityCatalyst is an Open Source Web application for managing a city's climate journey. Cities can start tracking greenhouse gas emissions using CityCatalyst from a variety of sectors -- buildings, transportation, waste, agriculture, industry -- in the GHG Protocol for Cities (GPC) format. They can assemble emissions data from different public data sources, including nationally-tracked environmental data, AI models, or satellite data. They can also update their emissions data manually, using well-established methodologies. The reports generated by these emissions inventories can be shown on a public dashboard for citizens or disclosed to investors or international tracking organizations. Upcoming versions of the platform will also include risk assessments (what effect will climate change have on the city?) and action planning (what can the city do to lower risk and emissions). As an Open Source tool, CityCatalyst lowers the costs of climate change tracking and puts power into the hands of cities of all sizes and in all parts of the globe.
CityCatalyst is built using the open source projects React, NextJS, ChakraUI, Tailwind, PostgreSQL, Sequelize, Nivo, Pigeon Maps and many more.
Project repository on Github

#### Related Links

- [CityCatalyst Github Repository](https://github.com/Open-Earth-Foundation/CityCatalyst)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/M7VQFR/feedback/)

---

### Empowering Sustainable Futures: Exploring ORES (Open Renewable Energy System) and Its Latest Innovations

- **Speakers:** Chris Xie, Karl Xiaofeng Yang
- **Room:** H.2214
- **Day:** Sunday
- **Time:** 16:50 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4828-empowering-sustainable-futures-exploring-ores-open-renewable-energy-system-and-its-latest-innovations/)

#### Abstract

As the world races to address the climate crisis, the open-source community is uniquely positioned to drive innovation and collaboration in renewable energy systems. The Open Renewable Energy System (ORES) project from LF Energy is a pioneering initiative that leverages the power of open source to design the specification of the modular, scalable, and interoperable components and modules, to create  disaggregated renewable energy systems.  
In this session, we will introduce ORES, highlighting its mission to democratize access to sustainable energy technologies. We will explore the project's latest updates, including enhancements in its plug and play energy router design, the integration of real-time monitoring systems, and support for decentralized energy grids, drop and deploy plug and play outdoor cabinet design proposals etc. 
Whether you're a developer, a sustainability advocate, or simply curious about open-source contributions to renewable energy, this talk will provide insights into how ORES is driving innovation and empowering communities to take charge of their energy future. Join us to discover how you can contribute to and benefit from this transformative open-source project.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-energy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-energy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KEPTCS/feedback/)

---

## FOSDEM Junior (18)

### MicroCode: Live, Portable Programming for Children

- **Speakers:** Lorraine Underwood
- **Room:** UD6.203
- **Day:** Saturday
- **Time:** 10:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5156-microcode-live-portable-programming-for-children/)

#### Abstract

MicroCode is a new tile based programming language that makes it possible to program the micro:bit without the need for an extra computer or Internet connection. All the programming takes place on a handheld shield. Come along and try out this new way of coding! All equipment is provided. With no written words, on the tiles children as young as 6 can join in.
MicroCode

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZWPRWM/feedback/)

---

### Learn to build your own mobile app with MIT App Inventor

- **Speakers:** Evan Patton
- **Room:** UD6.205
- **Day:** Saturday
- **Time:** 10:30 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5046-learn-to-build-your-own-mobile-app-with-mit-app-inventor/)

#### Abstract

In this hands on workshop, you will use MIT App Inventor to build two applications for your Android or iOS device. Those new to MIT App Inventor can have a simple first app up and running in less than 30 minutes. And what's more, our blocks-based tool facilitates the creation of complex, high-impact apps in significantly less time than traditional programming environments. The first app you create will be a cat you can pet to make meow. The second app will allow you to draw your own pictures via touch. Participants must bring both a laptop and a mobile device (phones and tablets are both good, running Android 4.0+ or iOS 12+).

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
Remember to bring an Android phone
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GF9BAJ/feedback/)

---

### Learn Python programming using Hedy

- **Speakers:** Jesús Pelay, Pink van de Hel, Annelies Vlaar
- **Room:** UD6.203
- **Day:** Saturday
- **Time:** 12:15 - 13:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5106-learn-python-programming-using-hedy/)

#### Abstract

Hedy is a programming language that aims to teach textual programming to kids. Hedy's unique approach involves gradual changes in the  syntax of the programming language, so students are not overloaded with information right away. This devroom is aimed at students from 9 to 12 years old, but anyone with a desire to start learning programming (or teaching) with text based language is welcome. You'll need your own laptop (no installs needed, Hedy is webbased) and reading- and basic typing skills (or someone to help you read and type). No prior programming experience is needed. When you have finished all 18 levels of Hedy, you know the basics of Python.

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WWJGYG/feedback/)

---

### Program a Tiny Computer!

- **Speakers:** Bernat Romagosa, John Maloney
- **Room:** UD6.205
- **Day:** Saturday
- **Time:** 12:15 - 13:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4856-program-a-tiny-computer-/)

#### Abstract

In this introductory, hands-on workshop you will learn how to program an
inexpensive, battery-powered, pocket-size computer (micro:bit or Calliope mini)
to respond to buttons, tilts, shakes, light, and more. Display icons or short
animations or the LED display or play tunes through the built-in speaker.
This workshop will use MicroBlocks, a blocks language similar to Scratch.
It is suitable for beginners aged 10 and up working independently or
younger children working with a parent.
To participate, you will need a laptop computer (not a mobile device).

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [The MicroBlocks website](https://microblocks.fun)
- [The MicroBlocks Git repository](https://bitbucket.org/john_maloney/smallvm/)
- [Workshop Slides](https://docs.google.com/presentation/d/1CXvRXuMgvuCe3hUaG3_mW-s2qoJI-pwxQkjZgGHecaU)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7R77XR/feedback/)

---

### Snap!GPT: Exploring Generative AI Through Visual Programming

- **Speakers:** Jens Mönig, Jadga Huegle
- **Room:** UD6.205
- **Day:** Saturday
- **Time:** 14:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5333-snap-gpt-exploring-generative-ai-through-visual-programming/)

#### Abstract

How do AI language models work and just how intelligent are they? Can generative AI be original? Let’s find out together! We’ll program an algorithm that invents stories all by itself just like ChatGPT based on texts we train it on. But what happens when we train it on other media such as songs or drawings? Will it also learn how to make music and doodle sketches? We’ll use the Snap! visual programming language. Please bring a laptop or tablet with a web browser.

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MCRJCK/feedback/)

---

### Modsoup : Recipe and ingredients - Creating a modpack/gamepack for Luanti/Minetest

- **Speakers:** Thomas Francois, Lemente
- **Room:** UD6.203
- **Day:** Saturday
- **Time:** 14:00 - 15:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6279-modsoup-recipe-and-ingredients-creating-a-modpack-gamepack-for-luanti-minetest/)

#### Abstract

Participants will discover how to customize the game Minetest (Luanti Engine) to create their own gaming experiences from open source mods. (notions introduced: open source mods, dependencies, incompatibilities, debugging, …)
If we have the time and the public are up for it, we will briefly introduce modding in Lua, and leave the participants with the Luanti Modding Book link (https://rubenwardy.com/minetest_modding_book) if they want to go further.
Participants will need a laptop, preferably with Luanti already installed (https://www.luanti.org/downloads/)
It’s better to play with a mouse!
You can already explore available games and mods on https://content.luanti.org/

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HESMVD/feedback/)

---

### Physics count game using ZIM

- **Speakers:** Karel Rosseel
- **Room:** UD6.203
- **Day:** Saturday
- **Time:** 15:45 - 17:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4517-physics-count-game-using-zim/)

#### Abstract

With ZIMjs.com you can make elearning apps, zimjs.com/apps
Kids need to know Englisch because ZIM code need to be typed (not dragging blocks).
Kids use an online free editor ZIM SLATE
The framework ZIM uses CREATEJS.com (used by Adobe Animate).
ZIM now 10 years anniversity, started in 2014 by highschool teacher Dan Zen video who created ZIM KIDS where there are several levels of coding lessons free online with simple editor coding with shapes, if you want to use assets students(kids 8+) start coding textual games and apps in SLATE and can save the code online zapp.html file.
You will learn to make a ZIM APP (Zapp) with physics. 
for example to count with hitting a ball original example on ZIMjs.com/physics/keep up the ball in the air
* soccerball zapp with the ball, you can pause

Note: You can change your ball to whatever ZIM assets
and let it fall onto the ground or beach or waterwaves.
playbeachball physics drag and stop onto waterwaves example zapp  that opens in free online editor for kids  ZIMjs.org/KIDS/SLATE where you can copy the code to your own file.


Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9YJCKF/feedback/)

---

### The Magic of Making a Radio Remote Controller

- **Speakers:** Kathy Giori, John Maloney
- **Room:** UD6.205
- **Day:** Saturday
- **Time:** 15:45 - 17:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5811-the-magic-of-making-a-radio-remote-controller/)

#### Abstract

Participants will learn to remotely control robotic dogs, cars, LED displays, music making machines, and other fun gadgets using the magic of radio communications. MicroBlocks, a human-friendly programming environment, will be used to program education-friendly hardware such as the micro:bit board. As a radio remote controller, the micro:bit supports both simple radio broadcasts and paired Bluetooth Low-Energy (BLE) connections.
We will also have available the CoCube, a tiny cube robot that can sense its position and orientation while driving on a special mat. Thanks to the CoCube team, we should have enough CoCubes for all workshop participants. This workshop is recommended for those planning to take the more advanced "Learn to program tabletop football playing robots with MicroBlocks" on day 2.
Advanced users can further challenge themselves to leverage a starter app or create their own app on a smartphone or tablet that can control the micro:bit devices over BLE. Starter project tutorials will be available to make sure all participants can succeed!

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [MicroBlocks Website](https://microblocks.fun)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QTKW9F/feedback/)

---

### Creative with Coding

- **Speakers:** Pauline Maas
- **Room:** UD6.203
- **Day:** Sunday
- **Time:** 09:00 - 10:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5587-creative-with-coding/)

#### Abstract

Create your own drawing by using the online free turtlestitch. You can start off with an example or create your own drawing. When you're finished your drawing will be stitched on an embroidery machine and you can take it home.  https://www.turtlestitch.org/

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7NBSPF/feedback/)

---

### Make live music with MicroBlocks

- **Speakers:** Bernat Romagosa
- **Room:** UD6.205
- **Day:** Sunday
- **Time:** 09:00 - 10:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4305-make-live-music-with-microblocks/)

#### Abstract

Get ready to dance to the beat of the microcontroller! In this session you'll learn the basics of live music production with MicroBlocks and you'll be creating your own beats in no time.

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [The MicroBlocks website](https://microblocks.fun)
- [The MicroBlocks Git repository](https://bitbucket.org/john_maloney/smallvm/)
- [Live music with MIDI devices (activity)](https://learn.microblocks.fun/en/activities/MIDI-music-en/)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JQPL8M/feedback/)

---

### Create a Critter using TurtleStitch

- **Speakers:** Pauline Maas
- **Room:** UD6.203
- **Day:** Sunday
- **Time:** 10:45 - 12:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5609-create-a-critter-using-turtlestitch/)

#### Abstract

Create your own finger puppet using turtlestitch. Use turtlestitch to create the outline for your finger puppet. It’ll then be stitched by a digital embroidery machine onto two layers of felt, and you can then decorate it, adding eyes, hair, etc. Suitable for children aged 9 + 
https://www.turtlestitch.org
https://warwick.ac.uk/wmgoutreach/resources/turtlestitch/project_2._finger_puppet.pdf
@megjlow@fosstodon.org

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [TurtleStitch](https://www.turtlestitch.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NMSXC8/feedback/)

---

### Making Magic Mirrors

- **Speakers:** Jens Mönig, Jadga Huegle
- **Room:** UD6.205
- **Day:** Sunday
- **Time:** 10:45 - 12:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5334-making-magic-mirrors/)

#### Abstract

Did you ever ask yourself how the artists Paul Signac or Andy Warhol would see you? Are you curious about the secret behind your dog’s eyes? Do mirrors always tell the truth or can we tweak them to show us what we want to see? We will use the Snap! visual programming language to create video effects for our webcam. In doing so we’ll learn about the digital ingredients of live movies and images and how to compute them in real time. Please bring a laptop or tablet with a web browser and a webcam.

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with a webcam with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/783KBQ/feedback/)

---

### Music by Coding

- **Speakers:** Pauline Maas
- **Room:** UD6.203
- **Day:** Sunday
- **Time:** 12:30 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5590-music-by-coding/)

#### Abstract

Sonic Pi is a free code-based music creation and performance tool. It is Powerful for professional musicians and DJs, Expressive for composition and performance. It is also  accessible for blind and partially sighted people and is simple for computing and music lessons. Learn to code creatively by composing or performing music in an incredible range of styles from Classical & Jazz to Hip hop & EDM. Free for everyone with a friendly tutorial. https://sonic-pi.net/

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/M99CZP/feedback/)

---

### Physical Computing with MIT App Inventor

- **Speakers:** John Maloney, Evan Patton
- **Room:** UD6.205
- **Day:** Sunday
- **Time:** 12:30 - 14:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4857-physical-computing-with-mit-app-inventor/)

#### Abstract

Physical Computing with MIT App Inventor
MIT App Inventor is a blocks program language that makes it easy to
create apps for Android phones and tablets. In this hands-on workshop
you'll learn how to connect App Inventor to the physical world for
remote control or data collection. Control a robotic dog, monitor
an house plant, or collect data for a science experiment --
all these become easy.
Previous experience with a blocks language like Scratch is helpful but not required.
This workshop is aimed at teens and adults; younger children are welcome to work with a parent.
To participate, you will need both a laptop computer and an Android
phone or tablet.

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
Remember to bring an Android phone with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [MicroBlocks Website](https://microblocks.fun)
- [MIT App Inventor Website](https://appinventor.mit.edu/)
- [MicroBlocks App Inventor Extension](https://community.appinventor.mit.edu/t/microblocks-ble-extension/129412)
- [MicroBlocks App Inventor Extension Documenation](https://wiki.microblocks.fun/en/appinventor/ai2extension)
- [Workshop Slides](https://docs.google.com/presentation/d/1ZpvAz51hyoX43FUML3NMyLw5t3LEQ2HCri83CpkiXZ0)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YQDZ9V/feedback/)

---

### Learn to program tabletop football playing robots

- **Speakers:** Shuai Liang, Jialing Han
- **Room:** UD6.205
- **Day:** Sunday
- **Time:** 14:15 - 15:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4696-learn-to-program-tabletop-football-playing-robots/)

#### Abstract

In this introductory, hands-on workshop you will learn how to program a tabletop soccer football playing robot using MicroBlocks, a blocks language similar to Scratch.
You will learn how to retrieve the robot's position and orientation in real time using MicroBlocks, how to move the robot to a specified location, how to control the servo to pick up the soccer ball, and ultimately complete the tabletop football playing robot task.

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RLKZDU/feedback/)

---

### Make Your Own Embroidered Bookmark

- **Speakers:** Joek van Montfort
- **Room:** UD6.203
- **Day:** Sunday
- **Time:** 14:15 - 15:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6025-make-your-own-embroidered-bookmark/)

#### Abstract

Turtlestitch (https://turtlestitch.org) is a Scratch like environment that let you tinker with Turtle art. Once you like the drawing on screen you export it as a file that will instruct an embroidery machine to stitch it. Making a personal bookmark is another hook to get people interested in coding and generative art.

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7MWBMV/feedback/)

---

### Learn Python programming using Hedy

- **Speakers:** Jesús Pelay, Pink van de Hel, Annelies Vlaar
- **Room:** UD6.203
- **Day:** Sunday
- **Time:** 16:00 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6666-learn-python-programming-using-hedy/)

#### Abstract

Hedy is a programming language that aims to teach textual programming to kids. Hedy's unique approach involves gradual changes in the  syntax of the programming language, so students are not overloaded with information right away. This devroom is aimed at students from 9 to 12 years old, but anyone with a desire to start learning programming (or teaching) with text based language is welcome. You'll need your own laptop (no installs needed, Hedy is webbased) and reading- and basic typing skills (or someone to help you read and type). No prior programming experience is needed. When you have finished all 18 levels of Hedy, you know the basics of Python.

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/H79NY3/feedback/)

---

### Creative Data Visualization in Snap!

- **Speakers:** Bernat Romagosa, Jens Mönig, Jadga Huegle
- **Room:** UD6.205
- **Day:** Sunday
- **Time:** 16:00 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6658-creative-data-visualization-in-snap-/)

#### Abstract

Data is called the oil of the 21st century. Equally important as the actual data is the way of analysing, summarising and visualising it in an understandable way. In this workshop, we want to look at different (famous) visualisations of ecological and societal data and reprogram them in Snap! Join us to see glacier melting, animal biodiversity loss and societal developments.
Please bring a laptop with a web browser.

Activities during FOSDEM Junior follow the Code Club policies and health and safety standards. 

All attendees must have an adult with them
Remember to bring your laptop with you
You must book a place to attend
Please don’t come if you are feeling unwell

Participants are required to sign up for this activity via the registration form.

#### Related Links

- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TLXUF7/feedback/)

---

## FOSS on Mobile Devices (11)

### Mainline vs libhybris: Technicalities, down to the buffer

- **Speakers:** Alfred Neumayer
- **Room:** H.2214
- **Day:** Saturday
- **Time:** 14:55 - 15:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4917-mainline-vs-libhybris-technicalities-down-to-the-buffer/)

#### Abstract

This is not on behalf of a specific community, only my direct experience with Ubuntu Touch, libhybris and Halium.
SailfishOS, Ubuntu Touch, Droidian. Many options exist for running a GNU/Linux environment on  an off-the-shelf mobile phone. But what makes these different from an application developer’s perspective for a smartphone OS built with libhybris drivers?
Let’s find out.

#### Related Links

- [libhybris](https://github.com/libhybris/libhybris)
- [GBM for libhybris brainstorming](https://github.com/libhybris/libhybris/issues/570)
- [Halium](https://github.com/Halium)
- [Halium QSG context](https://github.com/Halium/haliumqsgcontext)
- [Google's own info about gralloc](https://source.android.com/docs/core/graphics/arch-bq-gralloc)
- [Qt WebRTC demo app](https://github.com/fredldotme/webrtcdemo)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mobile:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mobile:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7KSSVY/feedback/)

---

### Kernel support for Mobile Linux: The missing 20%

- **Speakers:** Luca Weiss
- **Room:** H.2214
- **Day:** Saturday
- **Time:** 15:20 - 15:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4836-kernel-support-for-mobile-linux-the-missing-20-/)

#### Abstract

Supporting modern smartphones on mainline Linux is getting easier by the year; it's now possible to get a lot of hardware working with fairly minimal effort or issues.
But what do we do for the parts which are not easy, the bits where you as a developer get stuck?
Users of mobile phones expect everything to work, but the closer we get to that the more issues become apparent which are not just missing feature bringup.
We've managed to get 80% of the way, so let's talk about what's missing to get the remaining 20% to work and actually make phones mostly feature complete from a kernel perspective.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mobile:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mobile:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DNRQUP/feedback/)

---

### Weather and emergency alerts

- **Speakers:** Volker Krause, Nucleus
- **Room:** H.2214
- **Day:** Saturday
- **Time:** 15:45 - 16:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5102-weather-and-emergency-alerts/)

#### Abstract

Being able to receive weather and public emergency warnings can save lives, and we don't want people using FOSS to be at a disadvantage compared to proprietary platforms when it comes to that.
Cell broadcast covers some of this, but it's only part of the puzzle. It's typically only used for the most severe and urgent cases, is limited in the amount of data it can transmit, and doesn't allow monitoring of other areas. Public alerting is, therefore, often augmented by additional channels, including mobile apps. Despite being funded by public money, those are usually limited to proprietary platforms. So, as usual, we have to build this ourselves.
The foundation for this is OASIS' Common Alerting Protocol (CAP), which has been in widespread use for many years all over the world, and UnifiedPush as a free alternative for proprietary push notifications. On top of that, we currently have an aggregation server for alerts from about 100 countries, which notifies clients about incidents in their respective areas of interest.
In this talk, we'll show how this works and how alerts can be integrated into applications.

#### Related Links

- [FOSS Public Alert Server sourcecode](https://invent.kde.org/webapps/foss-public-alert-server)
- [FOSSWarn sourcecode](https://github.com/nucleus-ffm/foss_warn)
- [Join our Matrix space](https://matrix.to/#/#foss_warn:tchncs.de)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mobile:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mobile:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XMRJZY/feedback/)

---

### Bringing Oniro to Mobile: Challenges in Hardware Enablement

- **Speakers:** Francesco Pham
- **Room:** H.2214
- **Day:** Saturday
- **Time:** 16:10 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4684-bringing-oniro-to-mobile-challenges-in-hardware-enablement/)

#### Abstract

The Oniro Project, an open-source operating system built upon OpenHarmony and tailored for European market needs, is expanding its ecosystem to include mobile devices. In this lightning talk, we will discuss the ongoing effort to bring Oniro to the Volla X23 smartphone, focusing on the technical challenges and solutions in adapting Android drivers to a musl libc-based platform.
We will explore the role of libhybris in enabling compatibility with proprietary Android drivers, a critical step in hardware enablement for Oniro on mobile devices. The presentation will highlight how libhybris bridges the gap between the Bionic and musl libc environments, allowing us to leverage GPU acceleration and other hardware features while maintaining an open-source user space. Key challenges, such as adapting Android’s graphics stack and addressing ABI compatibility issues, will be outlined, along with our current progress in running Oniro in an LXC container for rapid testing.
This talk will provide insights into the broader implications of this work for the FOSS on Mobile ecosystem, offering a pathway to more accessible open-source mobile platforms. Join us to learn how Oniro aims to contribute to the vision of a truly open mobile ecosystem.

#### Related Links

- [Oniro Project](https://oniroproject.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mobile:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mobile:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NZYBFH/feedback/)

---

### Sxmo: A mobile UI for hackers

- **Speakers:** Maarten van Gompel (proycon)
- **Room:** H.2214
- **Day:** Saturday
- **Time:** 16:20 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5926-sxmo-a-mobile-ui-for-hackers/)

#### Abstract

In this talk we briefly present Sxmo and share the current state of
things. Sxmo is a hacker-friendly mobile UI for Linux phones, like those
running on postmarketOS. Our approach differs from what the
mobile user is accustomed too, but one that will appeal to those drawn to
software minimalism and those with an urge to tweak and control their system to
the max! We tie together various FOSS components, some interchangeable, via
POSIX shell scripts. Through our hook system users can customize these to a
large extent.

Do you want to SSH into your phone and have all functionality available remotely?
Do you like the idea of running a tiling window manager (sway, dwm) on your phone just like on your desktop?
Do feel nostalgia for operating your phone with menus (dmenu, bemenu, wofi) and hardware buttons?
Do you want to be the one in control of our own device and data, rather than be on the leash of big tech companies?

Then this talk may be interesting for you!

#### Related Links

- [Project website](https://sxmo.org)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mobile:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mobile:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SZ97BD/feedback/)

---

### Mirror Hall: Building virtual network displays to bridge mobile and desktop

- **Speakers:** Raffaele Tranquillini
- **Room:** H.2214
- **Day:** Saturday
- **Time:** 16:35 - 16:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4527-mirror-hall-building-virtual-network-displays-to-bridge-mobile-and-desktop/)

#### Abstract

Wireless displays are something most of us use, but in a fragmented and proprietary landscape. We propose a new approach to virtual screen sharing between Linux mobile and desktop devices.
This solution uses a combination of video pipelines optimized for ARM and x86 hardware, D-Bus, and low-latency UDP streaming to create virtual “second monitors” and stream the desktop between peer devices. It is optimized to be usable even on low-power hardware such as the Librem 5, allowing us to repurpose older devices as secondary network monitors without proprietary tools. [2]
In this talk, I will try to demystify some of the technicalities required for implementing efficient wireless desktop streaming using GStreamer, PipeWire, and D-Bus. To this end, we will explore how to build network video pipelines from scratch, with a focus on minimizing latency and making good use of hardware acceleration. Finally, we will present the Mirror Hall app, an experimental GTK4 app that encapsulates the above concepts. [2]
Links: 
1. https://notes.nokun.eu/post/2024-09-22-mirrorhall/
2. https://gitlab.com/nokun/mirrorhall

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mobile:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mobile:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RDVDBV/feedback/)

---

### OpenAGPS - Open source GNSS Assistance

- **Speakers:** Alexander Richards
- **Room:** H.2214
- **Day:** Saturday
- **Time:** 17:00 - 17:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6739-openagps-open-source-gnss-assistance/)

#### Abstract

Most, if not all, mobile devices have a GPS receiver in them, and most, if not all of them, support A-GPS. A-GPS as a technology is not designed with privacy in mind (in fact, it is specifically designed to not be private, as it sends the phones' IMSI to the A-GPS server), and one of the few providers of A-GPS services is Google. There exists, at present, no open source, privacy-respecting A-GPS service; mostly impacting FOSS on Mobile projects, such as Ubuntu Touch, who do not wish to use this Google service (and may not be allowed to either, as Google only officially provides SUPL services for Android devices, as far as I understand)
The OpenAGPS project aims to create a open-source A-GPS / SUPL (Secure User Plane Positioning) service. GNSS systems (such as GPS) are both surprisingly simple and complicated; the talk would provide a short overview into the functioning of a GNSS system, how assisted GNSS / A-GPS / SUPL works, how a privacy-respecting system could be built, and the current state of the OpenAGPS project.
This project has also received a grant from NLNet (Mobifree call) very recently; at the time of this submission we do not have any fully functioning code/codebase, although we hope to get a working prototype of the system in time for it to be potentially showed off as a working demo at FOSDEM.
Website (slight update: placeholder has been replaced with a blog, although it's still not got too much yet): https://openagps.net/
Source: https://gitlab.com/openagps/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mobile:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mobile:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/J3N3YA/feedback/)

---

### Mobile Browsers: the Best of Times, the Worst of Times

- **Speakers:** David Llewellyn-Jones
- **Room:** H.2214
- **Day:** Saturday
- **Time:** 17:25 - 17:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6411-mobile-browsers-the-best-of-times-the-worst-of-times/)

#### Abstract

Arguably the single most important piece of software on any mobile phone is its Web browser. This is especially true on alternative mobile platforms where Web apps are often the best or only way to access essential services and functionality.
While mobile apps are increasingly targeted at just the dominant platforms, they are also increasingly built using Web technologies, making them accessible to any platform with a decent browser. The result is that Linux-based mobile platforms beyond Android and iOS have the potential to be more viable than ever before.
But the embedded browser landscape is in continual flux, with multiple offerings built on different technologies, including Blink, V8, WebKit, JavaScriptCore, Gecko, SpiderMonkey and Servo Layout. On top of these are frameworks intended to make their use more accessible to embedded systems. These include the Chromium Embedded Framework, Web Platform for Embedded, Qt WebEngine and Gecko WebView.
In this talk I'll look at the different offerings available and consider their appropriateness for mobile Linux. What features do they offer, how practical is their use and why should you choose one over another? In particular I'll look at the minimal API needed for any practical implementation, how the APIs differ across the offerings and how they can be made use of as embedded browsers in mobile applications.
To give a more complete understanding of what embedded browsers are like to use in practice, the talk will include example applications with demonstration code.

#### Related Links

- [Gecko WebView](https://github.com/sailfishos/sailfish-browser)
- [Chromium Embedded Framework](https://bitbucket.org/chromiumembedded/cef/)
- [Qt WebEngine](https://wiki.qt.io/QtWebEngine)
- [Web Platform for Embedded](https://wpewebkit.org/)
- [Slides (PDF)](https://www.flypig.co.uk/presentations/fosdem25-mobile-browsers.pdf)
- [Slides (source)](https://codeberg.org/flypig/fosdem25-mobile-browsers.git)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mobile:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mobile:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3A7FHT/feedback/)

---

### libobscura: Cameras are STILL difficult

- **Speakers:** dcz
- **Room:** H.2214
- **Day:** Saturday
- **Time:** 17:50 - 18:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6184-libobscura-cameras-are-still-difficult/)

#### Abstract

The libobscura experiment exists to find out what a point-and-shoot API 
abstracting Video4Linux should look like. It has its roots on one hand in the  
Librem 5 project, where I wrote some 70% of the camera stack, and on the other 
hand in libcamera, which I found too difficult to use.
You think controlling a modern camera is easy? Think again. Between pixel 
formats, depths, media entities, pads and links, sensitivity, denoising, phase 
detection, shutter lengths, DMAbuf, OpenGL, feedback loops, requests, and 
statistics, there's enough opportunities to get lost in the detail.
Thankfully, Prototype Fund thinks I'm up for the challenge, so they are funding
me through libobscura in order to get lost, and maybe find something in the 
process.
Apart from showing the general problems of camera support, I'll tell about new 
problems since CCC. 
Project repo: https://codeberg.org/libobscura/libobscura

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mobile:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mobile:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EAH37V/feedback/)

---

### phosh: Yet another year around the sun!

- **Speakers:** Evangelos Ribeiro Tzaras
- **Room:** H.2214
- **Day:** Saturday
- **Time:** 18:15 - 18:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6323-phosh-yet-another-year-around-the-sun-/)

#### Abstract

phosh is a graphical shell for mobile devices built using GNOME technologies.
With more than 80 releases in about 6 years under it's belt
it is both time to celebrate and glimpse into what the future will bring!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mobile:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mobile:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3VTCVX/feedback/)

---

### postmarketOS: what is it and what's new?

- **Speakers:** Oliver Smith
- **Room:** H.2214
- **Day:** Saturday
- **Time:** 18:40 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4654-postmarketos-what-is-it-and-what-s-new-/)

#### Abstract

A quick introduction to postmarketOS (Linux Mobile distro based on Alpine that has been ported to lots of devices by now!), as well as an overview of cool things we did throughout the last year or so. Also what we are up to :>
Source code: https://postmarketos.org/source-code/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-mobile:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-mobile:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NYJTD9/feedback/)

---

## Free Java (17)

### The State of OpenJDK

- **Speakers:** Mark Reinhold
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 10:30 - 10:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5281-the-state-of-openjdk/)

#### Abstract

A review of the past year in the life of the OpenJDK Community, and a look at what’s ahead.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GRDJPZ/feedback/)

---

### ZGC: Paving the GC On-Ramp

- **Speakers:** Stefan Johansson
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 11:00 - 11:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6497-zgc-paving-the-gc-on-ramp/)

#### Abstract

ZGC is a powerful garbage collector. This talk showcases what we are doing to reduce the amount of configuration needed to use it well, so that power can be unleashed with a minimum effort for the user.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/C7KKXB/feedback/)

---

### Generational Shenandoah Update: Relevance and Best Practice Recommendations

- **Speakers:** Kelvin Nilsen
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 11:30 - 11:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5730-generational-shenandoah-update-relevance-and-best-practice-recommendations/)

#### Abstract

Generational mode of Shenandoah is a new experimental feature that has been added to JDK24.  The generational mode preserves pause-less operation of traditional Shenandoah, while decreasing CPU time consumed by GC and allowing higher allocation rates without degenerated cycles in the same heap sizes.  For many workloads, this allows robust deployment in smaller heap sizes.
This talk provides selected performance comparisons with traditional Shenandoah, Generational ZGC, and G1 GC. It provides selection criteria for helping to determine whether Generational mode of Shenandoah is a good match for your service needs.  It also provides best-practice recommendations for how to tune Generational Shenandoah to extract the greatest value for your particular service.

#### Related Links

- [The repo under which GenShen was developed](https://github.com/openjdk/shenandoah)
- [The integration PR: GenShen is now part of JDK24](https://github.com/openjdk/jdk/pull/21273)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7V7JNS/feedback/)

---

### Project Lilliput - Looking Back and Ahead

- **Speakers:** Roman Kennke
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 12:00 - 12:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5526-project-lilliput-looking-back-and-ahead/)

#### Abstract

After 3 years of development, Project Lilliput, also known as 'Compact Object Headers' is going to ship JEP 450 in JDK24. We want to celebrate that by looking back at how we got here and talk about what Java users can expect from it. We also talk about why we are not done, yet, how all Java users are going to benefit from 'Lilliput 2' and what it takes to get there.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3AZVCR/feedback/)

---

### (Almost) everything I knew about Java performance was wrong

- **Speakers:** Andrew Haley
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 12:30 - 12:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4987--almost-everything-i-knew-about-java-performance-was-wrong/)

#### Abstract

Much of the advice given to Java programmers seeking efficiency is
misleading or out of date.
This talk is a result of the author's experience trying making the
Java Virtual Machine more efficient, but it isn't just for JVM
engineers, it is also relevant to Java programmers. We will cover
wide-issue processors, branch and memory-access prediction, and the
way Java programmers can use tools to illuminate what is really going
on inside a computer when it runs their programs.
If you're looking for a talk about huge memories or millions of threads,
this isn't it. Rather, it's about how small details can have surprising
effects.
Mechanical Sympathy is when you use a tool or system with an
understanding of how it operates best. "You don't have to be an
engineer to be be a racing driver, but you do have to have Mechanical
Sympathy."
Project: https://github.com/openjdk/jdk

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FE39MC/feedback/)

---

### Monitoring Security Operations with JDK Flight Recorder Events

- **Speakers:** Seán Coffey
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 13:00 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5261-monitoring-security-operations-with-jdk-flight-recorder-events/)

#### Abstract

Java Flight Recorder (JFR) provides deep visibility into cryptographic operations offering developers unprecedented insights into their applications' security behavior. Learn how to leverage these JFR events to monitor and analyze cryptographic operations in production Java applications with minimal overhead.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GQ8NAW/feedback/)

---

### Quo Vadis, class space? A look at class metadata storage in the Hotspot JVM

- **Speakers:** Thomas Stüfe
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 13:30 - 13:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5186-quo-vadis-class-space-a-look-at-class-metadata-storage-in-the-hotspot-jvm/)

#### Abstract

This talk looks deeper at class metadata storage in the Hotspot JVM and the changes JEP 450 "Compact Object Headers" brought. We will examine the mechanics and CPU cache effects of oop iteration and propose a more cache-friendly solution. We will investigate the class storage limits and possible ways to circumvent them. Finally, we will examine an alternative to the current class space solution.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/F8NLXS/feedback/)

---

### Native memory tracking for all - Extending NMT beyond Hotspot

- **Speakers:** Johan Sjölén
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 14:00 - 14:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5641-native-memory-tracking-for-all-extending-nmt-beyond-hotspot/)

#### Abstract

Native Memory Tracking (NMT) has supported diagnosing memory issues in Hotspot for over a decade. Yet, much of the native memory allocated cannot be accounted for using NMT, as it is not only Hotspot but core libraries, JNI and FFM which may perform native allocations. Clearly, NMT must extend itself if it intends to remain a useful tool.
In this talk, I will present a design for extending NMT to core libraries and a possible future extension to FFM. External APIs will be shown in the context of porting small portions of the core libraries. Internal design details, including data structure design, will likewise be presented and its trade offs discussed. Finally, possible ways of bringing NMT and the new Foreign Function & Memory API will be presented.

#### Related Links

- [OpenJDK main repository](https://github.com/openjdk/jdk)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YM98HE/feedback/)

---

### Reduce the size of your Java run-time image

- **Speakers:** Severin Gehwolf
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 14:30 - 14:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4511-reduce-the-size-of-your-java-run-time-image/)

#### Abstract

When it comes to the on-disk-size of your OpenJDK installation it becomes apparent
that certain files take up a large part of the entire Java Development Kit (JDK) installation.
It can seem that certain files are monolithic and aren't possible to make smaller.
Yet, they can be smaller if you know how.
In this talk we show how you can create a custom run-time image for your
specific application without the need of the jmods folder otherwise being
present in a standard JDK. Forget about JRE and go all-in on custom run-time
images. The best thing about it is that - due to JEP 493 - this will no longer
need JMOD files of the JDK to be present.
Tune in to hear more about using jlink from a JDK without a jmods directory
and what new opportunities this allows.

#### Related Links

- [Link to OpenJDK - the reference implementation of Java SE](https://openjdk.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/K8NX3E/feedback/)

---

### InvokeDynamic in Practice with JRuby

- **Speakers:** Charles Nutter
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 15:00 - 15:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6038-invokedynamic-in-practice-with-jruby/)

#### Abstract

JRuby has been one of the largest consumers of invokeddynamic and method handles since they were introduced in Java 7. With the release of JRuby 10, we have upgraded our minimum Java to 21, and implemented many new optimizations. This talk will survey how JRuby uses invoke dynamic to compile and optimize Ruby code on the JVM.

#### Related Links

- [JRuby repository](https://github.com/jruby/jruby)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KSVAQ9/feedback/)

---

### Inner Workings of the FFI API in the JVM

- **Speakers:** Martin Doerr
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 15:30 - 15:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5647-inner-workings-of-the-ffi-api-in-the-jvm/)

#### Abstract

The Foreign Function & Memory API (JEP 454) introduced a new way of interacting with libraries written in other languages. It can be used as replacement for JNI.
This talk examines the inner workings of the Foreign Function Interface (FFI) API. After having it implemented for PowerPC, I'd like to discuss how the JVM handles native function calls and Java callbacks, focusing on key concepts like stack layouts, calling conventions, and cross-platform challenges.
The session is intended for developers curious about the technical foundations of free and open Java technologies and how JVM enhancements like the FFI API are realized. It will shed light on the low-level mechanisms that enable seamless integration of Java with native code while maintaining the performance and safety Java developers expect.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8SDEYY/feedback/)

---

### Foreign Function and Memory APIs and Swift/Java interoperability

- **Speakers:** Konrad 'ktoso' Malawski
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 16:00 - 16:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4886-foreign-function-and-memory-apis-and-swift-java-interoperability/)

#### Abstract

Swift is a fantastic general purpose language, which can and has been successfully used beyond its mobile origins, from embedded through server-side systems. One of Swift’s unique strengths is its powerful native language interoperability with C and C++. Recently, the Swift project started work on integrating improved Swift/Java interoperability  with the use of both JNI and the new Foreign Function and Memory APIs introduced in JDK22. In this talk we’ll deep dive into the deep integration approach taken between the language runtimes using the FMM APIs and their unique strengths but also challenges.

#### Related Links

- [Swift's Swift-Java interop project](https://github.com/swiftlang/swift-java)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FCUUNN/feedback/)

---

### Project Leyden - Past and the Future

- **Speakers:** Ashutosh Mehra
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 16:30 - 16:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5469-project-leyden-past-and-the-future/)

#### Abstract

Project Leyden was created in May 2022 with the goal of improving
footprint, startup time and time to peak performance of Java
applications. Initially, a variety of different approaches were under
consideration and the first proposed solutions only started to
clarify around 18 months ago. An early preview of the 'premain'
solution, prototyped by Oracle, was presented at the August 2023 JVM
Language Summit. It has been under very active development since then,
with a team that includes developers from Oracle, Red Hat, Microsoft,
Amazon and Google, and has already delivered improvements to JDK and
application startup time in OpenJDK 24 via JEP 483. The plan is for the
project to deliver a series of JEPs that improve performance
step by step rather than wait for a complete, shrink-wrapped solution
and the Leyden team is already working on the next set of enhancements.
In this talk we will explain what was delivered in JEP 483 and how it
works to improve startup, then go on to describe what other features are
in the pipeline. We will also touch upon some of the barriers we
currently face to improving performance and ideas we are exploring to
resolve them.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AUQKVT/feedback/)

---

### Valhalla Stage 2 - Nullness Emotion

- **Speakers:** Rémi Forax
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 17:00 - 17:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5957-valhalla-stage-2-nullness-emotion/)

#### Abstract

The first stage of Valhalla (https://openjdk.org/projects/valhalla/) is almost ready, soon we will release the first stage of the rocket, the ability to declare a class as a value class. A value class object is like a cheap box that is able to solarise itself on stack, avoiding the traditional boxing cost. The next phase is to allow to flatten value class into fields, but for that we need to get ride of null as a possible value.
This talk is about the challenges to introduce nullness emotion ('?' Or '!') to the Java type system.
Sadly, if you hope that Java can be turned into Kotlin, you will be disappointed.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZX7MVV/feedback/)

---

### Advancing Java Profiling: Achieving Precision and Stability with JFR , eBPF and user context

- **Speakers:** Johannes Bechberger, Jaroslav Bachorik
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 17:30 - 17:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4848-advancing-java-profiling-achieving-precision-and-stability-with-jfr-ebpf-and-user-context/)

#### Abstract

Java developers struggle with the trade-off between precise profiling and application stability.
Unofficial methods like AsyncGetCallTrace offer precision but risk crashes, while official APIs such as JVMTI, JMX, and StackWalker are stable but biased due to safepoint polling. Java Flight Recorder (JFR) reduces this bias but introduces interpolation errors.
This talk addresses these challenges with three key topics:
• Combining precise sampling with JFR’s stability to remove biases without sacrificing reliability.
• Using eBPF probes and examining JVM internals for safer, detailed profiling.
• Enhancing precision with user-supplied profiling contexts.
We will review the history of Java profilers and discuss the future of JVM profiling, with a focus on CPU profiling. Attendees will gain insights into new methods aimed at achieving accurate, stable performance analysis in Java applications, comparing them with async-profiler and existing tools.

#### Related Links

- [Datadog Java Profiler](https://github.com/DataDog/java-profiler)
- [Datadog Java Tracer](https://github.com/DataDog/dd-trace-java)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WT8BHQ/feedback/)

---

### Unpick performance mysteries benchmarking GraalVM native executables

- **Speakers:** Galder Zamarreño
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 18:00 - 18:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5335-unpick-performance-mysteries-benchmarking-graalvm-native-executables/)

#### Abstract

Java code that is ahead-of-time (AOT) compiled using GraalVM Community Edition native-image may run more slowly than code that is just-in-time (JIT) compiled with the HotSpot compiler. This is something I quickly discovered when I joined the GraalVM team at Red Hat. 
Diagnosing performance issues in Java code can be done using Java Microbenchmark Harness (JMH), which helps developers build, run and analyse microbenchmarks written in Java. However, it only works with Java virtual machines using JIT compilation. For the past four years I’ve been wondering how to make JMH achieve the same objectives when that Java code runs as GraalVM native executables.
Eventually I solved this problem creating an extension to JMH that allows Java developers to seamlessly run their existing JMH benchmarks as GraalVM native executables. In this talk I will demonstrate how to obtain benchmark results, gather performance statistics and inspect annotated assembly code. Finally I will compare how the GraalVM native-image AOT code differs from the JIT code of HotSpot.

#### Related Links

- [JMH extension git repository](https://github.com/galderz/fibula)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9VHLEZ/feedback/)

---

### Understanding the GraalVM Native Image Build Process

- **Speakers:** Tom Shull
- **Room:** UD2.208 (Decroly)
- **Day:** Saturday
- **Time:** 18:30 - 18:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5511-understanding-the-graalvm-native-image-build-process/)

#### Abstract

GraalVM Native Image is a popular tool for building standalone executables from Java applications. It is able to generate executables with fast startup time and low memory footprint through the use of a closed world assumption, constraints on dynamism, and many traditional compiler optimizations.
Unfortunately, Native Image's many advanced features can make its build process inscrutable to an inexperienced developer. It is hard to decipher how its many internal components (e.g. analysis, compiler phases, plugins, intrinsics, features, singletons, substitutions, etc.) work in concert and what assumptions must not be violated.
In this talk I will attempt to help make sense of the Native Image build process. I will first describe what components exist and how they interact with each other. Next, I will walk through a native image build and highlight key phases of the process. Finally, I will provide some practical tips to follow when trying to learn more about specific functionality within Native Image.

#### Related Links

- [GraalVM Repository](https://github.com/oracle/graal)
- [GraalVM Website](https://www.graalvm.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-free-java:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-free-java:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PTFJNH/feedback/)

---

## Funding the FOSS Ecosystem (12)

### What do maintainers need from funders and others? We asked Maintainers to find out.

- **Speakers:** Georg Link, Johan Linåker, Kevin Lumbard
- **Room:** K.3.601
- **Day:** Sunday
- **Time:** 09:10 - 09:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5680-what-do-maintainers-need-from-funders-and-others-we-asked-maintainers-to-find-out-/)

#### Abstract

Funding is an important but not the only piece to sustaining open source. Let’s step back and ask maintainers: What do open source communities need to be sustainable? This talk will share what we learned from interviewing maintainers and the insights we published in our peer-reviewed academic study (Reference: https://dl.acm.org/doi/10.1145/3674805.3686667).
Why this matters: It is difficult to know how to support the required maintenance labor for sustainable OSS. Microsoft recently expressed this idea, writing, “It would have been wonderful to see financial goals of maintainers on their sponsor's pages, as well as other types of sustainability ‘asks.’” They wanted this feedback to better assess who to give money to and how much.
As part of this talk, the audience will be invited into a conversation about the support that maintainers need. We want to encourage maintainers to articulate their needs and supporters to ask the right questions. We hope that this talk will contribute to sustainable open source by improving how we ask about project needs from a maintainer perspective.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-funding:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-funding:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RWRFSN/feedback/)

---

### Building Sustainability: A Case Study in Funding Diversification for Decidim

- **Speakers:** Nil Homedes
- **Room:** K.3.601
- **Day:** Sunday
- **Time:** 09:50 - 10:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5552-building-sustainability-a-case-study-in-funding-diversification-for-decidim/)

#### Abstract

Since its inception, Decidim has relied primarily on funding from the city of Barcelona, creating a dependency on this public organization. In 2022, following a funding crisis that nearly jeopardized the project, we developed a Sustainability Plan aimed at diversifying funding sources and reducing our dependence on a single funder.
A year and a half after implementing the plan, we have made significant progress toward our goal.
This session will reflect on our approach and key learnings. We will explain how we designed this plan, the challenges for sustainability that a FLOSS project faces, the learnings we have made during the process and the main actions we have taken
We will delve into the different strategies we have designed to attract new funders, especially from the private and philanthropic sector, as well as the challenges we face when it comes to receiving funding from public agencies. Finally, we will evaluate the successes and failures of this plan.
This is an ideal talk if you are interested in knowing the challenges that FLOSS projects face when seeking funding, want to learn which are the best strategies to diversify your sources of income and ensure a sustainable growth of your project.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-funding:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-funding:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ET9PKZ/feedback/)

---

### 20 Years of Hacking the Funding of XWiki and CryptPad

- **Speakers:** Ludovic Dubost
- **Room:** K.3.601
- **Day:** Sunday
- **Time:** 10:30 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4601-20-years-of-hacking-the-funding-of-xwiki-and-cryptpad/)

#### Abstract

Competing to propose Open Source Collaboration solutions against multi-billion companies is a challenging endeavor. But it's not a technical one. While your users will demoralize you showing you all what you miss compared to your proprietary competitors having deep pockets to fund their R&D, you'll think that Open Source software is just not good enough.
But the real issue is not technical, it's economical and financial. Over the 20 years of XWiki and CryptPad, we have been able to measure what we miss for Open Source to be able to provide end user applications respecting user's Freedom and Privacy.
We have also been able to see how the changes of price of competitors have brought us more customers allowing us to increase the funding of our own software.
The challenge is a financial challenge, a business model challenge. In this talk we will show how we manage to hack our funding throughout the years and find ways to progressively improve our software, gaining status year by year and then allowing to increase customer revenue.
We will also present our belief that in order for Open Source to strive, the community needs to solve the financial challenge and also chip in. We'll present our FOSS Fund, which is our own way to give back to other Open Source projects that we use at XWiki SAS.

#### Related Links

- [XWiki](https://www.xwiki.org)
- [CryptPad](https://cryptpad.org)
- [XWiki Repository](https://github.com/xwiki/xwiki-platform/)
- [CryptPad repository](https://github.com/cryptpad/cryptpad/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-funding:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-funding:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FYDFDC/feedback/)

---

### Why and How Companies Should Pay Open Source Maintainers

- **Speakers:** Vlad-Stefan Harbuz
- **Room:** K.3.601
- **Day:** Sunday
- **Time:** 11:10 - 11:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4149-why-and-how-companies-should-pay-open-source-maintainers/)

#### Abstract

In this talk, I present some economical arguments for why companies should pay the Open Source maintainers they depend on, and I suggest some technological solutions for how this might be accomplished.
Virtually all companies use Open Source software, making a critical subset of the Open Source ecosystem crucial for everything from watching YouTube videos to working with medical records. But the companies that use Open Source software rarely pay the maintainers of the software they depend on. I explain that this can lead to serious issues in the Open Source ecosystem, such as the international security risks we saw with the XZ backdoor and the Log4Shell vulnerability.
I explain that, if companies paid the Open Source maintainers they depend on, the Open Source ecosystem would become more sustainable and stable while retaining the significant economical advantages provided by Open Source governance models, and companies would benefit from this.
Next, I want to talk about how to actually pay maintainers. Forward-thinking companies have, in fact, shown their willingness to fund the Open Source software they depend on. But it is not always trivial to figure out which Open Source maintainers a large codebase depends on, and how to actually pay those maintainers.
At thanks.dev, we have created a platform that scans companies' codebases to identify the Open Source maintainers whose projects these codebases depend on. We then give companies an easy and financially transparent way to pay these maintainers.
But dependencies often form a complex tree, and it is not immediately clear how much money should go to each dependency's maintainer. Current methods, though helpful, are simplistic. I introduce a new algorithmic technique for fund allocation, which uses a combination of coupling and complexity metrics to calculate which dependencies are most critical to a certain project. Using this method can provide a better allocation of funds.
I am keen to hear the community's feedback on both my economical and my technological suggestions, and to further develop solutions together.

#### Related Links

- [Vlad's work — vlad.website](https://vlad.website)
- [thanks.dev](https://thanks.dev)
- [Open Source Pledge](https://opensourcepledge.com)
- [Slides (Google Slides)](https://docs.google.com/presentation/d/13m81TYYOplfHT2HzAoh6EcFFqEZILje2VZklgw4eueo/edit?usp=sharing)
- [Slides (PDF)](https://vlad.website/static/why-and-how-companies-should-pay-open-source-maintainers.pdf)
- [Mailing list to discuss this talk and Open Source sustainability generally](https://vlad.website/why-and-how-companies-should-pay-open-source-maintainers/#join-the-conversation)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-funding:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-funding:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8JK38S/feedback/)

---

### Funding the FOSS Ecosystem

- **Speakers:** Emmy Tsang
- **Room:** K.3.601
- **Day:** Sunday
- **Time:** 11:50 - 12:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6397-funding-the-foss-ecosystem/)

#### Abstract

Open scholarly infrastructures — open-source systems and solutions supporting the discovery and sharing of research — are pivotal in ensuring access to knowledge and fostering innovation. In 2024, Invest in Open Infrastructure (IOI) mapped and analysed over $415M in grant funding for open infrastructure to uncover key trends and opportunities with the aim of driving more informed, strategic, and coordinated investment towards a healthy and resilient ecosystem of open infrastructure. The analysis shows a significant number of grant awards reference the use of open infrastructure but do not directly support their development. Further, while a substantial portion of grant funding supports research and development work of open infrastructures, a significant need for sustained operational support remains largely unaddressed. This presentation will highlight these funding trends and discuss their implications for the sustainability of open infrastructure. We will also discuss potential strategies to catalyze investments from a more diverse pool of stakeholders to foster a more robust funding ecosystem for open infrastructure.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-funding:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-funding:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YWS3D9/feedback/)

---

### Storytelling, networking, and strategy: three keys to successful fundraising

- **Speakers:** Amy Parker
- **Room:** K.3.601
- **Day:** Sunday
- **Time:** 12:30 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5318-storytelling-networking-and-strategy-three-keys-to-successful-fundraising/)

#### Abstract

Drawing on my 20+ years of experience raising philanthropic support for organizations like the Wikimedia Foundation, Smithsonian Institution, and New York Public Library, I will share tried and tested fundraising techniques that also can be applied in FOSS organizations like OpenSSL, where I am the Chief Funding Officer. 
To provide context, I first will share a brief overview of some US-specific and global giving data as well as the lessons we can learn from this data (for example: giving from individuals far surpasses giving from other sources). We’ll then take a close look at the fundraising truism that it’s all about making “the right ask to the right person at the right time” and how to apply this in your fundraising. Storytelling is the key to setting up the “right ask.” Networking is the key to getting to the “right person.” And events (from networking at conferences to hosting a reception) are one strategy for creating “the right time.”

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-funding:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-funding:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DJ7WXJ/feedback/)

---

### Funding FOSS together: Combining public and private efforts

- **Speakers:** Mirko Swillus, Michael Winser
- **Room:** K.3.601
- **Day:** Sunday
- **Time:** 13:10 - 13:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5279-funding-foss-together-combining-public-and-private-efforts/)

#### Abstract

This presentation highlights the different motivations and goals of two organizations that have been funding the FOSS ecosystem since 2022, one funded by the private sector, the other by the public sector.  
Alpha-Omega is an associated project of the OpenSSF, with a mission to protect society by catalyzing sustainable security improvements to the most critical open source software projects and ecosystems. 
The Sovereign Tech Agency is an initiative funded by the German ministry for economic affairs and climate action and is strengthening the Open Source ecosystem in the public interest, with a focus on maintenance. 
We will talk about the different approaches and backgrounds, but most importantly about the overlaps and future opportunities when it comes to joint efforts to strengthen the ecosystem.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-funding:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-funding:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7EWTDR/feedback/)

---

### When is it Right to Say No to Funding?

- **Speakers:** Karen Sandler
- **Room:** K.3.601
- **Day:** Sunday
- **Time:** 13:50 - 14:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6481-when-is-it-right-to-say-no-to-funding-/)

#### Abstract

With so many FOSS projects vying for funding opportunities and concerns about how to secure funding and bring stability to the FOSS ecosystem, it's hard to imagine deciding to decline funding that is immediately available. In this talk, we'll explore why accepting funding must be done thoughtfully. Not only should funding models support the fundamental goals of the project, but developers should also recognize that there are times when funding opportunities are not in their long term interests. We'll explore specific examples of circumstances where accepting funding from particular sources would compromise the project's brand or values, and when the expectations of the funder don't exactly match the developer's plans, leading to strained relationships going forward.  These issues touch on a variety of topics including project governance, brand management, community management and ethics, in addition to fundraising strategies for long term donor relationships.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-funding:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-funding:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FGTLFL/feedback/)

---

### How do we get the European Union to invest in FOSS maintenance and security?

- **Speakers:** Nicholas Gates, Felix Reda
- **Room:** K.3.601
- **Day:** Sunday
- **Time:** 14:30 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6133-how-do-we-get-the-european-union-to-invest-in-foss-maintenance-and-security-/)

#### Abstract

How do we get the European Union to invest in FOSS maintenance and security? This talk will explore the idea that the public sector should expand investment into Free and Open Source Software, with focus on investing in and maintaining FOSS being used as part of critical digital infrastructures. Instead of just calling for more funding for open source, public digital infrastructure, digital commons, etc, the talk will concretely compare proposed funding approaches, discuss the practicalities of an institution like the EU investing in FOSS maintenance and security, and examine how the funding might be delivered in the next Multiannual Financial Framework.
The second part of the talk will highlight the opportunity for a Sovereign Tech Agency at the EU level which plays a greater role in funding the maintenance and security of FOSS. The German government's support to build the Sovereign Tech Fund, now the Sovereign Tech Agency, has received a lot of attention in Europe and globally for its ability to support and invest in the FOSS ecosystem. This talk will present an initial legal analysis for what an EU-scale Sovereign Tech Fund could look like, in consideration of three different potential institutional set-ups: (2) one EU funding body to rule them all, (2) a federated set up with a coordinating body/system, and (3) a free for all for all Member States to set up their own funding bodies. It will then consider the next steps for developing a more comprehensive feasibility assessment of this topic and making the case for FOSS funding to policymakers in the European Commission.

#### Related Links

- [EU Open Source Policy Summit 2024 Panel: The Case for a Big EU OSS Fund](https://www.youtube.com/watch?si=63a_KrRDs9-NkbUS&t=2399&v=WThUgwjIanM&feature=youtu.be)
- [Feasibility Study: Sovereign Tech Fund](https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/news/feasibility-study-sovereign-tech-fund)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-funding:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-funding:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SZLASC/feedback/)

---

### Small seeds - why funding new ideas matters

- **Speakers:** Marie Kreil, Marie-Lena Wiese
- **Room:** K.3.601
- **Day:** Sunday
- **Time:** 15:10 - 15:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5211-small-seeds-why-funding-new-ideas-matters/)

#### Abstract

More money for Free and Open Source Software - a never ending issue. In a tech world built on start-ups, venture capital and data-gathering apps, the fight for sustainable funding for ethical technology projects is a fierce one. After some big victories for FOSS funding in the last years, this talk is about the importance of not forgetting the small, underdog civil society projects.
How do we fund technology in a sustainable way? Fund infrastructure, fund maintenance, fund that project some random person in Nebraska has been thanklessly maintaining since 2003. While infrastructure is extremely important (no questions asked), in this talk we want to explore why a diverse funding landscape that also allows for supporting new people and groups with fresh ideas can only be incredibly valuable to the field of FOSS.
How can we use existing funding structures, bend and twist them to meet the real needs of communities? How can we make them more useful to projects and people who are not typically the recipients of their money? We want to talk about how to build support infrastructure that allows us to fund in ways that bring more diversity, more novel ideas and more inclusivity to our communities - and we want to talk about how to do this in a sustainable way. 
The background to this talk is our experience in managing the German FOSS Prototype Fund, which has funded nearly 400 projects over the past eight years together with the German Federal Ministry of Education and Research. Following an extensive internal and external evaluation, and as the initial funding was coming to an end, we spent the last year designing and setting up a new, more sustainable funding structure for early-stage projects. 
This talk is a call to government institutions, funders and other organisations with the power to distribute money to join forces, break down the barriers of their traditional funding models and create a broad and vibrant network of small, diverse and lightweight funds that meet the needs of different groups and communities. It is an invitation to communities to come together and share their needs in order to help build structures that can actually support their work. There is hope in FOSS projects, old and new, big and small. Let's hack all kinds of systems to give them the support they need.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-funding:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-funding:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HU9PZV/feedback/)

---

### The VC Dilemma: Pros and Cons of Venture Capital for Open Source Software

- **Speakers:** Stefano Pampaloni
- **Room:** K.3.601
- **Day:** Sunday
- **Time:** 15:50 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6473-the-vc-dilemma-pros-and-cons-of-venture-capital-for-open-source-software/)

#### Abstract

Venture Capital (VC) is often seen as a powerful driver of innovation, but when applied to the world of open source software, it can create tensions between profit-oriented goals and the core values of open source: collaboration, transparency, and open access.
In this talk, we will explore:
Lessons from the past:  Successes and failures of open source startups funded by VCs.
The current interest of VCs in European open source: An overview of opportunities for European startups and the influence of VC on the ecosystem.
Risks of VC for open source: Loss of independence, push towards closed models, and challenges in balancing economic sustainability with ethical values.
Proposals for a sustainable future:
Evaluate the B-Corp models, which balance profit and social impact.
Leveraging foundations to ensure community governance of open source projects, preserving their independence.
The goal is to foster a critical discussion on how to create a balance between funding and sustainability, preventing the dynamics of Venture Capital from undermining the fundamental values of open source.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-funding:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-funding:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PVPNCB/feedback/)

---

### Open source funding: you’re doing it wrong

- **Speakers:** Andrew Nesbitt, Benjamin Nickolls
- **Room:** K.3.601
- **Day:** Sunday
- **Time:** 16:30 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5576-open-source-funding-you-re-doing-it-wrong/)

#### Abstract

After a decade saying we need to support our digital infrastructure, are we any closer to doing so? 
In this talk we hope to convince you that observable usage is the best determinant of open source ‘criticality’ and to argue that, if this is the case, much of the funding flowing to open source projects today is misdirected.
Using open and freely available data from thousands of sources, helpfully collated by ecosyste.ms, we demonstrate how a few popular projects absorb much of the funding that we see while the most critical projects, and the communities that depend upon them, miss out. 
We show how today’s intractable approaches to funding open source projects make collectively supporting our shared digital infrastructure impossible, and advocate for more openness between and amongst both supporters and open source communities to enable better coordination and collaboration.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-funding:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-funding:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ERJ9U8/feedback/)

---

## GCC (GNU Toolchain) (11)

### Welcome to the GCC (GNU Toolchain) devroom

- **Speakers:** Jose E. Marchesi, Thomas Schwinge, Marc Poulhiès
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 15:00 - 15:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6668-welcome-to-the-gcc-gnu-toolchain-devroom/)

#### Abstract

Welcome to the GCC (GNU Toolchain) devroom from the organizers.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-gcc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-gcc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7RCPRX/feedback/)

---

### Pushing the Sega Dreamcast with GCC

- **Speakers:** Falco Girgis
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 15:05 - 15:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6468-pushing-the-sega-dreamcast-with-gcc/)

#### Abstract

GCC is the lifeblood which powers continued development for many legacy and niche processors, such as the Hitachi SH4, found in the Sega Dreamcast. See how far a group of retro game developers, reverse engineers, and language enthusiasts are able to push the console, armed with the latest version of the GNU Toolchain, taking a deep-dive through community-driven ports to the platform, such as Super Mario 64, Sonic Mania, Doom 64, and Grand Theft Auto 3.

#### Related Links

- [KallistiOS: Independent SDK and Operating System for Sega Dreamcast](https://github.com/KallistiOS/KallistiOS)
- [Super Mario 64 DC](https://github.com/mrneo240/sm64-port)
- [Doom 64 DC](https://github.com/jnmartin84/doom64-dc)
- [Sonic Mania DC](https://github.com/michael-fadely/Sonic-Mania-Decompilation)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-gcc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-gcc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9ZERHA/feedback/)

---

### First contributions to GCC: from plugins to trunk

- **Speakers:** Javier Martinez
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 15:40 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6237-first-contributions-to-gcc-from-plugins-to-trunk/)

#### Abstract

C++ has many features but sometimes we want more. We will briefly tell the story of why and how we wrote a GCC plugin, used it in production, and later contributed the feature in-tree - now part of GCC 14. The goal of the talk is to motivate users to try GCC development, highlighting that there can be a smooth transition from plugins to in-tree patches.
There will be a written tutorial to go with the talk available to anyone to follow in their own time. The tutorial goes over writing your first custom attribute, static analysis, and instrumentation passes. All packed in the exercise of writing a toy Aspect Oriented C++ via plugins.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-gcc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-gcc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/A98UWW/feedback/)

---

### Tutorial: How to add a builtin function to the GCC backend

- **Speakers:** Jeremy Bennett
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 15:55 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5684-tutorial-how-to-add-a-builtin-function-to-the-gcc-backend/)

#### Abstract

A common first step to adding full code-generation functionality for a new instruction, or set of instructions is to add them to the back-end as a builtin function.  This is particularly common with RISC-V where custom ISA extensions are common place.
In this tutorial I will take you through the steps to add a builtin-function to the back-end, using a case study from the OpenHW CV32E4Pv2 RISC-V core.  This has 8 ISA extensions, with a total of more than 300 instructions.
I will conclude by looking at some of the things we got wrong. In particular unexpected consequences when the new compiler started being used more widely.

#### Related Links

- [GNU Compiler Collection](https://gcc.gnu.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-gcc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-gcc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WRYGFF/feedback/)

---

### Using the Valgrind error manager for file descriptor tracking

- **Speakers:** Alexandra Petlanova Hajkova
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 16:25 - 16:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4178-using-the-valgrind-error-manager-for-file-descriptor-tracking/)

#### Abstract

The valgrind error manager makes it easy for valgrind tools to report issues that can include execution backtraces for multiple events, integrate with gdb, generate xml reports and lets users suppress specific issues. The valgrind error manager contains a fast unwinder which can be used to detect "equivalent" issues.
For valgrind 3.23.0 we introduced "core errors" which are tool independent and can be used to report on core events for resources that are explicitly created and destroyed. We used this to add errors when using file descriptors that can be reported by any valgrind tool by using --track-fds=yes. This allows reporting on bad use of file descriptors, file descriptors that are double closed, used after closing, and file descriptors that "leak". Because these are "normal" valgrind errors all these events can be reported in the xml output, suppressed by the user, intercepted by gdb and integrated in CI runs with --error-exitcode.
For Valgrind 3.24.0 we added bad file descriptor usage errors.

#### Related Links

- [Valgrind project web page](https://valgrind.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-gcc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-gcc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QRNSBP/feedback/)

---

### Cobol is the Original Safe Language

- **Speakers:** James Lowden
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 16:55 - 17:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6612-cobol-is-the-original-safe-language/)

#### Abstract

Although it was invented decades before the term "safe language", COBOL was created to meet that very need.  At the time in that environment, the predominate alternatives were FORTRAN, and assembly language.
Safety means different things to different people and in different contexts.   By some definition, no language is safe.  By others, COBOL may be considered among the safest.

#### Related Links

- [Slides](http://www.schemamania.org/jkl/Presentations/Fosdem/2025/slides.pdf)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-gcc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-gcc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KBNJLF/feedback/)

---

### Optimizing switch statements: overview and what's new

- **Speakers:** Filip Kastl
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 17:20 - 17:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4547-optimizing-switch-statements-overview-and-what-s-new/)

#### Abstract

During compilation, GCC breaks down switch statements into simpler statements. If a switch has a specific structure, GCC may use techniques that result in faster code. We call these techniques "switch optimizations".
In this talk we'll overview switch optimizations in GCC. Then we'll go into more detail on turning switches into array lookups. In GCC this is called "switch conversion". I'll introduce a new method called "exponential transformation" that I recently contributed to switch conversion. If time permits, we will also discuss potential future work on switch optimizations.
I plan to make this talk beginner-friendly. I myself have started working on GCC just 2 years ago. The talk should however give the audience a good idea about what switch optimizations are available and what they do.
Expected prior knowledge: What is a C switch statement. Very basic understanding of assembly.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-gcc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-gcc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/F8W9EF/feedback/)

---

### Incremental LTO in GCC

- **Speakers:** Michal Jireš
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 17:40 - 18:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5378-incremental-lto-in-gcc/)

#### Abstract

Incremental LTO in GCC
Link Time Optimization (LTO) postpones many compiler steps into linking, when we have access to all files linked together. This allows us to optimize across compilation units leading to significantly faster and smaller binaries. However it comes at a cost of long compile times because after even a minor edit the entire application needs to be re-optimized.
Incremental LTO will be a new feature of GCC 15 which aims to reduce those compile times for small changes by caching LTO partitions unaffected by the change.
This talk will cover quick overview of Incremental LTO and how to use it in upcoming GCC 15 along with a simple example. I will also show estimate of how much compile time can be saved when recompiling GCC itself.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-gcc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-gcc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AXMCFD/feedback/)

---

### CRC detection and optimization

- **Speakers:** Mariam Arutunian, Hayk Aslanyan
- **Room:** K.3.201
- **Day:** Saturday
- **Time:** 18:00 - 18:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5171-crc-detection-and-optimization/)

#### Abstract

Cyclic redundancy check (CRC) is a widely used error-detection mechanism that helps in the validation of data communication and storage in the digital world. While traditional bitwise implementations are slow and less efficient, alternative methods such as lookup tables, carry-less multiplication, and hardware CRC instructions offer significant performance improvements. In this talk, I will present a novel method for automatically identifying and replacing inefficient bitwise CRC implementations with optimized alternatives. The approach uses fast detection of candidate code fragments, symbolic execution for validation, and automatic replacement with more efficient implementations.  The method is implemented in the GCC compiler as a separate pass and is open-source available. Experimental evaluation was performed for i386, AArch64, and RISC-V architectures, and the results demonstrated up to 91%, 98%, and 93% performance improvements respectively, highlighting the effectiveness of the proposed optimization.

#### Related Links

- [Add a new pass for naive CRC loops detection](https://github.com/gcc-mirror/gcc/commit/062ad209e496a69925b1ac1d80d9b99c54801830)
- [Implement internal functions for efficient CRC computation.](https://github.com/gcc-mirror/gcc/commit/bb46d05ad64e4e0acb3307e76bab340aa8587d3e)
- [Add built-ins and tests for bit-forward and bit-reversed CRCs.](https://github.com/gcc-mirror/gcc/commit/c5126f0a004c27b180ac48f9e874e3744c088a09)
- [RISC-V: Add CRC expander to generate faster CRC.](https://github.com/gcc-mirror/gcc/commit/74eb3570e6fba73b0e2bfce2a14d7696e30b48a8)
- [Add symbolic execution support.](https://github.com/gcc-mirror/gcc/commit/148e20466c2c246df9472efed0f2ae94cb65a0f8)
- [Verify detected CRC loop with symbolic execution and LFSR matching](https://github.com/gcc-mirror/gcc/commit/dcc6101cb166b4c59afecc2a3cf1d7aa655fe76a)
- [Replace the original CRC loops with a faster CRC calculation](https://github.com/gcc-mirror/gcc/commit/4d2b9202fe94c54e63fb07d48293a78da3d82532)
- [Add tests for CRC detection and generation](https://github.com/gcc-mirror/gcc/commit/113e902e842b9b6d038162dfa751c25377b594d3)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-gcc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-gcc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MKUXFS/feedback/)

---


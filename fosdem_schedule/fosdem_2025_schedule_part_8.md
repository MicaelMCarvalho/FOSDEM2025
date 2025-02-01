# FOSDEM 2025 Schedule - Part 8 of 11

*Generated on 2025-02-01*

## Table of Contents

- [Open Hardware and CAD/CAM (19)](#open-hardware-and-cad/cam-19)
- [Open Media (11)](#open-media-11)
- [Open Research (22)](#open-research-22)
- [Open Source Design (8)](#open-source-design-8)
- [Open Source Firmware, BMC and Bootloader (12)](#open-source-firmware,-bmc-and-bootloader-12)
- [Open Source In The European Legislative Landscape and Beyond (34)](#open-source-in-the-european-legislative-landscape-and-beyond-34)

## Open Hardware and CAD/CAM (19)

### Horizon EDA - past, present and future

- **Speakers:** Lukas
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 11:10 - 11:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5047-horizon-eda-past-present-and-future/)

#### Abstract

Horizon EDA is a full-featured CAD application for printed circuit board design covering all steps from parts management to schematic entry and board layout. In this talk, I'll go into what has happened since the last talk 2020, where the project is right now and where it's headed.

#### Related Links

- [Project Website](https://horizon-eda.org/)
- [Project repo](https://github.com/horizon-eda/horizon)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MWWH9L/feedback/)

---

### KiCad Project Status

- **Speakers:** Wayne Stambaugh
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 11:40 - 12:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4152-kicad-project-status/)

#### Abstract

The current state of the KICad project including the upcoming 9.0 stable release feature set as well as plans for version 10 features.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/J7CSJP/feedback/)

---

### Lessons From 10 Years of Certifying Open Source Hardware

- **Speakers:** Michael Weinberg
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 12:10 - 12:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4257-lessons-from-10-years-of-certifying-open-source-hardware/)

#### Abstract

10 years ago, the Open Source Hardware Association (OSHWA) kicked off the process of creating an open source hardware certification.  In the decade since, OSHWA has certified thousands of pieces of hardware from over 50 countries on 6 continents [1] as compliant with the community definition of open source hardware.[2]  
This presentation will discuss why the certification program was created in the first place, how it is being used today, and what lessons other communities might be able to learn from its success. 
[1] https://certification.oshwa.org/list.html
[2] https://www.oshwa.org/definition/

#### Related Links

- [OSHWA Certification Directory](https://certification.oshwa.org/list.html)
- [OSHWA Certification Site](https://certification.oshwa.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XKT3G3/feedback/)

---

### Naja Python: ECO, Netlist Optimization, and Netlist Data Collection Made Easy with a Simple Python API

- **Speakers:** Christophe Alexandre
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 12:30 - 12:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4775-naja-python-eco-netlist-optimization-and-netlist-data-collection-made-easy-with-a-simple-python-api/)

#### Abstract

The Naja project offers an open-source Structural Netlist API designed to streamline post-synthesis Electronic Design Automation (EDA) workflows. 
This presentation will explore Naja’s Python API, which facilitates efficient netlist editing, optimization, and netlist data collection. The talk will showcase the API and will show examples of performing Engineering Change Orders (ECOs) and netlist simplifications, such as constant propagation and dead logic elimination.
Naja is available here: https://github.com/najaeda/naja

#### Related Links

- [naja github repository](https://github.com/najaeda/naja)
- [naja gate level verilog parser repository](https://github.com/najaeda/naja-verilog)
- [najaeda: naja python package](https://pypi.org/project/najaeda/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GTL37K/feedback/)

---

### ngspice - XSPICE elemental devices made available in KiCad

- **Speakers:** Holger Vogt
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 12:50 - 13:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5619-ngspice-xspice-elemental-devices-made-available-in-kicad/)

#### Abstract

XSPICE code models have been intrgrated into ngspice since starting the ngspice project. Currently 68 device models are available, ranging from simple elements like analog gain cells or digital inverters up to complex ones like a digital state machine , SRAMs, 3D table models or interfaces to digital Verilog building blocks compiled with Verilator. The simulation with digital blocks is fast, since event based. The interface between digital and analog blocks is automated.
The use of the XSPICE code models has been hampered a bit due to their specific interfaces and the lack of graphical symbols of its elements for creating user readable circuit diagrams.
So I have started a project to provide XSPICE code model support via the well-known KiCad/ngspice integration. It comprises of a symbol library and its assiciated device models assembled in a subcircuit model library. In the talk I will inform about its concept and status and will present some application examples.
https://forum.kicad.info/t/simulation-with-xspice-code-models/56384
https://sourceforge.net/projects/ngspice/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/U3TCWD/feedback/)

---

### Product development in mechanical engineering with open-source software

- **Speakers:** Aleksander Sadowski
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 13:20 - 13:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4534-product-development-in-mechanical-engineering-with-open-source-software/)

#### Abstract

The presentation titled "Product Development in Mechanical Engineering with Open-Source Software" aims to provide mechanical engineering startups with a practical guide for implementing the product development process using open-source software. The goal is to specifically promote innovation, particularly in the field of mechanical engineering. Established mechanical engineering companies can also benefit from this guide, adopting specific approaches into their own product development processes.
To illustrate the process clearly, it will be demonstrated through a concrete product example. The open-source tools used will be introduced, their application in the development process explained, and the results from each step shown. The presentation is based on the publication "How to Succeed in the Product Development Process with Open-Source Software" in "konstruktionspraxis".
The product will go through the following steps:

Patent search for public domain technologies based on the requirements list
Product concept from selected patent and utility model documents
Product safety based on the concept, including risk assessment and access to harmonized standards
Preliminary design of the product using a spreadsheet
Detailed design in 3D CAD, generation of technical drawings, FEM simulation
Product lifecycle management, file versioning, and infrastructure

The following software will be used:
- FreeCAD
- PrePoMax
- LibreOffice (Writer, Calc, Impress)
- Mozilla Firefox
- www.espacenet.com (not open-source, but freely accessible)
The presentation will be made publicly available as a PDF after the talk.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3PZWQP/feedback/)

---

### Sonata - Open source hardware and bitstream for evaluating CHERIoT

- **Speakers:** John Thomson
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 13:50 - 14:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6553-sonata-open-source-hardware-and-bitstream-for-evaluating-cheriot/)

#### Abstract

The Sunburst Project was created to get CHERIoT Hardware into the hands of embedded engineers.
CHERI and CHERIoT extends conventional hardware ISAs with new architectural features for enabling fine-grained memory protection and highly scalable software compartmentalisation.
Sonata is an open source hardware board (PCB), bitstream and all the constituent parts to allow engineers to experiment with CHERIoT.
The Sonata design is fully open sourced under an Apache 2.0 licence. The board design has also been ported to KiCad.
CHERI has been developed by University of Cambridge and SRI International. CHERIoT was created by Microsoft. Ibex is managed by lowRISC. Sonata has been prepared by lowRISC CIC and NewAE.

#### Related Links

- [Software repo](https://github.com/lowRISC/sonata-software)
- [Sonata system](https://github.com/lowRISC/sonata-system)
- [Sonata board PCB](https://github.com/newaetech/sonata-pcb)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EHJKT3/feedback/)

---

### Refactoring Sketcher in FreeCAD

- **Speakers:** Ajinkya Dahale
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 14:10 - 14:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4483-refactoring-sketcher-in-freecad/)

#### Abstract

Sketcher is the 2D constrained drawing workbench in FreeCAD. While a powerful tool making the backbone for more complex 3D workbenches, all the years of development has added a significant bloat to the code-base. This includes 10,000+ line files and 1000+ line functions with little to no testing.
In this talk I will present the method and progress in the ongoing effort to refactor the Sketcher workbench in FreeCAD, such that it is more maintainable and extensible for the future. Topics covered include identifying places for improvement in the first place, adding tests, and finally* methods of refactoring.

#### Related Links

- [Pull request containing the first merged set of changes](https://github.com/FreeCAD/FreeCAD/pull/15811)
- [PR containing full set of changes done so far](https://github.com/FreeCAD/FreeCAD/pull/14696)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/G7LRYY/feedback/)

---

### Verilog-AMS in Gnucap

- **Speakers:** Felix
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 14:30 - 14:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5880-verilog-ams-in-gnucap/)

#### Abstract

Gnucap is a Free versatile and modern, modular, analog and mixed-signal simulator.
Verilog-AMS is a standardised behavioural language for analog and mixed-signal
systems based on the IEEE 1364-2005 industry standard, commonly known as Verilog.
Gnucap was invented to advance circuit simulator technology from around 1985,
at the time SPICE was developped (1973-1993) at UC Berkeley. Gnucap was
released under GPLv3+ in 2001 to avoid patent issues. Today, proprietary
simulators supposedly implement the most efficient algorithms yet inspired by
public research from the past century. Meanwhile, the Gnucap project is making
progress harvesting the breaktroughs, for use in free/libre software.
To address the interoparability across circuit design tools, and across
modelling domains, Verilog-AMS was created. Verilog-AMS extends traditional
Verilog by analog features known from SPICE, and permits models that interact
with both the digital and analog domains. The standard expertly allows for
vendor-independent representations of modern circuit designs.
1 In this talk, we will explain the new revision of our proposed IEEE 1364-2005
  compliant schematic interchange format, and how seamless interaction will
  empower FOSS EDA tools. We will outline work in progress, possibly demonstrate
  an application, and hint at opportunities. We will explain how the interchange
  will extend towards PCB design and layout
2 We will summarise new mixed signal features available in modelgen-verilog.
  This includes monitored analog events, as well as discrete modelling in terms
  of user defined primitives. We will expand on the usefulness of discrete
  disciplines and "connect modules", and give an update on the implementation
  status.
3 On the algorithmic end, we have added a plugin interface for VLSI-ready
  matrix solvers to the zoo. We will highlight a new solver combining temporal
  sparsity with the time/space efficiency of "conventional sparse" LU
  decomposition. We will explain why Gnucap will outpace traditional (open
  source) solvers on virtually all instances, both small and big circuits.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/Q78AJD/feedback/)

---

### The IHP OpenPDK Initiative: Status and RoadMap

- **Speakers:** Wladek Grabinski
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 14:50 - 15:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5882-the-ihp-openpdk-initiative-status-and-roadmap/)

#### Abstract

In the field of semiconductor technology, compact modeling, and IC designs, the OpenPDK Initiative provides an international platform for discussing advanced technologies, fostering collaboration among industry and academic leaders in electronic design automation (EDA). We review selected R\&D topics presented at a recent event by prominent academic researchers and industrial professionals who presented and discussed innovative approaches in CAD/EDA tools, techniques including compact/SPICE modeling, and IC design that address the demands of emerging semiconductor technology applications. However, the semiconductor industry also faces many challenges in maintaining the growth of its workforce with skilled technicians and engineers. To address the increasing need for well-trained workers worldwide, we must find innovative ways to attract skilled talent and strengthen the local semiconductor workforce ecosystem. The FOSS CAD/EDA tools with the recently available open access PDKs provide a new platform to connect IC design beginners, enthusiasts and experienced mentors to benefit from the collaboration opportunities enabled by the fast-growing open-source IC design movement. The collaborative development of open-source integrated circuit (IC) designs is becoming increasingly feasible due to the rapid expansion of OpenPDKs recently offered by SkyWater, GF and IHP with an open schedule of MPW Runs for FMD-QNC project in 2024-25. This paper demonstrates the FOSS CAD/EDA contribution to the SPICE/Verilog-A modeling/standardization, compete IC design flow (Xschem, Qucs-S, ngspice, Xyce, OpenVAF, OpenEMS, Magic, kLayout, OpenRoad), in addition selected, open-source examples of analog/RF and digital IC designs will be presented.

#### Related Links

- [IHP Open PDK](https://github.com/IHP-GmbH/IHP-Open-PDK)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TEHFYA/feedback/)

---

### The OpenFlexure Microscope

- **Speakers:** Julian Stirling
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 15:20 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4336-the-openflexure-microscope/)

#### Abstract

The OpenFlexure Microscope is an open source laboratory-grade digital robotic microscope. As a robotic microscope, it is able to automatically scan microscope slides creating, enormous multi-gigapixel digital representations of samples. The microscope is already undergoing evaluation for malaria and cancer diagnosis in Tanzania, Rwanda, and the Philippines. As an open project our key goal is to support local manufacturing of microscopes in low resource settings. But, how can an open source project empower local manufacturers to make hardware certified for diagnostic use?
Collaborative hardware design is notoriously difficult without complex Product Lifecycle Management (PLM) systems. However, Git provides more powerful version control than the most expensive proprietary PLM systems, especially if you use a code-based CAD package. Platforms like GitLab give clear records of project management through issue and merge request threads. Also, CI pipelines give us the ability to perform regular code quality checks, automate the generation of print-ready 3D models, and to generate detailed always-up-to-date assembly documentation and diagrams.
This high-quality consistent documentation has enabled thousands of microscopes to be built around the world, in over 50 countries. Microscopes have been used on all seven continents, from the Antarctic sea ice to the rainforest in Panama. They have been used for educational workshops in Sweden and Ghana, and even built by mobile makerspaces in wartime Ukraine. Hospitals already use the microscope to for remote consultancy and training, however without certification it cannot be used for diagnosis.
Combining good documentation with accessible calibration routines, gives manufacturers and users confidence that their locally-manufactured device performs as well as the thousands of other OpenFlexure Microscopes around the world. Building in robust calibration is crucial in our push towards medical certification.
This talk will involve live microscopy demonstrations, give an overview of the microscope and its applications, as well as diving into deeper questions of open source workflows for managing diagnostic device design.

#### Related Links

- [Hardware Repo](https://gitlab.com/openflexure/openflexure-microscope/)
- [Software Repo](https://gitlab.com/openflexure/openflexure-microscope-server)
- [Other repos](https://gitlab.com/openflexure)
- [Prototype image viewer with enormous stitched images](https://johemianknapsody.github.io/viewer.html)
- [Docs](https://build.openflexure.org/openflexure-microscope/v7.0.0-beta2/)
- [Website](https://openflexure.org/)
- [Forum](https://openflexure.discourse.group/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZDN7M3/feedback/)

---

### Opensource Rocketry and Tools, FreeCAD and beyond.

- **Speakers:** jo hinchliffe
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 15:50 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4220-opensource-rocketry-and-tools-freecad-and-beyond-/)

#### Abstract

Rocketry has its challenges but there are numerous open source tools available to enable the design, simulation and manufacture of amateur, high power and experimental air frames. In this talk Jo will show some of these tools and usage highlighting along the way how it’s only open source community development that could possibly enable such interesting and interoperable tools to be developed.
Jo is a technical author, maker, and community developer who has an interest in space. Jo has developed and flown numerous open source rocket designs and has pushed the development of opensource rocketry tools. Jo has worked with Libre Space Foundation who built and launched a completely opensource satellite off the international space station as well as other on orbit opensource space projects. Jo has a wide range of clients he writes for and is the author of “FreeCAD for Makers” available for free download from the Raspberry Pi Press and also wrote "Design an RP2040 board with KiCad".

#### Related Links

- [FreeCAD Project lnk](https://www.freecad.org/)
- [Rocket workbench addon for FreeCAD](https://github.com/davesrocketshop/Rocket)
- [Openrocket, opensource rocket design and simulation tool link](https://openrocket.info/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CJHWUB/feedback/)

---

### WireViz - Beautiful wiring documentation

- **Speakers:** Daniel Rojas
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 16:20 - 16:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4612-wireviz-beautiful-wiring-documentation/)

#### Abstract

Easily and beautifully document cables and wiring harnesses.
Built out of frustration with existing wiring documentation tools, WireViz uses human-readable, YAML-formatted text to describe the makeup of a cable or wiring harness, and automatically generates an easy to understand graphical diagram including pinouts, wire lengths, color schemes, mating connectors, images, assembly notes, etc. together with a bill of materials for stockkeeping or ordering.
Since the input is purely text-based, it lends itself perfectly for integration into a version control system. The tool fills a gap between classic PCB-level eCAD/EDA tools (such as KiCad), and the world of traditional electrical plans (QElectroTech being an open source representative).
This talk will show some sample diagrams to highlight the tool's most useful features, give a look at how the GraphViz engine –running under the hood– can be (ab)used to create highly appealing technical drawings, and show the ups and downs of being a mechanical engineer (with no professional coding experience) suddenly having an open-source project explode in popularity.

#### Related Links

- [Repository](https://github.com/wireviz/WireViz)
- [Author](https://www.danielrojas.net/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ULRNYH/feedback/)

---

### Programmatic CAD with Parametrix

- **Speakers:** Charles Braquet
- **Room:** H.1309 (Van Rijn)
- **Day:** Sunday
- **Time:** 16:40 - 17:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4199-programmatic-cad-with-parametrix/)

#### Abstract

A lightweight Javascript library for programmatic 3D modeling. Enabling WebUI and CLI deployment of  3D model. Emphasizing parametrizing of 3D model for more autonomy of the maker and re-usability of designs.

#### Related Links

- [sources](https://github.com/charlyoleg2/parametrix)
- [Documentation](https://charlyoleg2.github.io/parametrix/)
- [Example](https://charlyoleg2.github.io/parame78/)
- [published package](https://www.npmjs.com/package/geometrix)
- [Slides](https://charlyoleg2.github.io/parametrix/docs/prez)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-hardware:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-hardware:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BLEPGF/feedback/)

---

## Open Media (11)

### Toward a unified abstract content API

- **Speakers:** Romain Beauxis
- **Room:** K.3.401
- **Day:** Sunday
- **Time:** 09:00 - 09:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4705-toward-a-unified-abstract-content-api/)

#### Abstract

[Liquidsoap])(https://www.liquidsoap.info/) is a general-purpose scripting language specialized in creating media stream. 
Recently, the tool was adapted to incorporate an abstract notion of content that can support raw content (PCM audio, YUV video) but also opaque encoded content such as mp3 audio, x264 encoded video, etc.
Such content can be read from files, separated into different tracks and recombined at will through different outputs (icecast, files, srt, rtmp, etc) without the need to decode and re-encode.
The backbone of this abstraction relies on the recent advances in abstract descriptions of streams as popularized by tools such as FFmpeg.
Typically, a media stream is described via opaque binary blobs, representing fractions of audio (an mp3 frame, a raw PCM segment), video (a video frame), etc.
In this context, Presentation Timestamp (PTS) and Decoder Timestamp (DTS) can efficiently describe when to present a piece of content to the listener/viewer or the encoder/encapsulation.
However, when applied to dynamic streams produced by liquidsoap scripts, another layer of complexity arises. Most liquidsoap streams need to be produced in real-time and can dynamically switch from one stream to the next.
This results in added complexity with regard to stream description: how to make sure that abstract content is generated in real-time (e.g. 2s of content is generated in 2s, slowing down the application if needed), how to maintain DTS/PTS consistency when switching from one stream to the next, etc.
In this talk, we will present the challenges and solutions that are currently implemented in liquidsoap and explain the kind of abstract content API we hope to see emerging in the future to support the next generation of media streaming application.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-media:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-media:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KEPDUE/feedback/)

---

### Writing an MP4 Muxer for Fun and Profit

- **Speakers:** Dennis Sädtler
- **Room:** K.3.401
- **Day:** Sunday
- **Time:** 09:40 - 10:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6795-writing-an-mp4-muxer-for-fun-and-profit/)

#### Abstract

MP4 is the most popular media container, but for us at the OBS Project it has some limitations that made its use undesirable for the majority of our users due to the data loss potential. Safer alternatives such as MKV - our previous default - have their own downsides that have been plaguing our users for the past decade. So last year I set out to explore our options to build something better by creatively (ab)using the ISO-BMFF specification, resulting in what we now call "Hybrid MP4".
This talk is based on my blog post by the same name, with a few additions and a new demo for a slightly cursed use of the hybrid MP4 concept.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-media:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-media:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PKDU7F/feedback/)

---

### PipeWire state of the union

- **Speakers:** Wim Taymans
- **Room:** K.3.401
- **Day:** Sunday
- **Time:** 10:20 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4749-pipewire-state-of-the-union/)

#### Abstract

PipeWire is a low-level framework for transporting Multimedia content between applications. Most desktops use it these days to implement audio services, camera and screen-sharing services.
This talk will give and overview of the new features that were added to PipeWire in the last year. It will also talk about what is next.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-media:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-media:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/U8ZNUT/feedback/)

---

### FFglitch: the multimedia bitstream editor

- **Speakers:** Ramiro Polla
- **Room:** K.3.401
- **Day:** Sunday
- **Time:** 11:00 - 11:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6416-ffglitch-the-multimedia-bitstream-editor/)

#### Abstract

In this talk I will present FFglitch, a multimedia bitstream editor written to create glitch art and codec art.
As an FFmpeg developer, I have always been amazed by the visual glitches that are created when we get something wrong in the code. But since those glitches are considered bugs, and not features, we have to fix the bugs and get rid of the glitches. FFglitch was born as a project where those glitches are features, and not bugs.
FFglitch leverages the FFmpeg codebase to turn decoders into bitstream editors. It allows precise editing of bitstream values, along with built-in scripting support, real-time input from HID and MIDI controllers, and network communication.

#### Related Links

- [Project website](https://ffglitch.org/)
- [Project GitHub](https://github.com/ramiropolla/ffglitch-core)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-media:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-media:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CSLNWU/feedback/)

---

### Embedded Video Systems With Zephyr

- **Speakers:** Josuah Demangeon
- **Room:** K.3.401
- **Day:** Sunday
- **Time:** 11:40 - 12:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4949-embedded-video-systems-with-zephyr/)

#### Abstract

Zephyr is a real-time operating system providing Video APIs to embedded devices. It enables building video feeds out of any supported hardware, low-power or high-performance alike.
The image sensor market explodes and cameras are used for many purposes: optics, electronics and signal processing is empowering medical imaging, agriculture, drones, conferencing, traffic monitoring, robotics, automation, scientific equipment... Through computer vision, imaging becomes an integral part of an information system around it: images that act.
A Zephyr-themed overview of the video information chain, from photons to software APIs.

#### Related Links

- [The Zephyr RTOS repository](https://github.com/zephyrproject-rtos/zephyr)
- [The Zephyr RTOS documentation](https://docs.zephyrproject.org/latest/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-media:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-media:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FK3RXK/feedback/)

---

### How MistServer handles SRT connections in independent child processes

- **Speakers:** Jaron Viëtor
- **Room:** K.3.401
- **Day:** Sunday
- **Time:** 12:20 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6052-how-mistserver-handles-srt-connections-in-independent-child-processes/)

#### Abstract

One of MistServer's (an open source media server) core features is the inherent resilience of handling each connection in a separate process. However, this was not possible for SRT connections using libsrt, since it manages its own sockets as an internal resource. Because of this, for years, MistServer's implementation of SRT used a single process for all connections combined: unlike other protocols in the system! The alternatives would be to either fork libsrt (or hope to upstream some pretty drastic changes) or build an entire alternative library from scratch... Or is a there a secret third option..? Spoiler: there is!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-media:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-media:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UJCBBK/feedback/)

---

### Multiview decoding in libavcodec and ffmpeg CLI

- **Speakers:** Anton Khirnov
- **Room:** K.3.401
- **Day:** Sunday
- **Time:** 13:00 - 13:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6023-multiview-decoding-in-libavcodec-and-ffmpeg-cli/)

#### Abstract

The libavcodec library (part of the FFmpeg project) recently gained the ability to decode multiview HEVC (MV-HEVC) video, typically used for encoding stereoscopic 3D. This talk will cover the technical details of the implementation, associated support in ffmpeg CLI transcoder, and how it fits with recent and planned architectural changes.

#### Related Links

- [FFmpeg project homepage](https://ffmpeg.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-media:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-media:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KXS3DK/feedback/)

---

### Enhancing Web Media Support: A WebAssembly-Driven Open-Source Framework

- **Speakers:** Jerome Gorin, Maja Bystrom
- **Room:** K.3.401
- **Day:** Sunday
- **Time:** 13:40 - 14:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5119-enhancing-web-media-support-a-webassembly-driven-open-source-framework/)

#### Abstract

In 2024, we presented our open-source project that opens browser support to a variety of formats. This project introduces a new HTML5 syntax designed to create dynamic media pipelines for use cases related to media content handling. It leverages several technologies, including WebAssembly, Emscripten, Web Components, and GPAC. Together, these tools enable dynamic support for data formats not natively supported by browsers. This enables the option of display of data in legacy formats and promotes the development of new formats without relying on browsers to supply native support and without relying on generation and maintenance of browser plugins. 
The proposed HTML5 syntax is intuitive and flexible, catering both to novice web designers and professional developers within the open-source community who want to ensure that media content is accessible across all browsers. However, creating new decoders and integrating into the underlying GPAC media filter framework can be challenging for developers unfamiliar with WebAssembly and GPAC’s framework. 
To address this, alongside the player and SDK, we have updated our Visual Studio Code extension to streamline the development and integration of custom media decoders. The extension is now fully integrated with GitHub repositories, enabling users to retrieve, modify, compile, and test WebAssembly decoders directly. Additionally, we have released a new set of license-free decoders covering various use cases, including documents, images, audio, and video.
Our visual studio code extension is available at the following URL :
https://marketplace.visualstudio.com/items?itemName=Bevara.bevara-access
This project is open to contributions. Below are the links to our repositories:
•   Filters Repository: Contains all license-free media filters that can be integrated “as is“ into web pages or modified.
•   Solver Repository: The fundamental glue component that enables the dynamic building of media filters within web pages.
•   Player Repository: Provides the SDK and tools for compiling media filters locally.
By encouraging the use of public forks on open projects—which require making derived projects public—we aim to foster a growing repository of freely available decoders for the community to use and build upon.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-media:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-media:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3EYWKG/feedback/)

---

### More innovations in H.264/AVC software decoding

- **Speakers:** Thibault Raffaillac
- **Room:** K.3.401
- **Day:** Sunday
- **Time:** 14:20 - 15:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5455-more-innovations-in-h-264-avc-software-decoding/)

#### Abstract

This talk will present a range of architectural and optimization techniques that were used in the development of a state-of-the-art H.264 software decoder (https://github.com/tvlabs/edge264), to drastically reduce code and binary size and improve speed. The techniques are applicable to other audio/video codecs, and will be presented as HOWTOs to help participants use them in their projects. It complements my talk from last year at FOSDEM'24, and will focus this time on (i) efficient parsing of input bitstream, (ii) writing C that yields near-optimal SIMD for both SSE and NEON, and (iii) additional architectural patterns to reduce code complexity .

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-media:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-media:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SZMDAZ/feedback/)

---

### GStreamer: State of the Union 2025

- **Speakers:** Nicolas Dufresne
- **Room:** K.3.401
- **Day:** Sunday
- **Time:** 15:00 - 15:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6318-gstreamer-state-of-the-union-2025/)

#### Abstract

GStreamer is a popular multimedia framework making it possible to create a large variety of applications dealing with audio and video. Since the last FOSDEM, it has received a lot of new features: progress on the Rust RTP stack, new Vulkan Video Encoders, Zero-copy support on Linux with GTK4 and more to be found in the presentation. I will go over those major improvements and explain who they can be most useful for. Finally, we'll have a peek at what we anticipate to be in the next release.
GStreamer is a highly versatile plugin-based multimedia framework that caters to a whole range of multimedia needs, whether desktop applications, streaming servers or multimedia middleware; embedded systems, desktops, or server farms. It is also cross-platform and works on Linux, *BSD, Solaris, macOS, Windows, iOS and Android.
This talks targets everyone who cares about Free and Open Source multimedia on embedded systems. GStreamer is the standard multimedia framework, not only on the Linux desktop, but most importantly, in embedded Linux systems.

#### Related Links

- [GStreamer Git Repository](https://gitlab.freedesktop.org/gstreamer/gstreamer/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-media:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-media:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QTTVSZ/feedback/)

---

### Scaling to 12k Live Streams

- **Speakers:** Vladimir Vitkov
- **Room:** K.3.401
- **Day:** Sunday
- **Time:** 15:40 - 16:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4694-scaling-to-12k-live-streams/)

#### Abstract

According to Law Ballot Counting for any and all elections in Bulgaria need to be streamed live and archived.
We will Share how we've built a system designed to record, stream and archive 12k polling places with uncertain connectivity, personel and not much experience. The system was designed, implemented, deployed and operated in less than 2 months.
We will cover different points of the process:

Why it was necessary
How it was designed and implemented
Challenges
Possible developments

Projects that are used in implementing the solution:

MediaMTX - https://github.com/bluenviron/mediamtx/
nginx-rtmp-module - https://github.com/arut/nginx-rtmp-module
Python
Celery
A hell of a lot of bash

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-media:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-media:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/M9LHPQ/feedback/)

---

## Open Research (22)

### Creating an Open Knowledge Graph for Climate

- **Speakers:** Peter Murray-Rust
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 10:30 - 10:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6006-creating-an-open-knowledge-graph-for-climate/)

#### Abstract

semanticClimate is a global hybrid community where interns from colleges (mainly in India) create climate knowledge to help the world make informed decisions. We work with trustable material such as the UN/IPCC reports (over 15,000 pages of important, but dense text). The resulting knowledge products include:

term-based dictionaries (ontologies) enhanced with Wikipedia and Wikidata
a Corpus tool for scraping and analysing the current Open scholarly literature
a knowledge graph created from the above with navigation tools

and F/OSS software to make this easy and automatic.
semanticClimate interns come from high-school up and need have no knowledge of software. They learn-by-doing, and in some weeks have 2-hour online sessions daily - these are recorded and transcribed to text for all to see. Interns are encouraged to give public talks (e.g. OKFN, Wikipedia, CODATA) and to make 5 min videos. All software is modular, Git-branched, versioned and unit-tested. Where possible we publish it in J. Open Source Software.
The session image is part of our Climate Knowledge Graph
(my email is peter.murray.rust@googlemail.com. I can't change it in the form!)

#### Related Links

- [Collection of resources for semanticClimate. These include talks, videos and other outreach](https://semanticclimate.github.io/p/en/posts/resources/)
- [pygetpapers (search scholarly literature) Open Source. (Ayush Garg, see also publication in J. OpenSource Software https://joss.theoj.org/papers/10.21105/joss.04451.  AG was still at high school.](https://github.com/petermr/pygetpapers)
- [docanalysis (text analysis) Shweata Hegde. SNH was an undergraduate, initially with no software experience](https://github.com/petermr/docanalysis)
- [amilib (Peter Murray-Rust) Python library of > 1000 methods and > 300 user-oriented tests for downloading/transforming/republishing documents](https://github.com/petermr/amilib)
- [Semantic Climate Glossary (475 pages) created automatically and enhanced by manual multilingual terms](https://semanticclimate.github.io/p/en/posts/IPCC_Glossary/)
- [Presentation of semanticClimate at OKFN's "The Tech we Want" by Shweata N Hegde (ca 6 mins)](https://www.youtube.com/watch?v=o50Jd1w6xKw&t=16843s)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MRQFSV/feedback/)

---

### Model for Economic Tipping point Analysis (META) - a climate-economy integrated assessment model in Julia

- **Speakers:** Thomas Stoerk
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 10:55 - 11:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5985-model-for-economic-tipping-point-analysis-meta-a-climate-economy-integrated-assessment-model-in-julia/)

#### Abstract

The Model for Economic Tipping point Analysis (META) is one of a new generation of climate-economy integrated assessment models used to study the economic impacts of climate change. A typical output of such models is an estimate of the social cost of greenhouse gas emissions, a measure of the economic damage caused over its lifetime by a ton of greenhouse gas such as CO2 or CH4. 
META, however, computes many other economic as well as geophysical indicators. As its name suggests, META was built specifically to estimate the economic impact of tipping points in the climate system. To do so, META incorporates different tipping points modules, each of which replicate a geophysically realistic tipping point module from a study in the climate economics research literature. 
META was originally introduced in Dietz, Rising, Stoerk and Wagner (2021, Proceedings of the National Academy of Sciences, https://www.pnas.org/doi/full/10.1073/pnas.2103081118), and has since been updated and ported to Julia using the Mimi Framework. Follow-up research has improved several components of META. Similarly, META estimates have been used to inform conversations with authorities in the EU and the US. 
In this talk, I will give a short overview of META's structure, its capabilities, and ideas for the community on how to further improve and use META for open research in the future. 
META is freely available on Github under a GPL-3.0 copyleft licence: https://github.com/openmodels/META

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YYYMBL/feedback/)

---

### JOSSCast: Experimenting with Storytelling in Open Research

- **Speakers:** Abigail Cabunoc Mayes, Arfon Smith
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 11:20 - 11:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6149-josscast-experimenting-with-storytelling-in-open-research/)

#### Abstract

The Journal of Open Source Software (JOSS) bridges the worlds of open source and open research. To amplify this mission, we recently completed the first season of JOSSCast, an experimental podcast designed to test how storytelling can connect researchers, developers, and contributors across disciplines. In this session, I’ll share what we learned from the experience—what worked, what didn’t, and how we can use podcasts to strengthen open research.
You’ll get insights on:

The challenges and rewards of using podcasts to support open research.
How storytelling can engage both technical and non-technical audiences.
Practical tips for creating content that builds community.

Come hear about how we’re using experiments like JOSSCast to innovate and grow the open research ecosystem.

#### Related Links

- [The Journal of Open Source Software - github repository](https://github.com/openjournals/joss)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NFMLMP/feedback/)

---

### Do we need another open source software taxonomy?

- **Speakers:** Sophia Vargas
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 11:45 - 12:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5264-do-we-need-another-open-source-software-taxonomy-/)

#### Abstract

How many times have you built a taxonomy for open source software analysis? Whether you’re writing a survey for open source contributors or categorizing thousands of repositories, you’ve most likely had to create some kind of organizational structure to make sense of the data. Over the course of researching and analyzing open source projects, I’ve searched for and created many bespoke taxonomies to meet my analytical needs. In this talk, I’d like to share key learnings and pitfalls in my pursuit to answer “how do project characteristics influence behavior?”, as well as propose a solution for open source researchers to share and collaborate on open source taxonomies. No one should have build a new OSS taxonomy in a vacuum!

#### Related Links

- [This talk will reference work and software from CHAOSS project](https://chaoss.community/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/897RMH/feedback/)

---

### Guix + Software Heritage: Source Code Archiving to the Rescue of Reproducible Deployment

- **Speakers:** Simon Tournier
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 12:10 - 12:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5897-guix-software-heritage-source-code-archiving-to-the-rescue-of-reproducible-deployment/)

#### Abstract

What's Guix? GNU Guix is a software deployment tool that supports reproducible
software deployment. As research results are increasingly the outcome of
computational processes, software plays a central role. The ability to verify
research results and to experiment with methodologies, core tenets of the
scientific methods, requires reproducible software deployment.
What's Software Heritage? Software Heritage is a long term, non-profit, multistakeholder initiative with the ambitious goal to collect, preserve and share all source code publicly available. To our knowledge, Software Heritage is the largest publicly available archive of software source code.
Could we connect Guix with Software Heritage? Yes! It makes Guix the first free software distribution and tool backed by Software Heritage, to our knowledge.
This presentation describes design and implementation we came up and reports on the archival coverage for package source code with data collected over five years. It opens to some remaining challenges toward a better open and reproducible research.

#### Related Links

- [GNU Guix](https://guix.gnu.org/)
- [Guix for Science and HPC](https://hpc.guix.info/)
- [Software Heritage](https://www.softwareheritage.org/)
- [Source Code Archiving to the Rescue of Reproducible Deployment (paper)](https://doi.org/10.1145/3641525.3663622)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3SWD7Y/feedback/)

---

### Closed data, open software: building new ways into the French web archives

- **Speakers:** Guillaume Levrier, Dorothée Benhamou-Suesser
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 12:35 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5223-closed-data-open-software-building-new-ways-into-the-french-web-archives/)

#### Abstract

This presentation aims at presenting a fully open-source pipeline to extract, curate, and explore web archives, a captive data source whose access is restricted. Its purpose is to detail both the technical pipeline and the socio-institutional setting that made it possible to emerge, highlighting the challenges of developing open tools for closed sources.
The French web archives is an institutional repository of data maintained by the French National Library (BnF). It contains more than 2 petabytes of data spanning over close to 30 years, which accounts to more than 50 billion web pages. Access to this data is restricted under the heritage and legal deposit law: academic researchers willing to work on web archives as data are expected to submit research projects that, upon a formal or informal agreement, will enable them to access this data. But what then?
Building the methodological means to pursue epistemological goals in that context is particularly challenging. Web archivists do provide toolkits for exploration. Recent initiatives have scaled up the effort to make these sources more accessible. The RESPADON project has successfully managed to build a “captive web archive” capacity into the Hyphe software, and in doing so has opened a new way into developing tools for such data.
In this presentation, we will present a new solution to extensively study, at the qualitative level, specific topics in the full-text indexed collections of the French web archives. Built around the PANDORÆ software, this pipeline has been designed to interrogate the captive data source on site, but also extract relevant metadata in a compliant manner to enable its exploration off-site, while ensuring reproducibility by publishing the code. In doing so, this pipeline provides an up-to-date example of the “one-way mirror” situation of building open tools that are fit to operate on closed data sources.

#### Related Links

- [Software Repository](https://github.com/Guillaume-Levrier/PANDORAE)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RNF7UU/feedback/)

---

### Preserving LHC Analyses with Rivet: A Foundation for Reproducible and Reusable Particle Physics Research

- **Speakers:** Christian Gutschow
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 13:00 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4810-preserving-lhc-analyses-with-rivet-a-foundation-for-reproducible-and-reusable-particle-physics-research/)

#### Abstract

In high-energy physics, ensuring that analyses remain reproducible and interpretable over time is a significant challenge. As the Large Hadron Collider (LHC) produces vast datasets and as analyses evolve, reproducibility becomes crucial for both current and future research efforts. Rivet (Robust Independent Validation of Experiment and Theory) addresses this challenge by providing a framework for the preservation and reinterpretation of LHC analyses. This talk will discuss how Rivet facilitates analysis preservation, enabling researchers to reproduce, validate, and reuse complex particle collision studies long after initial publication. We’ll explore specific use cases, including how Rivet supports reinterpretation for new physics searches, and the technical underpinnings that make Rivet an indispensable tool for long-term data analysis preservation. This presentation will emphasise Rivet’s role within the broader landscape of open science and data preservation, with insights into its integration with other high-energy physics frameworks. Attendees will gain a clear understanding of Rivet’s contributions to sustainable research practices and reproducibility within the scientific community.

#### Related Links

- [Rivet gitlab repo](https://gitlab.com/hepcedar/rivet)
- [Rivet website](https://rivet.hepforge.org/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KYA3HU/feedback/)

---

### CartABl: instrumenting the authoring of interactive maps and figures

- **Speakers:** OlivierAubert
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 13:25 - 13:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6010-cartabl-instrumenting-the-authoring-of-interactive-maps-and-figures/)

#### Abstract

The talk will introduce CartABl https://igarun.univ-nantes.io/CartABl/ , a free (GPL) web-based authoring tool for creating interactive maps and figures, and discuss its impact on user workflows and design decisions. Designed primarily for geographers and cartographers, CartABl also serves broader communities seeking to produce interactive cartographic content. It addresses the technical barrier that coding poses to creating interactive cartographic content (using js) through a graphical interface for defining interactions. It integrates seamlessly with traditional workflows by enhancing maps created in vector graphics editors like Inkscape or Adobe Illustrator with interactivity, without requiring programming knowledge. CartABl leverages SVG (Scalable Vector Graphics) as its base format, embedding interactive rules as declarative elements interpreted by a lightweight JavaScript runtime. This results in standalone, browser-compatible interactive SVG files, preserving the scalability and versatility of the format.
The development of CartABl follows an instrumental genesis approach, where tool and user co-evolve through iterative feedback. Initial prototypes allowed basic interactivity like tooltips and layer toggling. Feedback from its application in projects such as L’Atlas Bleu, a journal focused on coastal and marine maps, guides its refinement. This iterative process not only improves the tool but also influences how cartographers structure and design their graphical maps and figures: the structure of the graphical objects must be adapted to facilitate the definition of interaction rules, and the interactive features proposed by the tool impact the design decisions of the users.
CartABl aims to democratize interactive cartography, making it accessible and intuitive for professionals and non-experts alike. By transforming workflows and expanding the possibilities of digital cartographic publishing, it stands out as a valuable resource for advancing geographic and graphic research and communication.

#### Related Links

- [Repository](https://gitlab.univ-nantes.fr/igarun/CartABl/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XZ8F3E/feedback/)

---

### Opening the Unlocked Manuscript Chest: A Compact Edition Template for Visualizing Archival HTR Material

- **Speakers:** Nooshin Shahidzadeh Asadi
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 13:50 - 14:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6331-opening-the-unlocked-manuscript-chest-a-compact-edition-template-for-visualizing-archival-htr-material/)

#### Abstract

Necturus is a free and open-source tool for visualizing the connection between handwritten manuscript images and their machine-readable transcriptions. While platforms like Transkribus and eScriptorium excel at generating text from handwritten material, they leave visualization to the side—Transkribus hides its solution behind a paywall, and eScriptorium offers none at all. Yet, for many research endeavors, the line-by-line relationship between text and image remains critical, as seen in projects like the Beckett Digital Manuscript Project and the Joyce Letters Project.
Designed as a lightweight, embeddable React component, Necturus makes it easy for libraries, archives, and researchers to present manuscript images alongside their transcriptions in an interactive and accessible format. A plug-and-play template allows deployment via GitHub Pages with no coding required, while a full version supports scalable, customizable setups for larger projects. By emphasizing both transcription and the manuscript as objects of study, Necturus offers a practical solution for those who value visualization in the process of, as Transkribus puts it, “unlocking the past”.
Project Repositories: Necturus, Necturus Compact

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BBVYV8/feedback/)

---

### Explore large image datasets with Panoptic

- **Speakers:** Félix Alié, David Godicke, Edouard Bouté
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 14:15 - 14:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4635-explore-large-image-datasets-with-panoptic/)

#### Abstract

Panoptic is a tool to explore locally and easily big images datasets: https://github.com/CERES-Sorbonne/Panoptic
Images abound on the web and digital social networks. Their proliferation is one of the characteristics of digital culture. In particular, they are widely mobilized in contemporary controversies, with the aim of revealing and debating important social issues. Far beyond natively digital images, whether moving or still, images are first and foremost an object of study in their own in many disciplines (art history, film studies...), just as they can be a way of accessing a research field (photographs of animal and plant species, pages from digitized books...). A key challenge for the human and social sciences is to equip themselves with tools for exploring, sorting and annotating image corpora.
While a number of tools already exist for working with such corpora (XnView, Tropy, voxel51, Aikon, Arkindex, for example), a key issue to be resolved is the multiplication in the number of images we work with: how can we efficiently explore, sort and annotate a corpus of several tens of thousands of images? How can we provide researchers with a tool that facilitates such work?
Indeed, working with a large number of images means first of all having a synoptic view of them, in order to understand them as a whole, but also being able to manipulate them directly in the presentation interface (for both exploration and analysis).
Secondly, working with a large number of images also imposes time constraints on analysis, which can be resolved by using similar-image clustering tools (computer vision tools), to group together images that have formal similarities (reduces exploration time), but also by using batch annotation functionalities (reduces analysis time).
Finally, working with images is rarely just about working with images, but also with textual data associated with the images (texts of tweets, photographer's name, shooting date, etc.). Another challenge, then, is to adopt a plurisemiotic approach to the content of the corpus being worked on, in order to avoid having to move back and forth between different work spaces.
Created at CERES, by developers, researchers and designers, Panoptic is an open source tool for visualizing, exploring and annotating large images corpora. In particular, the tool integrates algorithms for grouping images by similarity (by using ml model CLIP), to help users with sorting and exploration. The tool also offers various filtering, search and annotation options, enabling the creation, analysis and export of sub-corpora.
Our talk will present the tool we have developed, and how its various functions are designed to meet the methodological needs of research using tools for working with large volumes of images.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/7VRBVR/feedback/)

---

### How Open-Source Software is Shaping the Future of Healthcare

- **Speakers:** Miguel Xochicale
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 14:40 - 15:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5196-how-open-source-software-is-shaping-the-future-of-healthcare/)

#### Abstract

Open-source software has been a powerful catalyst for innovation in computer and software engineering, driving significant advancements in healthcare, particularly in medical and surgical technologies. Recently, the open-source movement has expanded beyond software, encompassing the release of code, data, and AI models, further accelerating progress across diverse fields. However, in healthcare, open-sourcing faces distinct challenges, including navigating regulatory hurdles to meet industry standards, ensuring robust patient data protection, managing the costs of specialised hardware and software maintenance, and addressing the limited availability of expert clinicians needed to annotate, test, and validate AI innovations.
In this talk, Miguel will explore how open-source technologies are advancing healthcare, with a focus on medical and surgical innovations. He will highlight key advancements while exploring the complexities of clinical translation, using three of his projects as examples: Fetal Ultrasound Image Synthesis, endoscopy-based video analysis for surgery, and real-time AI diagnosis of eye movement disorders. The talk will examine the challenges of clinical translation and showcase examples of innovative technologies that leverage open-source software, models, and data to address some of the most complex problems in healthcare. Finally, to inspire and spark innovation among the next generation of engineers, researchers, and clinicians from academia and industry, this talk will showcase how the emerging open-source software community for surgical and medical technologies is striving to: (a) Foster Collaboration and Community Building, (b) Enhance Security and Transparency, (c) Promote Customisation and Flexibility, (d) Ensure Cost-Effectiveness, Sustainability, and Scalability, and (e) Drive Rapid Innovation and Future-Proofing.

#### Related Links

- [The GitHub repository for this talk](https://github.com/mxochicale/open-healthcare-slides)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/NWWWXZ/feedback/)

---

### Active Tigger: Accelerating Collaborative Text Annotation for Social Sciences and Beyond

- **Speakers:** Emilien SCHULTZ
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 15:05 - 15:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5497-active-tigger-accelerating-collaborative-text-annotation-for-social-sciences-and-beyond/)

#### Abstract

This presentation introduces Active Tigger, an open-source research tool designed to accelerate collaborative text annotation in the social sciences.
The increasing use of text-as-data in social science research has created a pressing need for efficient annotation tools. While small datasets can be manually annotated, the exponential growth in available textual data (e.g., from newspapers and social media) demands solutions that enable collaborative annotation and automation. Moreover, the emergence of generative AI and large language models (LLMs) has highlighted the importance of robust corpus annotation practices, particularly for evaluating prompt-engineered outputs from LLM-as-a-service platforms like OpenAI or Hugging Face.
To address these challenges, we created an annotation platform, Active Tigger. A first version was developed in 2022 using R and RShiny (J. Boelaert, GitLab Repository). This tool embeds several annotation heuristics, including active learning—iteratively predicting and selecting annotations to maximize training quality—to help researchers build training datasets in order to fine-tuning encoder models. The tool quickly became integral to the research team's activities and beyond, which incited us to develop of a second, more robust version.
The current iteration of Active Tigger, built with a Python-based API and a React frontend, introduces enhanced flexibility and scalability. It supports collaborative workflows, accommodates a broader range of use cases, and is now in beta testing, with early adopters exploring its potential.
This presentation will cover three key aspects:
The journey of Active Tigger: From addressing specific social science needs to adapting to the evolving landscape of LLMs.
Showcase: Demonstrating the annotation workflow using active learning and BERT fine-tuning.
Future directions: Exploring the tool's evolution in the context of widespread LLM availability, discussing the trade-offs between focusing on specialized tasks and enabling broader applications.
Github repository of Active Tigger : https://github.com/emilienschultz/activetigger

#### Related Links

- [Github repository](https://github.com/emilienschultz/activetigger)
- [Slides](https://emilienschultz.github.io/atfosdem2025/#/title-slide)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TKAMM7/feedback/)

---

### PICO Scholar: Advancing Open Research with an Open-Source AI Platform

- **Speakers:** Cristina DeLisle, Matias Vizcaino
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 15:20 - 15:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6129-pico-scholar-advancing-open-research-with-an-open-source-ai-platform/)

#### Abstract

PICO Scholar is an open-source project at the proof-of-concept stage, developed by a team from Georgia Tech’s Master in Computer Science program with early guidance from Robert Gordon University (Andrews et al., 2023). Recently recognized with a 2nd place finish at the Red Hat & Intel AI Hackathon, PICO Scholar aims to tackle the growing challenge of sifting through massive, fast-evolving literature—whether in healthcare, engineering, or education. Traditional search tools often struggle with specialized terminology, inconsistent metadata, and a lack of transparent workflows. By integrating domain-adaptive AI and real-time collaboration features, our platform offers a more robust, efficient way for researchers to discover, analyze, and evaluate relevant studies.
We’re not just building another search engine—we’re creating an AI-driven collaboration hub designed to adapt across multiple domains and languages. As we move toward our first functional use case—helping conference organizers manage submissions—we’re actively seeking developers, researchers, and domain experts to guide our roadmap and expand the platform’s capabilities. Join us in making systematic reviews faster, more accurate, and truly open to all.
PICO Scholar GitHub repository
Join the PICO Scholar community questionnaire

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CEXE3H/feedback/)

---

### Human-Computer Counter-Choreographies

- **Speakers:** Joana
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 15:35 - 16:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4560-human-computer-counter-choreographies/)

#### Abstract

Human-Computer Counter-Choreographies is an artistic research project that combines critical design, choreography and embodied sense-making with data tracking. The project has evolved into various formats such as workshops, a live-coding performance piece, web-based tools and artworks.
In this talk, Joana Chicau will introduce the motivations behind the project and how it has impacted audiences by raising awareness of data tracking. She will also demo a custom version of the open-source DuckDuckGo privacy extension which unveils online tracking algorithms through audio and visual feedback.

#### Related Links

- [Gitlab Link for Human-Computer Counter-Choregraphies](https://gitlab.com/hc-cc/human-computer-counter-choregraphies)
- [Portfolio Website](https://joana.art/)
- [Web-based Artwork: Choreographing You](https://re-coding.technology/choreographing-you/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/A9NZPN/feedback/)

---

### Serving a Sustainable Coding Community: The INBO Coding Club Story

- **Speakers:** Damiano Oldoni, Dirk Maes, Oberon Geunens, Amber Mertens, Rhea Maesele, Emma Cartuyvels
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 16:00 - 16:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5480-serving-a-sustainable-coding-community-the-inbo-coding-club-story/)

#### Abstract

In January 2018, inspired by similar initiatives, a group of enthusiastic researchers at the Research Institute for Nature and Forest (INBO) launched a coding club. The INBO coding club was, is, and will continue to be a welcoming space for anyone interested in learning more about programming and data analysis, with a particular focus on ecological and environmental topics.
Our goal has always been to foster an environment of collaborative experimentation, where participants share code, learn from one another, and grow together—regardless of their level of experience. Everyone is encouraged to contribute, express their ideas freely, and engage as equals. We firmly believe that learning is a mutual process, independent of expertise levels, and that doing it together is not only more effective but also more enjoyable.
More than seven years—and a pandemic—later, the INBO R Coding Club remains vibrant and thriving. We are excited to share the strategies that have helped sustain this initiative, transforming initial enthusiasm into a widely recognized and enduring effort both within and beyond INBO. 
Key lessons learned include:
Learn together: Create a supportive space where every question is valued, and mistakes are celebrated as opportunities for growth.
As live as possible, as remote as necessary: Live coding in the same room is far more engaging and effective than remote sessions.
Community-driven evolution: The club should always prioritize the needs of its community, with feedback playing a central role in shaping its activities.
Dedication: A committed core team is essential for the consistent and sustainable organization of club activities.
Full openness: All session materials—including slides, code, and recordings—are freely available to everyone.

#### Related Links

- [Official website of the INBO coding club](https://coding-club.inbo.be/)
- [GitHub repository of the INBO coding club](https://github.com/inbo/coding-club)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QJKT3F/feedback/)

---

### Research 101: Promoting Diversity Through Open Science Literacy

- **Speakers:** Deborah Udoh
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 16:15 - 16:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5199-research-101-promoting-diversity-through-open-science-literacy/)

#### Abstract

In an era driven by data and digital collaboration, access to foundational research skills is increasingly essential—yet research capacity remains deeply unequal across the globe. For instance, Africa has only 20 health researchers per million people, compared to 246 per million in Europe, according to the World Health Organization’s Global Observatory on Health Research and Development. This stark disparity highlights the urgent need for accessible, inclusive research training to bridge the gap in global knowledge production.
Pre-Seeds (Research 101) is an open-source, community-driven initiative inspired by OLS’s capacity-building programs, such as Open Seeds and Nebula. The course is designed to break down barriers to research literacy and amplify underrepresented voices in open science. It is targeted at research enthusiasts, citizen scientists, early-career researchers, and Research Software Engineers (RSEs) from non-academic backgrounds. 
Currently in its early stages, Pre-seeds aims to create a flexible, modular curriculum covering key aspects of research often taken for granted, such as research design, ethical considerations, data management, and collaborative practices. The project leverages open tools like GitHub to promote collaboration, transparency, and reproducibility, inviting broad participation across disciplines and experience levels.
This session will present Pre-Seeds as a growing, collaborative effort to build an inclusive research ecosystem. By showcasing the project’s vision and its potential real-world applications, we’ll open the floor to feedback and invite attendees to join us in shaping this initiative—whether through expertise, funding, or community engagement—to co-create a more diverse and accessible future for open science.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YVDYJC/feedback/)

---

### Building Bridges Between Researchers, Technologists, and Infrastructure

- **Speakers:** Jonathan Starr
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 16:30 - 16:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5933-building-bridges-between-researchers-technologists-and-infrastructure/)

#### Abstract

Open science is at the forefront of transformative progress in research, yet its advancement is often stymied by fragmented infrastructure, limited interoperability, and inadequate crediting of research outputs. These challenges hinder the accessibility, reproducibility, and verification of research, slowing the pace of and trust in discovery and innovation.
This talk introduces the Scientific Coordination Infrastructure and Operating Systems Collaborative (SciOS) as a solution-oriented 501c3 (US non-profit) initiative to bridge the gap between researchers and technologists. SciOS facilitates the ongoing development of open, scalable, and interoperable infrastructure that empower the scientific community.
This talk will explore the rapid development of solutions possible when researchers and technologies exist in the same space.
Key Technologies and Innovations:


dPIDs and CODEX:
   Decentralized Persistent Identifiers (dPIDs) generate cryptographically unique, permanent identifiers for research artifacts. Combined with CODEX, an open system for managing versionable research objects, dPIDs ensure trust, reproducibility, and accessibility in scientific outputs.  


Journal Creation Software:
   SciOS supports tools that enable decentralized, community-driven curation-based journals. These platforms exist on an open repository of human knowledge accessible to everyone, and empower scientific communities to elevate from that repository research that aligns with their values, quality definitions, and scope with minimal friction.


DeSci Publish:
   Operating on CODEX, DeSci Publish redefines scientific publishing by allowing researchers to share data, code, manuscripts, and more as versionable objects. 


Granular Citation Systems:
   Through dPIDs, CODEX, and decentralized platforms, SciOS enables journals to credit contributions ranging from datasets and software to peer review and editorial work.


Automating Metadata Creation:
   In partnership with DeSci Labs and Discourse Graphs, SciOS automates the generation of metadata and discourse nodes. This initiative creates a map of research claims and evidence, allowing researchers to evaluate the relevance of prior work at a granular level.  


Research Assessment Tools:
   Collaborating with the CoARA ERIP working group, SciOS is developing tools that combine human expertise with AI to evaluate modular research objects. These tools enable clear, reliable assessments tailored for rapid response to research outputs.


Open Source Permanent Versionable Containers and Attestation Platform:
   SciOS supports this platform to create immutable repositories for software tools. It provides versionable digital containers enriched by community validations, enabling researchers and engineers to track, validate, and determine software impact across domains.  


Institute of Open Science Practices (IOSP):
   IOSP fosters collaboration between researchers and technologists, guiding the adoption of innovative infrastructure. It facilitates workshops and conferences powered by novel tools, enabling open science practices throughout the research lifecycle.  



Join us to explore how SciOS’s collaborative efforts and cutting-edge tools are transforming open science. Discover how decentralized infrastructure, automated metadata, and innovative publishing systems can break barriers, foster trust, and accelerate discovery across disciplines. Together, we can build the open science infrastructure the world needs.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MYHFDS/feedback/)

---

### Voluntary data sharing is broken: Data donation for scientific research as site of digital repair

- **Speakers:** Dwayne Ansah
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 16:55 - 17:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5849-voluntary-data-sharing-is-broken-data-donation-for-scientific-research-as-site-of-digital-repair/)

#### Abstract

In the digital age, the pervasive presence of the internet has fundamentally altered the landscape of capitalism, knowledge and human communication. However, alongside its transformative potential, voluntary data sharing in the public interest, or data donation, is plagued by systemic issues, ranging from lack of trust and privacy breaches to legal uncertainty, undermining its intended role as a democratizing force. 
Recognizing this brokenness, we turn to the concept of digital repair as a lens through which to understand and address these deficiencies. Drawing from social innovation and data governance theories, this abstract advances the sociology of repair centered on the concept of data altruism, the new EU framework for voluntary data sharing for objectives of general interest, including scientific research purposes. This talk explores the potential of data donation as a means to not only rectify the fractures in the digital data ecosystem, but also to stimulate a more socially sustainable data economy. 
By conceptualizing data donation within the framework of sociology of repair, this talk proposes its implications for reframing data agency, and advancing notions of digital constitutionalism. This talk is explicitly an effort to facilitate discussion about useful and plausible conceptual tools to theorize data donation. Through an ethnographically-informed investigation, this talk contributes to an understanding of the infrastructure enabling data altruism for scientific research purposes in the Netherlands, offering insights that are fruitful for navigating future research journeys into the European data economy.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/D9NZLK/feedback/)

---

### The conundrum challenges for Research Software and Research Data in Open Science

- **Speakers:** Teresa Gomez-Diaz
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 17:20 - 17:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4607-the-conundrum-challenges-for-research-software-and-research-data-in-open-science/)

#### Abstract

Abstract
The Borgman's conundrum challenges [1] have been initially formulated concerning the difficulties to share Research Data: which Research Data might be shared, by whom, with whom, under what conditions, why, and to what effects.
In our previous work, we have proposed a Research Software Definition [2] with a formulation that we have adapted in order to propose a Research Data definition [3,4].  We have thus constructed a framework to understand and to explain Research Software and Research Data in the Open Science context [5].
This framework is constructed in three stages: definition, dissemination, and evaluation of these research outputs [2,3,4], and it is now completed with answers to the Borgman's conundrum challenges for Research Data [3] and for Research Software [6].
In this talk we will present our answers to the Borgman's conundrum challenges,  and we will explain the comparison methodologies that we have developed in order to construct and to complete this Open Science framework.
It is our understanding that to provide correct and clear answers to the conundrum questions will have, as a consequence, the improvement of Research Software and Research Data sharing and dissemination practices, which, in turn, will enhance trustworthiness, correctness, rigor, reproducibility, reusability and transparency in the research endeavor.
This is a joint work with Prof. Tomas Recio, Universidad Antonio de Nebrija, Madrid.
This FOSDEM'25 presentation follows and extends our previous talks at FOSDEM:


[FOSDEM'21] Free/Open source Research Software production at the Gaspard-Monge Computer Science laboratory. Lessons learnt.
https://archive.fosdem.org/2021/schedule/event/open_research_gaspard_monge/


[FOSDEM'22] On the dissemination/evaluation loop for Research Software.
https://archive.fosdem.org/2022/schedule/event/open_research_cdur/


References
[1] Borgman, C.L. The conundrum of sharing research data. J Am Soc Inf Sci Tec 2012, 63, 1059–1078. 
https://doi.org/10.1002/asi.22634
[2] Gomez-Diaz, T.; Recio, T. On the evaluation of research software: the CDUR procedure [version 2; peer review: 2 approved]. F1000Research 2019, 8 1353. 
https://doi.org/10.12688/f1000research.19994.2
[3] Gomez-Diaz, T.; Recio, T. Research Software vs. Research Data I: Towards a Research Data definition in the Open Science context. [version 2; peer review: 3 approved]. F1000Research 2022, 11 118. 
https://doi.org/10.12688/f1000research.78195.2
[4] Gomez-Diaz, T.; Recio, T. Research Software vs. Research Data II: Protocols for Research Data dissemination and evaluation in the Open Science context. [version 2; peer review: 2 approved]. F1000Research 2022, 11 117.
https://doi.org/10.12688/f1000research.78459.2
[5] Gomez-Diaz, T.; Recio, T. Towards an Open Science definition as a political and legal framework: on the sharing and dissemination of research outputs. 

POLIS 2020, N. 19. https://doi.org/10.58944/yuro5734
Version 3, 2021, available at https://zenodo.org/doi/10.5281/zenodo.4577065

[6] Gomez-Diaz, T.; Recio, T. The conundrum challenges for Research Software in Open Science, Computers, 2024, 13(11), 302. 
https://doi.org/10.3390/computers13110302

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UJXP9H/feedback/)

---

### Beyond Compliance: Assessing Modern Slavery Statements using the Wikirate platform

- **Speakers:** Vasiliki Gkatziaki
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 17:45 - 18:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5448-beyond-compliance-assessing-modern-slavery-statements-using-the-wikirate-platform/)

#### Abstract

Modern slavery impacts millions of people worldwide, posing urgent ethical and human rights challenges In response, the UK and Australian Modern Slavery Acts require companies meeting specific revenue thresholds to produce annual modern slavery statements, aiming to increase accountability in addressing modern slavery risks. Since 2016, Walk Free and Wikirate have partnered to assess companies’ response to these Acts, leveraging Wikirate’s open-data platform. This assessment considers whether companies are releasing statements that meet the legal requirements, but also if they detail policies and actions that go beyond compliance to enable businesses to better respond to modern slavery. Key to this initiative is its open, collaborative approach, and therefore, a set of accessible metrics on Wikirate that empowers non-expert researchers to contribute meaningfully. Through the project, volunteers and researchers have conducted an in-depth analysis of over 2000 MSA statements. Over the years, the project has mobilized thousands of volunteers and engaged over 20 universities worldwide, using Wikirate’s crowdsourcing platform to organize and perform research at scale. The insights generated through the research not only inform Walk Free’s advocacy efforts with governments and companies but also demonstrate the power of open research principles in tackling complex global issues.

#### Related Links

- [Wikirate platform](https://wikirate.org)
- [Wikirate's github repository](https://github.com/wikirate/wikirate)
- [Beyond Compliance Dashboard (key findings of research)](https://beyondcompliance.wikirate.org/dashboard/all-sectors)
- [Corporate Reporting on Modern Slavery: A Dataset on Compliance and Beyond](https://wikirate.org/Corporate_Reporting_on_Modern_Slavery_A_Dataset_on_Compliance_and_Beyond)
- [swaggerhub documentation of Wikirate's REST API](https://app.swaggerhub.com/apis-docs/Decko/Wikirate/1.0.0)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DZEZVR/feedback/)

---

### Research Software, Sustainability, and RSEs

- **Speakers:** Daniel S. Katz
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 18:10 - 18:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6244-research-software-sustainability-and-rses/)

#### Abstract

Research software projects often are initially funded by a grant that supports development of the software. But when the grant ends, the projects have to shift to another model to support the required software maintenance, if the software is going to continue being used. This talk will look at the Parsl project and its effort to become sustainable, across a set of project phases. It will also look at the different kinds of RSE work that have taken place during the project. These activities, phases, and developer types appear to be useful concepts for planning or studying other research software projects, or research software as a whole.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/GF8CAL/feedback/)

---

### Applying the "Do No Harm" Principle to Open* Practices and Technology

- **Speakers:** Malvika Sharan
- **Room:** AW1.126
- **Day:** Saturday
- **Time:** 18:35 - 19:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6603-applying-the-do-no-harm-principle-to-open-practices-and-technology/)

#### Abstract

The "Do No Harm" principle, well-established in fields like medical research, healthcare, and humanitarian aid, has significant potential to improve the quality and reduce the negative effects of open research practices and technology.
As open research/science practices become a norm across different disciplines, it is important to identify, improve awareness of, and reduce its known or unintended negative impacts on people and their communities. While efforts like ethical source licenses (like the Do No Harm and Hippocratic License) are yet to become an acceptable legal pathway to enforcing responsible practices in open source, more general adoption and use of the "Do No Harm" will help account for societal and environmental implications of research and technology.
In this talk, I will introduce a “do no harm” framework to identify risks and develop actionable plans to mitigate the negative impacts of open research practices and technology. This framework examines the development and deployment of technology across four critical areas: the actors involved or affected, the dynamics and relationships within impacted communities, the economic realities faced by researchers, and environmental impact. Additionally, I will highlight practical methods for addressing the potential negative consequences of our work.
This session is designed for anyone involved in open source/science, including researchers, designers, contributors, developers, maintainers, and community members who seek to better understand and navigate the ethical challenges of open research and technology. Attendees will gain insights into global disparities in technology and explore how they can share responsibility to ensure their work promotes more equitable benefits by combining open practices with the do-no-harm principle.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-research:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-research:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PWRRHL/feedback/)

---

## Open Source Design (8)

### Design in 5 mins (okay, 20 mins): ecosystem mapping and user research? what is it and how to do it!

- **Speakers:** Antonia Valencia, caroline sinders
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 13:00 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5465-design-in-5-mins-okay-20-mins-ecosystem-mapping-and-user-research-what-is-it-and-how-to-do-it-/)

#### Abstract

Are you starting a new open source project or about to launch one? Understanding your project's value within its broader ecosystem, how it’s different and similar, how it interacts or impacts other projects, and how to talk about it in the wider open source community is crucial. This talk explores the importance of ecosystem mapping and user research from a design perspective, highlighting how these tools can uncover nuances of the interconnected roles of stakeholders, technologies, and communities, and how to use these skills if you’re a technologist, designer, project manager, or a combo of all three!  Join us to learn tips and tricks for embedding ecosystem thinking into your open source practice!

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-design:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-design:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8E7ZQW/feedback/)

---

### Thunderbird: Building a Cross-Platform, Scalable Open-Source Design System

- **Speakers:** Laurel Terlesky
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 13:30 - 13:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4876-thunderbird-building-a-cross-platform-scalable-open-source-design-system/)

#### Abstract

Explore Thunderbird's journey toward a cohesive, scalable, and data-informed open-source design system that unites desktop, Thunderbird for Android, and beyond. Building on the recent Supernova enhancements to the Thunderbird desktop interface and expanding into Android with Material 3 as our base, the need for a unified design approach has never been clearer.
Discover how open-source designers can help shape Thunderbird’s future. We’ll dive into creating a unified design system that’s consistent, collaborative, and open to community input, elevating the user experience across platforms. Whether you're a designer, developer, or curious contributor, see how you can be part of Thunderbird’s evolution.

#### Related Links

- [Thunderbird, open source email and productivity app (desktop and android)](https://www.thunderbird.net/en-US/)
- [Thunderbird Community Participation links](https://www.thunderbird.net/en-US/participate/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-design:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-design:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/99VQTP/feedback/)

---

### CLI Design for Designers and Developers

- **Speakers:** Hartmut Obendorf
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 14:00 - 14:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4832-cli-design-for-designers-and-developers/)

#### Abstract

OSS projects are used to not having a designer. What would you ask one if you had them available? To look at your Command Line Interface? This is why it is exactly what you should do. 
CLI Design isn't necessarily a natural thing for most designers, but it is a very impactful and fun way to involve yourself. Here, we will help you with some techniques, some thoughts, and some resources to start out.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-design:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-design:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/SWEHCC/feedback/)

---

### From Accessibility to Inclusion - Interdisciplinary Design

- **Speakers:** Raashi Saxena
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 14:30 - 14:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6054-from-accessibility-to-inclusion-interdisciplinary-design/)

#### Abstract

This talks explores the intersection of digital accessibility for people with disabilities with other disciplines, including language support, artificial intelligence, privacy and data protection, security, and safety widely used open-source tools and applications. For example, how does AI bias, dark patterns, and lack of language support lead to discrimination, and how can we across the FOSS community work together to ensure inclusion of everyone?
Digital accessibility for people with disabilities is an emerging topic that is unfortunately often approached with ambivalent feelings. Many designers meanwhile know of design accessibility and may even recognize the growing need to ensure design that is accessible to people with disabilities. Yet how to address accessibility across FOSS tools and applications is commonly not well understood, and there are often sensitivities and myths. For example, does security of tools exclude accessibility? How can a single design achieve both priorities? This includes the design of standards, polices, applications, and basically all open-source digital technologies which unfortunately commonly misses accessibility and the involvement of people with disabilities. The talk will raise hard questions about intersectionality approaches for inclusive design within the FOSS ecosystem. 
This session will attempt to map out some of the interfaces between different disciplines and what each can bring to a shared table of requirements, including accessibility, security, user experience design, usability, and more.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-design:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-design:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/QNKTMZ/feedback/)

---

### Piracy, and Open Source: Reimagining Creativity

- **Speakers:** Zekun Yang
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 15:00 - 15:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5322-piracy-and-open-source-reimagining-creativity/)

#### Abstract

This talk explores an unexpected connection between open source and piracy(intellectual property piracy)—two concepts often seen as opposites. While intellectual property laws are meant to protect innovation, they also create barriers, especially for underdeveloped nations, by restricting access to essential knowledge and resources. It deepens global inequalities and limit opportunities for creativity and growth.
To illustrate this, I will introduce China’s Shanzhai culture. Shanzhai is a Chinese term used to describe counterfeit, parody and it becomes a subculture known for creating knockoffs and bootlegs. Despite its controversial start, Shanzhai companies began developing their own innovative designs by responding to market needs. Over time, as China experienced rapid economic and technological growth, the country transitioned from the Shanzhai phase to a more innovation-driven future. Today, China ranks 11th in the Global Innovation Index, making it the only middle-income economy in the top 30 for 2024.
Like piracy, open source challenges traditional ownership models, but it offers a more inclusive and ethical way forward. By sharing tools, ideas, and technology openly, we break down barriers, foster collaboration, and build a creative ecosystem that includes everyone. This talk invites you to rethink how we approach intellectual property, innovation, and the future of creativity.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-design:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-design:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/CGCNZA/feedback/)

---

### Towards Free-Fair-Patterns: Free to Use, Free from Deceptive Patterns, Fair for All

- **Speakers:** Lorena Sánchez Chamorro
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 15:30 - 15:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6501-towards-free-fair-patterns-free-to-use-free-from-deceptive-patterns-fair-for-all/)

#### Abstract

How do we make open source really fair for all? Open-source designers and developers take a lot of ethical ownership of their projects. Despite this, there is always the danger of accidentally creating deceptive designs that steer users into choices harmful to them - aka dark patterns. We could help them with open designs by creating fair patterns, but where do we even start?
In the last years, I have studied and talked with different populations that are affected by these designs, and professional UX/UI designers that face the challenges related to deceptive designs. A repository of "fair patterns" or "bright patterns" as opposed to manipulative design is a necessary tool to mitigate these harmful designs, but the burden of creating these is very high. Open source design presents as a key to creating these patterns. In this talk, I will address the main problems that UX/UI designers face in the context of manipulative designs and discuss some unexpected challenges and potential solutions. With this I help the open source design community in creating more ethical interfaces with free-fair patterns: free from these deceptive patterns, free to use, and fair for all.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-design:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-design:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/H8ZVVU/feedback/)

---

### The Engineer’s Guide to Design: Merging Technical and Creative Skills in Open Source Projects

- **Speakers:** Khushi Garg
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 16:00 - 16:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4433-the-engineer-s-guide-to-design-merging-technical-and-creative-skills-in-open-source-projects/)

#### Abstract

In open-source projects, designers with technical backgrounds bring a unique perspective that bridges the gap between creative vision and practical implementation. This talk explores how understanding code, development workflows, and technical constraints can elevate design work in open-source environments, leading to smoother collaboration, more feasible designs, and faster iteration.
Drawing from my own journey from engineering to design, I’ll share practical techniques for creating developer-friendly design assets, communicating effectively with technical contributors, and using interactive prototypes to resolve UX issues early. 
I’ll also discuss methods for gathering and interpreting community feedback and offer tips on mentoring designers within open-source communities, helping them embrace a developer-centric approach. 
Attendees will walk away with actionable insights on integrating technical know-how into their design process, empowering them to create high-impact, accessible, and cohesive designs that enhance open-source projects for all.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-design:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-design:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UQ9JKA/feedback/)

---

### XWiki: Improving web accessibility with respect to backward compatibility

- **Speakers:** Lucas C
- **Room:** K.3.201
- **Day:** Sunday
- **Time:** 16:30 - 16:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5131-xwiki-improving-web-accessibility-with-respect-to-backward-compatibility/)

#### Abstract

XWiki is an open source software that has celebrated its twentieth birthday last year. This knowledge management web platform gives a lot of tools for users to customize it to their own needs. Because of this wide ecosystem, one of the most important properties of our software is backward compatibility. In the recent years, the need for our project to be up to standards concerning accessibility has arisen. I was in charge of improving the accessibility of XWiki standard. I'll show you the roadblocks we found as a community and the workarounds we used to improve accessibility without breaking (too much) backward compatibility.

#### Related Links

- [XWiki standard repository](https://github.com/xwiki/xwiki-platform)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-design:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-design:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8XPEXB/feedback/)

---

## Open Source Firmware, BMC and Bootloader (12)

### Open Source Firmware, BMC and Bootloader devroom - intro

- **Speakers:** Daniel Kiper
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 10:30 - 10:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6649-open-source-firmware-bmc-and-bootloader-devroom-intro/)

#### Abstract

A short introduction, history of devroom, and agenda.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bmc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bmc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/3HEHLV/feedback/)

---

### Multi-Profile UKIs and other ways to supercharge your Unified Kernel Images

- **Speakers:** Lennart Poettering
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 10:35 - 10:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5074-multi-profile-ukis-and-other-ways-to-supercharge-your-unified-kernel-images/)

#### Abstract

systemd-stub/ukify/systemd-measure recently acquire support for "multi-profile" UKIs (i.e. a UKI that can synthesize multiple boot menu entries instead of one, each with sligh varations in kernel command line and similar). It already gained support for carrying multiple DeviceTrees with automatic matching against local hardware. There is working in include multiple system firmwares inside UKIs for confidential computing bring-your-own-firmware cases. All this elevates UKIs to a new level, and in this talk I'd like to provide an overview of what's going on and where we are going.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bmc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bmc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LNCBC3/feedback/)

---

### wolfBoot: resilient, quantum-resistant secure boot for all architectures

- **Speakers:** Daniele Lacamera
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 11:00 - 11:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5180-wolfboot-resilient-quantum-resistant-secure-boot-for-all-architectures/)

#### Abstract

wolfBoot is an open source secure bootloader developed by wolfSSL Inc. and ported across many architectures.  This talk will describe real-life scenarios of deploying quantum resistant and hybrid secure boot mechanisms on embedded systems.
Initially designed in 2018 to implement secure boot on small microcontrollers (ARMv7 Cortex-M), wolfBoot has been then ported to several architectures including ARM Cortex-A, RISC-V, PowerPC, Renesas RX, and more recently it has been deployed in x86_64 as complete bios replacement with Intel FSP. On new ARMv8-M microcontrollers, it can supervise the secure domain and expose an interface to access cryptography from non-secure world.
Based on RFC9019, wolfBoot only uses static memory and has a predictable execution flow at compile time, which makes it suitable to use in safety-critical environments. It relies on wolfCrypt for public key authentication. It offers protection against rollbacks and has some advanced unique features such as delta updates and mitigations against fault injections. 
After briefly introducing the project, the talk will focus on the urge to migrate new systems towards securing boot with quantum resistant algorithms in the next decade.
We will explore the mechanisms currently provided by wolfBoot to pair PQC (ML-DSA, LMS, XMSS) with classic cryptography (ECC, RSA, ED) to authenticate the signature of the firmware at boot and upon updates.
Repository on github

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bmc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bmc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KHWNAT/feedback/)

---

### Building firmware with firmware-action

- **Speakers:** Vojtech Vesely, Marvin Drees
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 11:25 - 11:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5197-building-firmware-with-firmware-action/)

#### Abstract

At 9elements we do firmware, which is rather niche and complicated. As developing firmware is already difficult enough, we think that building / compiling it should not be. Which is the reason why we made firmware-action -- an automation tool to build firmware, powered by Dagger that can be used on your local machine as well as in CI/CD pipelines.
firmware-action is an open-source tool under MIT license available at https://github.com/9elements/firmware-action

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bmc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bmc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PANNM7/feedback/)

---

### Building flashless servers with Open Source Firmware for higher security and better flexibility

- **Speakers:** Jean-Marie Verdun
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 11:50 - 12:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6249-building-flashless-servers-with-open-source-firmware-for-higher-security-and-better-flexibility/)

#### Abstract

We will cover into that talk a new proposal to design and distribute open source firmware in the datacenter world by relying on secure boot from a single component (the BMC) and extensive attestation from the remaining part of a server. The BMC will starts from a network boot and load all required firmware (from PCIe end points, to microcontroller) from a trusted source before starting target. This approach is currently implemented on HPE Gen11 servers which supports Open Source Firmware. Our goal is to enhance security by decoupling the firmware and hardware supply chain, and allowing easier update process.

#### Related Links

- [CoreDHCP Discover plugin support for Automatic OpenBMC network distribution on BananaPI machines](https://github.com/vejmarie/coredhcp/tree/discover)
- [Automatic testing of systems running Open Source Firmware configuration through OpenBMC network boot device](https://github.com/opencomputeproject/OCP-OPF-Testing-and-Validation)
- [BananaPI R4 reference firmware with integrated coredhcp startup for automatic firmware distribution management](https://github.com/opencomputeproject/OCP-OPF-Backend)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bmc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bmc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/RLXM9X/feedback/)

---

### GRUB - Project Status Update

- **Speakers:** Daniel Kiper
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 12:15 - 12:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5781-grub-project-status-update/)

#### Abstract

The presentation will discuss current state of GRUB upstream development.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bmc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bmc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ZXJEQK/feedback/)

---

### Latest implementation of AMD SEV-SNP in OVMF

- **Speakers:** Richard Lyu
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 12:40 - 13:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5493-latest-implementation-of-amd-sev-snp-in-ovmf/)

#### Abstract

As confidential computing continues to gain importance, AMD SEV-SNP has matured within the open-source community. This session will provide an overview, from the OVMF perspective, of how it integrates with QEMU and the Linux Kernel to encrypt memory and safeguard memory security in a virtualized environment. The session is open to UEFI developers as well as virtualization, kernel, and security developers. Attendees will gain insights into how AMD SEV-SNP in confidential computing protects systems in virtualized environments, the latest upstream development progress, and an analysis of the protections it offers. The session will also address whether these protections are adequate and if there is a need to adopt this technology.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bmc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bmc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EXG7AZ/feedback/)

---

### no more boot loader: boot using the Linux kernel

- **Speakers:** Marta Lewandowska
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 13:05 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6469-no-more-boot-loader-boot-using-the-linux-kernel/)

#### Abstract

We will introduce nmbl (no more boot loader), our fast, secure boot scheme based on the Linux kernel.
GRUB is a powerful, flexible, fully-featured boot loader used by many distributions on multiple architectures, but its complexity is difficult to maintain, and it necessarily lags behind the Linux kernel exposing many security holes. The kernel itself, on the other hand, has a large developer base, fast feature development, quick responses to vulnerabilities, and much better overall scrutiny. Our approach is to use the Linux kernel as its own boot loader in the form of a unified kernel image (UKI). Loaded by the EFI stub on UEFI, an UKI is made up of all the components needed to reach the final boot target: the kernel, initramfs, and kernel command line, in one signed bundle. All necessary drivers, filesystem support, and networking are already built in and code duplication is avoided. 
We will describe the work and testing done so far and our approach to customization, as well as fallback, and hope for your feedback and use cases.

#### Related Links

- [project repo](https://github.com/rhboot/nmbl-poc/)
- [blog](https://fizuxchyk.wordpress.com/2024/06/13/nmbl-we-dont-need-a-bootloader/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bmc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bmc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HRKVSU/feedback/)

---

### TrenchBoot - project status update

- **Speakers:** Daniel Kiper, Maciej Pijanowski
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 13:30 - 13:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5979-trenchboot-project-status-update/)

#### Abstract

TrenchBoot is an open source project led by 3mdeb, Apertus Solutions, and Oracle. It aims at the security and integrity of the boot process by leveraging advanced silicon security features, like Intel Trusted Execution Technology (TXT) and AMD Secure Startup. It integrates with open source projects like GRUB2, Xen, and Linux, to perform a measured launch of the operating system software, also called Dynamic Root of Trust for Measurement (DRTM).
The presentation will provide an overview of the project's current status, emphasizing the key developments during the last year such as progress towards upstreaming patches in Linux and GRUB, as well as bringing UEFI support for Xen boot path.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bmc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bmc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/KCRP8U/feedback/)

---

### U-Boot ACPI support on ARM64

- **Speakers:** Patrick Rudolph
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 13:55 - 14:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6018-u-boot-acpi-support-on-arm64/)

#### Abstract

The Server Base Boot Requirements (SBBR) by ARM requires UEFI and ACPI support on AArch64 platforms.
While UEFI is already natively supported by U-Boot, ACPI support on ARM64 was only recently added.
A first patch series added basic support for booting Linux on QEMU's sbsa-ref machine, which doesn't provide a device-tree to the OS, but ACPI tables only. This is opening the path for U-Boot booting recent ARM server platforms using the SBBR specification.
The session gives an overview how ACPI tables are generated by U-Boot drivers. The challenges of integrating the ACPI subsystem with U-Boot's infrastructure on ARM64 are described and an outlook is provided.
Questions this talk should answer:
- How does the ACPI driver model work?
- How does this integrate with U-Boot?
- What to expect next in U-Boot's ACPI implementation?

#### Related Links

- ["Das U-Boot" Source Tree](https://source.denx.de/u-boot/u-boot)
- [U-Boot patch series - "Implement ACPI on aarch64"](https://lore.kernel.org/u-boot/20241023132116.970117-1-patrick.rudolph@9elements.com/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bmc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bmc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LQ3XSN/feedback/)

---

### WoA laptops: a quest for getting the right DTB

- **Speakers:** Dmitry Baryshkov, Christopher Obbard
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 14:20 - 14:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6224-woa-laptops-a-quest-for-getting-the-right-dtb/)

#### Abstract

Windows-on-ARM devices (primarily laptops) provide a nice execution environment for running Linux or any other open-source OS. As the provisioned ACPI tables make heavy use of PEP, it is next to impossible to make use of the ACPI in a proper way, This talk focuses on the the possible ways to select and sideload corresponding device tree blob before passing control to the OS kernel.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bmc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bmc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/E9WGYF/feedback/)

---

### Open Source Firmware, BMC and Bootloader devroom - outro

- **Speakers:** Piotr Król
- **Room:** UB4.136
- **Day:** Saturday
- **Time:** 14:40 - 14:45
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6650-open-source-firmware-bmc-and-bootloader-devroom-outro/)

#### Abstract

Closing notes and information about pPub (physical Pub) meetup.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-bmc:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-bmc:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BWTV7Q/feedback/)

---

## Open Source In The European Legislative Landscape and Beyond (34)

### Welcome to the EU Policy Devroom!

- **Speakers:** Simon Phipps
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 09:00 - 09:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-4081-welcome-to-the-eu-policy-devroom-/)

#### Abstract

Meet the DevRoom managers, hear how the day will run, ask any questions about these.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/S78SJK/feedback/)

---

### Room Changeover and Intro to the Implementation and Compliance Block

- **Speakers:** Jordan Maris
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 09:05 - 09:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6685-room-changeover-and-intro-to-the-implementation-and-compliance-block/)

#### Abstract

Room Changeover and Intro to the Implementation and Compliance Block

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PLWHY3/feedback/)

---

### An Introduction to the Open Source AI definition

- **Speakers:** Stefano Maffulli
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 09:10 - 09:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6724-an-introduction-to-the-open-source-ai-definition/)

#### Abstract

What does the AI Act mean for Open Source AI: A presentation by the European Commission. TBC

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/ESFB8U/feedback/)

---

### Why Europe needs the OSAID: Openwashing and the AI act

- **Speakers:** Jordan Maris
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 09:20 - 09:30
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6686-why-europe-needs-the-osaid-openwashing-and-the-ai-act/)

#### Abstract

In this talk, we'll discuss the Open Source Exemption in the AI Act, how it came about, why it's prompted a wave of Open washing, and how the Open Source AI Definition offers a solution.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PHYK7V/feedback/)

---

### Unlocking Transparency in Platforms’ Content Moderation Activities: Introducing dsa_tdb, a Python Package for Analyzing the Digital Services Act Transparency Database

- **Speakers:** Enrico Ubaldi, Lucas Verney
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 09:30 - 09:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5813-unlocking-transparency-in-platforms-content-moderation-activities-introducing-dsatdb-a-python-package-for-analyzing-the-digital-services-act-transparency-database/)

#### Abstract

The Digital Services Act (DSA) has introduced several transparency provisions for providers of online platforms, strengthening users’ rights to information about the content moderation systems they are subjected to. In particular, online platforms are obliged to inform their users of the content moderation decisions they take and explain the reasons behind those decisions in so-called Statements of Reasons (SoR). To enhance transparency and facilitate scrutiny over content moderation decisions, platforms have to submit these SoRs to a publicly available database, the “DSA Transparency Database", managed by the European Commission. 
This database allows to track a standardised set of metadata about each content moderation decision (with any personal data removed) taken by providers of online platforms in almost real-time. Its website also offers various tools for accessing, analyzing, and downloading the information related to the content moderation decisions taken by online platforms, contributing to the monitoring of the dissemination of illegal and harmful content online. 
However, due to their size and number of attributes, accessing and analyzing these data has been a significant challenge for researchers. To address this, the Transparency Database team has developed dsa_tdb, a Python package that enables users to easily access, analyze, and inspect the Statements of Reasons listed in the Transparency Database. 
This talk will showcase the capabilities of dsa_tdb, highlighting its potential for researchers, policymakers, and civil society organizations. We will demonstrate the wide array of tools that the package (and its containerized application) offers to users featuring different levels of technical knowledge, from quick dashboarding and visualizations to more advanced data processing. We will also show how the package can be used to uncover trends and patterns in platform content moderation activities and discuss the implications of these findings for the development of more transparent and accountable online ecosystems. 
In addition to presenting dsa_tdb, we will also discuss the broader transparency provisions introduced by the DSA, including the database tracking the online platforms’ terms and conditions, the Advertisement repositories, the Transparency reports, and the Transparency Database itself. We will explore how these provisions can be leveraged to promote greater transparency and accountability in the digital services sector, and discuss the challenges and opportunities associated with their implementation.
You can check the dsa_tdb code repository here: https://code.europa.eu/dsa/transparency-database/dsa-tdb
... as well as its online documentation: https://dsa.pages.code.europa.eu/transparency-database/dsa-tdb/

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/P8X7MF/feedback/)

---

### Presentation by the European Commission on the Cyber Resilience Act

- **Speakers:** Filipe Jones Mourao
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 09:40 - 09:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6687-presentation-by-the-european-commission-on-the-cyber-resilience-act/)

#### Abstract

Officials from the European Commission's Cybersecurity and Digital Privacy Policy (H2) Unit will come to present the implementation of the Cyber Resilience Act

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/AKWJJE/feedback/)

---

### Community-driven compliance: The CRA and the Open Regulatory Compliance Working Group

- **Speakers:** Tobie Langel
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 09:50 - 10:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6122-community-driven-compliance-the-cra-and-the-open-regulatory-compliance-working-group/)

#### Abstract

On November 20, 2024 the Cyber Resilience Act (CRA) was published in Official Journal of the European Union, starting a three year race for compliance by the global technology industry. This legislation sets new cybersecurity requirements that manufacturers and the open source projects they rely upon must meet.
In this presentation, we will explore how the Open Regulatory Compliance (ORC) Working Group of the Eclipse Foundation is collaborating in the open with numerous open source foundations, SMEs, and the industry to address the compliance obligations in the CRA.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JLCJR3/feedback/)

---

### Panel Discussion: Open Source and Policy Implementation: Lessons from the AI act, CRA and DSA

- **Speakers:** Simon Phipps, Tobie Langel, Filipe Jones Mourao
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 10:00 - 10:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6691-panel-discussion-open-source-and-policy-implementation-lessons-from-the-ai-act-cra-and-dsa/)

#### Abstract

In this panel discussion, we will delve into the current status of implementation of the CRA, examining how Standards will shape compliance, and the initiatives taken by the Community to overcome the challenges the CRA poses.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8FRZNH/feedback/)

---

### Workshops: DSA / AI / CRA

- **Speakers:** Jordan Maris
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 10:20 - 10:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6725-workshops-dsa-ai-cra/)

#### Abstract

The room will split into three workshops, with a first on the Digital Services Act, a second on Artificial Intelligence, and a third on the Cyber Resilience Act.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/YYDSFV/feedback/)

---

### Feedback from the Workshops on DSA / AI / CRA

- **Speakers:** Jordan Maris
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 10:50 - 11:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6688-feedback-from-the-workshops-on-dsa-ai-cra/)

#### Abstract

Wrap up by Implementation and compliance block organisers and Rapporteur feedback

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BHU79A/feedback/)

---

### Room changeover & Intro to the Public sector Open Source block

- **Speakers:** Axel Thévenet
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 11:00 - 11:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6692-room-changeover-intro-to-the-public-sector-open-source-block/)

#### Abstract

Room changeover & Intro to the Public sector Open Source block

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/WUKYAX/feedback/)

---

### Presentation from MEP Alexandra Geese

- **Speakers:** Axel Thévenet
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 11:10 - 11:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6693-presentation-from-mep-alexandra-geese/)

#### Abstract

Details to be confirmed

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/MPKM7Q/feedback/)

---

### Making Workspaces Work Together (And Across Borders)

- **Speakers:** Alexander Smolianitski, samuel paccoud
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 11:20 - 11:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6406-making-workspaces-work-together-and-across-borders-/)

#### Abstract

Ensuring digital sovereignty has become a critical concern for governments in Europe. On February 7, 2024, France and Germany took a significant step forward by announcing their collaboration towards creating sovereign digital workspaces for their public administrations. This session brings together representatives from DINUM (French Interministerial Digital Directorate) and ZenDiS (the German Centre for Digital Sovereignty), who are co-developing La Suite Numérique (France) and openDesk (Germany). Both initiatives prioritise open-source solutions in developing their respective digital suites. DINUM and ZenDiS thus demonstrate that digital sovereignty relies heavily on close international collaboration. In their joint presentation, they discuss strategies of cooperation between their complementary initiatives, shedding light on potential opportunities for future collaboration within the broader open source community.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/UEURJZ/feedback/)

---

### openDesk and beyond: building the EuroStack

- **Speakers:** Vittorio Bertola
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 11:35 - 12:00
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5729-opendesk-and-beyond-building-the-eurostack/)

#### Abstract

In Europe, there is now wide agreement that we need to build our "sovereign" alternatives to dominant big tech products and services, and that they need to be based on open source. However, which policies would be the right ones to reach the objective? What should governments do: write code, fund code, fund companies, fund maintainers, hire maintainers, whatever? Should they mandate the adoption of European and/or open software by policy? Should they leave everything to the market? The openDesk case can provide some useful insight on what can work in practice. The goal of this discussion will be to touch upon the recent debates surrounding the establishment of a Eurostack while comparing this to the practical realities of the development of open source in the European public sector.
This discussion will de done together with Alexandra Geese and Alexander Smolianitski.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/9TJEW8/feedback/)

---

### Digital Identies in disarray

- **Speakers:** Gregor "Little Detritus" Bransky, Amelia Andersdotter
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 12:00 - 12:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6510-digital-identies-in-disarray/)

#### Abstract

eIDAS 2.0 was proposed under the assumption that all EU citizens would be required to hold a hardware trust anchor for their electronic identity. However, a proposal to introduce such an obligatory hardware was struck down in June 2024 and an adapted version could not guarantee the provisioning of eID cards before 2031. 
This has left the implementation of eIDAS 2.0 in disarray. While real challenges exist which are causing economic harm to entire sectors, politicians remain focused on social media use-cases. Meanwhile, industry self-regulation is not capable of producing authenticators of sufficiently robust fundamental rights protections. Hardware anchored solutions are beneficial to industries in some member states, while software anchored solutions leave more space for industries in others. 
We will present the arising problems with regards to fundamental rights, national security and the challenge to find solutions for the time until 2031. We will focus on the European situation, while not ignoring the impact of foreign influencers like Mark Zuckerberg and Ashton Kuchner, or the impact of the recent Australian social media ban for children on the attention span of European legislators.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/DJ8NDE/feedback/)

---

### Accelerating Digital Transformation in Europe: The Role of Digital Public Goods and Open Source Collaboration

- **Speakers:** Amreen Taneja
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 12:10 - 12:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5850-accelerating-digital-transformation-in-europe-the-role-of-digital-public-goods-and-open-source-collaboration/)

#### Abstract

Digital Public Goods (DPGs) are essential for achieving the United Nations Sustainable Development Goals (SDGs). Defined as open-source software, open data, open AI models, and open content that meet privacy, security, and interoperability best practices, DPGs offer governments the tools to build equitable, transparent, and sustainable digital systems.
This session highlights recent advancements in the DPG Standard—the framework for vetting and recognizing DPGs—alongside collaborative efforts, such as UNICEF’s leadership in scaling DPGs globally. It will also explore successful implementations in Europe through a practical example from Primero (UNICEF): A DPG helping social service workers manage sensitive data related to child protection and gender-based violence. 
By focusing on these tools’ adoption and alignment with the DPG Standard, the session will demonstrate how collaboration between organizations and governments is fostering digital sovereignty, interoperability, and public sector innovation in Europe.
Attendees will gain actionable insights into how the DPG Standard and DPGs like Primero are enabling governments to create scalable, transparent, and resilient digital ecosystems.
Proposed Format:


Introduction: DPGs and the DPG Standard 
Overview of DPGs, their role in advancing the SDGs, and how the DPG Standard ensures trust, security, and interoperability.


Key updates to the DPG Standard, including:


--Enhanced privacy requirements.
--  Ethical AI provisions for transparency and accountability.

UNICEF’s Showcase: Primero and their European Implementations
Highlighting Primero as a transformative DPG for managing child protection and gender-based violence data.
Success stories of Primero’s implementation in various regions, with a focus on its impact and potential in Europe.

Collaborative efforts between UNICEF, governments, and partners to scale Primero and ensure alignment with the DPG Standard.


Closing Remarks 

Summarizing the complementary roles of the DPG Standard, DPG implementations, and collaboration efforts in Europe.
Closing call to action: Encouraging policymakers and developers to adopt and contribute to DPGs as part of Europe’s digital transformation journey. 

This will be followed up with a fishbowl discussion on how DPGs are being leveraged for Government collaborations.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/N9YJZZ/feedback/)

---

### Digital Commons as Pillars of Digital Sovereignty in Europe

- **Speakers:** Nicholas Gates
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 12:25 - 12:35
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6132-digital-commons-as-pillars-of-digital-sovereignty-in-europe/)

#### Abstract

This session will explore all the latest thinking around Digital Commons as a policy priority for Europe. The concept of Digital Commons – highly open and shared digital resources which are maintained and governed by communities – represents a transformative approach to building a more open and equitable digital ecosystem. Through the Next Generation Internet (NGI) Commons project, supported by the European Commission, ‘Europe’ as such is developing an intellectual and policy basis for investing in and supporting Digital Commons as providers of public digital infrastructures that support European digital sovereignty and advance European values around digital-era governance.

#### Related Links

- [NGI Commons Workshop 2024: A Summary Report](https://commons.ngi.eu/2024/07/08/ngi-commons-workshop-2024-a-summary-report/)
- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/8L7TFM/feedback/)

---

### Public Sector Open Source fishbowl

- **Speakers:** Axel Thévenet
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 12:35 - 12:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6694-public-sector-open-source-fishbowl/)

#### Abstract

Public Sector Open Source fishbowl: 
This interactive discussion will highlight different policy approaches for promoting the use of open source in government, both in Europe and beyond. In particular, it will be discussed how the European Commission is using the notion of Digital Commons more as a tool to focus policymaking and investment around open technologies, in comparison to the efforts of many other international organisations -- like the UN, World Bank, and others -- which are using the language of Digital Public Goods and using this to guide policy making and investment, particularly in the development and humanitarian sectors. The discussion will give some time to the question of public infrastructures based on open source and real world use cases for DPGs and Digital Commons in Europe. Significant space will be given to audience participation, allowing for questions from, and participation of, the audience.
This discussion will include Nicholas Gate, Amreen Taneja and Bolaji Ayodeji.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EDELUD/feedback/)

---

### Wrap up by Public Sector Open Source block organisers

- **Speakers:** Axel Thévenet
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 12:55 - 13:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6703-wrap-up-by-public-sector-open-source-block-organisers/)

#### Abstract

Wrap up by Public Sector Open Source block organisers and Rapporteur feedback

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JP8K3S/feedback/)

---

### Room Changeover and Intro to Open source strategy for competitiveness block

- **Speakers:** Sebastian Raible
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 13:05 - 13:10
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6695-room-changeover-and-intro-to-open-source-strategy-for-competitiveness-block/)

#### Abstract

Room Changeover and Intro to Open source strategy for competitiveness block

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/LHP8TD/feedback/)

---

### Open Source as a Cultural Movement: Europe's Call to Action for a Fair and Sustainable Future

- **Speakers:** Stefano Pampaloni
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 13:10 - 13:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6492-open-source-as-a-cultural-movement-europe-s-call-to-action-for-a-fair-and-sustainable-future/)

#### Abstract

The growing concentration of power and capital in the hands of a few large tech companies is putting our democracy at risk and hindering fair and sustainable development. These companies control vast amounts of data and exert disproportionate influence over politics and public institutions, leveraging an extractive economic model that undermines digital sovereignty and collective well-being.
In this talk, I will discuss how Europe can take an active role in promoting open source as a concrete cultural reaction against turbo capitalism. The collaborative model of open source represents an opportunity to build a sustainable and inclusive digital ecosystem, capable of contributing to the Sustainable Development Goals (SDGs) and ensuring greater technological sovereignty. Specifically, we will explore the potential of European policies to support open source and limit the disproportionate influence of big tech, while promoting values such as transparency, participatory innovation, and sharing.
The aim is to stimulate reflection on how Europe can lead the shift toward a technological system that is not only innovative but also fair and democratic through the adoption and promotion of open source software.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/EJTQKW/feedback/)

---

### Building Europe's Platform Mesh: Cloud-Native APIs for Multi-Provider Integration and Digital Sovereignty

- **Speakers:** Mirza Kopic, Marvin Beckers
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 13:25 - 13:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5746-building-europe-s-platform-mesh-cloud-native-apis-for-multi-provider-integration-and-digital-sovereignty/)

#### Abstract

The open source Platform Mesh project, part of the EU initiative IPCEI-CIS, is a framework for a multi-provider cloud-edge continuum that should span the European continent. Some of the central questions the project wants to answer are: How can the different service offerings across a wide array of providers be unified? How can they communicate in a common language?
We discuss how a combination of Cloud Native building blocks that emerged from the Kubernetes ecosystem (kcp and kube-bind, among others) could be used to create the foundation for the next generation of cloud platforms.
We demonstrate a prototype which meshes together declarative APIs that allows us to consume services across multiple control plane instances, instantiating what we call the “Platform Mesh”. As an outlook, we connect the development of declarative APIs to ongoing European developments coming from the upcoming regulations on switching data processing services from within the Data Act, and possible future legislation fostering interoperability in the cloud native computing landscape.
This talk is a call for action for how to build the next level of European platforms, addressing key European Union objectives in cloud computing sovereignty and standardization.
We will conclude by discussing how this reference architecture aligns with broader EU initiatives in technological sovereignty and cross-border digital service integration
Links
- https://www.kcp.io/ (framework behind platform mesh)
- https://apeirora.eu/ (project initiative)
- https://www.ecofed.eu/ (collaborators)

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/TLLBGG/feedback/)

---

### Building Public-Private Open Source Ecosystems: GFOSS's approach in Academic-Industry Collaboration

- **Speakers:** Alexandros Melidis
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 13:40 - 13:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5669-building-public-private-open-source-ecosystems-gfoss-s-approach-in-academic-industry-collaboration/)

#### Abstract

GFOSS (Greek Free/Open Source Software Society), with its 16 year history as an umbrella organization representing 37 academic institutions and research centers, is expanding its membership model to include private IT companies through an innovative approach that goes beyond traditional industry representation and participation. This talk presents our framework for creating meaningful academic-industry collaboration in open technologies, including staff exchange programs between member companies and universities, targeted career development initiatives, and collaborative open source project development through projectathons and hackathons.
We will share our vision for a dynamic ecosystem where private sector membership in GFOSS offers a value proposition that includes direct access to academic research and talent pools, participation in joint research projects, opportunities for private sector staff to engage in academic teaching and research and pathways for commercial adoption of academic open source projects. 
The framework also addresses practical aspects such as revenue-based tiered membership fees, balanced voting mechanisms, and special provisions for startups. Our primary focus is on creating sustainable, mutually beneficial relationships between academia and industry that advance open source adoption and innovation. Insights gained from GFOSS framework approach will inform future policy proposals at both national and European levels, particularly regarding research funding mechanisms, public procurement specifications, and innovation support programs.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BHPGNZ/feedback/)

---

### European Competitiveness in Microelectronic and AI

- **Speakers:** Florian 'Flo' Wohlrab, Frédéric Desbiens
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 13:50 - 14:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6675-european-competitiveness-in-microelectronic-and-ai/)

#### Abstract

Just recently the EU is putting extreme effort on Microelectronics, accelerated by the awakening of AI and our realization of it's importance. How can the EU catch up on Microelectronics fast? Open standards and open source is in our view a must ingredient to enable EU companies into a competitive stage and therefore a solid open source system to draw from is important.
Most of Microelectronic development has been happening in USA and various Asian countries while in the EU except for established, traditional players, not much new (innovations) has happened. With the arrival of AI and more real use cases, the need of a strong, competitive Microelectronic industry has arrived and the European Union has realized it's importance and putting more resources to make sure we are in a competitive and self sustaining position in this key technology.
While the field is complex there is a big value add in the design (creation) of chips.
Investment into microelectronics are high with various parts being used in each project, such as CPU's (Central Processing Units) being the brain of any digital Chip. With RISC-V as an open standard of how to structure that CPU and not for profits such as OpenHW Foundation we can leverage a industry proven, high quality platform, allowing European established players but also startups to jump start their time to market by re-using and sharing proven building blocks, saving time and money and allowing much more testing and also potential interaction between companies and research units.
Programs such as Tristan or Isolde, initiated by the Chips JU are a proven way to build the base for a sovereign and independent yet innovative European Union and we will highlight some cases how it is used from big players such as Thales or Bosch but also startups like Axelera AI and a variety of small medium Businesses and what was possible so far, while also critical asking: Is it enough and what could be done more?
In this Talk the OpenHW Foundation a global non profit, Headquartered in Brussels is showing the recent successes especially in Europe, what is ongoing and where we should pay more attention.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/K7EH7J/feedback/)

---

### OSS 4 ALL: What can policymakers do to increase the uptake of OSS in the EU?

- **Speakers:** Francesco Panella
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 14:05 - 14:20
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-5589-oss-4-all-what-can-policymakers-do-to-increase-the-uptake-of-oss-in-the-eu-/)

#### Abstract

Duration:
15 minutes (this can be adjusted and shortened if necessary)
Format:
Speedstorming
Context:
OSS has become a cornerstone of innovation, collaboration, and digital sovereignty in Europe. However, its widespread adoption and integration into both public and private sectors face numerous challenges. Despite its benefits-including enhanced transparency, reduced costs, and technological independence-various actors, from corporations to grassroots to public entities, remain hesitant to adopt OSS solutions.
Objectives:
This session will engage the participants in speedstorming exercise to take up one challenge, proposing one policy action to reduce the OSS adoption barriers. 
Expected results:
Through insights gathered from this co-creation session, the workshop aims to contribute to exchanges with the European Commission’s Units dealing with the European digital ecosystem, providing grassroots perspectives that reflect the real needs of OSS users and contributors. The outputs will feed into the work carried out by Martel Innovate and Digital for Planet on EU-funded cooperation projects in shaping policy roadmaps. They will directly inform projects like NGI Commons, NGI4ALL.E and NexusForum.EU, which aim to bridge the European digital ecosystem and communities with European Commission priorities.
Structure:
The session will be composed of a short introduction (5 minutes) and an interactive exercise (10 minutes).
>     Speakers
Monique Calisti (CEO - Martel Innovate and President - Digital 4 Planet) and Francesco Panella (Policy analyst and consultant, Martel Innovate)

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/HD9PF3/feedback/)

---

### Panel Discussion: A European Strategy for Digital Sovereignty

- **Speakers:** Sebastian Raible, Marcel Kolaja (Policy and Advocacy Director for Europe at Access Now, former MEP)
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 14:20 - 14:55
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6698-panel-discussion-a-european-strategy-for-digital-sovereignty/)

#### Abstract

Panel Discussion: A European Strategy for Digital Sovereignty

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/VTLHH9/feedback/)

---

### Wrap up by Open Source strategy for competitiveness block organisers and Rapporteur feedback

- **Speakers:** Sebastian Raible
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 14:55 - 15:05
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6704-wrap-up-by-open-source-strategy-for-competitiveness-block-organisers-and-rapporteur-feedback/)

#### Abstract

Wrap up by Open Source strategy for competitiveness block organisers and Rapporteur feedback

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/FKB7BS/feedback/)

---

### Room Changeover and Intro to the Open Source in the policymaking process block

- **Speakers:** Jordan Maris
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 15:05 - 15:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6699-room-changeover-and-intro-to-the-open-source-in-the-policymaking-process-block/)

#### Abstract

Room Changeover and Intro to the Open Source in the policymaking process block

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/BWZBMS/feedback/)

---

### Opening Speech by Markéta Gregorová, Member of the European Parliament

- **Speakers:** Markéta Gregorová
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 15:15 - 15:25
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6700-opening-speech-by-markta-gregorov-member-of-the-european-parliament/)

#### Abstract

Opening Speech by Markéta Gregorová, Member of the European Parliament (Greens/EFA)

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/U83TFT/feedback/)

---

### Lobbying the EU

- **Speakers:** Jules Obry, Jordan Maris, Sebastian Raible
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 15:25 - 15:40
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6410-lobbying-the-eu/)

#### Abstract

How do the EU institutions work, and how do I make my voice heard as an activist? What is on the agenda, and how do I find out? How do I identify allies? What about the national and regional level?

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/XUFNCA/feedback/)

---

### Towards Open Source-Compatible Standards

- **Speakers:** Tobie Langel
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 15:40 - 15:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6111-towards-open-source-compatible-standards/)

#### Abstract

As policy makers are rushing towards standardizing open source security best practices, it is critical to make sure that the standards developed to organize open source software development and maintenance are themselves open source-compatible. Why is this important? What makes a standard open source-compatible? What can we learn from previous efforts such as OpenStand and what can we improve? We'll cover this and more in this talk.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/JK8MYY/feedback/)

---

### Panel: European Standardisation and the Open Source community

- **Speakers:** Simon Phipps, Tobie Langel, Jordan Maris, fukami, Filipe Jones Mourao
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 15:50 - 16:15
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6696-panel-european-standardisation-and-the-open-source-community/)

#### Abstract

Standardisation experts from the Eclipse Foundation, OpenSSF, the Open Source Initiative, and the European Commission talk about Standardisation, Open Source, the interplay between the two, and the impact on EU law.

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/PFHEEN/feedback/)

---

### Open Source in the policymaking process: Fishbowl discussion

- **Speakers:** Simon Phipps
- **Room:** AW1.120
- **Day:** Sunday
- **Time:** 16:15 - 16:50
- **Event Page:** [Link](https://fosdem.org/2025/schedule/event/fosdem-2025-6702-open-source-in-the-policymaking-process-fishbowl-discussion/)

#### Abstract

Open Source in the policymaking process: Fishbowl discussion

#### Related Links

- [Chat room(web)](https://chat.fosdem.org/#/room/#2025-eu-policy:fosdem.org)
- [Chat room(app)](https://matrix.to/#/#2025-eu-policy:fosdem.org?web-instance[element.io]=chat.fosdem.org)
- [Submit Feedback](https://pretalx.fosdem.org/fosdem-2025/talk/A8A9V3/feedback/)

---


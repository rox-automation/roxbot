---
draft: false
date: 2023-11-20
categories:
  - development
  - gui
  - can
---

# Plotting live data with Plotjuggler

Containerization is crucial for a reliable CI/CD workflow, but it can be challenging when you need live data visualization, especially for things like tuning motion control.

The good news? There's a simple solution. Just send your data to Plotjuggler using a UDP socket. I've included a code example below to show you how it's done. It's straightforward yet still packs in all the features you need.

Need to analyze data quickly? Just use the UDP_Client from the example. With just a few lines of code, you're all set.

Happy coding!

![Plotjuggler](img/motor_pos.png)

<!-- more -->

```python
--8<-- "code/udp_plot.py"
```

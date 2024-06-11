# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## Planned

* gps node (`gps-node` branch)


## Unreleased

## v2.2.0

* add `examples/node.py` - classless node implementation
* add `adapters.mqtt_logger.MqttLogger` that forwards python logging to a mqtt topic
* rename `bridges` to `adapters`. Also rename `MqttBridge` to `MqttAdapter`. This is to avoid confusion with
stand-alone [mqtt-bridge](https://gitlab.com/roxautomation/components/mqtt-bridge)

## v2.1.0
    * move vectors to `rox-vectors` package.


## v2.0.0
    * initial release after move to github and refactoring.

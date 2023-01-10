# JSON Referencing Test Suite

This repository contains a set of test cases that implementers of JSON referencing specifications can use to test their implementations.

It is meant to be language agnostic and should require only a TOML parser.
The conversion of the TOML objects into tests within a specific language and test framework of choice is left to be done by the implementer.

This suite is inspired by the [official JSON Schema Test Suite](https://github.com/json-schema-org/JSON-Schema-Test-Suite), where some of its tests originated.
Indeed JSON referencing is heavily influenced by JSON Schema, and it is only [recently](https://github.com/json-schema-org/referencing) that discussions have begun to formalize JSON referencing in a more cross-specification-amenable way.

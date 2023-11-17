# Design Patterns Python Implementation

This Python project aims to provide a comprehensive implementation of various design patterns categorized into three main types: creational, behavioral, and structural. Design patterns are reusable solutions to common problems encountered in software design, promoting code maintainability, flexibility, and scalability.

## Table of Contents

- [Creational Patterns](#creational-patterns)
- [Behavioral Patterns](#behavioral-patterns)
- [Structural Patterns](#structural-patterns)
- [Usage](#usage)

## Creational Patterns
Object creation.

### 1. Singleton Pattern
- Implementation of the Singleton pattern ensures that a class has only one instance and provides a global point of access to it.

### 2. Factory Method Pattern
- The Factory Method pattern defines an interface for creating an object but lets subclasses alter the type of objects that will be created.

### 3. Abstract Factory Pattern
- Abstract Factory pattern provides an interface to create families of related or dependent objects without specifying their concrete classes.

### 4. Builder Pattern
- The Builder pattern separates the construction of a complex object from its representation, allowing the same construction process to create various representations.

### 5. Prototype Pattern
- Prototype pattern creates new objects by copying an existing object, known as the prototype.

## Behavioral Patterns
Object interaction and responsibility.

### 1. Observer Pattern
- Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

### 2. Strategy Pattern
- The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. It lets the algorithm vary independently from clients that use it.

### 3. Command Pattern
- Command pattern encapsulates a request as an object, thereby allowing for parameterization of clients with different requests, queuing of requests, and logging of the requests.

### 4. Chain of Responsibility Pattern
- Chain of Responsibility pattern passes the request along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

### 5. State Pattern
- State pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

## Structural Patterns
Object composition.

### 1. Adapter Pattern
- Adapter pattern allows incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces by converting the interface of a class into another interface that a client expects.

### 2. Decorator Pattern
- Decorator pattern attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

### 3. Proxy Pattern
- Proxy pattern provides a surrogate or placeholder for another object to control access to it.

### 4. Composite Pattern
- Composite pattern composes objects into tree structures to represent part-whole hierarchies. It lets clients treat individual objects and compositions of objects uniformly.

### 5. Bridge Pattern
- Bridge pattern decouples abstraction from implementation so that the two can vary independently.

## Usage

To use this library, simply clone the repository and import the desired design pattern module into your Python project. Follow the example codes and documentation provided for each pattern to integrate them seamlessly into your application.

```python
from design_patterns.singleton import Singleton

# Example of using the Singleton pattern
instance = Singleton.get_instance()

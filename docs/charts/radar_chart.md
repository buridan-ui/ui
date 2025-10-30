---
title: "Radar Chart"
description: "A versatile chart for visualizing quantitative data trends over time or categories, supporting gradients, stacking, and custom legends."
order: 0
---

# Radar Chart

Radar Charts are ideal for showing changes over time or the magnitude of multiple datasets stacked together. They combine the smoothness of line charts with the visual impact of filled areas.

# Usage
Copy the following helper functions into your Reflex application.

--FULL_SOURCE_PAGE_OF_COMPONENT(info)--

# Examples
Below are examples demonstrating how these components and charts can be used.

## Basic
A minimal example showing multivariate data in a radial layout with filled areas.
--DEMO_AND_SINGLE_FUNCTION(radar_v1)--

## Stroke with Dots
Displays data points with visible markers along the radar lines for clarity.
--DEMO_AND_SINGLE_FUNCTION(radar_v2)--

## Stacked
Visualizes multiple data series layered on top of each other for comparison.
--DEMO_AND_SINGLE_FUNCTION(radar_v3)--

## Lines Only
Shows only the outline strokes without filled areas for a cleaner look.
--DEMO_AND_SINGLE_FUNCTION(radar_v4)--

## Circle Grid
Uses circular grid lines instead of polygon shapes for the background.
--DEMO_AND_SINGLE_FUNCTION(radar_v5)--

## Filled Grid
Renders the grid with filled background sections for enhanced visual contrast.
--DEMO_AND_SINGLE_FUNCTION(radar_v6)--

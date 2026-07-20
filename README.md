# Learning Manim: Math Animations

## 🚀 Getting Started

These animations are built using the **Manim Community Edition (ManimCE)**.

### Prerequisites
We need to have Python, FFmpeg, and a LaTeX distribution installed on our system.

### Installation
```bash
pip install manim
```

### Running the Code
To render any of the scenes locally, navigate to the script directory and run:
```bash
manim -pql filename.py SceneName
```
* `-p`: Preview the video automatically after rendering.
* `-ql`: Render in Low Quality (480p, 15fps) for fast testing. Use `-qh` for High Quality (1080p, 60fps).

---

## 📊 Projects & Visualizations

### 1. Statistical Animations (Chi-Square Distribution)
These advanced scenes explore probability density functions (PDFs) and geometry mapping for statistical distributions.

#### Chi-Square Visualization
Visual explanation of data mapping and geometric properties of the Chi-Square distribution.
<video src="distributions\media\videos\1.1.chi-square\1080p60\ChiSquareViz.mp4" controls width="100%"></video>

#### Chi-Square Plotting
Dynamic graphing of the Chi-Square curve with changing degrees of freedom.
<video src="distributions/media/videos/1.chi-square/1080p60/ChiSquarePlot.mp4" controls width="100%"></video>

---

### 2. Personal Learning & Concept Demos
Experimental animations created while practicing camera movements, text layout, and custom transformations.

#### Concept Demo
<video src="Personal-learning/media/videos/2/1080p60/demo.mp4" controls width="100%"></video>

---

### 3. Foundation Tutorials (Shape Basics)
Core foundational scripts practicing `Mobject` creation, transformation, and placement.

#### Create Circle
Basic rendering using the `Create` animation engine.
<video src="manim_community/tutorials/media/videos/tutorials/480p15/CreateCircle.mp4" controls width="100%"></video>

#### Square to Circle
Morphing a polygon into a curve using `Transform`.
<video src="manim_community/tutorials/media/videos/tutorials/480p15/SquareToCircle.mp4" controls width="100%"></video>

#### Replacing Square by Circle
An alternative transition using `ReplacementTransform`.
<video src="manim_community/tutorials/media/videos/tutorials/480p15/ReplacingSquareByCircle.mp4" controls width="100%"></video>

#### Square and Circle
Managing multiple objects simultaneously on a single screen layout.
<video src="manim_community/tutorials/media/videos/tutorials/480p15/SquareAndCircle.mp4" controls width="100%"></video>

---

## 🛠️ Built With
* [Manim Community Edition](https://manim.community) - The math animation engine.
* Python - Programming language.

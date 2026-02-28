# 🎬 Video Processing Automation Toolkit

A Python-based video automation toolkit built to streamline repetitive editing tasks during freelancing projects.

This project automates:

* ⏱️ Intro trimming (bulk cutting first few seconds)
* 🎨 Logo removal (color-based masking & replacement)
* 🔊 Audio preservation after frame processing
* 📁 Batch processing for entire folders

Built to eliminate manual editing overhead and improve turnaround time.

---

## 🚀 Why This Project?

During video editing freelancing assignments, I repeatedly had to:

* Remove branded intros
* Trim fixed duration segments from hundreds of videos
* Remove yellow logo overlays
* Preserve original audio
* Process videos in bulk

Manual editing was inefficient and non-scalable.

So I engineered an automated Python pipeline to handle everything programmatically.

---

# 🏗️ Architecture Overview

The project contains two independent processing modules:

## 1️⃣ `videocut` – Intro Removal Automation

### 🔹 Tech Stack

* `moviepy`
* `os`

### 🔹 What It Does

* Removes a fixed time range from the beginning of videos
* Preserves remaining video content
* Processes entire folders automatically
* Re-encodes using `libx264`

### 🔹 Core Logic

```python
remaining_video = video.subclip(cut_end, video.duration)
```

### 🔹 Features

* Duration validation
* Batch processing support
* Configurable cut time
* Automatic output folder creation

---

## 2️⃣ `logocut` – Logo Removal via Color Masking

### 🔹 Tech Stack

* `OpenCV (cv2)`
* `NumPy`
* `moviepy`
* `time`
* `os`

### 🔹 Processing Pipeline

1. Read video frame-by-frame
2. Convert frame to HSV color space
3. Detect yellow logo using HSV thresholding
4. Identify contours
5. Replace detected region with white overlay
6. Reconstruct video
7. Re-attach original audio using MoviePy

### 🔹 Yellow Detection Range

```python
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
```

### 🔹 Key Techniques Used

* HSV Color Space segmentation
* Contour detection (`cv2.findContours`)
* Bounding box extraction
* Frame-level modification
* Audio-video recombination
* Temporary intermediate file handling

---

# 📂 Folder Structure

```
video-automation/
│
├── videocut.py
├── logocut.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/video-automation.git
cd video-automation
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Required Dependencies

```
moviepy
opencv-python
numpy
```

> ⚠️ Ensure FFmpeg is installed and added to system PATH.

---

# ▶️ Usage

## 🔹 Trim First 4.2 Seconds From All Videos

```python
input_folder = 'G:/EDITED/Math/2022'
output_folder = 'E:/savedVideo/2022'
cut_start = 0
cut_end = 4.2

process_videos(input_folder, output_folder, cut_start, cut_end)
```

---

## 🔹 Remove Yellow Logo From Videos

```python
input_folder = 'E:/savedVideo/2022'
output_folder = 'E:/editedVideos/2014'

process_videos_in_folder(input_folder, output_folder)
```

---

# 📊 Performance Considerations

* Time complexity proportional to total frame count
* Frame-by-frame processing impacts large videos
* Temporary `.avi` used for intermediate storage
* Re-encoding cost depends on resolution & FPS
* CPU-bound (no GPU acceleration implemented)

---

# 🧠 Engineering Decisions

| Decision                    | Reason                 |
| --------------------------- | ---------------------- |
| HSV instead of RGB          | Better color isolation |
| Frame-level processing      | Precise logo detection |
| Separate audio reattachment | Avoid audio loss       |
| Batch folder support        | Scalability            |
| Temporary video file        | OpenCV compatibility   |

---

# 🔮 Future Improvements

* GPU acceleration (CUDA)
* Smart object removal instead of white masking
* Configurable color ranges
* CLI interface
* Docker containerization
* Async / multiprocessing support
* Progress bar integration (tqdm)

---

# 💼 Business Impact

This automation:

* Reduced manual editing time significantly
* Enabled high-volume video processing
* Improved delivery consistency
* Increased freelancing throughput
* Eliminated repetitive manual work

---

# 📌 Example Use Cases

* YouTube intro trimming
* Batch preprocessing before upload
* Removing fixed-position watermarks
* Educational video processing
* Content repurposing workflows

---

# 🏁 Final Note

This project demonstrates applied computer vision, media processing, and automation engineering used in real freelancing production environments.

If you're working with repetitive video editing workflows — automate it.

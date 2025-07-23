# 🕵️ Professional Image Lie Detection Tool

An AI-powered facial expression and micro-expression analysis tool for detecting deception and lying indicators in images.

## ✨ Features

- 🎯 **Professional Analysis**: Multi-dimensional analysis based on psychology and micro-expression theory
- 👁️ **Eye Analysis**: Eye contact, blink frequency, pupil changes, and other indicators
- 😐 **Facial Micro-expressions**: Expression duration, symmetry, forced expression detection
- 🤸 **Body Language**: Head posture, facial orientation, overall tension level
- 💫 **Emotional Consistency**: Expression-emotion matching analysis
- 📊 **Detailed Reports**: Structured JSON format analysis results

## 🚀 Quick Start

### Requirements

- Python 3.7+
- [Ollama](https://ollama.ai/) local runtime environment
- Supported AI models (recommended: `gemma3:12b`)

### Install Dependencies

```bash
pip install requests
```

### Install Ollama Model

```bash
# Install recommended model
ollama pull gemma3:12b

# Start Ollama service
ollama serve
```

## 📖 Usage

### Basic Usage

```bash
python lie_detector.py <image_path>
```

### Specify Model

```bash
python lie_detector.py <image_path> <model_name>
```

### Examples

```bash
# Analyze with default model
python lie_detector.py person.jpg

# Analyze with specific model
python lie_detector.py person.jpg gemma3:12b
```

## 📊 Analysis Results

The tool provides detailed analysis across the following dimensions:

### Overall Assessment
- **Lie Probability**: 0.0-1.0 probability score
- **Truthfulness Score**: 1-10 credibility rating
- **Confidence Level**: Reliability of analysis results
- **Overall Impression**: Comprehensive evaluation description

### Detailed Analysis
- **Eye Analysis**: Eye contact, blink patterns, pupil response
- **Facial Micro-expressions**: Expression duration, facial symmetry, muscle tension
- **Body Language**: Head position, facial orientation, overall tension
- **Emotional Consistency**: Expression matching, emotional conflict analysis

### Indicator Identification
- **Deception Indicators**: List of potential lying signs
- **Truthfulness Indicators**: Evidence supporting honesty

## ⚠️ Important Disclaimer

**This tool is for educational and research purposes only. Analysis results are for reference only and cannot be used as:**
- Evidence in legal proceedings
- Medical or psychological diagnostic basis
- Sole basis for any formal decision-making

Human expressions and behaviors are influenced by multiple factors including cultural background, personal habits, emotional states, etc. Please treat analysis results rationally.

## 🛠️ Technical Architecture

- **Language**: Python 3
- **AI Engine**: Ollama local deployment
- **Image Processing**: Base64 encoding transmission
- **Analysis Method**: Based on psychological micro-expression theory
- **Output Format**: Structured JSON + user-friendly display

## 📝 Output Example

```
🎯 Overall Assessment:
   🎲 Lie Probability: 0.35 (0=honest, 1=lying)
   ✅ Truthfulness Score: 7/10
   🔍 Confidence Level: 0.82
   💭 Overall Impression: Natural expression with slight tension indicators

🔬 Detailed Analysis:
   👁️  Eye Analysis:
      • Good eye contact, no obvious avoidance
      • Normal blink frequency
   
   😐 Facial Micro-expressions:
      • Appropriate smile duration
      • Facial expressions basically symmetrical
```

## 🤝 Contributing

Issues and Pull Requests are welcome to improve this project!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 🔗 Related Resources

- [Ollama Official Website](https://ollama.ai/)
- [Micro-expression Psychology Basics](https://en.wikipedia.org/wiki/Microexpression)
- [Facial Action Coding System (FACS)](https://en.wikipedia.org/wiki/Facial_Action_Coding_System)

---

**⭐ If this project helps you, please give it a Star!**
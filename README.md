<h1 align="center" id="title">Battery Performance Analysis System</h1>

<p id="description">An advanced analysis system that evaluates battery performance through comprehensive measurement of electrolyte resistance (Re), charge transfer resistance (Rct), and battery impedance during charge and discharge cycles. The project utilizes sophisticated data processing and visualization techniques to provide detailed insights into battery behavior and performance metrics.</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="shields">
<img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white" alt="shields">
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="shields">
</p>

<h2>🧐 Features</h2>

Here are some of the project's key features:

* **Comprehensive Battery Analysis**: Measures key performance indicators including Re, Rct, and Battery Impedance.
* **Dual-Mode Analysis**: Separate analysis for both charge and discharge cycles.
* **Advanced Data Processing**: Sophisticated algorithms for processing raw battery data.
* **Interactive Visualizations**: Plotly-based interactive charts for detailed performance analysis.
* **Comparative Analysis**: Side-by-side comparison of charge and discharge characteristics.
* **Batch Processing**: Handles multiple battery datasets efficiently.
* **Data Validation**: Robust error checking and data validation.

<h2>💻 Built with</h2>

Technologies used in the project:

* **Python**: Core programming language.
* **Plotly**: Interactive data visualization.
* **Pandas**: Data manipulation and analysis.
* **NumPy**: Numerical computations.
* **Custom Data Processing Algorithms**.

<h2>📊 Visualization Examples</h2>

The system generates interactive Plotly charts showing:

- Electrolyte Resistance (Re) comparisons:
  <p align="center">
    <img src="/home/psyk/Desktop/cleaned_dataset/images/charge_Re.png" alt="Electrolyte Resistance (Charge)">
    <img src="/home/psyk/Desktop/cleaned_dataset/images/discharge-Re.png" alt="Electrolyte Resistance (Discharge)">
    <img src="/home/psyk/Desktop/cleaned_dataset/images/combined_re.png" alt="Electrolyte Resistance (Combined)">
  </p>

- Charge Transfer Resistance (Rct) analysis:
  <p align="center">
    <img src="/home/psyk/Desktop/cleaned_dataset/images/charge_rct.png" alt="Charge Transfer Resistance (Charge)">
    <img src="/home/psyk/Desktop/cleaned_dataset/images/discharge_rct.png" alt="Charge Transfer Resistance (Discharge)">
    <img src="/home/psyk/Desktop/cleaned_dataset/images/combined_rct.png" alt="Charge Transfer Resistance (Combined)">
  </p>

- Battery Impedance measurements:
  <p align="center">
    <img src="/home/psyk/Desktop/cleaned_dataset/images/charge_bi.png" alt="Battery Impedance (Charge)">
    <img src="/home/psyk/Desktop/cleaned_dataset/images/discharge_bi.png" alt="Battery Impedance (Discharge)">
    <img src="/home/psyk/Desktop/cleaned_dataset/images/combined_bi.png" alt="Battery Impedance (Combined)">
  </p>

<h2>🛠️ Installation Steps:</h2>

<p>1. Download the repository from drive link:</p>

```

```
<p>2. Create and activate virtual environment:</p>

```
python -m venv venv
venv\Scripts\activate # Windows
```
```
source venv/bin/activate # Linux/Mac
```

<p>3. Install required dependencies:</p>

```
pip install -r requirements.txt
```

<p>4. Prepare your data:</p>

- Place battery data files in the `data` directory.
- Ensure `metadata.csv` is properly formatted.
- Verify file paths in configuration.

<p>5. Run the analysis:</p>

```
python3 plotting.py
```

<h2>📊 Output Examples</h2>

The system provides:

* Individual battery performance metrics.
* Comparative analysis between batteries.
* Performance visualizations including:
  - Re (Electrolyte Resistance)
  - Rct (Charge Transfer Resistance)
  - Battery Impedance.
* Both charge and discharge cycle analysis.

<h2>🔒 Data Processing</h2>

* Automated data validation.
* Statistical analysis.
* Performance metric calculations.
* Comprehensive error handling.
* Batch processing capabilities.

<h2>🚧 Future Roadmap</h2>

* Implement machine learning for performance prediction.
* Add temperature correlation analysis.
* Real-time monitoring capabilities.
* Enhanced statistical analysis.
* Automated report generation.
* Battery health prediction.

<h2>📂 Dataset</h2>

The project uses the [NASA Battery Dataset](https://www.kaggle.com/datasets/patrickfleith/nasa-battery-dataset/data) from Kaggle, which provides comprehensive data on battery performance across various conditions.

<h2>🛡️ License:</h2>

This project is licensed under the MIT License.

<h2>💖 Like my work?</h2>

This project needs a ⭐️ from you. Don't forget to leave a star ⭐️

<h2>🙏 Acknowledgments</h2>

* Battery research community.
* Python scientific computing community.
* Plotly visualization library.
* Open-source contributors.

---
<p align="center">Developed by Abhash Goyal. For inquiries, contact abhashgoyal200@gmail.com.</p>
<p>Linkedin: https://www.linkedin.com/in/abhashgoyal-4692b91b8/</p>

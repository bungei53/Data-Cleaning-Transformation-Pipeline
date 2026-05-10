import os
from data_processor import DataProcessor
from pipeline import TransformationPipeline
from visualization import Visualizer

def main():
    # Setup
    output_dir = "../outputs"
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Generate Data
    print("Generating synthetic messy data...")
    raw_df = DataProcessor.generate_messy_data(200)
    raw_df.to_csv("../data/raw_data.csv", index=False)
    
    # 2. Run Pipeline
    pipeline = TransformationPipeline()
    cleaned_df, records = pipeline.run_end_to_end(raw_df)
    
    # 3. Save Results
    cleaned_df.to_csv("../data/cleaned_data.csv", index=False)
    
    # 4. Visualize
    print("Generating visualizations...")
    Visualizer.plot_age_distribution(cleaned_df, "../outputs/age_dist.png")
    Visualizer.plot_cholesterol_trends(cleaned_df, "../outputs/cholesterol_box.png")
    
    print("Pipeline execution complete. Check 'outputs/' folder.")

if __name__ == "__main__":
    main()

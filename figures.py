import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def plot_model_scores(original_scores, n_samples=112):
    # Use a bold font for all text
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.labelweight'] = 'bold'
    
    # Model names with line breaks for Claude versions
    original_models = [
        'o1-preview',  # 0.848
        'Gemini 1.5 Pro',  # 0.786
        'ChatGPT 4o',  # 0.759
        'Claude 3.5 Sonnet\n(20240620)',  # 0.756
        'Claude 3.5 Sonnet\n(20241022)',  # 0.804
        'Llama 3.1 405B',  # 0.688
        'Mistral Large 2'  # 0.580
    ]
    
    # Create pairs and sort by score
    pairs = list(zip(original_models, original_scores))
    pairs.sort(key=lambda x: x[1], reverse=True)
    
    # Unzip the sorted pairs
    models, scores = zip(*pairs)
    scores = list(scores)
    
    # Calculate confidence intervals
    confidence_intervals = []
    for score in scores:
        std_err = np.sqrt((score * (1 - score)) / n_samples)
        ci = stats.norm.interval(0.95, loc=score, scale=std_err)
        confidence_intervals.append((ci[1] - score, score - ci[0]))
    
    # Convert to numpy arrays for easier manipulation
    errors = np.array(confidence_intervals).T
    
    # Create the plot with larger figure size
    plt.figure(figsize=(14, 7))
    x = np.arange(len(models))
    
    # Create bars
    bars = plt.bar(x, scores, color='lightcoral', alpha=0.7)
    
    # Add error bars
    plt.errorbar(x, scores, yerr=errors, fmt='none', color='gray', capsize=5)
    
    # Customize the plot
    plt.ylim(0, 1.0)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Increase font sizes significantly and make bold
    plt.xticks(x, models, rotation=45, ha='right', fontsize=14, weight='bold')
    plt.yticks(fontsize=14, weight='bold')
    plt.ylabel('Score', fontsize=16, weight='bold')
    
    # Add value labels on top of each bar with larger, bold font
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}',
                ha='center', va='bottom',
                fontsize=14,
                weight='bold')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    return plt

# Example usage with scores matching the original model order:
scores = [0.848, 0.786, 0.759, 0.756, 0.804, 0.688, 0.580]
plt = plot_model_scores(scores)
plt.show()

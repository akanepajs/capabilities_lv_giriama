import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def wilson_score_interval(p, n, z=1.96):
    denominator = 1 + z**2/n
    center = (p + z**2/(2*n))/denominator
    spread = z * np.sqrt(p*(1-p)/n + z**2/(4*n**2))/denominator
    return center - spread, center + spread

def plot_model_scores(original_scores, n_samples=112, color='lightcoral'):
    # Create new figure
    plt.figure(figsize=(6, 4.5))  # Slightly taller to accommodate rotated labels
    
    # Use a bold font for all text
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.labelweight'] = 'bold'
    
    original_models = [
        'o1-preview',
        'Claude',
        'Gemini',
        'Llama',
        'GPT-4o',
        'Mistral'
    ]
    
    # Create pairs and sort by score
    pairs = list(zip(original_models, original_scores))
    pairs.sort(key=lambda x: x[1], reverse=True)
    
    # Unzip the sorted pairs
    models, scores = zip(*pairs)
    scores = list(scores)
    
    # Calculate Wilson score intervals
    confidence_intervals = []
    for score in scores:
        lower, upper = wilson_score_interval(score, n_samples)
        confidence_intervals.append((upper - score, score - lower))
    
    errors = np.array(confidence_intervals).T
    
    x = np.arange(len(models))
    
    # Create bars
    bars = plt.bar(x, scores, color=color, alpha=0.7)
    
    # Add error bars
    plt.errorbar(x, scores, yerr=errors, fmt='none', color='gray', capsize=10)
    
    plt.ylim(0, 1.0)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Rotate labels 45 degrees and adjust alignment
    plt.xticks(x, models, rotation=45, ha='right', fontsize=14, weight='bold')
    plt.yticks(fontsize=14, weight='bold')
    plt.ylabel('Score', fontsize=16, weight='bold')
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}',
                ha='center', va='bottom',
                fontsize=14,
                weight='bold')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()

# Rest of the code remains the same
def get_significance_level(score, best_score, n_samples):
    if score == best_score:
        return ''
    
    # Perform two-proportion z-test
    z_stat = (best_score - score) / np.sqrt(best_score*(1-best_score)/n_samples + score*(1-score)/n_samples)
    p_value = 1 - stats.norm.cdf(z_stat)
    
    # Return appropriate number of asterisks based on p-value
    if p_value < 0.001:
        return '***'
    elif p_value < 0.01:
        return '**'
    elif p_value < 0.05:
        return '*'
    return ''

def generate_latex_table(english_scores, latvian_scores, latvian_auto_scores, giriama_scores, n_samples=112):
    # Create model names and scores pairs
    models = ['o1-preview', 'Claude', 'Gemini', 'Llama', 'GPT-4o', 'Mistral']
    data = list(zip(models, english_scores, latvian_scores, latvian_auto_scores, giriama_scores))
    
    # Find best scores and indices for each language
    best_english = max(english_scores)
    best_latvian = max(latvian_scores)
    best_latvian_auto = max(latvian_auto_scores)
    best_giriama = max(giriama_scores)
    
    # Calculate averages
    avg_english = np.mean(english_scores)
    avg_latvian = np.mean(latvian_scores)
    avg_latvian_auto = np.mean(latvian_auto_scores)
    avg_giriama = np.mean(giriama_scores)
    
    # Generate table
    table = """\\begin{table}[t]
\\centering
\\footnotesize
\\begin{tabular}{@{}lcccc@{}}
\\hline
\\textbf{Model} & \\textbf{English} & \\textbf{Latvian} & \\textbf{Latvian (AT)} & \\textbf{Giriama} \\\\
\\hline"""
    
    # Add model rows
    for model, eng, lat, lat_auto, gir in data:
        # Get significance levels
        eng_stars = get_significance_level(eng, best_english, n_samples)
        lat_stars = get_significance_level(lat, best_latvian, n_samples)
        lat_auto_stars = get_significance_level(lat_auto, best_latvian_auto, n_samples)
        gir_stars = get_significance_level(gir, best_giriama, n_samples)
        
        # Make scores bold if they're the highest in their column
        eng_fmt = f"\\textbf{{{eng:.3f}}}" if eng == best_english else f"{eng:.3f}"
        lat_fmt = f"\\textbf{{{lat:.3f}}}" if lat == best_latvian else f"{lat:.3f}"
        lat_auto_fmt = f"\\textbf{{{lat_auto:.3f}}}" if lat_auto == best_latvian_auto else f"{lat_auto:.3f}"
        gir_fmt = f"\\textbf{{{gir:.3f}}}" if gir == best_giriama else f"{gir:.3f}"
        
        row = f"\n{model} & {eng_fmt}{eng_stars} & {lat_fmt}{lat_stars} & {lat_auto_fmt}{lat_auto_stars} & {gir_fmt}{gir_stars} \\\\"
        table += row
    
    # Add average row
    table += f"""
\\hline
\\textbf{{AVG}} & \\textbf{{{avg_english:.3f}}} & \\textbf{{{avg_latvian:.3f}}} & \\textbf{{{avg_latvian_auto:.3f}}} & \\textbf{{{avg_giriama:.3f}}} \\\\
\\hline
\\end{{tabular}}
\\caption{{Model performance across languages. AT: autotranslated. Each model: n={n_samples}; AVG: n={n_samples*6}. Boldface indicates the highest score in each column. Asterisks indicate statistically significant differences from the highest-scoring model within each language variant (*: p<0.05, **: p<0.01, ***: p<0.001).}}
\\label{{tab:model-comparison}}
\\end{{table}}"""
    
    return table

# Data
latvian_scores = [0.848, 0.804, 0.786, 0.688, 0.759, 0.580]
english_scores = [0.875, 0.866, 0.846, 0.839, 0.821, 0.768]
latvian_auto_scores = [0.821, 0.777, 0.732, 0.643, 0.723, 0.580]
giriama_scores = [0.643, 0.482, 0.509, 0.411, 0.464, 0.348]

# Generate plots
plot_model_scores(latvian_scores, color='lightcoral')
plot_model_scores(english_scores, color='lightblue')
plot_model_scores(giriama_scores, color='lightgreen')
plt.show()

# Generate and print the table
latex_table = generate_latex_table(english_scores, latvian_scores, latvian_auto_scores, giriama_scores)
print(latex_table)

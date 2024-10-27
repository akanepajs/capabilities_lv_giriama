import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Wilson Score Interval Calculation
def wilson_score_interval(p, n, z=1.96):
    denominator = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denominator
    spread = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denominator
    return center - spread, center + spread

# Plot Model Scores with Improved Contrast
def plot_model_scores(original_scores, n_samples=112, color='#1f77b4'):
    plt.figure(figsize=(6, 4.5))
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['axes.labelweight'] = 'bold'
    plt.rcParams['axes.facecolor'] = '#f0f0f0'

    # Split model names manually into two parts
    original_models_parts = [
        ['o1-preview-', '2024-09-12'],
        ['claude-3-5-sonnet-', '20241022'],
        ['gemini-1.5-', 'pro-002'],
        ['Meta-Llama-3.1-405B-', 'Instruct-Turbo'],
        ['gpt-4o-', '2024-08-06'],
        ['mistral-large-', '2407']
    ]

    # Create two-line labels
    original_models = [f'{part1}\n{part2}' for part1, part2 in original_models_parts]

    pairs = list(zip(original_models, original_scores))
    pairs.sort(key=lambda x: x[1], reverse=True)
    models, scores = zip(*pairs)
    scores = list(scores)

    confidence_intervals = []
    for score in scores:
        lower, upper = wilson_score_interval(score, n_samples)
        confidence_intervals.append((upper - score, score - lower))

    errors = np.array(confidence_intervals).T
    x = np.arange(len(models))
    bars = plt.bar(x, scores, color=color, alpha=0.85)

    plt.errorbar(x, scores, yerr=errors, fmt='none', color='#333333', capsize=10)
    plt.ylim(0, 1.0)
    plt.grid(True, axis='y', linestyle='--', color='#cccccc', alpha=0.7)

    # Removed bold from x-axis labels but kept it for other elements
    plt.xticks(x, models, rotation=45, ha='right', fontsize=12, weight='normal', color='#333333')
    plt.yticks(fontsize=14, weight='bold', color='#333333')
    plt.ylabel('Score', fontsize=16, weight='bold', color='#333333')

    # Add more bottom margin to accommodate rotated two-line labels
    plt.subplots_adjust(bottom=0.25)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height, f'{height:.3f}',
                 ha='center', va='bottom', fontsize=14, weight='bold', color='#333333')

    plt.tight_layout()

# [Rest of the code remains exactly the same...]

# Sample Data
latvian_scores = [0.848, 0.804, 0.786, 0.688, 0.759, 0.580]
english_scores = [0.875, 0.866, 0.846, 0.839, 0.821, 0.768]
latvian_auto_scores = [0.821, 0.777, 0.732, 0.643, 0.723, 0.580]
giriama_scores = [0.643, 0.482, 0.509, 0.411, 0.464, 0.348]

# Generate Plots with Different Colors for Contrast
plot_model_scores(latvian_scores, color='#1f77b4')  # Latvian scores in blue
plot_model_scores(english_scores, color='#ff7f0e')  # English scores in orange
plot_model_scores(giriama_scores, color='#2ca02c')  # Giriama scores in green
plt.show()

# Generate LaTeX Table
def generate_latex_table(english_scores, latvian_scores, latvian_auto_scores, giriama_scores, n_samples=112):
    models = ['o1-preview-2024-09-12', 'claude-3-5-sonnet-20241022', 'gemini-1.5-pro-002', 'Meta-Llama-3.1-405B-Instruct-Turbo', 'gpt-4o-2024-08-06', 'mistral-large-2407']
    data = list(zip(models, english_scores, latvian_scores, latvian_auto_scores, giriama_scores))

    best_english = max(english_scores)
    best_latvian = max(latvian_scores)
    best_latvian_auto = max(latvian_auto_scores)
    best_giriama = max(giriama_scores)

    avg_english = np.mean(english_scores)
    avg_latvian = np.mean(latvian_scores)
    avg_latvian_auto = np.mean(latvian_auto_scores)
    avg_giriama = np.mean(giriama_scores)

    table = """\\begin{table}[t]
\\centering
\\footnotesize
\\begin{tabular}{@{}lcccc@{}}
\\hline
\\textbf{Model} & \\textbf{English} & \\textbf{Latvian} & \\textbf{Latvian (AT)} & \\textbf{Giriama} \\\\
\\hline"""

    for model, eng, lat, lat_auto, gir in data:
        eng_stars = get_significance_level(eng, best_english, n_samples)
        lat_stars = get_significance_level(lat, best_latvian, n_samples)
        lat_auto_stars = get_significance_level(lat_auto, best_latvian_auto, n_samples)
        gir_stars = get_significance_level(gir, best_giriama, n_samples)

        eng_fmt = f"\\textbf{{{eng:.3f}}}" if eng == best_english else f"{eng:.3f}"
        lat_fmt = f"\\textbf{{{lat:.3f}}}" if lat == best_latvian else f"{lat:.3f}"
        lat_auto_fmt = f"\\textbf{{{lat_auto:.3f}}}" if lat_auto == best_latvian_auto else f"{lat_auto:.3f}"
        gir_fmt = f"\\textbf{{{gir:.3f}}}" if gir == best_giriama else f"{gir:.3f}"

        row = f"\n{model} & {eng_fmt}{eng_stars} & {lat_fmt}{lat_stars} & {lat_auto_fmt}{lat_auto_stars} & {gir_fmt}{gir_stars} \\\\"
        table += row

    table += f"""
\\hline
\\textbf{{AVG}} & \\textbf{{{avg_english:.3f}}} & \\textbf{{{avg_latvian:.3f}}} & \\textbf{{{avg_latvian_auto:.3f}}} & \\textbf{{{avg_giriama:.3f}}} \\\\
\\hline
\\end{{tabular}}
\\caption{{Model performance across languages. AT: autotranslated. Each model: n={n_samples}; AVG: n={n_samples*6}. Boldface indicates the highest score in each column. Asterisks indicate statistically significant differences from the highest-scoring model within each language variant (*: p<0.05, **: p<0.01, ***: p<0.001).}}
\\label{{tab:model-comparison}}
\\end{{table}}"""

    return table

# Sample Data
latvian_scores = [0.848, 0.804, 0.786, 0.688, 0.759, 0.580]
english_scores = [0.875, 0.866, 0.846, 0.839, 0.821, 0.768]
latvian_auto_scores = [0.821, 0.777, 0.732, 0.643, 0.723, 0.580]
giriama_scores = [0.643, 0.482, 0.509, 0.411, 0.464, 0.348]

# Generate Plots with Different Colors for Contrast
plot_model_scores(latvian_scores, color='#1f77b4')  # Latvian scores in blue
plot_model_scores(english_scores, color='#ff7f0e')  # English scores in orange
plot_model_scores(giriama_scores, color='#2ca02c')  # Giriama scores in green
plt.show()

# Generate and Print LaTeX Table
latex_table = generate_latex_table(english_scores, latvian_scores, latvian_auto_scores, giriama_scores)
print(latex_table)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


#CompTotal
#AIThreat


data = pd.read_csv("survey_results_public.csv")


y = data[(data['ConvertedCompYearly'].notna()) & (data['AIThreat'] == "Yes")]
n = data[(data['ConvertedCompYearly'].notna()) & (data['AIThreat'] == "No")]


def print_stats(arr, name=""):
    suffix = f"_{name}" if name else ""
    print(f"x{suffix} = {np.mean(arr)}")
    print(f"s{suffix} = {np.std(arr)}")
    print(f"n{suffix} = {arr.size}")
    print(f"min{suffix} = {np.min(arr)}")
    print(f"q1{suffix} = {np.percentile(arr, 25)}")
    print(f"med{suffix} = {np.median(arr)}")
    print(f"q3{suffix} = {np.percentile(arr, 75)}")
    print(f"max{suffix} = {np.max(arr)}")
    print(f"iqr{suffix} = {np.percentile(arr, 75) - np.percentile(arr, 25)}")
    print(f"range{suffix} = {np.max(arr) - np.min(arr)}")


#print("========== YES ORIGINAL ============")
#print_stats(y["ConvertedCompYearly"].to_numpy(), "y_original")
#print("========== NO ORIGINAL ============")
#print_stats(n["ConvertedCompYearly"].to_numpy(), "n_original")


y_std_dev = np.std(y["ConvertedCompYearly"])
y_mean = np.mean(y["ConvertedCompYearly"])
y_upper_bound = y_mean + 2 * y_std_dev
y_lower_bound = y_mean - 2 * y_std_dev


n_std_dev = np.std(n["ConvertedCompYearly"])
n_mean = np.mean(n["ConvertedCompYearly"])
n_upper_bound = n_mean + 2 * n_std_dev
n_lower_bound = n_mean - 2 * n_std_dev


y_trimmed = y[(y_lower_bound <= y['ConvertedCompYearly']) & (y['ConvertedCompYearly'] <= y_upper_bound)]
n_trimmed = n[(n_lower_bound <= n['ConvertedCompYearly']) & (n['ConvertedCompYearly'] <= n_upper_bound)]


#print("========== YES TRIMMED ============")
#print_stats(y_trimmed["ConvertedCompYearly"].to_numpy(), "y_trimmed")
y_trimmed.to_csv('yes.csv', index=False)
#print("========== NO TRIMMED ============")
#print_stats(n_trimmed["ConvertedCompYearly"].to_numpy(), "n_trimmed")
n_trimmed.to_csv('no.csv', index=False)


# plt.hist(n_trimmed["ConvertedCompYearly"].to_numpy(), bins=50, density=True, alpha=0.5)
# plt.hist(y_trimmed["ConvertedCompYearly"].to_numpy(), bins=50, density=True, alpha=0.5)
# #plt.show()
# # Presentation graphs:
sns.set_theme(style='whitegrid', palette='muted')

# fig, ax = plt.subplots(figsize=(10, 5))

sal = data[data['ConvertedCompYearly'].notna()].copy()
sal_mean = np.mean(sal['ConvertedCompYearly'])
sal_std  = np.std(sal['ConvertedCompYearly'])
sal_trimmed = sal[
    (sal['ConvertedCompYearly'] >= sal_mean - 2 * sal_std) &
    (sal['ConvertedCompYearly'] <= sal_mean + 2 * sal_std)
]

min_val, q1, median, q3, max_val = sal_trimmed['ConvertedCompYearly'].quantile([0.00, 0.25, 0.5, 0.75, 1.00])

# ax.boxplot(
#     sal_trimmed['ConvertedCompYearly'],
#     vert=False,
#     whis=(0, 100),
#     showfliers=False,
#     patch_artist=True,
#     boxprops=dict(facecolor='#4A90D9', alpha=0.85),
#     medianprops=dict(color='white', linewidth=2),
#     whiskerprops=dict(color='#555555'),
#     capprops=dict(color='#555555'),
#     widths=0.4
# )

# for val, label in zip(
#     [min_val, q1, median, q3, max_val],
#     ['Min', 'Q1', 'Median', 'Q3', 'Max']
# ):
#     ax.axvline(val, color='gray', linewidth=0.8, linestyle='--', alpha=0.5)
#     ax.text(val, 0.82, f'{label}\n${val/1000:.0f}k', ha='center',
#             transform=ax.get_xaxis_transform(),
#             fontsize=8, color='black', fontweight='bold')

# ax.set_title('Distribution of Developer Annual Salaries', fontsize=14, fontweight='bold', pad=12)
# ax.set_xlabel('Annual Salary (USD)', fontsize=11)
# ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1000:.0f}k'))
# ax.set_yticks([])

# plt.tight_layout()
# plt.savefig('salary_boxplot.png', dpi=150, bbox_inches='tight')
# plt.show()


''' Releative frequncy bar chart of AI opionion '''
# fig, ax = plt.subplots(figsize=(7, 5))

# counts = data['AIThreat'].value_counts(normalize=True) * 100

# bars = ax.bar(
#     ['Yes', 'Unsure', 'No'],
#     counts.values,
#     color=['#4A90D9', '#A865B5','#E05C5C'],
#     edgecolor='white',
#     width=0.5
# )

# for bar, val in zip(bars, counts.values):
#     ax.text(bar.get_x() + bar.get_width() / 2, val + 0.5,
#             f'{val:.1f}%', ha='center', va='bottom',
#             fontweight='bold', fontsize=12)

# ax.set_title('Relative Frequency of AI Fear Among Developers', fontsize=14, fontweight='bold', pad=12)
# ax.set_xlabel('Fearful of AI?', fontsize=11)
# ax.set_ylabel('Relative Frequency (%)', fontsize=11)
# ax.set_ylim(0, max(counts.values) * 1.15)
# sns.despine()

# plt.tight_layout()
# plt.savefig('ai_fear_barplot.png', dpi=150, bbox_inches='tight')
# plt.show()

'''Y_trimmed dist'''
fig, ax = plt.subplots(figsize=(10, 5))

ax.hist(
    y_trimmed['ConvertedCompYearly'],
    bins=50,
    color='#4A90D9',
    edgecolor='white',
    alpha=0.85
)

ax.set_title('Salary Distribution — Developers Fearful of AI', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Annual Salary (USD)', fontsize=11)
ax.set_ylabel('Count', fontsize=11)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1000:.0f}k'))

plt.tight_layout()
plt.savefig('hist_yes.png', dpi=150, bbox_inches='tight')
plt.show()


"""N_trimmed dist"""
fig, ax = plt.subplots(figsize=(10, 5))

ax.hist(
    n_trimmed['ConvertedCompYearly'],
    bins=50,
    color='#E05C5C',
    edgecolor='white',
    alpha=0.85
)

ax.set_title('Salary Distribution — Developers NOT Fearful of AI', fontsize=14, fontweight='bold', pad=12)
ax.set_xlabel('Annual Salary (USD)', fontsize=11)
ax.set_ylabel('Count', fontsize=11)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1000:.0f}k'))

plt.tight_layout()
plt.savefig('hist_no.png', dpi=150, bbox_inches='tight')
plt.show()

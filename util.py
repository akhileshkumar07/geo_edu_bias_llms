import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Function to produce a customized bar plot

def create_bar_plot(x, y, palette, xlabel, ylabel, title=None, ax=None,
                    figsize=(6, 4), title_fontsize=10, label_fontsize=9, 
                    tick_fontsize=8, save_path=None):
    
    created_fig = False
    # Create a new figure if no axis object is provided
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
        created_fig = True

    sns.barplot(x=x, y=y, palette=palette, ax=ax)

    # Set axis labels and title
    ax.set_xlabel(xlabel, fontsize=label_fontsize)
    ax.set_ylabel(ylabel, fontsize=label_fontsize)
    ax.set_title(title, fontsize=title_fontsize)
    ax.tick_params(axis='both', labelsize=tick_fontsize)

    # Add numeric labels to each bar
    for bar in ax.patches:
        width = bar.get_width()
        ax.text(
            width + max(x) * 0.01,  # Small offset from the end of the bar
            bar.get_y() + bar.get_height() / 2,
            f'{int(width)}',
            va='center', ha='left', fontsize=tick_fontsize
        )

    # Remove top and right spines for a cleaner look
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.grid(False)

    # Show or save the plot if a new figure was created
    if created_fig:
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()


# Function to extract universities and programs from a row of tuples

def extract_universities_programs(row):
    # row is expected to be a list of (university, program) tuples or list
    universities = [item[0] for item in row]
    programs = [item[1] for item in row]
    return universities, programs

# Function to generate a word cloud from a list of text entries

def generate_wordcloud(text_data, title=None, save_path=None):
    text = " ".join(text_data)  # Join all text items into a single string
    wordcloud = WordCloud(width=1200, height=600, background_color='white',
                          colormap='viridis', max_words=20).generate(text)
    
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)

    # Save the image if a path is specified
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')

    plt.show()


# Function to create a heatmap with annotations and styling

def create_heatmap(heatmap_df, ax, cmap, title, xlabel, ylabel, save_path=None):
    # Create heatmap with value annotations
    sns.heatmap(
        heatmap_df,
        annot=True,
        fmt="d",  # Format numbers as integers
        cmap=cmap,
        linewidths=0.001,
        linecolor='white',
        annot_kws={"fontsize": 8},
        ax=ax
    )

    # Set plot title and axis labels
    ax.set_title(title, fontsize=10)
    ax.set_xlabel(xlabel, fontsize=9)
    ax.set_ylabel(ylabel, fontsize=9)

    # Adjust tick label formatting
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', fontsize=8)
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=8)

    # Customize colorbar tick size
    colorbar = ax.collections[0].colorbar
    colorbar.ax.tick_params(labelsize=8)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()
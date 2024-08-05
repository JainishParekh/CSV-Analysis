import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from django.shortcuts import render
from .forms import UploadFileForm

def handle_uploaded_file(f):
    with open('uploaded_file.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return 'uploaded_file.csv'

def summary_stats_to_dict(summary_stats):
    stats_dict = summary_stats.to_dict()
    formatted_stats = {}
    for metric, columns in stats_dict.items():
        for column, value in columns.items():
            if column not in formatted_stats:
                formatted_stats[column] = {}
            formatted_stats[column][metric] = value
    return formatted_stats

def analysis(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            data = pd.read_csv(file_path)
            is_id_column = form.cleaned_data['is_id_column']

            if is_id_column:
                data = data.iloc[:, 1:]

            # Perform data analysis
            summary_stats = data.describe()
            missing_values = data.isnull().sum()
            

            # Generate plots
            numeric_cols = data.select_dtypes(include='number').columns
            fig, axes = plt.subplots(len(data.columns), 1, figsize=(6, 5 * len(data.columns)))
            if len(data.columns) == 1:
                axes = [axes]

            for ax, column in zip(axes, data.columns):
                if pd.api.types.is_numeric_dtype(data[column]):
                    sns.kdeplot(data[column], ax=ax)
                    ax.set_title(f'Probability Density Curve of {column}')
                else:
                    sns.countplot(y=data[column], ax=ax)
                    ax.set_title(f'Bar Plot of {column}')

                ax.set_xlabel(column)
                ax.set_ylabel('Frequency')

             # Add heatmap for correlation matrix
            if len(numeric_cols) > 1:
                corr_matrix = data[numeric_cols].corr()
                sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', ax=axes[-1])
                axes[-1].set_title('Correlation Heatmap')
            else:
                axes[-1].axis('off')  # Hide the heatmap if there are not enough numeric columns

            plt.tight_layout()
            buf = BytesIO()
            plt.savefig(buf, format='png', dpi=80)
            buf.seek(0)
            image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            plt.close(fig)

            context = {
                'data': data.head().to_html(classes="table-auto text-center w-full p-4 border-collapse border border-gray-400"),
                'summary_stats': summary_stats.to_html(classes="table-auto w-full text-center p-4 border-collapse border border-gray-400"),
                'missing_values': missing_values.to_frame(name='Missing Values').to_html(classes="table-auto text-center border-collapse border border-gray-400"),
                'plot': image_base64,
            }
            return render(request, 'results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'analysis.html', {'form': form})

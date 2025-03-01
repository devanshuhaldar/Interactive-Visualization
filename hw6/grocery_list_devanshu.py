import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
def generate_grocery_cost_data_for_past_year():
    np.random.seed(42)  # Setting seed for reproducibility

    # start_date = pd.to_datetime('today') - pd.DateOffset(years=1)
    # end_date = pd.to_datetime('today')
    start_date = pd.to_datetime('2023-01-01')
    end_date = pd.to_datetime('2023-12-31')

    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    seasons = ['Winter', 'Spring', 'Summer', 'Fall']
    categories = ['Carbs', 'Protein', 'Vegetables', 'Fruits', 'Drinks']
    num_categories = len(categories)

    # Initialize an empty DataFrame
    grocery_data = pd.DataFrame(columns=['Date', 'Day', 'Month', 'Season', 'Protein', 'Vegetables', 'Carbs', 'Fruits', 'Drinks'])

    # Generate sparse data with higher spending on specific days and seasons for every day in the past year
    for i, single_date in enumerate(pd.date_range(start_date, end_date)):
        # get the date data
        season = ""
        month = ""
        if (single_date.month in [12, 1, 2]):
            season = "Winter"
            if single_date.month == 12: month = "December"
            if single_date.month == 1: month = "January"
            if single_date.month == 2: month = "February"
        elif (single_date.month in [3, 4, 5]):
            season = "Spring"
            if single_date.month == 3: month = "March"
            if single_date.month == 4: month = "April"
            if single_date.month == 5: month = "May"
        elif (single_date.month in [6, 7, 8]):
            season = "Summer"
            if single_date.month == 6: month = "June"
            if single_date.month == 7: month = "July"
            if single_date.month == 8: month = "August"
        elif (single_date.month in [9, 10, 11]):
            if single_date.month == 9: month = "September"
            if single_date.month == 10: month = "October"
            if single_date.month == 11: month = "November"
            season = "Fall"
        # getting the current day
        day = days_of_week[i % 7]
        

        if season == 'Winter':
            if day in ['Sunday', 'Wednesday', 'Saturday']:
                # More money spent on Protein and Drinks
                protein_money = np.random.uniform(40, 60)
                drink_money = np.random.uniform(40, 60)
                
                # Less money spent on Fruits and Vegetables
                vegetable_money = np.random.uniform(20, 35)
                fruit_money = np.random.uniform(20, 35)

                # even less on Carbs
                carb_money = np.random.uniform(10, 15)
            else:
                # Less spending on other days
                protein_money = np.random.uniform(2, 10)
                drink_money = np.random.uniform(2, 10)
                vegetable_money = np.random.uniform(2, 10)
                fruit_money = np.random.uniform(2, 10)
                carb_money = np.random.uniform(2, 10)
        elif season == 'Spring':
            if day in ['Sunday', 'Wednesday', 'Saturday']:
                # More money spent on Protein, Drinks, and Vegetables
                protein_money = np.random.uniform(40, 60)
                drink_money = np.random.uniform(40, 60)
                vegetable_money = np.random.uniform(40, 60)
                
                # Less money spent on Fruits and Vegetables
                fruit_money = np.random.uniform(10, 20)

                # more on Carbs in spring
                carb_money = np.random.uniform(20, 30)
            else:
                # Less spending on other days
                protein_money = np.random.uniform(10, 12)
                drink_money = np.random.uniform(10, 12)
                vegetable_money = np.random.uniform(10, 12)
                fruit_money = np.random.uniform(10, 12)
                carb_money = np.random.uniform(10, 12)
        
        elif season == 'Summer':
            if day in ['Sunday', 'Wednesday', 'Saturday']:
                # More money spent on Protein, Drinks, and Vegetables
                fruit_money = np.random.uniform(30, 60)
                vegetable_money = np.random.uniform(30, 60)
                
                # Less money spent on Fruits and Vegetables
                carb_money = np.random.uniform(10, 30)

                # more on Carbs in spring
                drink_money = np.random.uniform(20, 40)
                protein_money = np.random.uniform(20, 40)
            else:
                # Less spending on other days
                protein_money = np.random.uniform(5, 15)
                drink_money = np.random.uniform(5, 15)
                vegetable_money = np.random.uniform(5, 15)
                fruit_money = np.random.uniform(5, 15)
                carb_money = np.random.uniform(5, 15)
        
        elif season == 'Fall':
            if day in ['Sunday', 'Wednesday', 'Saturday']:
                # More money spent on Protein, Drinks, and Vegetables
                fruit_money = np.random.uniform(40, 60)
                protein_money = np.random.uniform(40, 60)
                
                # Less money spent on Fruits and Vegetables
                vegetable_money = np.random.uniform(10, 30)

                # more on Carbs in spring
                carb_money = np.random.uniform(20, 40)
                drink_money = np.random.uniform(20, 40)
            else:
                # Less spending on other days
                protein_money = np.random.uniform(5, 10)
                drink_money = np.random.uniform(5, 10)
                vegetable_money = np.random.uniform(5, 10)
                fruit_money = np.random.uniform(5, 10)
                carb_money = np.random.uniform(5, 10)

        # Add the data to the DataFrame
        if i == 0:
            grocery_data = pd.DataFrame(
        {'Date': [str(single_date.month_name()) + ' ' + str(single_date.day) + ' ' + str(single_date.year)], 'Day': [day], 'Month': [month], 'Season': [season], 'Protein': [protein_money], 'Vegetables': [vegetable_money], 'Carbs': [carb_money], 'Fruits': [fruit_money], 'Drinks': [drink_money]})
        grocery_data = pd.concat([grocery_data, pd.DataFrame(
        {'Date': [str(single_date.month_name()) + ' ' + str(single_date.day) + ' ' + str(single_date.year)], 'Day': [day], 'Month': [month], 'Season': [season], 'Protein': [protein_money], 'Vegetables': [vegetable_money], 'Carbs': [carb_money], 'Fruits': [fruit_money], 'Drinks': [drink_money]})], ignore_index=True)

    return grocery_data

def get_daily_stacked_bar_chart(grocery_cost_data, intervals):
        fig = grocery_cost_data.plot(kind='bar', x='Date', stacked=True, title="Devanshu's Grocery Cost Every Day For The Past Year",figsize=(12, 6), rot=45.0, backend='matplotlib')
        for i, label in enumerate(fig.xaxis.get_ticklabels()):
            if (i % intervals != 0):
                label.set_visible(False)


# Group data by Month 
grocery_cost_data_last_year = generate_grocery_cost_data_for_past_year()
grouped_data = grocery_cost_data_last_year.groupby('Month').agg({
    'Protein': 'sum',
    'Vegetables': 'sum',
    'Carbs': 'sum',
    'Fruits': 'sum',
    'Drinks': 'sum'
}).reset_index()
# print(grocery_cost_data_last_year)
print(grouped_data)

# x = ['A', 'B', 'C', 'D']
# y1 = [10, 20, 10, 30]
# y2 = [20, 25, 15, 25]
 
# # plot bars in stack manner
# plt.bar(x, y1, color='r')
# plt.bar(x, y2, bottom=y1, color='b')
# plt.show()
months = grouped_data['Month']
proteins = grouped_data['Protein']
vegetables = grouped_data['Vegetables']
carbs = grouped_data['Carbs']
fruits = grouped_data['Fruits']
drinks = grouped_data['Drinks']
print(months)
print(vegetables)
# plt.bar(months,proteins, color = 'red')
# plt.bar(months,vegetables, bottom = proteins, color = 'blue')
# plt.bar(months, carbs, bottom = vegetables, color = 'green')
# plt.bar(months, fruits, bottom = carbs, color = 'yellow')
# plt.bar(months,drinks, bottom = fruits, color = 'lightblue')

# plt.show()



# fig = px.bar(grouped_data, x='Month', y=['Protein', 'Vegetables', 'Carbs', 'Fruits', 'Drinks'],
#              title='Monthly Grocery Expenses', labels={'value': 'Expense ($)'}, 
#              template='plotly_dark', barmode='stack')
# fig.show()
import numpy as np
salaries=np.array([35000, 42000, np.nan, 50000, np.inf, 38000, np.nan])
print("______Detecting infinte and missing values_____\n",np.isnan(salaries),np.isinf(salaries))
salaries[np.isnan(salaries)]=3000
salaries[np.isinf(salaries)]=3000
print("______Cleaned Dataset______\n",salaries)

clean_data=salaries[~np.isinf(salaries)]
clean_data=salaries[~np.isnan(salaries)]
print("____After removing invalid Data_____\n",clean_data)
copy_view=np.array([10, 20, 30, 40])
copy_arr=copy_view.copy()
view_arr=copy_view.view()
modify=salaries.view()
modify[1]=999
print("______Modified______\n",modify)
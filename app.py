import streamlit as st
import pickle

with st.sidebar:
    option = st.selectbox(
    'Select any one below',
    ('Home', 'Markdown Prediction', 'IsHoliday Prediction','Unemployment Prediction','Type Prediction' ))

if option == 'Home':
     st.markdown("""The dataset comprises store, sales, and features data, offering details on store attributes like name, 
     department, date, type, size, weekly sales, and environmental factors such as holiday status, temperature,
     fuel price, multiple markdowns, CPI, and unemployment. The primary focus is on predicting weekly sales, 
     Holiday,Unemployment and Type serving as the target variable for our modeling endeavors.""")

     st.markdown("Contact details")

     st.write("LinkedIn : https://www.linkedin.com/in/sangeetha-m-a66aa1251")
     st.write("Gmail_Id : sangeethamp94@gmail.com")

if option == 'Markdown Prediction':
    st.title("Markdown Prediction")
    
    with open(r'C:\Users\sangeetha\Downloads\MarkdownPrediction.pkl','rb') as f:
      model = pickle.load(f)

    col1,col2 = st.columns(2)

    with col1:
        Store = st.slider("Store: ", min_value=1, max_value=45)
        Type = st.selectbox(
        'Select any one Type',
        (0.,1.,2.)) 
        Size = st.slider("Size: ", min_value = 34875 ,max_value = 219622)
        Temperature = st.slider("Temperature: ", min_value = -7.29, max_value = 101.95)
        Fuel_Price = st.slider("Fuel_Price: ", min_value = 2.472, max_value = 4.468)
        MarkDown2  = st.slider("MarkDown2: ", min_value = -265.76, max_value = 104519.54 )
        MarkDown3  = st.slider("MarkDown3: ", min_value = -29.1, max_value = 141630.61)
        MarkDown4  = st.slider("MarkDown4: ", min_value = 0.0, max_value = 67474.85)
        MarkDown5  = st.slider("MarkDown5: ", min_value = 0.0, max_value = 108519.28)
        CPI        = st.slider("CPI: ", min_value = 126.064, max_value = 227.2328068)
  
    with col2:
        
        Unemployment= st.slider("Unemployment: ", min_value = 3.879, max_value = 14.313)
        IsHoliday  = st.selectbox(
        'Select any one ',
        (0.,1.)) 
        Dept       = st.slider("Dept: ", min_value = 1, max_value = 99)
        Weekly_Sales= st.slider("Weekly_Sales: ", min_value = 0.0, max_value = 693099.36)
        Day        = st.slider("Day: ", min_value = 1, max_value = 31)
        Month      = st.slider("Month: ", min_value = 1, max_value =12)
        Year       = st.selectbox(
        'Select any one Year',
        (2010,2011,2012))
    if st.button('Predict'):
        Markdown_pred = model.predict([[Store,Type,Size,Temperature,Fuel_Price,MarkDown2,MarkDown3,MarkDown4,MarkDown5,CPI,Unemployment,IsHoliday,Dept,Weekly_Sales,Day,Month,Year]])

        st.markdown(Markdown_pred)


if option == 'IsHoliday Prediction':

    st.title("IsHoliday Prediction")

    with open(r'C:\Users\sangeetha\Downloads\IsHolidayPrediction.pkl','rb') as f:
      model1 = pickle.load(f)

    col1,col2 = st.columns(2)

    with col1:
        Store = st.slider("Store: ", min_value=1, max_value=45)
        Type = st.selectbox(
        'Select any one Type',
        (0.,1.,2.)) 
        Size = st.slider("Size: ", min_value = 34875, max_value = 219622)
        Temperature = st.slider("Temperature: ", min_value = -7.29, max_value = 101.95)
        Fuel_Price = st.slider("Fuel_Price: ", min_value = 2.472, max_value = 4.468)
        MarkDown1  = st.slider("MarkDown1: ", min_value =  0.0, max_value = 88646.76)
        MarkDown2  = st.slider("MarkDown2: ", min_value = -265.76, max_value = 104519.54 )
        MarkDown3  = st.slider("MarkDown3: ", min_value = -29.1, max_value = 141630.61)
        MarkDown4  = st.slider("MarkDown4: ", min_value = 0.0, max_value = 67474.85)
        MarkDown5  = st.slider("MarkDown5: ", min_value = 0.0, max_value = 108519.28)
        
    with col2:

        CPI        = st.slider("CPI: ", min_value = 126.064, max_value = 227.2328068)
        Unemployment= st.slider("Unemployment: ", min_value = 3.879, max_value = 14.313)
        Dept       = st.slider("Dept: ", min_value = 1, max_value = 99)
        Weekly_Sales= st.slider("Weekly_Sales: ", min_value = 0.0, max_value = 693099.36)
        Day        = st.slider("Day: ", min_value = 1, max_value = 31)
        Month      = st.slider("Month: ", min_value = 1, max_value =12)
        Year       = st.selectbox(
        'Select any one Year',
        (2010,2011,2012))
    if st.button('Predict'):
        holiday_pred = model1.predict([[Store,Type,Size,Temperature,Fuel_Price,MarkDown1,MarkDown2,MarkDown3,MarkDown4,MarkDown5,CPI,Unemployment,Dept,Weekly_Sales,Day,Month,Year]])
    
    if 'holiday_pred' == 0.:
        st.markdown('False')
    else:
        st.markdown('True')


if option == 'Unemployment Prediction':
    
    st.title("Unemployment Prediction")

    with open(r'C:\Users\sangeetha\Downloads\Unemp.pkl','rb') as f:
      model2 = pickle.load(f)

    col1,col2 = st.columns(2)

    with col1:
        Store = st.slider("Store: ", min_value=1, max_value=45)
        Type = st.selectbox(
        'Select any one Type',
        (0.,1.,2.)) 
        Size = st.slider("Size: ", min_value = 34875, max_value = 219622)
        Temperature = st.slider("Temperature: ", min_value = -7.29, max_value = 101.95)
        Fuel_Price = st.slider("Fuel_Price: ", min_value = 2.472, max_value = 4.468)
        MarkDown1  = st.slider("MarkDown1: ", min_value =  0.0, max_value = 88646.76)
        MarkDown2  = st.slider("MarkDown2: ", min_value = -265.76, max_value = 104519.54 )
        MarkDown3  = st.slider("MarkDown3: ", min_value = -29.1, max_value = 141630.61)
        MarkDown4  = st.slider("MarkDown4: ", min_value = 0.0, max_value = 67474.85)
        MarkDown5  = st.slider("MarkDown5: ", min_value = 0.0, max_value = 108519.28)
        
    with col2:
        
        CPI        = st.slider("CPI: ", min_value = 126.064, max_value = 227.2328068)
        IsHoliday  = st.selectbox(
        'Select any one ',
        (0.,1.)) 
        Dept       = st.slider("Dept: ", min_value = 1, max_value = 99)
        Weekly_Sales= st.slider("Weekly_Sales: ", min_value = 0.0, max_value = 693099.36)
        Day        = st.slider("Day: ", min_value = 1, max_value = 31)
        Month      = st.slider("Month: ", min_value = 1, max_value =12)
        Year       = st.selectbox(
        'Select any one Year',
        (2010,2011,2012))

    if st.button('Predict'):
        unemp_pred = model2.predict([[Store,Type,Size,Temperature,Fuel_Price,MarkDown1,MarkDown2,MarkDown3,MarkDown4,MarkDown5,CPI,IsHoliday,Dept,Weekly_Sales,Day,Month,Year]])
    
        st.markdown(unemp_pred)

if option == 'Type Prediction':

    st.title("Type Prediction")

    with open(r'C:\Users\sangeetha\Downloads\Type_prediction.pkl','rb') as f:
      model3 = pickle.load(f)

    col1,col2 = st.columns(2)

    with col1:
        Store = st.slider("Store: ", min_value=1, max_value=45)
        Size = st.slider("Size: ", min_value = 34875, max_value = 219622)
        Temperature = st.slider("Temperature: ", min_value = -7.29, max_value = 101.95)
        Fuel_Price = st.slider("Fuel_Price: ", min_value = 2.472, max_value = 4.468)
        MarkDown1  = st.slider("MarkDown1: ", min_value =  0.0, max_value = 88646.76)
        MarkDown2  = st.slider("MarkDown2: ", min_value = -265.76, max_value = 104519.54 )
        MarkDown3  = st.slider("MarkDown3: ", min_value = -29.1, max_value = 141630.61)
        MarkDown4  = st.slider("MarkDown4: ", min_value = 0.0, max_value = 67474.85)
        MarkDown5  = st.slider("MarkDown5: ", min_value = 0.0, max_value = 108519.28)
        CPI        = st.slider("CPI: ", min_value = 126.064, max_value = 227.2328068)
  
    with col2:
        
        Unemployment= st.slider("Unemployment: ", min_value = 3.879, max_value = 14.313)
        IsHoliday  = st.selectbox(
        'Select any one ',
        (0.,1.)) 
        Dept       = st.slider("Dept: ", min_value = 1, max_value = 99)
        Weekly_Sales= st.slider("Weekly_Sales: ", min_value = 0.0, max_value = 693099.36)
        Day        = st.slider("Day: ", min_value = 1, max_value = 31)
        Month      = st.slider("Month: ", min_value = 1, max_value =12)
        Year       = st.selectbox(
        'Select any one Year',
        (2010,2011,2012))
    if st.button('Predict'):
        type_pred = model3.predict([[Store,Size,Temperature,Fuel_Price,MarkDown1,MarkDown2,MarkDown3,MarkDown4,MarkDown5,CPI,Unemployment,IsHoliday,Dept,Weekly_Sales,Day,Month,Year]])
    
        if 'type_pred' == 0.:
            st.markdown("A")
        elif 'type_pred' == 1.:
            st.markdown("B")
        else:
            st.markdown("C")

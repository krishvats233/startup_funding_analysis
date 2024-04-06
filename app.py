import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Jai mahakal

st.set_page_config(layout='wide',page_title='StartUp Analysis')
#Ham jo hai vo kagel pai hea coding krega nhi tho google colab mai data upload krke krna padta hai
df=pd.read_csv("startup_cleaned.csv")
st.sidebar.title('StartUp Funding Analysis')
option=st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'])
print(df.info())

df['date']=df['date'].str.replace('05/072018',"05/07/2018")
df['date']=df['date'].str.replace('01/07/015',"01/07/2015")


df['date']=df['date'].str.replace('12/05.2015',"12/05/2015")
df['date']=df['date'].str.replace('13/04.2015',"13/04/2015")

df['date']=pd.to_datetime(df['date'],dayfirst=True,errors='coerce')

df['year']=df['date'].dt.year #here we extrct the ear from date object
df['month']=df['date'].dt.month
explore0=0
explore1=0


def load_investor_detail(investor):
    st.title(investor)
    #oad thesecnt 5 investment of the investor
    last5_df=df[df['investor'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader("Most Recent Investments")
    st.dataframe(last5_df)

    col1,col2=st.columns(2)
    with col1:
     #biggest investment
     big_investments=df[df['investor'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False)

     st.subheader("Biggest Investments")
     fig,ax=plt.subplots()
     ax.bar(big_investments.index,big_investments.values)
     st.pyplot(fig)
    with col2:
        vertical=df[df['investor'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader("Sector Invested in")
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical,labels=vertical.index,autopct="%0.01f%%")
        st.pyplot(fig1)

    col3,col4=st.columns(2)
    with col3:
           round = df[df['investor'].str.contains(investor)].groupby('round')['amount'].sum()
           st.subheader("Round Invested in")
           fig3, ax3 = plt.subplots()
           ax3.pie(round, labels=round.index, autopct="%0.01f%%")
           st.pyplot(fig3)

    with col4:
            round = df[df['investor'].str.contains(investor)].groupby('city')['amount'].sum()
            st.subheader("City Invested in")
            fig2, ax2 = plt.subplots()
            ax2.pie(round, labels=round.index, autopct="%0.01f%%")
            st.pyplot(fig2)


    #year on year investment

    yoy=df[df['investor'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader("YOY Invested in")
    fig4, ax4 = plt.subplots(figsize=(10,6))
    ax4.plot(yoy.index,yoy.values)

    st.pyplot(fig4)

    st.header("Similar Investors")


    for i in range(0,1):

       similar=df[df['investor'].str.contains('Softbank')]['investor'].str.split(",").sample(5).values[0][i]

       st.markdown("""# """ + similar+"""
## Introduction
This is a simple card created using Markdown.

## Steps
- Write content in Markdown syntax.
- Choose a Markdown editor.
- Format the content using Markdown.
- Preview the card.
- Save the card with a `.md` extension.
- Convert Markdown to other formats if needed.
""")

    for i in range(0, 1):
        similar = df[df['investor'].str.contains('Softbank')]['investor'].str.split(",").sample(5).values[0][i]

        st.markdown("""# """ + similar + """
  ## Introduction
  This is a simple card created using Markdown.

  ## Steps
  - Write content in Markdown syntax.
  - Choose a Markdown editor.
  - Format the content using Markdown.
  - Preview the card.
  - Save the card with a `.md` extension.
  - Convert Markdown to other formats if needed.
  """)


def load_overall_analysis():
    st.title("Overall Analysis")
    #toal invested amount
    total=round(df['amount'].sum())
    col1,col2,col3,col4=st.columns(4)



    with col1:
         st.metric('Total ',total,"Cr")
        #max funding

    max_funding=df.groupby('startup')['amount'].sum().sort_values(ascending=False).head(1).values[0]
    with col2:
     st.metric('Max Funding ',max_funding, "Cr")
    #avg_ticket size
    avg_ticket_size=round(df.groupby('startup')['amount'].sum().mean())
    with col3:
        st.metric('Average Funding ', avg_ticket_size, "Cr")
    num_startup=df['startup'].nunique()
    with col4:
        st.metric('Funded Startup ',num_startup,"")
    st.header("MOM graph")
    selected_option=st.selectbox('Selected Type',['Total','Count'])
    if selected_option=='Total':
      temp = df.groupby(['year','month'])['amount'].sum().reset_index()
      temp['x_axis'] = temp['month'].astype('str') + "-" + temp['year'].astype('str')
      fig4, ax4 = plt.subplots(figsize=(10,6))
      ax4.plot(temp["x_axis"],temp["amount"])

      st.pyplot(fig4)
    else:

        temp = df.groupby(['year', 'month'])['startup'].count().reset_index()
        temp['x_axis'] = temp['month'].astype('str') + "-" + temp['year'].astype('str')
        fig5, ax6 = plt.subplots(figsize=(10, 6))
        ax6.plot(temp["x_axis"], temp["startup"])

        st.pyplot(fig5)


if option=='Overall Analysis':
        load_overall_analysis()

elif option=='StartUp':
    st.title('StartUp Analysis')
    st.sidebar.selectbox('Select One',sorted(df['startup'].unique().tolist()))
    btn1=st.sidebar.button('Find StartUP Details')



else:

    selected_investor=st.sidebar.selectbox('Select One',sorted(set(df['investor'].str.split(",").sum())))
    btn2 =st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_detail(selected_investor)


if(explore0):
    print("mahadev")
    st.subheader("jai bagwan kaal bhairav")






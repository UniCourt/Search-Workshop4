# KIBANA DASHBOARDS

The best way to understand your data is to visualize it. With dashboards, you can turn your data 
from one or more data views into a collection of panels that bring clarity to your data, tell a 
story about your data, and allow you to focus on only the data that’s important to you.
### Index pattern
In a Kibana dashboard, an index pattern is used to define which Elasticsearch indices to search 
and visualize data from. When you create a dashboard, you start by specifying an index pattern, 
which can be a single index or a combination of multiple indices. Once you have defined the index 
pattern, you can use it to search for specific fields in your data and create visualizations 
based on that data.
### Panels
Panels display your data in charts, tables, maps, and more, which allow you to compare your data 
side-by-side to identify patterns and connections. Dashboards support several types of panels to 
display your data, and several options to create panels.

### Creating an Index Pattern for our logs.
1. Click on the hamburger menu and go to <b>stack management</b>.
2. In the side menu, click on <b>Index Pattern</b> and click on the button <b>Create index 
   pattern</b>.
3. Now, give the index pattern name as <b>product-app-logs-index</b> and click on Next step.
4. select the time field as <b>@timestamp</b> and click on <b>Create index pattern</b>.

---
**NOTE**:
Make sure that the index <b>product-app-logs-index</b> is available and has the logs for the 
queries that were fired.
---

### Creating A Dashboard
1. Click on the hamburger menu in the top right and select <b>Dashboard</b>.
2. Click on <b>Create new dashboard</b>.
3. After this the editing page for Dashboard will open, in the page click the <b>Create 
   visualization</b> button.
4. Select the index pattern <b>product-app-logs-index</b>
5. Now, lets create a visualization to see the logs for the APIs that we created.

Follow the links below to for steps to create a dashboard:
- https://www.elastic.co/guide/en/kibana/current/create-a-dashboard-of-panels-with-web-server-data.html
- https://www.elastic.co/guide/en/kibana/current/dashboard.html

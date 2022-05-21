import {Component} from 'react'
import Productos from './componets/Productos'
import Layout from './componets/layout'
import Navbar from './componets/Navbar'
import Title from './componets/Title'
class App extends Component{
  state = {
    productos:[]
  }
  componentDidMount(){
    fetch('http://localhost:8000/productos/')
    .then((Response)=>{
      return Response.json()
    })
    .then((prod)=>{
      this.setState({productos:prod})
      console.log(prod);
    })
  }
  render(){
    return(
      <div>
        <Navbar></Navbar>
        <Layout>
        <Title></Title>
        <Productos productos={this.state.productos}/>
        </Layout>
      </div>
    )
  }
}
export default App;
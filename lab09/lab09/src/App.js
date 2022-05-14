import React, { Component } from 'react';
import './App.css';
class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      articulos : [{
        codigo:1,
        descripcion:'coca cola',
        precio:2.50
      },
      {
        codigo:2,
        descripcion:'inka cola',
        precio:2.20
      }
    ]
  }
}
  render(){
    return(
      <div >
        <table class="table table-hover">
          <thead>
            <tr class="table-dark">
              <th>Codigo</th>
              <th>Descripcion</th>
              <th>Precio</th>
              <th>Borrar</th>
            </tr>

          </thead>
          <tbody>
          {this.state.articulos.map(
            elemento=>{
              return(
                <tr key={elemento.codigo} class="table-info">
                  <td>{elemento.codigo}</td>
                  <td>{elemento.descripcion}</td>
                  <td>{elemento.precio}</td>
                  <td><button onClick={()=>this.borrar(elemento.codigo)} class="btn btn-success">Borrar</button></td>
                </tr>
              )
            }
          )
          }
          </tbody>
        </table>
      </div>
    );
  }
  borrar(cod){
    var temp = this.state.articulos.filter((el)=>el.codigo !== cod);
    this.setState({
      articulos:temp
    });
  }
}
export default App;
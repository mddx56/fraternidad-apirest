import{j as e,r as i}from"./index-57f3d5cd.js";function h(){return e.jsxs(e.Fragment,{children:[e.jsx("h1",{className:"text-2xl mt-8 font-bold",children:"🥳"}),e.jsxs("p",{className:"py-2",children:["✓ ",e.jsx("span",{className:"font-semibold",children:"Calendario de eventos "}),"El sistema puede tener un calendario donde se muestren todos los eventos planificados en fechas específicas"]}),e.jsxs("p",{className:"py-2 ",children:["✓ ",e.jsx("span",{className:"font-semibold",children:"Notificaciones y recordatorios"})," El sistema puede enviar notificaciones y recordatorios automáticos a los miembros sobre eventos próximos, cambios en la programación "]}),e.jsxs("p",{className:"py-2",children:["✓ ",e.jsx("span",{className:"font-semibold",children:"Recopilación de pagos "})," Para eventos que requieran una tarifa de inscripción o contribución financiera."]})]})}function p(){return e.jsx("div",{className:"hero min-h-full rounded-l-xl bg-base-200",children:e.jsx("div",{className:"hero-content py-12",children:e.jsxs("div",{className:"max-w-md",children:[e.jsxs("h1",{className:"text-3xl text-center font-bold ",children:[e.jsx("img",{src:"login.png",width:45,className:"inline-block mr-2 mask mask-circle",alt:"logo"}),"Fraternidad"]}),e.jsx("div",{className:"text-center mt-12",children:e.jsx("img",{src:"login.png",width:180,alt:"Logo",className:"inline-block"})}),e.jsx(h,{})]})})})}function j({styleClass:s,children:t}){return e.jsx("p",{className:`text-center  text-error ${s}`,children:t})}function d(s){const[t,l]=i.useState(s.defaultValue),o=a=>{l(a),s.updateFormValue({updateType:s.updateType,value:a})};return e.jsxs("div",{className:`form-control w-full ${s.containerStyle}`,children:[e.jsx("label",{className:"label",children:e.jsx("span",{className:"label-text text-base-content "+s.labelStyle,children:s.labelTitle})}),e.jsx("input",{type:s.type||"text",value:t,placeholder:s.placeholder||"",onChange:a=>o(a.target.value),className:"input  input-bordered w-full "})]})}function b(){const s={password:"",username:""},[t,l]=i.useState(!1),[o,a]=i.useState(""),[n,m]=i.useState(s),u=r=>{if(r.preventDefault(),a(""),n.username.trim()==="")return a("Ingrese su correo.");if(n.password.trim()==="")return a("Ingrese su contraseña.");l(!0),localStorage.setItem("token","DumyTokenHere"),l(!1),window.location.href="/app/welcome/"},c=({updateType:r,value:x})=>{a(""),m({...n,[r]:x})};return e.jsx("div",{className:"min-h-screen bg-base-200 flex items-center",children:e.jsx("div",{className:"card mx-auto w-full max-w-5xl  shadow-xl",children:e.jsxs("div",{className:"grid  md:grid-cols-2 grid-cols-1  bg-base-100 rounded-xl",children:[e.jsx("div",{className:"",children:e.jsx(p,{})}),e.jsxs("div",{className:"py-24 px-10",children:[e.jsx("h2",{className:"text-2xl font-semibold mb-2 text-center",children:"Inicia sesión"}),e.jsxs("form",{onSubmit:r=>u(r),children:[e.jsxs("div",{className:"mb-4",children:[e.jsx(d,{type:"text",defaultValue:n.username,placeholder:"Escribe tu Nombre de Usuario",updateType:"username",containerStyle:"mt-4",labelTitle:"Correo electrónico",updateFormValue:c}),e.jsx(d,{defaultValue:n.password,placeholder:"Escribe tu contraseña",type:"password",updateType:"password",containerStyle:"mt-4",labelTitle:"Contraseña",updateFormValue:c})]}),e.jsx("div",{className:"text-right text-primary",children:e.jsx("a",{href:"/forgot-password",children:e.jsx("span",{className:"text-sm  inline-block  hover:text-primary hover:underline hover:cursor-pointer transition duration-200",children:"¿Olvidaste tu contraseña?"})})}),e.jsx(j,{styleClass:"mt-8",children:o}),e.jsx("button",{type:"submit",className:"btn mt-2 w-full btn-primary"+(t?" loading":""),children:"Inicia sesión"}),e.jsxs("div",{className:"text-center mt-4",children:["¿No tienes una cuenta? ",e.jsx("a",{href:"/#",children:e.jsx("span",{className:"  inline-block  hover:text-primary hover:underline hover:cursor-pointer transition duration-200",children:"Regístrate"})})]})]})]})]})})})}function N(){return e.jsx("div",{className:"",children:e.jsx(b,{})})}export{N as default};
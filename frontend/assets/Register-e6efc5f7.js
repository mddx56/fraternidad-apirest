import{r as m,j as d,L as T,s as H}from"./index-7752c481.js";import{c as R,a as j,u as U,b as Y,L as V,o as Z}from"./LandingIntro-a8af82ea.js";import"./utils-b785b58d.js";let B={data:""},G=e=>typeof window=="object"?((e?e.querySelector("#_goober"):window._goober)||Object.assign((e||document.head).appendChild(document.createElement("style")),{innerHTML:" ",id:"_goober"})).firstChild:e||B,J=/(?:([\u0080-\uFFFF\w-%@]+) *:? *([^{;]+?);|([^;}{]*?) *{)|(}\s*)/g,Q=/\/\*[^]*?\*\/|  +/g,q=/\n+/g,y=(e,t)=>{let r="",i="",s="";for(let a in e){let n=e[a];a[0]=="@"?a[1]=="i"?r=a+" "+n+";":i+=a[1]=="f"?y(n,a):a+"{"+y(n,a[1]=="k"?"":t)+"}":typeof n=="object"?i+=y(n,t?t.replace(/([^,])+/g,o=>a.replace(/(^:.*)|([^,])+/g,l=>/&/.test(l)?l.replace(/&/g,o):o?o+" "+l:l)):a):n!=null&&(a=/^--/.test(a)?a:a.replace(/[A-Z]/g,"-$&").toLowerCase(),s+=y.p?y.p(a,n):a+":"+n+";")}return r+(t&&s?t+"{"+s+"}":s)+i},x={},P=e=>{if(typeof e=="object"){let t="";for(let r in e)t+=r+P(e[r]);return t}return e},W=(e,t,r,i,s)=>{let a=P(e),n=x[a]||(x[a]=(l=>{let c=0,u=11;for(;c<l.length;)u=101*u+l.charCodeAt(c++)>>>0;return"go"+u})(a));if(!x[n]){let l=a!==e?e:(c=>{let u,g,f=[{}];for(;u=J.exec(c.replace(Q,""));)u[4]?f.shift():u[3]?(g=u[3].replace(q," ").trim(),f.unshift(f[0][g]=f[0][g]||{})):f[0][u[1]]=u[2].replace(q," ").trim();return f[0]})(e);x[n]=y(s?{["@keyframes "+n]:l}:l,r?"":"."+n)}let o=r&&x.g?x.g:null;return r&&(x.g=x[n]),((l,c,u,g)=>{g?c.data=c.data.replace(g,l):c.data.indexOf(l)===-1&&(c.data=u?l+c.data:c.data+l)})(x[n],t,i,o),n},X=(e,t,r)=>e.reduce((i,s,a)=>{let n=t[a];if(n&&n.call){let o=n(r),l=o&&o.props&&o.props.className||/^go/.test(o)&&o;n=l?"."+l:o&&typeof o=="object"?o.props?"":y(o,""):o===!1?"":o}return i+s+(n??"")},"");function O(e){let t=this||{},r=e.call?e(t.p):e;return W(r.unshift?r.raw?X(r,[].slice.call(arguments,1),t.p):r.reduce((i,s)=>Object.assign(i,s&&s.call?s(t.p):s),{}):r,G(t.target),t.g,t.o,t.k)}let L,I,F;O.bind({g:1});let b=O.bind({k:1});function K(e,t,r,i){y.p=t,L=e,I=r,F=i}function v(e,t){let r=this||{};return function(){let i=arguments;function s(a,n){let o=Object.assign({},a),l=o.className||s.className;r.p=Object.assign({theme:I&&I()},o),r.o=/ *go\d+/.test(l),o.className=O.apply(r,i)+(l?" "+l:""),t&&(o.ref=n);let c=e;return e[0]&&(c=o.as||e,delete o.as),F&&c[0]&&F(o),L(c,o)}return t?t(s):s}}var ee=e=>typeof e=="function",C=(e,t)=>ee(e)?e(t):e,te=(()=>{let e=0;return()=>(++e).toString()})(),M=(()=>{let e;return()=>{if(e===void 0&&typeof window<"u"){let t=matchMedia("(prefers-reduced-motion: reduce)");e=!t||t.matches}return e}})(),re=20,$=new Map,se=1e3,z=e=>{if($.has(e))return;let t=setTimeout(()=>{$.delete(e),w({type:4,toastId:e})},se);$.set(e,t)},ae=e=>{let t=$.get(e);t&&clearTimeout(t)},S=(e,t)=>{switch(t.type){case 0:return{...e,toasts:[t.toast,...e.toasts].slice(0,re)};case 1:return t.toast.id&&ae(t.toast.id),{...e,toasts:e.toasts.map(a=>a.id===t.toast.id?{...a,...t.toast}:a)};case 2:let{toast:r}=t;return e.toasts.find(a=>a.id===r.id)?S(e,{type:1,toast:r}):S(e,{type:0,toast:r});case 3:let{toastId:i}=t;return i?z(i):e.toasts.forEach(a=>{z(a.id)}),{...e,toasts:e.toasts.map(a=>a.id===i||i===void 0?{...a,visible:!1}:a)};case 4:return t.toastId===void 0?{...e,toasts:[]}:{...e,toasts:e.toasts.filter(a=>a.id!==t.toastId)};case 5:return{...e,pausedAt:t.time};case 6:let s=t.time-(e.pausedAt||0);return{...e,pausedAt:void 0,toasts:e.toasts.map(a=>({...a,pauseDuration:a.pauseDuration+s}))}}},_=[],k={toasts:[],pausedAt:void 0},w=e=>{k=S(k,e),_.forEach(t=>{t(k)})},ie={blank:4e3,error:4e3,success:2e3,loading:1/0,custom:4e3},oe=(e={})=>{let[t,r]=m.useState(k);m.useEffect(()=>(_.push(r),()=>{let s=_.indexOf(r);s>-1&&_.splice(s,1)}),[t]);let i=t.toasts.map(s=>{var a,n;return{...e,...e[s.type],...s,duration:s.duration||((a=e[s.type])==null?void 0:a.duration)||(e==null?void 0:e.duration)||ie[s.type],style:{...e.style,...(n=e[s.type])==null?void 0:n.style,...s.style}}});return{...t,toasts:i}},ne=(e,t="blank",r)=>({createdAt:Date.now(),visible:!0,type:t,ariaProps:{role:"status","aria-live":"polite"},message:e,pauseDuration:0,...r,id:(r==null?void 0:r.id)||te()}),N=e=>(t,r)=>{let i=ne(t,e,r);return w({type:2,toast:i}),i.id},p=(e,t)=>N("blank")(e,t);p.error=N("error");p.success=N("success");p.loading=N("loading");p.custom=N("custom");p.dismiss=e=>{w({type:3,toastId:e})};p.remove=e=>w({type:4,toastId:e});p.promise=(e,t,r)=>{let i=p.loading(t.loading,{...r,...r==null?void 0:r.loading});return e.then(s=>(p.success(C(t.success,s),{id:i,...r,...r==null?void 0:r.success}),s)).catch(s=>{p.error(C(t.error,s),{id:i,...r,...r==null?void 0:r.error})}),e};var le=(e,t)=>{w({type:1,toast:{id:e,height:t}})},de=()=>{w({type:5,time:Date.now()})},ce=e=>{let{toasts:t,pausedAt:r}=oe(e);m.useEffect(()=>{if(r)return;let a=Date.now(),n=t.map(o=>{if(o.duration===1/0)return;let l=(o.duration||0)+o.pauseDuration-(a-o.createdAt);if(l<0){o.visible&&p.dismiss(o.id);return}return setTimeout(()=>p.dismiss(o.id),l)});return()=>{n.forEach(o=>o&&clearTimeout(o))}},[t,r]);let i=m.useCallback(()=>{r&&w({type:6,time:Date.now()})},[r]),s=m.useCallback((a,n)=>{let{reverseOrder:o=!1,gutter:l=8,defaultPosition:c}=n||{},u=t.filter(h=>(h.position||c)===(a.position||c)&&h.height),g=u.findIndex(h=>h.id===a.id),f=u.filter((h,A)=>A<g&&h.visible).length;return u.filter(h=>h.visible).slice(...o?[f+1]:[0,f]).reduce((h,A)=>h+(A.height||0)+l,0)},[t]);return{toasts:t,handlers:{updateHeight:le,startPause:de,endPause:i,calculateOffset:s}}},me=b`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
 transform: scale(1) rotate(45deg);
  opacity: 1;
}`,ue=b`
from {
  transform: scale(0);
  opacity: 0;
}
to {
  transform: scale(1);
  opacity: 1;
}`,pe=b`
from {
  transform: scale(0) rotate(90deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(90deg);
	opacity: 1;
}`,fe=v("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${e=>e.primary||"#ff4b4b"};
  position: relative;
  transform: rotate(45deg);

  animation: ${me} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;

  &:after,
  &:before {
    content: '';
    animation: ${ue} 0.15s ease-out forwards;
    animation-delay: 150ms;
    position: absolute;
    border-radius: 3px;
    opacity: 0;
    background: ${e=>e.secondary||"#fff"};
    bottom: 9px;
    left: 4px;
    height: 2px;
    width: 12px;
  }

  &:before {
    animation: ${pe} 0.15s ease-out forwards;
    animation-delay: 180ms;
    transform: rotate(90deg);
  }
`,ge=b`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`,he=v("div")`
  width: 12px;
  height: 12px;
  box-sizing: border-box;
  border: 2px solid;
  border-radius: 100%;
  border-color: ${e=>e.secondary||"#e0e0e0"};
  border-right-color: ${e=>e.primary||"#616161"};
  animation: ${ge} 1s linear infinite;
`,xe=b`
from {
  transform: scale(0) rotate(45deg);
	opacity: 0;
}
to {
  transform: scale(1) rotate(45deg);
	opacity: 1;
}`,be=b`
0% {
	height: 0;
	width: 0;
	opacity: 0;
}
40% {
  height: 0;
	width: 6px;
	opacity: 1;
}
100% {
  opacity: 1;
  height: 10px;
}`,ye=v("div")`
  width: 20px;
  opacity: 0;
  height: 20px;
  border-radius: 10px;
  background: ${e=>e.primary||"#61d345"};
  position: relative;
  transform: rotate(45deg);

  animation: ${xe} 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
  animation-delay: 100ms;
  &:after {
    content: '';
    box-sizing: border-box;
    animation: ${be} 0.2s ease-out forwards;
    opacity: 0;
    animation-delay: 200ms;
    position: absolute;
    border-right: 2px solid;
    border-bottom: 2px solid;
    border-color: ${e=>e.secondary||"#fff"};
    bottom: 6px;
    left: 6px;
    height: 10px;
    width: 6px;
  }
`,ve=v("div")`
  position: absolute;
`,we=v("div")`
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  min-width: 20px;
  min-height: 20px;
`,je=b`
from {
  transform: scale(0.6);
  opacity: 0.4;
}
to {
  transform: scale(1);
  opacity: 1;
}`,Ne=v("div")`
  position: relative;
  transform: scale(0.6);
  opacity: 0.4;
  min-width: 20px;
  animation: ${je} 0.3s 0.12s cubic-bezier(0.175, 0.885, 0.32, 1.275)
    forwards;
`,Ee=({toast:e})=>{let{icon:t,type:r,iconTheme:i}=e;return t!==void 0?typeof t=="string"?m.createElement(Ne,null,t):t:r==="blank"?null:m.createElement(we,null,m.createElement(he,{...i}),r!=="loading"&&m.createElement(ve,null,r==="error"?m.createElement(fe,{...i}):m.createElement(ye,{...i})))},$e=e=>`
0% {transform: translate3d(0,${e*-200}%,0) scale(.6); opacity:.5;}
100% {transform: translate3d(0,0,0) scale(1); opacity:1;}
`,_e=e=>`
0% {transform: translate3d(0,0,-1px) scale(1); opacity:1;}
100% {transform: translate3d(0,${e*-150}%,-1px) scale(.6); opacity:0;}
`,ke="0%{opacity:0;} 100%{opacity:1;}",Ce="0%{opacity:1;} 100%{opacity:0;}",Oe=v("div")`
  display: flex;
  align-items: center;
  background: #fff;
  color: #363636;
  line-height: 1.3;
  will-change: transform;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1), 0 3px 3px rgba(0, 0, 0, 0.05);
  max-width: 350px;
  pointer-events: auto;
  padding: 8px 10px;
  border-radius: 8px;
`,Ae=v("div")`
  display: flex;
  justify-content: center;
  margin: 4px 10px;
  color: inherit;
  flex: 1 1 auto;
  white-space: pre-line;
`,Ie=(e,t)=>{let r=e.includes("top")?1:-1,[i,s]=M()?[ke,Ce]:[$e(r),_e(r)];return{animation:t?`${b(i)} 0.35s cubic-bezier(.21,1.02,.73,1) forwards`:`${b(s)} 0.4s forwards cubic-bezier(.06,.71,.55,1)`}},Fe=m.memo(({toast:e,position:t,style:r,children:i})=>{let s=e.height?Ie(e.position||t||"top-center",e.visible):{opacity:0},a=m.createElement(Ee,{toast:e}),n=m.createElement(Ae,{...e.ariaProps},C(e.message,e));return m.createElement(Oe,{className:e.className,style:{...s,...r,...e.style}},typeof i=="function"?i({icon:a,message:n}):m.createElement(m.Fragment,null,a,n))});K(m.createElement);var Se=({id:e,className:t,style:r,onHeightUpdate:i,children:s})=>{let a=m.useCallback(n=>{if(n){let o=()=>{let l=n.getBoundingClientRect().height;i(e,l)};o(),new MutationObserver(o).observe(n,{subtree:!0,childList:!0,characterData:!0})}},[e,i]);return m.createElement("div",{ref:a,className:t,style:r},s)},qe=(e,t)=>{let r=e.includes("top"),i=r?{top:0}:{bottom:0},s=e.includes("center")?{justifyContent:"center"}:e.includes("right")?{justifyContent:"flex-end"}:{};return{left:0,right:0,display:"flex",position:"absolute",transition:M()?void 0:"all 230ms cubic-bezier(.21,1.02,.73,1)",transform:`translateY(${t*(r?1:-1)}px)`,...i,...s}},ze=O`
  z-index: 9999;
  > * {
    pointer-events: auto;
  }
`,E=16,De=({reverseOrder:e,position:t="top-center",toastOptions:r,gutter:i,children:s,containerStyle:a,containerClassName:n})=>{let{toasts:o,handlers:l}=ce(r);return m.createElement("div",{style:{position:"fixed",zIndex:9999,top:E,left:E,right:E,bottom:E,pointerEvents:"none",...a},className:n,onMouseEnter:l.startPause,onMouseLeave:l.endPause},o.map(c=>{let u=c.position||t,g=l.calculateOffset(c,{reverseOrder:e,gutter:i,defaultPosition:t}),f=qe(u,g);return m.createElement(Se,{id:c.id,key:c.id,onHeightUpdate:l.updateHeight,className:c.visible?ze:"",style:f},c.type==="custom"?C(c.message,c):s?s(c):m.createElement(Fe,{toast:c,position:u}))}))},D=p;function Pe(){const e={username:"",password:"",email:"",first_name:"",last_name:""},t=R({username:j().required("Nombre de usuario es requerido").max(10,"el nomnre es muy largo"),password:j().required("Contraseña es requerida").min(8,"minimo 8 ").max(32,"Maximo de longitud 32"),email:j().email("Ingrese con un Correo Electronico valido").required("Email es requerido"),first_name:j().required("Nombres es requerido"),last_name:j().required("Apellidos es requerido")}),{register:r,handleSubmit:i,formState:{errors:s},reset:a}=U({defaultValues:e,resolver:Z(t)}),n=Y(H,{onSuccess:l=>{console.log(l.message),a(),D.success(l.message,{duration:5e3})},onError:l=>{console.log(l),D.error("No registrado..",{duration:5e3})}}),o=l=>{console.log(l);try{n.mutate(l)}catch(c){console.log(c)}};return d.jsxs("div",{className:"min-h-screen bg-base-200 flex items-center",children:[d.jsx("div",{className:"card mx-auto w-full max-w-5xl  shadow-xl",children:d.jsxs("div",{className:"grid  md:grid-cols-2 grid-cols-1  bg-base-100 rounded-xl",children:[d.jsx("div",{className:"",children:d.jsx(V,{})}),d.jsxs("div",{className:"py-24 px-10",children:[d.jsx("h2",{className:"text-2xl font-semibold mb-2 text-center",children:"Registrar Cuenta"}),d.jsxs("form",{onSubmit:i(o),children:[d.jsxs("div",{className:"mb-4",children:[d.jsxs("div",{className:"form-control w-full mb-4",children:[d.jsx("label",{className:"label",htmlFor:"username",children:"Nombre de Usuario"}),d.jsx("input",{className:"input  input-bordered w-full",...r("username"),id:"username",type:"text"}),s.username&&d.jsx("p",{className:"error-message",children:s.username.message})]}),d.jsxs("div",{className:"form-control w-full mb-4",children:[d.jsx("label",{htmlFor:"password",children:"Contraseña"}),d.jsx("input",{className:"input  input-bordered w-full",...r("password"),id:"password",type:"password"}),s.password&&d.jsx("p",{className:"error-message",children:s.password.message})]}),d.jsxs("div",{className:"form-control w-full mb-4",children:[d.jsx("label",{htmlFor:"email",children:"Correo Electronico"}),d.jsx("input",{className:"input  input-bordered w-full",...r("email"),id:"email",type:"email"}),s.email&&d.jsx("p",{className:"error-message",children:s.email.message})]}),d.jsxs("div",{className:"form-control w-full mb-4",children:[d.jsx("label",{htmlFor:"first_name",children:"Nombres"}),d.jsx("input",{className:"input  input-bordered w-full",...r("first_name"),id:"first_name",type:"text"}),s.first_name&&d.jsx("p",{className:"error-message",children:s.first_name.message})]}),d.jsxs("div",{children:[d.jsx("label",{htmlFor:"last_name",children:"Apellidos"}),d.jsx("input",{className:"input  input-bordered w-full",...r("last_name"),id:"last_name",type:"text"}),s.last_name&&d.jsx("p",{className:"error-message",children:s.last_name.message})]})]}),d.jsxs("button",{type:"submit",className:"btn mt-2 w-full btn-primary",children:[n.isLoading&&d.jsx("span",{className:"loading loading-spinner"}),"Registrar"]}),d.jsxs("div",{className:"text-center mt-4",children:["¿Ya tienes cuenta?",d.jsx(T,{to:"/login",children:d.jsx("span",{className:"inline-block hover:text-primary hover:underline hover:cursor-pointer transition duration-200",children:"Inicia sesion"})})]})]})]})]})}),d.jsx(De,{})]})}function He(){return d.jsx("div",{className:"",children:d.jsx(Pe,{})})}export{He as default};

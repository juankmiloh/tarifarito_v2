(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-5621180c"],{"133c":function(e,t,s){"use strict";s("d785")},"3cbc":function(e,t,s){"use strict";var a=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"pan-item",style:{zIndex:e.zIndex,height:e.height,width:e.width}},[s("div",{staticClass:"pan-info"},[s("div",{staticClass:"pan-info-roles-container"},[e._t("default")],2)]),e._v(" "),s("div",{staticClass:"pan-thumb",style:{backgroundImage:"url("+e.image+")"}})])},i=[],r=(s("c5f6"),{name:"PanThumb",props:{image:{type:String,required:!0},zIndex:{type:Number,default:1},width:{type:String,default:"150px"},height:{type:String,default:"150px"}}}),n=r,c=(s("133c"),s("2877")),u=Object(c["a"])(n,a,i,!1,null,"799537af",null);t["a"]=u.exports},"8f73":function(e,t,s){"use strict";s("b804")},b804:function(e,t,s){},d785:function(e,t,s){},ecac:function(e,t,s){"use strict";s.r(t);var a=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("div",{staticClass:"app-container"},[e.user?s("div",[s("el-row",{attrs:{gutter:20}},[s("el-col",{attrs:{span:6,xs:24}},[s("user-card",{attrs:{user:e.user}})],1),e._v(" "),s("el-col",{attrs:{span:18,xs:24}},[s("el-card",[s("el-tabs",{model:{value:e.activeTab,callback:function(t){e.activeTab=t},expression:"activeTab"}},[s("el-tab-pane",{attrs:{label:"Administrar Cuenta",name:"account"}},[s("account",{attrs:{user:e.user}})],1)],1)],1)],1)],1)],1):e._e()])},i=[],r=(s("7f7f"),s("5530")),n=s("2f62"),c=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("el-card",{staticStyle:{"margin-bottom":"20px"}},[s("div",{staticClass:"clearfix",attrs:{slot:"header"},slot:"header"},[s("span",[e._v("Acerca de")])]),e._v(" "),s("div",{staticClass:"user-profile"},[s("div",{staticClass:"box-center"},[s("pan-thumb",{attrs:{image:e.user.avatar,height:"100px",width:"100px",hoverable:!1}},[s("div",[e._v("Hola")])])],1),e._v(" "),s("div",{staticClass:"box-center"},[s("div",{staticClass:"user-name text-center"},[e._v(e._s(e.user.name))]),e._v(" "),s("div",{staticClass:"user-role text-center text-muted"},[e._v(e._s(e._f("uppercaseFirst")(e.user.privilegio)))])])]),e._v(" "),s("div",{staticClass:"user-bio"},[s("div",{staticClass:"user-education user-bio-section"},[s("div",{staticClass:"user-bio-section-header"},[s("svg-icon",{attrs:{"icon-class":"user"}}),s("span",[e._v("Información")])],1),e._v(" "),s("div",{staticClass:"user-bio-section-body"},[s("div",{staticClass:"text-muted"},[e._v("\n          "+e._s(e.user.descripcion)+"\n        ")])])])])])},u=[],o=s("3cbc"),l={components:{PanThumb:o["a"]},props:{user:{type:Object,default:function(){return{name:"",email:"",avatar:"",roles:""}}}}},d=l,p=(s("8f73"),s("2877")),m=Object(p["a"])(d,c,u,!1,null,"0c964ec4",null),v=m.exports,f=function(){var e=this,t=e.$createElement,s=e._self._c||t;return s("el-form",[s("el-form-item",{attrs:{label:"Nombre"}},[s("el-input",{model:{value:e.user.usuario,callback:function(t){e.$set(e.user,"usuario","string"===typeof t?t.trim():t)},expression:"user.usuario"}})],1),e._v(" "),s("el-form-item",{attrs:{label:"Usuario"}},[s("el-input",{model:{value:e.user.name,callback:function(t){e.$set(e.user,"name","string"===typeof t?t.trim():t)},expression:"user.name"}})],1)],1)},b=[],h={props:{user:{type:Object,default:function(){return{name:"",email:""}}}},methods:{submit:function(){this.$message({message:"User information has been updated successfully",type:"success",duration:5e3})}}},_=h,g=Object(p["a"])(_,f,b,!1,null,null,null),x=g.exports,C={name:"Profile",components:{UserCard:v,Account:x},data:function(){return{user:{},activeTab:"account"}},computed:Object(r["a"])({},Object(n["b"])(["name","avatar","roles","usuario","introduction","privilegio"])),created:function(){this.getUser()},methods:{getUser:function(){this.user={name:this.name,role:this.roles.join(" | "),email:"admin@test.com",avatar:this.avatar,usuario:this.usuario,descripcion:this.introduction,privilegio:this.privilegio}}}},y=C,w=Object(p["a"])(y,a,i,!1,null,null,null);t["default"]=w.exports}}]);
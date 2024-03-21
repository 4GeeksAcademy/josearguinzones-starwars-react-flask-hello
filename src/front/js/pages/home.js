import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { useNavigate } from "react-router-dom";

export const Home = () => {
	const { store, actions } = useContext(Context);
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("")
	const navigate = useNavigate()

	const registrarse = async (e) => {
		e.preventDefault()
		if (email != "" && password != "") {
			await actions.registrarse(email, password)

		}
		else {
			alert("faltan datos")
		}

	}

	const iniciar_sesion = async (e) => {
		e.preventDefault()
		if (email != "" && password != "") {
			await actions.iniciar_sesion(email, password)
			if (store.auth) {
				navigate("/demo")
			}
		}
		else {
			alert("faltan datos")
		}

	}

	return (
		<div className="text-center mt-5 container">
			<h1>Hello </h1>
			<form>
				<div className="mb-3">
					<label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
					<input value={email} onChange={(e) => setEmail(e.target.value)} type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
					<div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
				</div>
				<div className="mb-3">
					<label htmlFor="exampleInputPassword1" className="form-label">Password</label>
					<input value={password} onChange={(e) => setPassword(e.target.value)} type="password" className="form-control" id="exampleInputPassword1" />
				</div>

				<button onClick={(e) => registrarse(e)} className="btn btn-primary">registrarse</button>
				<button onClick={(e) => iniciar_sesion(e)} className="btn btn-primary">iniciar sesion</button>

			</form>
		</div>
	);
};

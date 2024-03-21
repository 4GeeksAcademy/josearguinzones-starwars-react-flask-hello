const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			auth: false
		},
		actions: {
			// Use getActions to call a function within a fuction


			registrarse: async (email, password) => {
				try {
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/user", {
						method: "POST",
						body: JSON.stringify({
							email: email,
							password: password
						}),
						headers: { "Content-Type": "application/json" }
					})
					const data = await resp.json()
					// setStore({ message: data.message })
					console.log(data)
					// don't forget to return something, that is how the async resolves
					return data;
				} catch (error) {
					console.log("Error loading message from backend", error)
				}
			},

			iniciar_sesion: async (email, password) => {
				try {
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/login", {
						method: "POST",
						body: JSON.stringify({
							email: email,
							password: password
						}),
						headers: { "Content-Type": "application/json" }
					})
					if (resp.status == 200) {
						const data = await resp.json()
						localStorage.setItem("token", data.access_token)
						setStore({ auth: true })

					}
					else {
						setStore({ auth: false })
					}

				} catch (error) {
					console.log("Error loading message from backend", error)
				}
			},
			logout:()=>{
				localStorage.removeItem("token")
				setStore({ auth: false })
				
			}

		}
	};
};

export default getState;

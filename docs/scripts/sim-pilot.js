var host = 'wss://sim-pilot.herokuapp.com/api/'
	if (window.location.hostname == '0.0.0.0' || window.location.hostname == 'localhost'){
		host = 'ws://'+ window.location.host + '/api/'
	};

Vue.component('alerts', {
	props: ['data'],
	template: `
<div>
	<div v-for="(log,i) in data">
 		<div class="toast" id="myToast" style="position: absolute; top: 0; right: 0;">
        <div class="toast-header">
            <strong class="mr-auto"><i class="fa fa-grav"></i> We miss you!</strong>
            <small>11 mins ago</small>
            <button type="button" class="ml-2 mb-1 close" data-dismiss="toast">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
        <div class="toast-body">
            <div>It's been a long time since you visited us. We've something special for you. <a href="#">Click here!</a></div>
        </div>
    </div>
            </div>
    </div>
	`,
});

Vue.component('logs', {
	props: ['data','names'],
	template: `
		<div>
			<div v-for="(log,i) in data">
				<div v-if="log.primary" class="alert alert-dismissible alert-primary"">
					{{ log.primary }}
				</div>
				<div v-if="log.secondary" class="alert alert-dismissible alert-secondary">
					{{ log.secondary }}
				</div>
				<div v-if="log.success" class="alert alert-dismissible alert-success">
					{{ log.success }}
				</div>
				<div v-if="log.info" class="alert alert-dismissible alert-info"">
					{{ log.info }}
				</div>
				<div v-if="log.danger" class="alert alert-dismissible alert-danger"">
					{{ log.danger }}
				</div>
				<div v-if="log.warning" class="alert alert-dismissible alert-warning"">
					{{ log.warning }}
				</div>
				<div v-if="log.link" class="alert alert-dismissible alert-link"">
					{{ log.link }}
				</div>

					<div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
					<div class="toast-header">
					<img src="..." class="rounded mr-2" alt="...">
					<strong class="mr-auto">Bootstrap</strong>
					<small>11 mins ago</small>
					<button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
					<span aria-hidden="true">&times;</span>
					</button>
					</div>
					<div class="toast-body">
					Hello, world! This is a toast message.
					</div>
					</div>

			</div>
		</div>
	`,
	methods: {
		character_name: function (character_id) {
			this.$parent.addName(character_id);
			return this.$parent['names'][character_id];
		},
	}
});

const app = new Vue({
	el: "#app",
	data: {
		endPoint:null,
		alerts: [],
		status: "disconnected"
	},
	methods: {
		connect() {

			this.socket = new WebSocket(host);
			this.socket.onopen = () => {

				$('.loader').hide()
				this.status = "connected";
				this.alerts.unshift({primary: 'Connecting to ' + host})
				this.socket.onmessage =  (event)  => {	

					msg = JSON.parse(event.data)
					//console.warn(msg)
					if ('endPoint' in msg){
						app['endPoint'] = msg.endPoint
						app[msg.endPoint] = msg.payload
						// dispatch(msg)
					} else if ('alert' in msg) {
						this.alerts.unshift(msg.alert)
						this.alerts = this.alerts.slice(0,10);
					} else if ('error' in msg) {
						console.warn('ERROR')
						console.warn(msg)
					} else {
						console.warn('NO ENDPOINT')
						console.warn(msg)
					}
				};
			};

			this.socket.onerror = () => {
				$('.loader').show()
			};
			this.socket.onclose = () => {
				$('.loader').show()
				setTimeout(this.connect, 5000)
			};

		},
		disconnect() {
			this.socket.close();
			this.status = "disconnected";
			this.logs = [];
		},
		sendMessage(e) {
			this.socket.send(JSON.stringify(this.message) );
			this.logs.unshift({ event: "Sent message", data:this.message });
			this.message = "";
		},
		addName(id){
			this.names[id] = null;
			this.saveNames();
		},
		saveNames(){
			const parsed = JSON.stringify(this.names);
			localStorage.setItem('names', parsed);
		}

	},
	mounted() {
				
		if (!(localStorage.getItem('names'))) {
			localStorage.setItem('names', JSON.stringify({}));
		}

		try {
			this.names = JSON.parse(localStorage.getItem('names'));
		} catch(e) {
			localStorage.removeItem('names');
		}
	
	},
	watch: {
		names(newName) {
			localStorage.names = JSON.stringify(newName);
		}
	}
});

app.connect();

$(document).ready(function(){
	$(".show-toast").click(function(){
		$(".toast").toast('show');
	});
});
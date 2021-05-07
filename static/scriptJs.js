// API KEYS
// https://cdn-api.co-vin.in/api/v2/admin/location/states/
// https://cdn-api.co-vin.in/api/v2/admin/location/districts/5
// https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=801105&date=07-05-2021
// /v2/appointment/sessions/public/calendarByDistrict
// states_api = 'https://cdn-api.co-vin.in/api/v2/admin/location/states/'
// districts_api = `https://cdn-api.co-vin.in/api/v2/admin/location/districts/5`
let submitBtn = document.getElementById('submitBtn');
submitBtn.addEventListener('click', function submitForm() {
    let pin_code = document.getElementById('pin_code').value;
    let vaccineDetailsCont = document.getElementById('vaccineDetailsCont');
    let today = new Date();
    let dd = String(today.getDate()).padStart(2, '0');
    let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    let yyyy = today.getFullYear();
    today_day = dd + '-' + mm + '-' + yyyy;
    appointment_pin_date = `https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=${pin_code}&date=${today_day}`
    async function getData() {
        let response = await fetch(appointment_pin_date);
        let data = await response.json();
        data.centers.forEach(function myFun(item, index) {
            for (let session_data of item.sessions) {
                let htmlStr = `
                    <div class="row">
                        <div class="col-lg-8 offset-lg-2 justify-content-center">
                            <div class="card text-center vaccineDetailsCard">
                                <div class="card-header">
                                    <p class="card-title">
                                    ${item.name}, ${item.block_name} ${item.district_name}
                                    </p>
                                </div>
                                <div class="card-body">
                                    <p class="card-text vaccineDetailsCardText">
                                        <span>Date:</span> ${session_data.date}
                                    </p>
                                    <div class="row">
                                        <div class="col-lg-6 col-6">
                                            <p class="card-text vaccineDetailsCardText">
                                            <span>From:</span> ${item.from}
                                            </p>
                                        </div>
                                        <div class="col-lg-6 col-6">
                                            <p class="card-text vaccineDetailsCardText">
                                            <span>To:</span> ${item.to}
                                            </p>
                                        </div>
                                    </div>
                                    <p class="card-text vaccineDetailsCardText">
                                        <span>Available Capacity:</span> ${session_data.available_capacity}
                                    </p>
                                    <p class="card-text vaccineDetailsCardText">
                                        <span>Fee Type:</span> ${item.fee_type}
                                    </p>
                                    <p class="card-text vaccineDetailsCardText">
                                        <span>Min Age Limit:</span> ${session_data.min_age_limit}
                                    </p>
                                </div>
                                <div class="card-footer text-muted">
                                    <span>Slots:</span>   ${session_data.slots}
                                </div>
                            </div>
                        </div>
                    </div>`
                vaccineDetailsCont.innerHTML += htmlStr

            }
        });
    }
    getData();
    vaccineDetailsCont.innerHTML = ''
})
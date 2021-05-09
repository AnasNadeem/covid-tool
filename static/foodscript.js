function loadPageSt() {
    location_api = `https://api.covidmealsforindia.com/user/location_filter`;
    async function getData() {
        let response = await fetch(location_api);
        let data = await response.json();
        data.data.forEach(function myFun(item, index) {
            let stateList = document.getElementById('stateList');
            let optionhtml = `<option value="${index}">${item}</option>`;
            stateList.innerHTML += optionhtml;
        })
    }
    getData();
}
loadPageSt();
let searchBtn = document.getElementById('searchBtn')
searchBtn.addEventListener('click', function doStuff() {
    let stateList = document.getElementById('stateList');
    const selectedState = [].filter
        .call(stateList.options, option => option.selected)
        .map(option => option.text);
    let searchQuery = document.getElementById('keywordCityPro').value;
    main_api = `https://api.covidmealsforindia.com/user/restaurants?search_query=${searchQuery}&location_filter=${selectedState}`
    async function getAllData() {
        let response = await fetch(main_api);
        let res_data = await response.json();
        res_data.data.restaurants.forEach(function myMainFun(item) {
            let mainInfo = document.getElementById('mainInfo');
            let maincodeHtml = `
                    <div class="row">
                    <div class="col-lg-6 mx-auto">
                        <div class="card cardInfoMeal text-center">
                            <div class="card-body">
                                <h5 class="card-title">
                                    ${item.restaurant_name}
                                    <a target="_blank" href="http://wa.me/${item.phone_numbers[0]}">
                                        <i class="fa fa-whatsapp whatsappLogo" aria-hidden="true"></i>
                                    </a>
                                </h5>
                                <p class="card-text cardInfoText">
                                    <i class="fas fa-map-marker-alt cardLogo"></i>
                                    ${item.tmp_location.address_complete}
                                </p>
                                <p class="card-text cardInfoText">
                                    <i class="fa fa-phone-alt cardLogo" aria-hidden="true"></i>
                                    ${item.phone_numbers}
                                </p>
                                <p class="card-text cardInfoText">
                                    <i class="fas fa-hotel cardLogo"></i>
                                    ${item.service_type}
                                </p>
                                <p class="card-text cardInfoText">
                                    <i class="fas fa-truck-moving cardLogo"></i>
                                    ${Object.keys(item.delivery_mode)}
                                </p>
                            </div>
                            <div class="card-footer text-muted">
                                ${Object.keys(item.service_days)}
                            </div>
                        </div>
                    </div>
                </div>
                    `
            mainInfo.innerHTML += maincodeHtml;
        })
    }
    mainInfo.innerHTML = ''
    getAllData();
})
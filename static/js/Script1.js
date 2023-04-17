// JavaScript source code
document.body.style.background = 'url(https://images.unsplash.com/photo-1486427944299-d1955d23e34d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80)';
document.body.style.backgroundSize = "cover";
//$('OURCLASS').click(function () {

//    alert('you clicked')

//})

$('.fa-circle-xmark-user').click(delete_user)
$('.fa-circle-xmark-feedback').click(delete_feedback)
$('.fa-circle-plus').click(add_feedback)
$('.feedback').click(see_feedback)
$('#navlink3log').click(logout)

//async function deleteCupcake() {
//    const id = $(this).attr('id')
//    console.log($(this).parent().parent().parent().parent().parent().parent().parent())
//    await axios.delete(`/api/cupcakes/${id}`)
//    $(this).parent().parent().parent().parent().parent().parent().parent().remove()
//}

$("#new_cupcake_form").submit(addNewCupcake)

async function addNewCupcake() {
    let flavor = $("#flavor").val();
    let rating = $("#rating").val();
    let size = $("#size").val();
    console.log(`${flavor}, ${rating}, ${size}`);
    
    await axios.post("/api/cupcakes", {
        "flavor": `${flavor}`,
        "size": `${size}`,
        "rating": `${rating}`,
        "image": ""
    })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
}



//FEATURES FOR ICON BAR -- SIZE UP, CHANGE COLOR,  AND ADD ANIMATION ON HOVER//
$(".species-icon").hover(
    function () {
        $(this).addClass("fa-lg");
        $(this).addClass("fa-beat");
        $(this).addClass("text-primary");
        /*$(this).addClass("pop_form");*/
        /*$("#pop_form").append(miniform);*/
    }, function () {
        $(this).removeClass("fa-lg");
        $(this).removeClass("fa-beat");
        $(this).removeClass("text-primary");
        /*$("#miniform").remove();*/
    }
);

$(".github-icon").hover(
    function () {
        $(this).addClass("fa-lg");
        $(this).addClass("fa-beat");
        $(this).addClass("text-primary");
        /*$(this).addClass("pop_form");*/
        /*$("#pop_form").append(miniform);*/
    }, function () {
        $(this).removeClass("fa-lg");
        $(this).removeClass("fa-beat");
        $(this).removeClass("text-primary");
        /*$("#miniform").remove();*/
    }
);

$(".reqs-icon").hover(
    function () {
        $(this).addClass("fa-lg");
        $(this).addClass("fa-beat");
        $(this).addClass("text-primary");
        /*$(this).addClass("pop_form");*/
        /*$("#pop_form").append(miniform);*/
    }, function () {
        $(this).removeClass("fa-lg");
        $(this).removeClass("fa-beat");
        $(this).removeClass("text-primary");
        /*$("#miniform").remove();*/
    }
);



$(".notes-icon").hover(
    function () {
        $(this).addClass("fa-lg");
        $(this).addClass("fa-beat");
        $(this).addClass("text-primary");
    }, function () {
        $(this).removeClass("fa-lg");
        $(this).removeClass("fa-beat");
        $(this).removeClass("text-primary");
    }
);

$(".edit-icon").hover(
    function () {
        $(this).addClass("fa-lg");
        $(this).addClass("fa-beat");
        $(this).addClass("text-primary");
    }, function () {
        $(this).removeClass("fa-lg");
        $(this).removeClass("fa-beat");
        $(this).removeClass("text-primary");
    }
);

$(".bday-icon").hover(
    function () {
        $(this).addClass("fa-lg");
        $(this).addClass("fa-beat");
        $(this).addClass("text-primary");
    }, function () {
        $(this).removeClass("fa-lg");
        $(this).removeClass("fa-beat");
        $(this).removeClass("text-primary");
    }
);



let home = 'https://github.com/Fern-Ali/';
let repo = 'https://github.com/Fern-Ali/CupcakeDataBase';
let reqs = 'https://github.com/Fern-Ali/CupcakeDataBase/blob/master/requirements.txt';

//$(".edit-icon").on("click", addPetPage);
//$(".species-icon").on("click", editPetPage);
$(".github-icon").on("click", { event_type: home }, goToGithub);
$(".project-icon").on("click", { event_type: repo }, goToGithub);
$(".reqs-icon").on("click", { event_type: reqs }, goToGithub);



function addPetPage() {
    window.location.href = '/add';
    return false;
}

function editPetPage() {
    let id = $(this).attr('id');
    window.location.href = `/pets/${id}/edit`;
    return false;
}

function goToGithub(event) {

    window.location.href = event.data.event_type;
    return false;
}

///////////////////////////

function delete_user() {
    const id = $(this).attr('id')
    window.location.href = `/users/${id}/delete`;
    return false;
}

async function logout() {
    const id = $(this).attr('id')
    
    await axios.post(`/logout`)
    window.location.href = `/`;
   
}

function delete_feedback() {
    const id = $(this).attr('id')
    window.location.href = `/feedback/${id}/delete`;
    return false;
}

function add_feedback() {
    const id = $(this).attr('id')
    window.location.href = `/users/${id}/feedback/add`;
    return false;
}

function see_feedback() {
    const id = $(this).attr('id')
    window.location.href = `/feedback/${id}/update`;
    return false;
}

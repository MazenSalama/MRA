from flask import Flask, request, render_template, url_for, jsonify, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = '123456'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:MasMaz135?@localhost/mra"  # Change this place to mysql url eg mysql://scott:tiger@localhost/mydatabase
db = SQLAlchemy(app)


# Utils
def convert_date(date_time_str):
    date_obj = datetime.strptime(date_time_str, "%Y-%m-%d")
    return date_obj


def convert_datetime(date_time_str):
    date_obj = datetime.strptime(date_time_str, "%H:%M")
    return date_obj


# Model For Database


class PatientsDetails(db.Model):
    __tablename__ = "patientsdetails"
    id = db.Column(db.Integer, primary_key=True)
    ecw_id = db.Column(db.Integer)
    mbi = db.Column(db.Integer)
    hic = db.Column(db.Integer)
    subscriber_id = db.Column(db.Integer)
    member_name = db.Column(db.String(150))
    lastname = db.Column(db.String(150))
    firstname = db.Column(db.String(150))
    dob = db.Column(db.Date, default=date.today)
    insurance = db.Column(db.String(150))
    ecw_pcp = db.Column(db.String(150))
    last_appt_date = db.Column(db.Date, default=date.today)
    last_appt_provider_name = db.Column(db.String(150))
    last_visit_type = db.Column(db.String(150))
    next_appt_date = db.Column(db.Date, default=date.today)
    next_appt_time = db.Column(db.DateTime, default=datetime.utcnow)
    next_appt_provider_name = db.Column(db.String(150))
    next_appt_provider = db.Column(db.String(150))
    next_visit_type = db.Column(db.String(150))
    vos_gis = db.Column(db.String(150))
    assignment = db.Column(db.String(150))
    new_patient_history = db.Column(db.Text(450))
    research_done_visit = db.Column(db.String(150))
    awe_2020 = db.Column(db.String(150))
    
    
    
    confirmed_mra_already_captured_in_2020 = db.Column(db.String(150))
    confirmed_mra_not_addressed_in_2020 = db.Column(db.String(150))
    confirmed_mra__never_captured_addressed = db.Column(db.String(150))
    mra_addressed_by_pma_but_not_captured_by_cms_ = db.Column(db.String(150))
    true_suspects = db.Column(db.String(150))
    resolved_hcc_not_currently_valid = db.Column(db.String(150))




    evidence_confirmed_mra_already_captured_in_2020 = db.Column(db.String(1000))
    evidence_confirmed_mra_not_addressed_in_2020 = db.Column(db.String(1000))
    evidence_confirmed_mra__never_captured_addressed = db.Column(db.String(1000))
    evidence_mra_addressed_by_pma_but_not_captured_by_cms_ = db.Column(db.String(1000))
    evidence_true_suspects = db.Column(db.String(1000))
    evidence_resolved_hcc_not_currently_valid = db.Column(db.String(1000))





    appt_back_check_status = db.Column(db.String(150))
    pre_research_already_cap = db.Column(db.String(150))
    post_research_dx_to_capture = db.Column(db.String(150))
    post_research_suspects_identified = db.Column(db.String(150))
    post_appt_total_captured = db.Column(db.String(150))
    pre_proj_cap = db.Column(db.String(150))
    post_proj_cap = db.Column(db.String(150))
    patient_dup_checker_1_rs = db.Column(db.String(150))
    patient_dup_checker_2_rs = db.Column(db.String(150))
    pt_dup_checker_key_1 = db.Column(db.String(150))
    pt_dup_checker_key_2 = db.Column(db.String(150))
    checker = db.Column(db.String(150))



class ICD10(db.Model):
    __tablename__ = "ICD10"
    id = db.Column(db.Integer, primary_key=True)
    d_code = db.Column(db.String(150))
    description = db.Column(db.String(150))
    model = db.Column(db.Integer)
   

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        userpatients = PatientsDetails.query.all()
        icd10 = ICD10.query.all()
        print('=====================>>>>>>>>>>>>>>',icd10)
        userpatient = PatientsDetails(
            ecw_id="",
            mbi="",
            hic="",
            subscriber_id="",
            member_name="",
            lastname="",
            firstname="",
            dob="",
            insurance="",
            ecw_pcp="",
            last_appt_date="",
            last_appt_provider_name="",
            last_visit_type="",
            next_appt_date="",
            next_appt_time="",
            next_appt_provider_name="",
            next_appt_provider="",
            next_visit_type="",
            vos_gis="",
            assignment="",
            new_patient_history="",
            research_done_visit="",
            awe_2020="",


            confirmed_mra_already_captured_in_2020="",
            confirmed_mra_not_addressed_in_2020="",
            confirmed_mra__never_captured_addressed="",
            mra_addressed_by_pma_but_not_captured_by_cms_="",
            true_suspects="",
            resolved_hcc_not_currently_valid="",



            evidence_confirmed_mra_already_captured_in_2020="",
            evidence_confirmed_mra_not_addressed_in_2020="",
            evidence_confirmed_mra__never_captured_addressed="",
            evidence_mra_addressed_by_pma_but_not_captured_by_cms_="",
            evidence_true_suspects="",
            evidence_resolved_hcc_not_currently_valid="",




            appt_back_check_status="",
            pre_research_already_cap="",
            post_research_dx_to_capture="",
            post_research_suspects_identified="",
            post_appt_total_captured="",
            pre_proj_cap="",
            post_proj_cap="",
            patient_dup_checker_1_rs="",
            patient_dup_checker_2_rs="",
            pt_dup_checker_key_1="",
            pt_dup_checker_key_2="",
            checker="",
        )
        pagename = "home"
        num_of_patients = len(userpatients)
        return render_template(
            "index.html",
            pagename=pagename,
            userpatients=userpatients,
            userpatient=userpatient,
            num_of_patients=num_of_patients,
            icd10 = icd10
        )
    else:

        ecw_id = request.form["ecw_id"]
        mbi = request.form["mbi"]
        hic = request.form["hic"]
        subscriber_id = request.form["subscriber_id"]
        member_name = request.form["member_name"]
        lastname = request.form["lastname"]
        firstname = request.form["firstname"]
        dob = convert_date(request.form["dob"])
        insurance = request.form["insurance"]
        ecw_pcp = request.form["ecw_pcp"]
        last_appt_date = convert_date(request.form["last_appt_date"])
        last_appt_provider_name = request.form["last_appt_provider_name"]
        last_visit_type = request.form["last_visit_type"]
        next_appt_date = convert_date(request.form["next_appt_date"])
        next_appt_time = convert_datetime(request.form["next_appt_time"])
        next_appt_provider_name = request.form["next_appt_provider_name"]
        next_appt_provider = request.form["next_appt_provider"]
        next_visit_type = request.form["next_visit_type"]
        vos_gis = request.form["vos_gis"]
        assignment = request.form["assignment"]
        new_patient_history = request.form["new_patient_history"]
        research_done_visit = request.form["research_done_visit"]
        awe_2020 = request.form["awe_2020"]





        confirmed_mra_already_captured_in_2020 = request.form[
            "confirmed_mra_already_captured_in_2020"
        ]
        confirmed_mra_not_addressed_in_2020 = request.form[
            "confirmed_mra_not_addressed_in_2020"
        ]
        confirmed_mra__never_captured_addressed = request.form[
            "confirmed_mra__never_captured_addressed"
        ]
        mra_addressed_by_pma_but_not_captured_by_cms_ = request.form[
            "mra_addressed_by_pma_but_not_captured_by_cms_"
        ]
        true_suspects = request.form["true_suspects"]
        resolved_hcc_not_currently_valid = request.form[
            "resolved_hcc_not_currently_valid"
        ]






        evidence_confirmed_mra_already_captured_in_2020 = request.form[
            "evidence_confirmed_mra_already_captured_in_2020"
        ]
        evidence_confirmed_mra_not_addressed_in_2020 = request.form[
            "evidence_confirmed_mra_not_addressed_in_2020"
        ]
        evidence_confirmed_mra__never_captured_addressed = request.form[
            "evidence_confirmed_mra__never_captured_addressed"
        ]
        evidence_mra_addressed_by_pma_but_not_captured_by_cms_ = request.form[
            "evidence_mra_addressed_by_pma_but_not_captured_by_cms_"
        ]
        evidence_true_suspects = request.form["evidence_true_suspects"]
        evidence_resolved_hcc_not_currently_valid = request.form[
            "evidence_resolved_hcc_not_currently_valid"
        ]





        appt_back_check_status = request.form["appt_back_check_status"]
        pre_research_already_cap = request.form["pre_research_already_cap"]
        post_research_dx_to_capture = request.form["post_research_dx_to_capture"]
        post_research_suspects_identified = request.form[
            "post_research_suspects_identified"
        ]
        post_appt_total_captured = request.form["post_appt_total_captured"]
        pre_proj_cap = request.form["pre_proj_cap"]
        post_proj_cap = request.form["post_proj_cap"]
        patient_dup_checker_1_rs = request.form["patient_dup_checker_1_rs"]
        patient_dup_checker_2_rs = request.form["patient_dup_checker_2_rs"]
        pt_dup_checker_key_1 = request.form["pt_dup_checker_key_1"]
        pt_dup_checker_key_2 = request.form["pt_dup_checker_key_2"]
        checker = request.form["checker"]
        print(firstname)
        userpatient = PatientsDetails(
            ecw_id=ecw_id,
            mbi=mbi,
            hic=hic,
            subscriber_id=subscriber_id,
            member_name=member_name,
            lastname=lastname,
            firstname=firstname,
            dob=dob,
            insurance=insurance,
            ecw_pcp=ecw_pcp,
            last_appt_date=last_appt_date,
            last_appt_provider_name=last_appt_provider_name,
            last_visit_type=last_visit_type,
            next_appt_date=next_appt_date,
            next_appt_time=next_appt_time,
            next_appt_provider_name=next_appt_provider_name,
            next_appt_provider=next_appt_provider,
            next_visit_type=next_visit_type,
            vos_gis=vos_gis,
            assignment=assignment,
            new_patient_history=new_patient_history,
            research_done_visit=research_done_visit,
            awe_2020=awe_2020,



            confirmed_mra_already_captured_in_2020=confirmed_mra_already_captured_in_2020,
            confirmed_mra_not_addressed_in_2020=confirmed_mra_not_addressed_in_2020,
            confirmed_mra__never_captured_addressed=confirmed_mra__never_captured_addressed,
            mra_addressed_by_pma_but_not_captured_by_cms_=mra_addressed_by_pma_but_not_captured_by_cms_,
            true_suspects=true_suspects,
            resolved_hcc_not_currently_valid=resolved_hcc_not_currently_valid,


            evidence_confirmed_mra_already_captured_in_2020=evidence_confirmed_mra_already_captured_in_2020,
            evidence_confirmed_mra_not_addressed_in_2020=evidence_confirmed_mra_not_addressed_in_2020,
            evidence_confirmed_mra__never_captured_addressed=evidence_confirmed_mra__never_captured_addressed,
            evidence_mra_addressed_by_pma_but_not_captured_by_cms_=evidence_mra_addressed_by_pma_but_not_captured_by_cms_,
            evidence_true_suspects=evidence_true_suspects,
            evidence_resolved_hcc_not_currently_valid=evidence_resolved_hcc_not_currently_valid,




            appt_back_check_status=appt_back_check_status,
            pre_research_already_cap=pre_research_already_cap,
            post_research_dx_to_capture=post_research_dx_to_capture,
            post_research_suspects_identified=post_research_suspects_identified,
            post_appt_total_captured=post_appt_total_captured,
            pre_proj_cap=pre_proj_cap,
            post_proj_cap=post_proj_cap,
            patient_dup_checker_1_rs=patient_dup_checker_1_rs,
            patient_dup_checker_2_rs=patient_dup_checker_2_rs,
            pt_dup_checker_key_1=pt_dup_checker_key_1,
            pt_dup_checker_key_2=pt_dup_checker_key_2,
            checker=checker,
        )
        db.session.add(userpatient)
        db.session.commit()
        flash('Successfully Added Details','success')
        return redirect("/")


@app.route("/details/<int:id>", methods=["GET", "POST"])
def details(id):
    if request.method == "GET":
        userpatients = PatientsDetails.query.filter_by(id=id).all()

    return render_template("details.html", userpatients=userpatients)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        member_name = request.form["member_name"]
        dob = request.form['dob']
        comparison_type = request.form['comparison_type']
        processed_dob = dob
        if comparison_type == 'OR':
            userpatients = db.session.query(PatientsDetails).filter((PatientsDetails.member_name == member_name) | (PatientsDetails.dob == processed_dob)).all()
        elif comparison_type == 'AND':
            userpatients = db.session.query(PatientsDetails).filter((PatientsDetails.member_name == member_name) & (PatientsDetails.dob == processed_dob)).all()
        # else:
        #     userpatients = db.session.query(PatientsDetails).filter((PatientsDetails.member_name == member_name) | (PatientsDetails.dob == processed_dob)).all()
              

    return render_template("search.html", userpatients=userpatients)


@app.route("/search_page", methods=["GET", "POST"])
def search_page():
    return render_template("search.html")


@app.route("/delete/<int:id>")
def delete_user(id):
    user_to_delete = PatientsDetails.query.get_or_404(id)
    db.session.delete(user_to_delete)
    db.session.commit()
    return redirect("/")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    userpatient = PatientsDetails.query.get_or_404(id)
    icd10 = ICD10.query.all()
    if request.method == "POST":
        userpatient.ecw_id = request.form["ecw_id"]
        userpatient.mbi = request.form["mbi"]
        userpatient.hic = request.form["hic"]
        userpatient.subscriber_id = request.form["subscriber_id"]
        userpatient.member_name = request.form["member_name"]
        userpatient.lastname = request.form["lastname"]
        userpatient.firstname = request.form["firstname"]
        userpatient.dob = convert_date(request.form["dob"])
        userpatient.insurance = request.form["insurance"]
        userpatient.ecw_pcp = request.form["ecw_pcp"]
        userpatient.last_appt_date = convert_date(request.form["last_appt_date"])
        userpatient.last_appt_provider_name = request.form["last_appt_provider_name"]
        userpatient.last_visit_type = request.form["last_visit_type"]
        userpatient.next_appt_date = convert_date(request.form["next_appt_date"])
        userpatient.next_appt_time = convert_datetime(request.form["next_appt_time"])
        userpatient.next_appt_provider_name = request.form["next_appt_provider_name"]
        userpatient.next_appt_provider = request.form["next_appt_provider"]
        userpatient.next_visit_type = request.form["next_visit_type"]
        userpatient.vos_gis = request.form["vos_gis"]
        userpatient.assignment = request.form["assignment"]
        userpatient.new_patient_history = request.form["new_patient_history"]
        userpatient.research_done_visit = request.form["research_done_visit"]
        userpatient.awe_2020 = request.form["awe_2020"]


        userpatient.confirmed_mra_already_captured_in_2020 = request.form[
            "confirmed_mra_already_captured_in_2020"
        ]
        userpatient.confirmed_mra_not_addressed_in_2020 = request.form[
            "confirmed_mra_not_addressed_in_2020"
        ]
        userpatient.confirmed_mra__never_captured_addressed = request.form[
            "confirmed_mra__never_captured_addressed"
        ]
        userpatient.mra_addressed_by_pma_but_not_captured_by_cms_ = request.form[
            "mra_addressed_by_pma_but_not_captured_by_cms_"
        ]
        userpatient.true_suspects = request.form["true_suspects"]
        userpatient.resolved_hcc_not_currently_valid = request.form[
            "resolved_hcc_not_currently_valid"
        ]




        userpatient.evidence_confirmed_mra_already_captured_in_2020 = request.form[
            "evidence_confirmed_mra_already_captured_in_2020"
        ]
        userpatient.evidence_confirmed_mra_not_addressed_in_2020 = request.form[
            "evidence_confirmed_mra_not_addressed_in_2020"
        ]
        userpatient.evidence_confirmed_mra__never_captured_addressed = request.form[
            "evidence_confirmed_mra__never_captured_addressed"
        ]
        userpatient.evidence_mra_addressed_by_pma_but_not_captured_by_cms_ = request.form[
            "evidence_mra_addressed_by_pma_but_not_captured_by_cms_"
        ]
        userpatient.evidence_true_suspects = request.form["evidence_true_suspects"]
        userpatient.evidence_resolved_hcc_not_currently_valid = request.form[
            "evidence_resolved_hcc_not_currently_valid"
        ]














        userpatient.appt_back_check_status = request.form["appt_back_check_status"]
        userpatient.pre_research_already_cap = request.form["pre_research_already_cap"]
        userpatient.post_research_dx_to_capture = request.form[
            "post_research_dx_to_capture"
        ]
        userpatient.post_research_suspects_identified = request.form[
            "post_research_suspects_identified"
        ]



        userpatient.post_appt_total_captured = request.form["post_appt_total_captured"]
        userpatient.pre_proj_cap = request.form["pre_proj_cap"]
        userpatient.post_proj_cap = request.form["post_proj_cap"]
        userpatient.patient_dup_checker_1_rs = request.form["patient_dup_checker_1_rs"]
        userpatient.patient_dup_checker_2_rs = request.form["patient_dup_checker_2_rs"]
        userpatient.pt_dup_checker_key_1 = request.form["pt_dup_checker_key_1"]
        userpatient.pt_dup_checker_key_2 = request.form["pt_dup_checker_key_2"]
        userpatient.checker = request.form["checker"]

        db.session.commit()
        flash('Successfully Updated Details','success')
        return redirect("/")
    else:
        pagename = "updatepage"
        userpatients = PatientsDetails.query.all()
        return render_template(
            "index.html",
            pagename=pagename,
            userpatient=userpatient,
            userpatients=userpatients,
            icd10 = icd10
        )


if __name__ == "__main__":
    app.run(debug=True)

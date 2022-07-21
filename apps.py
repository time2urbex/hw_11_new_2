from flask import Flask, render_template

app = Flask(__name__)


def main_code():

    @app.route('/')
    def page_main():

        result: load_candidates_from_json(path)
        return render_template('list.html')


    @app.route('/candidate/<x>')
    def get_candidate_by_id(uid):
        candidates = get_all_candidates()
        for candidate in candidates:
            if candidate['id'] == uid:
                return candidate
        return render_template('skill.html')

    @app.route('/search/<candidate_name>')



    @app.route('/skill/<skill_name>')
    def get_candidate_by_id(uid):
        candidates = get_all_candidates()
        for candidate in candidates:
            if candidate['name'] == candidate_name:
                return candidate
        return render_template('skill.html')

    pass


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx

from flowcase.helpers import clean_name, get_role_from_cv_roles, get_tags_from_cv
from flowcase.types.cv import CVResponse
from flowcase.types.department import Department
from flowcase.types.employee import Employee


def create_person_node(user: Employee) -> tuple[str, dict]:
    # this seems to have been used with some other user object, than Employee
    return (
        clean_name(user.name),
        {
            "type": "person",
            #            "role": user.get("role"),
            "title": user.title,
            "office_name": user.get("office_name"),
            "country_code": user.country_code,
        },
    )


def create_person_node_from_cv(cv: CVResponse, office_name) -> tuple[str, dict]:
    return (
        clean_name(cv.name),
        {
            "type": "person",
            "title": cv.title,
            "office_name": office_name,
            "country_code": cv.country_code,
        },
    )


def get_all_people_graph(
    noa_departments, add_roles: bool = True, add_tags: bool = True
) -> nx.Graph:
    # make a graph of all of Noa Ignite
    nodes = []  # roles & people
    edges = []  # (node, node)
    G = nx.Graph()
    for department, people in noa_departments:
        if department not in nodes:
            nodes.append(
                (
                    department,
                    {
                        "type": "department",
                        "members": len(people),
                        "office_name": department,
                    },
                )
            )

        for user, cv in people:
            user_name = clean_name(user.get("name"))
            if user_name and user_name not in nodes:
                nodes.append(create_person_node(user))
                # relation person -> department
                edges.append((department, user_name))

                if add_roles:
                    for role in cv.get("cv_roles"):
                        if get_role_from_cv_roles(role):
                            nodes.append(
                                (get_role_from_cv_roles(role), {"type": "role"})
                            )
                            edges.append((user_name, get_role_from_cv_roles(role)))
                if add_tags and get_tags_from_cv(cv):
                    # skills are nodes too
                    nodes.extend(
                        [(cv_tag, {"type": "skill"}) for cv_tag in get_tags_from_cv(cv)]
                    )

                    # and user-> skill are egdes
                    edges.extend([(user_name, t) for t in get_tags_from_cv(cv)])

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    return G


def get_roles_and_people_graph(department: Department) -> nx.Graph:
    # what would be a relation.
    # tech skill?
    # roles? .. yeah. probly roles..
    nodes = []  # roles & people
    edges = []  # (node, node)
    G = nx.Graph()

    for user, cv in department:
        if cv.name and cv.name not in nodes:
            # print(user)
            nodes.append(create_person_node_from_cv(user, department.name))

        for role in cv.cv_roles:
            if get_role_from_cv_roles(role):
                nodes.append((get_role_from_cv_roles(role), {"type": "title"}))
                edges.append((cv.name, get_role_from_cv_roles(role)))

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # nx.draw(G)
    return G


def get_skills_and_people_graph(department: Department) -> nx.Graph:
    # what would be a relation.
    # tech skill?
    # roles? .. yeah. probly roles..
    nodes = []  # roles & people
    edges = []  # (node, node)
    G = nx.Graph()

    for user, cv in department:
        # people are nodes
        user_name = cv.name
        if user_name and user_name not in nodes:
            nodes.append(create_person_node_from_cv(user, office_name=department.name))

        if get_tags_from_cv(cv):
            # skills are nodes too
            nodes.extend(
                [(cv_tag, {"type": "skill"}) for cv_tag in get_tags_from_cv(cv)]
            )

            # and user-> skill are egdes
            edges.extend([(user_name, t) for t in get_tags_from_cv(cv)])

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    # nx.draw(G)
    return G
